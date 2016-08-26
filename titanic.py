# Загружаем необходимые библиотеки
import pandas
#import matplotlib.pyplot as plt
#import os

# Загрузите датасет titanic.csv и осмотрите.
data = pandas.read_csv("../titanic.csv", index_col="PassengerId")
#print(data.head())

# -------- Задание №1 --------
# Какое количество мужчин и женщин ехало на корабле?
male = data['Sex'].value_counts()[0]
female = data['Sex'].value_counts()[1]
# В качестве ответа приведите два числа через пробел.
print(male, female)

# -------- Задание №2 --------
# Какой части пассажиров удалось выжить? Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен), округлив до двух знаков.
print (((data['Survived'].value_counts()[1]/data['Survived'].count()) * 100).round(2))

# -------- Задание №3 --------
# Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров. В качестве ответа приведите два числа через пробел.
print (data['Age'].mean().round(2), data['Age'].median())

# -------- Задание №4 --------
# Коррелируют ли число братьев/сестер/супругов с числом родителей/детей? Посчитайте корреляцию Пирсона между признаками SibSp и Parch.
print(data['SibSp'].corr(data['Parch'],method='pearson').round(2))

# -------- Задание №5 --------
# Какое самое популярное женское имя на корабле? Извлеките из полного имени пассажира (колонка Name) его личное имя (First Name). Это задание — типичный пример того, с чем сталкивается специалист по анализу данных. Данные очень разнородные и шумные, но из них требуется извлечь необходимую информацию. Попробуйте вручную разобрать несколько значений столбца Name и выработать правило для извлечения имен, а также разделения их на женские и мужские.
AllName = data['Name'][data['Sex']=="female"].str.split(" ",expand=True)
MissName = AllName.loc[(AllName[1]=="Miss.")|(AllName[2]=="Miss.")|(AllName[3]=="Miss.")][2]
AllMrsName = AllName.loc[(AllName[1]=="Mrs.")|(AllName[2]=="Mrs.")|(AllName[3]=="Mrs.")].fillna('missing')

MrsName = pandas.Series()
for i in range(len(AllMrsName.columns)):
    MrsName=MrsName.append(AllMrsName[i].loc[AllMrsName[i].str.contains("^\(.*")].str.replace("^\(","").str.replace("\)",""))

#print(MissName)
WomanName = MrsName.append(MissName)

print(WomanName.value_counts().head(1))






