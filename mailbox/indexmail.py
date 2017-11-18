import sqlite3
import re
import dateutil.parser
import zlib

def parseheader(hdr):
    if hdr is None or len(hdr) < 1:
        return None

    sender = None
    x = re.findall('\nFrom: .*<(\S+@\S+)>\n', hdr)
    if (len(x) != 1):
        x = re.findall('\nFrom: (\S+@\S+)\n', hdr)
    sender = x[0].strip().lower()
    sender = sender.replace("<","")
    # print(sender)

    subject = None
    x = re.findall('\nSubject: (.*)\n', hdr)
    if len(x) >= 1:
        subject = x[0].strip().lower()
    # print(subject)

    guid = None
    x = re.findall('\nMessage-ID: (.*)\n', hdr)
    if len(x) >= 1:
        guid = x[0].strip().lower()

    sent_at = None
    x = re.findall('\nDate: (.*)\n', hdr)
    if len(x) >= 1:
        try:
            sent_at = dateutil.parser.parse(x[0][:26]).isoformat()
        except:
            return None

    if sender is None or subject is None or guid is None or sent_at is None:
        return None
    return (guid, sender, subject, sent_at)

conn = sqlite3.connect('index.sqlite3')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS messages')
cur.execute('DROP TABLE IF EXISTS senders')
cur.execute('DROP TABLE IF EXISTS subjects')
cur.execute('DROP TABLE IF EXISTS replies')

cur.execute('''CREATE TABLE IF NOT EXISTS messages
    (id INTEGER PRIMARY KEY, guid TEXT UNIQUE, sent_at INTEGER,
    sender_id INTEGER, subject_id INTEGER,
    headers BLOB, body BLOB)''')
cur.execute('''CREATE TABLE IF NOT EXISTS senders
    (id INTEGER PRIMARY KEY, sender TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS subjects
    (id INTEGER PRIMARY KEY, subject TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS replies
    (from_id INTEGER, to_id INTEGER)''')

conn1 = sqlite3.connect('file:mailbox.sqlite3?mode=ro', uri=True)
cur1 = conn1.cursor()

counter = 0
senders = dict()
subjects = dict()
guids = dict()

cur1.execute('SELECT headers, body, sent_at FROM messages ORDER BY sent_at')
for message_row in cur1:
    counter = counter + 1
    parsed_header = parseheader(message_row[0])
    if parsed_header is None:
        continue
    (guid, sender, subject, sent_at) = parsed_header
    print(guid, sender, subject, sent_at)

    sender_id = senders.get(sender, None)
    subject_id = subjects.get(subject, None)

    if sender_id is None:
        cur.execute('INSERT OR IGNORE INTO senders (sender) VALUES (?)', (sender,))
        conn.commit()
        cur.execute('SELECT id FROM senders WHERE sender = ?', (sender,))
        try:
            row = cur.fetchone()
            sender_id = row[0]
            senders[sender] = sender_id
        except:
            print('Unable to get sender id', sender)
            break

    if subject_id is None:
        cur.execute('INSERT OR IGNORE INTO subjects (subject) VALUES (?)', (subject,))
        conn.commit()
        cur.execute('SELECT id FROM subjects WHERE subject = ?', (subject,))
        try:
            row = cur.fetchone()
            subject_id = row[0]
            subjects[subject] = subject_id
        except:
            print('Unable to get subject id', subject)
            break

    cur.execute('''INSERT OR IGNORE INTO messages
        (guid, sender_id, subject_id, sent_at, headers, body)
        VALUES (?, ?, ?, datetime(?), ?, ?)''',
        (guid, sender_id, subject_id, sent_at,
        (zlib.compress(message_row[0].encode())),
        (zlib.compress(message_row[1].encode()))))
    conn.commit()
    cur.execute('SELECT id FROM messages WHERE guid = ? LIMIT 1', (guid,))
    try:
        row = cur.fetchone()
        message_id = row[0]
        guids[guid] = message_id
    except:
        print('Unable to get message id', guid)
        break

cur.close()
cur1.close()
