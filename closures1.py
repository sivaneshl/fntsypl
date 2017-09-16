# closures

def transmit_to_space(message):
    "this is the enclosing function"
    def data_transmitter():
        "this is the nested function"
        print(message)

    #calling the nested function
    data_transmitter()

transmit_to_space("test message")
