# File: main.py
# Author: Jeff Flanegan
# Date: 11-16-2019
# CSC 217
# Final Project

from ypsurvey import YPSurvey # import YPSurvey class

# create database object using the YPSurvey constructor,
# which inherits the Survey constructor
p = YPSurvey('YoungPeopleFinal.db')

# This is the program driver and loops through the main menu
# as long as the user does not choose 3, which exits the loop and ends the program 
choice = 0
while choice != 3:

    #user input
    choice = int(input("Main Menu\n1.Number of people with specific phobias\n2.Percentage of people with phobia by demographic\n3.Quit\n"))
    
    #list output of phobias associate with total count
    if choice == 1:
        p.phobiaCount()

    #list output of phobia percentage by demographic
    if choice == 2: 
        p.phobiaDemo()