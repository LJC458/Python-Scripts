import time
import sys
import sqlite3
from datetime import datetime

DB_NAME = "db.sqlite"

def create_table():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
        now DATETIME,
        remote_addr TEXT,
        UserName TEXT
        ItemOrder TEXT,
        OrderPrice FLOAT,
        request_type TEXT,
        Email TEXT,
        created DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    """)
    conn.close()

def parse_line(line):
    split_line = line.split(",")
    if len(split_line) < 12:
        return []
    now = split_line[0]
    remote_addr = split_line[1]
    UserName = split_line[3]
    ItemOrder = split_line[4]
    OrderPrice = split_line[5]
    request_type = split_line[6]
    Email = split_line[7]
    created = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    return [
        now,
        remote_addr,
        UserName,
        ItemOrder,
        OrderPrice,
        request_type,
        Email,
        created
    ]

def insert_record(line, parsed):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    args = [line] + parsed
    cur.execute('INSERT INTO Orders VALUES (?,?,?,?,?,?,?,?)', args)
    print("committed")
    conn.commit()
    conn.close()

Order_FILE_A = "Order_a.txt"
Order_FILE_B = "Order_b.txt"

if __name__ == "__main__":
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
                    insert_record(line, parsed)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    finally:
        f_a.close()
        f_b.close()
        sys.exit()

