import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



dataframe = pd.read_csv('/Users/douglasmacsweeney/Documents/Assignment/PycharmFiles/Data/FPL_dataset.csv')
result = dataframe
sorted_results = result.sort_values(by=['Points','Player'], ascending=False)

finalnumbers = (sorted_results[0:6])

print(finalnumbers)

x1 = finalnumbers['Player']
y1 = finalnumbers['Points']

plot1 = plt.figure(1)
plot1.suptitle("Fantasy Premier League 19/20 - Top Players & Points Contributed")

plt.bar(x1, y1)

plt.xlabel('Player', color='grey')
plt.ylabel('Points', color='grey')
plt.grid(color='grey', linestyle='--', linewidth=1, axis='y', alpha=0.4)
plt.show()

plot2 = plt.figure(2)
plot2.suptitle("Top Goalscorers")

sorted_results1 = result.sort_values(by=['Goals_Scored','Player','Min_Played' ,'Shots_On_Target'], ascending=False)
playersgoals = (sorted_results1[0:5])
print(playersgoals)



x2 = playersgoals['Player']
y2 = playersgoals['Goals_Scored']
plt.scatter(x2,y2 , color= 'r')
plt.grid(color='grey', linestyle='--', linewidth=1, axis='y', alpha=0.4)
plt.plot(x2,y2)

plt.xlabel('Player' , color= 'grey')
plt.ylabel('Goals Scored', color= 'grey')
plt.show()

plot3 = plt.figure(3)
plot3.suptitle("Most Goals Scored by which Team")

TeamID = np.array(['Leicester','Arsenal','Liverpool','Man City','Southampton'])
plt.xlabel('Teams' , color= 'grey')
plt.ylabel('Goals Scored', color= 'grey')
plt.bar(TeamID , y2 , color= 'purple')
plt.show()


sorted_results1 = result.sort_values(by=['Assists','Player'], ascending=False)
sorteddf = (sorted_results1[0:9])

plot3 = plt.figure(3)
plot3.suptitle("Most Assists by Players")

plt.scatter(sorteddf.Player,sorteddf.Assists)
plt.xlabel('Players' , color= 'grey')
plt.ylabel('Assists', color= 'grey')
sns.set()
plt.show()
