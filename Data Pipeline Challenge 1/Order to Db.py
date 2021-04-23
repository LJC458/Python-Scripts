import time
import sys
import sqlite3
from datetime import datetime
import pdb



DB_NAME = "NewDB.sqlite"

def create_table():
    conn = sqlite3.connect(DB_NAME)

    if conn.execute("""
    CREATE TABLE IF NOT EXISTS OrdersTable2 
    (
        remote_addr TEXT,
        UserName TEXT,
        ItemOrder TEXT,
        OrderPrice FLOAT,
        request_type TEXT,
        Email TEXT
      )
    """):
        print('success')
    else:
        print('failed')

    print(conn.execute("Select * from OrdersTable2 ").fetchall())
    
    conn.close()

def parse_line(line):
    split_line = line.split(",")
    remote_addr = split_line[1]
    UserName = split_line[2]
    ItemOrder = split_line[3]
    OrderPrice = split_line[4]
    request_type = split_line[5]
    Email = split_line[6]
    #created = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    # returns empty list for some reason using '2021-04-22 19:25:10.039912, 193.70.117.63 , JaredWilliams4 , Jeans , 10.0 , PUT, JaredWilliams4@email.com'

    return [
        remote_addr,
        UserName,
        ItemOrder,
        OrderPrice,
        request_type,
        Email,
        # created
    ]

def insert_record(parsed):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    args = parsed
    #breakpoint()
    cur.execute('INSERT INTO OrdersTable2(remote_addr,UserName,ItemOrder,OrderPrice,request_type,Email) VALUES (?,?,?,?,?,?)', args)
    conn.commit()
    conn.close()

Order_FILE_A = "Order_a.txt"
Order_FILE_B = "Order_b.txt"

if __name__ == "__main__":
    #pdb.set_trace()
    create_table()
    try:
        f_a = open(Order_FILE_A, 'r')
        f_b = open(Order_FILE_B, 'r')
        while True:
            where_a = f_a.tell()
            line_a = f_a.readline()
            where_b = f_b.tell()
            line_b = f_b.readline()

            if not line_a and not line_b:
                time.sleep(1)
                f_a.seek(where_a)
                f_b.seek(where_b)
                continue
            else:
                if line_a:
                    line = line_a
                else:
                    line = line_b

                line = line.strip()
                parsed = parse_line(line)
                if len(parsed) > 0:
                    insert_record(parsed)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    finally:
        f_a.close()
        f_b.close()
        sys.exit()

