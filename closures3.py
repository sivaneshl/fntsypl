# return function

def transmit_to_space(message):
    "this is the enclosing function"
    def data_transmitter():
        "this is the nested function"
        print(message)

    return data_transmitter

func2=transmit_to_space("test message")
print("calling func2")
func2()
