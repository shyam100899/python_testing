import logging
import configparser
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - Line:%(lineno)d - %(message)s"
)

config = configparser.ConfigParser()


try:
    config.read(r"C:\Users\Shyam Ji\Desktop\python _program\config_file.ini")
    book_prices = {
        "science": int(config["book_price"]["science"]),
        "math": int(config["book_price"]["math"]),
        "history": int(config["book_price"]["history"]),
        "physics": int(config["book_price"]["physics"]),
        "biology": int(config["book_price"]["biology"]),
        "chemistry": int(config["book_price"]["chemistry"])
    } 
except FileNotFoundError as e:
    print("file not found")

student_details={1:["math","history"],
                 2:["biology","chemistry"],
                 3:["science"]}

def book_price_calculate(student_details):
    result ={}
    for student, subjects in student_details.items():
        total = 0
       
        for sub in subjects:
            total += book_prices.get(sub, 0)  # safe lookup
        


        if len(subjects) >= 2:
            discount_price = total - (total * 10 / 100)
            result[student] = discount_price
        else: 
            result[student] = total   # added this line
        
    return result
          

p = book_price_calculate(student_details)
for student,total_cost in p.items():
     print(f"Student {student} and total cost = {total_cost}")