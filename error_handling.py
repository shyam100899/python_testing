
# try:
#     num = int(input("Enter number: "))
#     result = 10 / num

# except ValueError:
#     print("Please enter valid number")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result:", result)

# finally:
#     print("Program finished")

# def check_age(age):
#     if age < 18:
#         raise ValueError("Age must be 18+")
#     return "Allowed"

# try:
#     print(check_age(15))
# except ValueError as e:
#     print(e)


# def write_log():
#     try:
#         log = input("Enter log: ")
#         with open("log.txt", "a") as f:
#             f.write(log + "\n")
#     except Exception as e:
#         print("Error writing log:", e)

# write_log()



# def handle_exceptions():
#     try:
#         # ValueError (manual + built-in)
#         num = int(input("Enter a number: "))
        
#         if num < 0:
#             raise ValueError("Number cannot be negative")  # custom raise
#         if num == 0:
#             raise ZeroDivisionError("You cannot divide by zero")
        # ZeroDivisionError
        # result = 10 / num
        # print("Result:", result)

        # # IndexError (manual raise)
        # lst = [1, 2, 3]
        # index = int(input("Enter index to access (0-2): "))
        
        # if index >= len(lst):
        #     raise IndexError("Index out of range")  # custom raise
        
        # print("List value:", lst[index])

        # KeyError (manual raise)
        # d = {"a": 1, "b": 2}
        # key = input("Enter key (a/b): ")
        
        # if key not in d:
        #     raise KeyError("Key not found")  # custom raise
        
        # print("Dictionary value:", d[key])

        # # TypeError (manual raise)
        # x = input("Enter something: ")
        # if not x.isdigit():
        #     raise TypeError("Only numeric values allowed")  # custom raise
        
        # print("Valid input:", x)

    # except ValueError as e:
    #     print("❌ ValueError:", e)

    # except ZeroDivisionError as e:
    #     print("❌ ZeroDivisionError:", e)

    # except IndexError as e:
    #     print("❌ IndexError:", e)

    # except KeyError as e:
    #     print("❌ KeyError:", e)

    # except TypeError as e:
    #     print("❌ TypeError:", e)

    # except Exception as e:
    #     print("❌ Unknown Error:", e)

    # else:
    #     print("✅ No error occurred")

    # finally:
    #     print("🔁 Program execution completed")




# Call function
# handle_exceptions()





def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File does not exist"
    finally:
        print("Done trying to read file")

html= read_file("log.txt")
setdata =set()
html1 = html.split()
for i in html1:
    setdata.add(i)


print(setdata)
sorted_words = sorted(setdata, key=len)
print(sorted_words)