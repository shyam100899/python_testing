def apply_discount(price,default=0.1):
    # 10% discount
    return price-(price * default)

def add_tax(amount):
    # 18% GST
    return amount * 1.18

final_price = add_tax(apply_discount(1000,0.2))
print(final_price)

def write_log():
    log = input("Enter your log message: ")

    with open("log.txt", "a") as file:
        file.write(log + "\n")

    print("Log saved successfully!")

# call function
write_log()




def get_log():
    return input("Enter your log message: ")

def write_log1(log):
    with open("log.txt", "a") as file:
        file.write(log + "\n")
    print("Log saved successfully!")

# main flow
log_data = get_log()
write_log1(log_data)