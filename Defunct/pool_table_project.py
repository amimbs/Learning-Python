# You have just been hired by University of Houston as a developer. Your first task is to create a pool table management app which will manage the pool tables in University Center Games Room.

# Here are the requested features:

#     As an admin you should be able to see all the tables (12)

#     As an admin each table in the list should show, whether the table is OCCUPIED or NOT OCCUPIED.

#     As an admin if the table is OCCUPIED then show the start time of the table, number of minutes played. (Hardmode - If the minutes are > 60 then show them in terms of hours)

#     As an admin you can only give out the tables that are NOT OCCUPIED. This means if pool table 8 is occupied and you try to give it out then the app will print a message saying "Pool Table 8 is currently occupied".

#     As an admin whenever I close the table it should write an entry in the text file / json file. The file should be named in the following format: (11-22-2017.txt or 11-22-2017.json) keeping track of all the tables. The entry can consists of the following information:

# Pool Table Number

# Start Date Time

# End Date Time

# Total Time Played

# Cost (if you are doing the hard mode)

from datetime import datetime


class Pool_Table:
    def __init__(self, number, start_date_time = None, end_date_time = None):
        self.number = number
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
