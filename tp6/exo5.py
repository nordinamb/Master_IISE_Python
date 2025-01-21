def process_input(user_input) :
    return 10 / int(user_input)

try :
    print(process_input("177"))
except ZeroDivisionError as e :
    print(f"Error: {e}")
except ValueError as e2 :
    print(f"Error: {e2}")