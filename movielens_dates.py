import re
from datetime import datetime

file = open('u.item', 'r')

with open('u_date_adjusted.item', 'w') as new_file:
    for line in file:
        regex = r'\d{2}-\w{3}-\d{4}'
        match = re.search(regex, line)
        if match is not None:
            date = datetime.strptime(match.group(), "%d-%b-%Y").date()
            line = re.sub(regex, str(date), line)
        new_file.write(line)

file.close()