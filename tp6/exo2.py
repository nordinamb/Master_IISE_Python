def convert_to_int(value):
    try :
        print(int(value))
    except ValueError:
        print("conversion echoue")
convert_to_int(2.5)