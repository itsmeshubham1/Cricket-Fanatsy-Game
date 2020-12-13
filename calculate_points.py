import sqlite3
db=sqlite3.connect("Cricket_Fandatabase.db") #connecting database
cur=db.cursor()

#fetching the data
cur.execute("SELECT * FROM match")   
rec=cur.fetchall()              

#function to calculate points
def cal_points(rec):
    points=0.0
    score=rec[1]

    #evaluate strike rate(run per balls faced)
    try:
        strike_rate=float(rec[1])/float(rec[2])

    #handling exception
    except:                     
        strike_rate=0
        

    #evaluate economy rate(run given per over)
    try:
        economy_rate=float(rec[7])/(float(rec[5])/6)

    #handling exception
    except:
        economy_rate=0
    

    fours,sixes=float(rec[3]),float(rec[4])
    wickets=10*float(rec[8])            #10 points for each wicket
    twos=int((score- 4*fours - 6*sixes)/2)
    fielding=float(rec[9])+float(rec[10])+float(rec[11]) #fielding(catch,stumping,run-out)

    """1point for each 2's & 4's
       2 point for each 6's
       10 points for fielding
       10 points for each wicket""" 
    points += (fours + 2 * sixes + 10 * fielding + twos + wickets)

    if score > 100:
        points += 10  # 10 points for century
    elif score >= 50:
        points += 5  # 5 points for half century

    if strike_rate > 1: 
        points += 4     #4 points for strike_rate>100
    elif strike_rate >= 0.8:
        points += 2  # 2 points for strike rate >= 80

    if wickets >= 5:
        points += 10  # Additional 10 points for 5 wickets
    elif wickets > 3:
        points += 5  # Additional 5 points for 3 wickets

    if economy_rate >= 3.5 and economy_rate <= 4.5:
        points += 4  # 4 points for economy rate between 3.5 and 4.5
    elif economy_rate >= 2 and economy_rate < 3.5:
        points += 7  # 7 points for economy rate between 2 and 3.5
    elif economy_rate < 2:
        points += 10  # 10 points for economy rate less than 2

    return points

                      
player_point={}     #taking dictionary for format{key:value}
for i in rec:
    player_point[i[0]]=cal_points(i)
print(player_point)

db.close()      #closing the database
                  

                  

    

    
