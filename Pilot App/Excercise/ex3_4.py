from pymongo import MongoClient
import matplotlib.pyplot as plt 
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_database()

customers = db["customers"]

group1 = customers.find({"ref":'events'}).count()
group2 = customers.find({"ref":'ads'}).count()
group3 = customers.find({"ref":'wom'}).count()


 
# Data to plot
labels = 'Events', 'Advertisements', 'Word ofMouth'
sizes = [group1, group2, group3]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()