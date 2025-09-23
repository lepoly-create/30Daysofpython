
'''Exercices: Day 16'''
##N1: get the current for many choose

from datetime import datetime
now = datetime.now()

print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Timestamp:", now.timestamp())

##N2: format thr current date using

formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted Date:", formatted_date)

##N3
from datetime import datetime

date_string = "5 December, 2019"
converted_date = datetime.strptime(date_string, "%d %B, %Y")
print("Converted:", converted_date)

##N4:
from datetime import datetime

now = datetime.now()
new_year = datetime(now.year + 1, 1, 1)
time_left = new_year - now
print("Time until New Year:", time_left)

##N5:
epoch = datetime(1970, 1, 1)
diff = now - epoch
print("Time since 1970:", diff)

##N6:
'''Quelques utilisations courantes :

Time series analysis : analyser des données avec dates/temps (finance, météo, etc.)

Timestamps d’événements : journalisation dans une application (logs, actions utilisateur)

Gestion de contenu : horodater des articles, des messages ou des posts de blog.

Planification : créer des rappels, compte à rebours, calendriers automatiques.'''



