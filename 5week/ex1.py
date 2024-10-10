import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.font_manager as font_manager 
import seaborn as sns

def addtext(x,y): 
    for i in range(len(x)) : 
        plt.text(i,y[i]+0.5,y[i], ha = 'center') 
        
hat = pd.read_csv('ch4-1.csv') 
print(hat.head(), end = '\n\n' ) 

font_path = "malgun.ttf" 
font_name = font_manager.FontProperties(fname=font_path).get_name() 
plt.rc('font', family=font_name) 

plt.figure(figsize=(15,10)) 
plt.bar(hat['hatchery'], hat['chick'], color = ('red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple')) #  부화장 별로 병아리수 Bar차트로 표현
plt.title('hatchery statistics') 
plt.xlabel('hatchery') 
plt.ylabel('chick count') 

addtext(hat['hatchery'], hat['chick']) 

plt.show() 

print("########파이차트를 그리기 위해 비율 계산") 

pct = hat['chick']/hat['chick'].sum() 
col7 = sns.color_palette('Pastel2',7)  

plt.figure(figsize=(10,10)) 
plt.pie(pct, labels = hat['hatchery'], autopct='%.1f%%', colors =col7, counterclock = False) 
plt.show()



