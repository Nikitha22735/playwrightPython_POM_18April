# 1. sqlite
import sqlite3

import pytest

@pytest.mark.dbHandling
def test_sqlite():
    try:
        dataTable = sqlite3.connect("C:\\Users\\Nikitha\\AppData\\Roaming\\DBeaverData\\workspace6\\.metadata\\sample-database-sqlite-1\\Chinook.db")
        editor = dataTable.cursor()
        editor.execute("select * from Album")
        # print(editor.fetchall())
        # print(editor.fetchone())
        # print(editor.fetchmany(5))
        results = editor.fetchall()
        print(len(results))
        # print(editor.description)
        titles = editor.description
        for i in range(0,len(titles)):
            print(titles[i][0])

        for i in titles:
            print(i[0])
    
    finally:
        editor.close()
        dataTable.close()

# =========================================================MYSQL==========================================
# pip install mysql-connector-python

# import mysql.connector
# def test_MySql():
#     try:
#         dataTable = mysql.connector.connect(
#             host="localhost",
#             port=3306,
#             database="MM0123",
#             user=os.getenv("usname"),
#             password=os.getenv("pw")

#         )
#         editor = dataTable.cursor()
#         editor.execute("select * from Album")
#         # print(editor.fetchall())
#         # print(editor.fetchone())
#         # print(editor.fetchmany(5))
#         results = editor.fetchall()
#         print(len(results))
#         # print(editor.description)
#         titles = editor.description
#         for i in range(0,len(titles)):
#             print(titles[i][0])

#         for i in titles:
#             print(i[0])
    
#     finally:
#         editor.close()
#         dataTable.close()


# # =========================================================Postgress==========================================
# # pip install pycopg2-binary

# import pycopg2
# def test_postGress():
#     try:
#         dataTable = pycopg2.connect(
#             host="localhost",
#             port=3306,
#             database="MM0123",
#             user=os.getenv("usname"),
#             password=os.getenv("pw")

#         )
#         editor = dataTable.cursor()
#         editor.execute("select * from Album")
#         # print(editor.fetchall())
#         # print(editor.fetchone())
#         # print(editor.fetchmany(5))
#         results = editor.fetchall()
#         print(len(results))
#         # print(editor.description)
#         titles = editor.description
#         for i in range(0,len(titles)):
#             print(titles[i][0])

#         for i in titles:
#             print(i[0])
    
#     finally:
#         editor.close()
#         dataTable.close()



# # =======================================MongoDB==================================================
# from pymongo import MongoClient
# import os

# @pytest.mark.dbHandling
# def test_mongodb():
#     try:
#         # Connect (similar to mysql.connector.connect)
#         dataTable = MongoClient("mongodb://localhost:27017/")
        
#         # Select database and collection
#         database = dataTable["MM0123"]
#         collection = database["Album"]
        
#         # Execute query
#         editor = collection.find()  # Equivalent to cursor.execute()
        
#         # Fetch results
#         results = list(editor)
#         print(len(results))
        
#         # Get field names (equivalent to editor.description)
#         if results:
#             titles = list(results[0].keys())
#             for i in range(0, len(titles)):
#                 print(titles[i])
            
#             for i in titles:
#                 print(i)
    
#     finally:
#         dataTable.close()


# # ==========================================oracle=============================================
# ##pip install oracledb

# import oracledb
# def test_oracledb():
#     try:
#         dataTable = oracledb.connect(
#             host="localhost",
#             port=3306,
#             service_name="MM0123",
#             user=os.getenv("usname"),
#             password=os.getenv("pw")

#         )
#         editor = dataTable.cursor()
#         editor.execute("select * from Album")
#         # print(editor.fetchall())
#         # print(editor.fetchone())
#         # print(editor.fetchmany(5))
#         results = editor.fetchall()
#         print(len(results))
#         # print(editor.description)
#         titles = editor.description
#         for i in range(0,len(titles)):
#             print(titles[i][0])

#         for i in titles:
#             print(i[0])
    
#     finally:
#         editor.close()
#         dataTable.close()


# # ==========================================snowflake=============================================
# ##pip install snowflake-connector-python

# import snowflake.connector
# def test_snowflake():
#     try:
#         dataTable = snowflake.connector.connect(
#             host="localhost",
#             port=3306,
#             database="MM0123",
#             user=os.getenv("usname"),
#             password=os.getenv("pw"),
#             warehouse="warehouse",
#             schema="PUBLIC",
#             Role="SYSADMIN"

#         )
#         editor = dataTable.cursor()
#         editor.execute("select * from Album")
#         # print(editor.fetchall())
#         # print(editor.fetchone())
#         # print(editor.fetchmany(5))
#         results = editor.fetchall()
#         print(len(results))
#         # print(editor.description)
#         titles = editor.description
#         for i in range(0,len(titles)):
#             print(titles[i][0])

#         for i in titles:
#             print(i[0])
            
#         assert len(titles)==3
    
#     finally:
#         editor.close()
#         dataTable.close()
