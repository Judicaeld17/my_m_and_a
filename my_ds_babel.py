import sqlite3
import csv
from io import StringIO
import pandas as pd
def sql_to_csv(database,table_name):
    connection = sqlite3.connect(database)
    requete = f"SELECT * FROM {table_name}"
    sql_data_to_df = pd.read_sql(requete,connection)
    return sql_data_to_df.iloc[:-1,:].to_csv(index=False)

def csv_to_sql(csv_content,database,table_name):
    data_list=[]
    # with open(csv_content,'r') as csv_file:
    csv_io = StringIO(csv_content)
    csv_reader = csv.reader(csv_io)
    for row in csv_reader:
        data_list.append(row)
    col_names = data_list[0]
    data =[ data_list[row_num] for row_num in range(1,len(data_list)) ]
#     print(col_names,data[10])
    try:
        connection =sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute(f"""
        CREATE TABLE "{table_name}" (
            "{col_names[0]}" TEXT,
            "{col_names[1]}" TEXT,
            "{col_names[2]}" TEXT,
            "{col_names[3]}" TEXT,
            "{col_names[4]}" TEXT,
            "{col_names[5]}" TEXT,
            "{col_names[6]}" TEXT);
        """)
        for row in data:
            cursor.execute(f""" INSERT INTO "{table_name}" ("{col_names[0]}","{col_names[1]}","{col_names[2]}","{col_names[3]}","{col_names[4]}","{col_names[5]}","{col_names[6]}")
            VALUES(?,?,?,?,?,?,?);
            """, (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print("SQLite error:",e)

# print("==========")
# def _main():
#     print(sql_to_csv('all_fault_line.db','fault_lines'))
#     csv_content = open("list_volcano.csv")
#     csv_to_sql(csv_content,"list_volcanos.db","volcanos")
# _main()
# print("==========")