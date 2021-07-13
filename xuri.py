import matplotlib.pyplot as plt
import pandas as pd

suicide = pd.read_csv('/root/dvexp/suicide.csv')
suicide_10_15 = suicide[(suicide['year'] >= 2010) & (suicide['year'] <= 2015)] 
suicide_top5 = suicide_10_15.groupby('country')['suicides_no'].sum().sort_values(ascending = False).head(5)
country_top5 = suicide_top5.index

pop = []
data = pd.Series([])
for i in country_top5:
    pop = suicide_10_15[suicide_10_15['country']==i].groupby(['year','country'])
    pop = pop['suicides_no'].sum()
    data = pd.concat([data,pop])
    # print(pop.values)
colors = ['#DDDDFF','#7D7DFF','#0000C6','#000079','#CEFFCE']
print(colors[0])
for year in range(2010,2016):
    bot = 0
    y=0
    for j in country_top5:
        plt.bar(year,data[year,j],align='center',bottom=bot,label=j,color=colors[y])
        bot=bot+data[year,j]
        y+=1
plt.legend()
plt.xlabel('year')
plt.ylabel('自杀人数')
plt.show()

houseinfo=data['houseinfo'].values
df=pd.DataFrame()
for i in houseinfo:
    l=i.split('|')
    d={'户型':l[0],'面积':l[1],'朝向':l[2],'装修风格':l[3],'共几层':l[4],'类型':l[5]}
    df=df.append(d,ignore_index=True)
data=data.join(df)
data=data.drop('houseinfo',axis=1)