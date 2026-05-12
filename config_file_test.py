import logging
import configparser
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - Line:%(lineno)d - %(message)s"
)

config = configparser.ConfigParser()



try:
    config.read(r"C:\Users\Shyam Ji\Desktop\python _program\config_file.ini")
    per_brick_cost       = int(config["raw_material"]["bricks"])
except FileNotFoundError as e:
    print("file not found")
    

def total_bricks_count(length,width,height,wall_type='single',room=1):

    if room == 1:
        # Single room
        total_area = 2 * (length + width) * height
    
    elif room > 1:
        total_length = length * room
    
        # outer walls
        outer_area =  2 * (total_length + width) * height
        
        # inner common walls (3 walls)
        inner_area = (room - 1) * (width * height)
        
        total_area = outer_area + inner_area
    else :
        raise ValueError("Currently only 1 or 4 rooms supported")

    if wall_type.lower() =='double':
        total_no_of_bricks = total_area * 9
        return total_no_of_bricks
    else:
        total_no_of_bricks = (total_area * 4.5)
        return total_no_of_bricks

def total_cost(total_bricks_count,per_brick_cost):
    return total_bricks_count,total_bricks_count * per_brick_cost

rooms  = int(input("Enter number of rooms: "))  
length = int(input("enter your length of room "))
width  = int(input("enter your width of room "))
height = int(input("enter your height of room "))
wall_type_data = str(input("enter your wall type: single or double"))

total_bricks,result = total_cost(total_bricks_count(length,width,height,wall_type=wall_type_data,room=rooms),per_brick_cost)
print(f"total bricks for construct a room required bricks is {total_bricks} and total cost for bricks is {result}")



