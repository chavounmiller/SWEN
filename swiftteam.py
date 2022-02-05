import mysql.connector as mysql

#variables
host = "swiftdb-cluster.cluster-cj9xsjwre8ky.us-east-2.rds.amazonaws.com"
user = "admin"
password = ""

#connect to mysql
try:
    db = mysql.connect(host=host,user=user,password=password,database="packages")
    print("Connected successfully")
except Exception as e:
    print(e)
    print("Failed to connect")

    
command_handler = db.cursor()

def logpackage():
    name = input("Name: ")
    trackingnumber = input("Tracking Number: ")
    weight = input("Weight: ")
    description = input("Description: ")
    sql = "INSERT INTO ship1 (Name, TrackingNumber, Weight, Description) VALUES (%s, %s, %s, %s)"
    val = (name, trackingnumber, weight, description)
    try:
        command_handler.execute(sql,val)
    except Exception as e:
        print(e)
    
    print("package was entered into database")
    db.commit()

def searchpackage(x):
    command_handler.execute("SELECT * from ship1")
    records= command_handler.fetchall()
    for record in records:
        if(x in record):
            print("\n The package you searched for is ",record)
            return record

def editpackage():
    x = input("Search for the package you would like to edit using TrackingNumber")
    edit = input("What would you like to edit? Enter Name, TrackingNumber, Weight, or Description")
    change = input("Change it to what?")
    command_handler.execute("UPDATE ship1 SET "+edit+"='"+change+"' WHERE TrackingNumber='"+x+"'")

    

    db.commit()

def deletepackage():
    x = input("Search for the package you would like to delete using TrackingNumber")
    command_handler.execute("DELETE FROM ship1 WHERE TrackingNumber='"+x+"'")
    db.commit()

def generatemanifest():
    command_handler.execute("SELECT * from ship1")
    records = command_handler.fetchall()
    print("\nMANIFEST DOCUMENT\n")
    for record in records:
        print(record)
    command_handler.execute("SELECT COUNT(Weight) FROM ship1")
    totalpkg = command_handler.fetchall()
    print("total packages ",totalpkg)
    command_handler.execute("SELECT SUM(Weight) FROM ship1")
    totalweight = command_handler.fetchall()
    print("total weight ",totalweight)

command_handler.execute("SHOW TABLES")
print("showing all tables in the database")
for table in command_handler:
    print(table)

#showing values in table

command_handler.execute("SELECT * from ship1")
records = command_handler.fetchall()
print("displaying records\n")
for record in records:
    print(record)

searchpackage('1z1234')
generatemanifest()
