import re
from datetime import datetime

file = open('u.item', 'r')

with open('u_date_adjusted.item', 'a')as new_file:
    for line in file:
        #print(line)
        regex = r'\d{2}-\w{3}-\d{4}'
        match = re.search(regex, line)
        if match is not None:
            #print(match)
            date = datetime.strptime(match.group(), "%d-%b-%Y").date()
            #print(date)
           #new_date = datetime.strftime(date, "%Y-%m-%d")
            #re.sub(regex, new_date, line)
            re.sub(regex, str(date), line)
        new_file.write(line)

file.close()