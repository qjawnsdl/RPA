import pandas as pd 
import matplotlib.pyplot as plt 

def addtext(x,y): 
    for i in range(len(x)) : 
        plt.text(i,y[i]+0.5,y[i], ha = 'center') 
        
hat = pd.read_csv('singer_youtube.csv') 
print(hat.head(), end = '\n\n' ) 

plt.figure(figsize=(15,10)) 
plt.bar(hat['name'], hat['youtube count'], color = ('red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple', 'pink', 'lightblue', 'lightgreen')) #  부화장 별로 병아리수 Bar차트로 표현
plt.title('aaaaa') 
plt.xlabel('Address') 
plt.ylabel('YouTube Count') 

addtext(hat['address'], hat['youtube count']) 

plt.show() 