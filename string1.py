text = "X-DSPAM-Confidence:    0.8475";
spos = text.find(':') + 1;
substr = text[spos:].strip();
print(substr);
