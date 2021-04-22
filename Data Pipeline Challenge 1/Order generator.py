
#Order generator taken from https://github.com/dataquestio/analytics_pipeline/blob/master/Order_generator.py

from faker import Faker
from datetime import datetime
import random
import time

LINE = """\
{now}, {remote_addr} , {UserName} , {ItemOrder} , {OrderPrice} , {request_type}, {Email}
"""

Order_FILE_A = "Order_a.txt"
Order_FILE_B = "Order_b.txt"
Order_MAX = 100

def generate_Order_line():
    fake = Faker()
    now = datetime.now()
    remote_addr = fake.ipv4()
    Name = fake.name()+ str(random.randrange(0,10,1))
    UserName= Name.replace(" ","") 
    ItemOrder = random.choice(["Tshirt", "Jeans", "Shoes"])
    OrderPrice = random.choice([5.00, 10.00, 12.00])
    request_type = random.choice(["GET", "POST", "PUT"])
    Email = UserName + "@email.com"

    Order_line = LINE.format(
        now = now,
        remote_addr = remote_addr,
        UserName = UserName,
        ItemOrder = ItemOrder,
        OrderPrice = OrderPrice,
        request_type = request_type,
        Email = Email
    )

    return Order_line

def write_Order_line(Order_file, line):
    with open(Order_file, "a") as f:
        f.write(line)
        f.write("\n")

def clear_Order_file(Order_file):
    with open(Order_file, "w+") as f:
        f.write("")

if __name__ == "__main__":
    current_Order_file = Order_FILE_A
    lines_written = 0

    clear_Order_file(Order_FILE_A)
    clear_Order_file(Order_FILE_B)

    while True:
        line = generate_Order_line()

        write_Order_line(current_Order_file, line)
        lines_written += 1

        if lines_written % Order_MAX == 0:
            new_Order_file = Order_FILE_B
            if current_Order_file == Order_FILE_B:
                new_Order_file = Order_FILE_A

            clear_Order_file(new_Order_file)
            current_Order_file = new_Order_file

        sleep_time = random.choice(range(1, 5, 1))

        time.sleep(sleep_time)