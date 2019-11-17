# File: ypsurvey.py
# Author: Jeff Flanegan
# Date: 11-16-2019
# CSC 217
# Final Project

import sqlite3 # import sqlite3 library
from survey import Survey # import Survey class

# inherit survey class
class YPSurvey(Survey):
    
    # constructor creates database object
    def __init__(self, db):

        # inherit Survey class constructor
        Survey.__init__(self, db) 
        
        # call Database connection from Survey class connection
        self.db = db
        self.conn = self.getConn() 
        self.cur = self.conn.cursor()

        #output database connection
        print("\n",Survey.__str__(self))
        
    # This accesses the database and queries all phobias along with the count of rows associated with all phobias
    # Each row is the associated Person to the phobia, as each person has selected possibly several phobias.
    # The output is a list of phobias followed by the number of people who selected them (count).
    def phobiaCount(self):

        #query phobia and count of phobia
        self.cur.execute('SELECT Phobia, COUNT(Phobia) AS Count\
            FROM Phobias\
            GROUP BY Phobia\
            ORDER BY count DESC')

        #get number of people in the study
        j = self.getNumberOfPersonIDs()
        j= int(j[0])
        print("\nIn a study of", j,"people:")

        # print column headers
        print()
        for col in self.cur.description:
            print (col[0], end="               ")
        print()

        # print rows of data
        for key, val in self.cur:
            #format for ease of view 
            print(f"{key:<15}{val:>10}")
        print()
         
    # This asks the user to select a Phobia and a Demographic. The output is the percentage
    # of total persons who have the associated phobia, and separated by the demographic choice.
    # If you were to separate by Gender, you will see the total percentage of males as well
    # as the total percentage of females by the chosen phobia.
    # For Example: There are 108 males who have a phobia of Heights in this survey,
    # 116 / 409(total males in survey) = 0.264, *100 = 26.4, int(26.4) = 26%.
    # Hence, 26% of males in this study are afraid of Heights.
    def phobiaDemo (self):

        # user input
        phobia = input("Select Phobia\n")
        group = input("Select Group: Gender, Age, Education\n")
        print()

        # Query database for phobia and demographic using user input.
        # This will return the data grouped by Demographic, followed
        # by the number of people in that group who have the phobia chosen.
        self.cur.execute("SELECT "+group+", COUNT(Demographics.PersonID) AS Percent\
            FROM Demographics JOIN Phobias ON Demographics.PersonID = Phobias.PersonID\
            WHERE Phobia = ?\
            GROUP BY "+group,(phobia,))
        
        # output title of chart
        print('\nPercentage of people who fear',phobia,'by', group, '\n')

        # print column headers
        for col in self.cur.description:
            print (col[0], end="               ")
        print()
        
        # This returns the number of people involved in the study,
        # grouped by their demographic, then makes an array of the number of people 
        # per demographic group. This will match with the query, as the phobia
        # query is returned in same order, since they are both grouped by the same demographic
        y = self.getNumberByDemographic(group)
        z =[]
        for key, val in y:
            z.append(val)

        # Print rows of data, taking the count of the persons per group as val,
        # dividing this number by the number of total people in the demographic group,
        # and multiplying this number by 100 to get the percentage of people
        # in the study who are a part of the chosen group with the chosen phobia.
        # Using integer division, we get a whole number as a percent.
        i = 0
        for key, val in self.cur: 
            #format output for ease of view
            print(f"{key:<16}{int((val/z[i])*100):>10}%")
            i+=1
        print()