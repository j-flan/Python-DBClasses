"""
File survey.py
Accesses the demographics data in a sqlite3 survey database
"""

import sqlite3


class Survey:
    """Represents survey information contained in a Demographic table"""
    
    def __init__(self, database):
        """Constructor creates a Survey object and connects to a
        Survey database using the input database parameter. 
        A cursor is also initialized to execute queries and hold the data.
        Initializes a List for use in retrieving demographic information."""
        self.__databaseName = database
        self.__conn = sqlite3.connect(database)
        self.__cur = self.__conn.cursor()
        self.__demographicList = list()

    def __str__(self):
        """Returns the database name"""
        return "Connected to "+str(self.__databaseName)
    
    def getConn(self):
        """Returns the database connection for use by child class objects"""
        return self.__conn       

    def clearDemographicList(self):
        """Clears the demographicList for reuse"""
        self.__demographicList.clear()

    def getNumberOfPersonIDs(self):
        """Returns the total number of people who took the survey"""
        self.__cur.execute('Select count(PersonID) from Demographics')
        total = 0
        for row in self.__cur:
            total = row
        return total

    def getNumberByDemographic(self, userDemographic):
        """Returns a copy of the demographicList, filled with the number of
        people in a particular demographic.
        Example: if userDemographic = "Gender", demographicList will contain
        a list of tuples with the number of females and males who took the survey"""
        self.clearDemographicList()
        self.__cur.execute("Select "+userDemographic+", count(?) from demographics group by "
                           +userDemographic,(userDemographic,) )
        for row in self.__cur:
            self.__demographicList.append(row)
        return self.__demographicList


