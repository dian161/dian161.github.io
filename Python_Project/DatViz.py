# Data Visualization for begginers
'''
    1. Scatterplot with Matplotlib >> Fungsi: korelasi antar 2  var dan distribusi
    2. Horizontal barchart with Pandas >> Fungsi: membandingkan dan melihat tren data
    3. Boxplot with Seaborn >> Fungsi: membandingkan dan distribusi
    4. Histogram with Plotnine (ggplot) >> Fungsi: distribusi
    5. Stacked barplot >> Fungsi: Membandingkan dan part the whole
'''
############################################################################################################
# Scatterplot 
'''
    Memiliki beberapa fitur:
    1. Linier atau nonlinier
    2. Kuat atau lemah korelasinya
    3. Positif atau negatif hubungannya

    Digunakan saat:
    1. Ingin mengetahui apakah ada hub antar 2 var
    2. Ketika var indepen memiliki beberapa nilai untuk var depen
    3. Ketika memiliki 2 var yg berpasangan dgn baik (jam kerja Vs uang yg dihasilkan)

    WARNING: jangan menggunakan scatterplot ketika too large a set of data
'''
#%%
print('------- Library -------')
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.get_dataset_names() #melihat dataset yg ada di sns
tips=sns.load_dataset('tips')
#%%
# type 1
print('------- Scatterplot Hub Antar Tips dengan Kejadian -------')
scatterplot=sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time").set(title='Tips by Time')
# typ2
print('------- Scatterplot Hub Antar Tips dengan Hari -------')
sns.relplot(data=tips, x='total_bill', y='tip', col='time', hue='day', style='day', kind='scatter').set(title='Tips by Day and divide by Time ')
#%%
'''
    Bar chart digunakan:
    1. dipake untuk kategorikal data such as kota dan genre movie
    2. digunakan untuk membandingkan antara grup dari data kategorik
'''
print('------- Barchart -------')
#barh >> untuk horizontal bar chart
plt.barh(tips['time'],tips['total_bill'],color='orange')
plt.ylabel('Time') #kategorik data untuk yticks
plt.xlabel('Total bill ($)')
plt.title('Total bill by Time')
plt.show()
# %%
# HITUNG ??
cats=['Female','Male']
tips['sex']=pd.Categorical(tips['sex'],categories=cats, ordered=True)
# %%
# MENGHITUNG JUMLAH FEMALE DAN MALE
newtip=tips.groupby(['tip','sex']).size().unstack(fill_value=0)
print(newtip)
tips.gender=newtip.sum()
print(tips.gender)
# %%
print('------- Select Data -------')
df2=tips.groupby('sex', as_index=False)['tip'].sum()
print(df2)
x=df2['sex']
y=df2['tip']
print('------- Bar Chart -------')
plt.bar(x,y,color=('red','blue'))
plt.xlabel=('Jenis Kelamin')
plt.ylabel=('Total Tip')
plt.title('Jumlah Tip Berdasarkan Jenis Kelamin')
# %%
# Melihat Total Bill di Setiap hari
print('------ Select Data (2) ------')
# long format datframe
df3=tips.groupby(['day','sex'],as_index=False)['total_bill'].sum()
print(df3)
# Diubah menjadi wide format datframe
newdf3=pd.pivot_table(data=df3, index=['day'],
                      columns=['sex'],values='total_bill')
print(newdf3)
#%%
print('------ Stacked Bar Chart ------')
sb=newdf3.plot.bar(stacked=True, color=['blue','red'])
sb.set_title('Total bill')
sb.set_xlabel('Hari')
sb.set_ylabel('Bill ($)')
sb.set_xticklabels(['Thursday','Friday','Saturday','Sunday'], rotation=0)
# %%
# Boxplot 
'''
    Boxplot guna:
    1. Memahami karakteristik dr dist data
    2. Melihat derajat penyebaran data (dilihat dr tinggi/panjang boxplot)
    3. Kesimetrisan sebaran data (dilihat dr median & whisker) 
        *simetris = data dist normal
    4. Panjang kotak menggambarkan tingkat penyebaran atau keragaman data pengamatan
        *adanya outlier pd bagian atas Boxplot diseretai Wishker bagian atas yg lbh panjang = dist data menjulur ke arah kanan (positif skewness)
        *adanya outlier pd bagian bawah Boxplot disertai Wishker bagian bawah yg lbh panjang = dist data menjulur ke arah kiri (negatif skewness)
    5. Untuk cepat mengidentifikasi nilai rata2, sebara, dan skewness dr suatu data
    
    Ukuran statistik yg bs diperoleh:
    1. Minimum
    2. Q1 = kuartil terendah atau kuartil pertama
    3. Q2 = median atau nilai pertengahan
    4. Maksimum
    5. Outlier (1.5) dan ekstrim (3) dari observasi

    Cara membandingkan Boxplot:
    1. Lihat Q2 atau middle line of IQR
    2. 
'''
#%%
print('------ Boxplot ------')
# Visualisasi
# Ingin mengetahui keragaman data dan distribusi 
sns.boxplot(x=tips['day'], y=tips['tip'],color='green').set(title='Tip Berdasarkan Hari')
# %%
# Pie chart 
'''
  **Pie chart scr default bergerak berawalan arah jarum jam, namun di MTK
    pie chart berotasi mengikuti arah jarum jam.
    untuk mengubah settingan default input 'counterclock=False'
'''
#%%
print('------ Menjumlahkan suatu value kategorik di dataset ------')
# Ingin melihat proporsi jenis kelamin yang merokok
rokok=tips.groupby(['smoker','sex'], as_index=False).size()
display(rokok)
rokok2=rokok.drop(labels=[2,3], axis=0)
#%%
print('----- Memilih salah satu baris: iloc  -----')
rokok2.iloc[0] #<< select data tanpa header atau label colomn
# %%
print('----- Pie Chart -----')
plt.pie(rokok2['size'], labels=rokok2['sex'],counterclock=False,
        autopct='%0.f%%', explode=(0,0.1), shadow=True, startangle=90)
plt.title('Jumlah Perokok')
# %%
