import sqlite3 as sq
cricket=sq.connect("Cricket_Fandatabase.db")        #Creating database for storing player's data
cur=cricket.cursor()

#Creating match table
cur.execute('''create table if not exists match(
Player TEXT NOT NULL,
Scored INTEGER,
Faced INTEGER,
Fours INTEGER,
Sixes INTEGER,
Bowled INTEGER,
Maiden INTEGER,
Given INTEGER,
Wkts INTEGER,
Catches INTEGER,
Stumping INTEGER,
"Ro*" INTEGER);
''' )

#Creating stats table
cur.execute('''create table if not exists stats(
Player PRIMARY KEY,
Matches INTEGER,
Runs INTEGER,
"100s" INTEGER,
"50s" INTEGER,
Value INTEGER,
Ctg TEXT NOT NULL); 
''')

#Creating teams table
cur.execute('''create table if not exists teams(
Name TEXT NOT NULL,
Players TEXT NOT NULL,
Value INTEGER);
''')

#Adding data to match table by taking input from user

while True:
    opt1=input("Add data to match table [y/n]: ")
    opt=opt1.title()            #title function so that lowercase also supported
    if opt=='Y':
        print("Player's information:-")
        print()
        val=[input("Name: ")]
        val.append(int(input("Scored: ")))      #append function so that data is inserted at the end.
        val.append(int(input("Faced: ")))
        val.append(int(input("Fours: ")))
        val.append(int(input("Sixes: ")))
        val.append(int(input("Bowled: ")))
        val.append(int(input("Maiden: ")))
        val.append(int(input("Given: ")))
        val.append(int(input("Wkts: ")))
        val.append(int(input("Catches: ")))
        val.append(int(input("Stumping: ")))
        val.append(int(input("RO*: ")))

        #To catch exceptions
        try:
            cur.execute("INSERT INTO match(Player,Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wkts,Catches,Stumping,'Ro*')VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                    (val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7],val[8],val[9],val[10],val[11]))
            cricket.commit()
            print("Data added successfully.")

        #To handle the exceptions
        except:                                             
            print("The following data can't be inserted.")
            print("Sorry for the incovinence.")
            cricket.rollback()
            
#Adding data to stats table by taking input from user
        print()
        print("Add data to player's stats table:-")
        print()
        val.append(int(input("Matches: ")))
        val.append(int(input("Runs: ")))
        val.append(int(input("100s: ")))
        val.append(int(input("50s: ")))
        val.append(int(input("Value: ")))
        val.append(input("Category as(BAT,BWL,AR,WK): "))

        #To catch exceptions
        try:
            cur.execute("INSERT INTO stats(Player,Matches,Runs,'100s','50s',Value,Ctg)VALUES(?,?,?,?,?,?,?)",
                        (val[0],val[12],val[13],val[14],val[15],val[16],val[17]))
            cricket.commit()
            print("Data added successfully.")

         #To handle the exceptions   
        except:
            print("The following data can't be inserted.")
            print("Sorry for the incovinence.")
            cricket.rollback()
            
    elif opt=='N':
        break
    
    else:
        print("Please give valid option.")
        continue
        

cur.close()     #closing the cursor
cricket.close() #Closing the database
