import pandas as pd
import matplotlib.pyplot as plt

#survival 0 = no , 1 = yes
#pclass -> Ticket class 1st,2nd,3rd
#sibsp -> of siblings / spouses aboard the Titanic   0 none , 1 one brother or husband , 2 with two
#parch -> of parents / children aboard the Titanic   0 none , 1 one child or parent , 2 with two
#embarked -> C= cherbourg , Q=Queenstown , S=southampton


#Load the Data
df=pd.read_csv('titanic.csv',index_col='PassengerId')

#print(df.isnull().sum())  to check for null values in each column
#print(df.head()) to print first 5 elements
#print(df.info()) to print num (of columns & rows & non-null & storage)
#print(df)


#Data Cleaning

#######i put the median in the ages nulls'##########
df['Age']=df['Age'].fillna(df['Age'].median())  #replace the null values with the median
#print(df.isnull().sum())  #to check for null values in each column after removing null ages



#######i put the Backward Fill in the Embarked nulls'##########
df['Embarked']=df['Embarked'].bfill()
#print(df.isnull().sum())


#######i deleted the cabin column because it is more than the half nulls ###############
df = df.drop('Cabin',axis=1)
#print(df.isnull().sum())




#Exploratory Data Analysis (EDA)


#print(df.info()) 
#print(df.describe().to_string()) 
#print(df['Survived'].value_counts())
#print(df['Pclass'].value_counts()
#print(df.groupby("Sex")["Survived"].mean())              #sex with surviving mean
#print(pd.crosstab(df['Pclass'],df['Survived']) )         #class with surviving

ss=df.groupby(['Sex','Pclass'])["Survived"].mean()                      #grouping the class with sex and surviving
print("The Mean of Surviving classified by gender and class:\n",ss)   
sc=df[df['Age']<12]['Survived'].mean()                  #the survived children under 18
print("The Mean of survived children under 12: \n",sc)      
fs=df.groupby("Fare")["Survived"].mean()                #the fares  
print("The Fares and survived mean: \n",fs)   

df["FareGroup"] = pd.cut(df["Fare"],3)
fgs=df.groupby("FareGroup")["Survived"].mean()
print("The Mean of every Fare  who survived:\n",fgs)                    #Fare Groups survived
Es=df.groupby("Embarked")["Survived"].mean()
print("The Mean of every Embarked people who survived:\n",Es)           #Embarked survived
sibsp=df.groupby("SibSp")["Survived"].mean()
print("The Mean of every siblings and spouses people who survived:\n",sibsp)        #siblings and spouses survived
parch=df.groupby("Parch")["Survived"].mean()
print("The Mean of every parents and children people who survived:\n",parch)        #parents and children survived

#Visulaization




ss.unstack().plot(kind='bar',color=['skyblue', 'salmon', 'lightgreen'])
plt.title("Survival Rate by Sex and Class")
plt.ylabel("Survival Rate")
plt.tight_layout()
plt.show()


fgs.plot(kind='bar',color=['skyblue', 'salmon', 'lightgreen'])
plt.title("Survival Rate by Fare Group")
plt.ylabel("Survival Rate")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

Es.plot(kind='bar',color=['skyblue', 'salmon', 'lightgreen'])
plt.title("Survival Rate by Embarked Location")
plt.ylabel("Survival Rate")
plt.xticks(
    ticks=[0,1,2],
    labels=["Cherbourg (C)", "Queenstown (Q)", "Southampton (S)"]
)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

sibsp.plot(kind='bar',color=['skyblue', 'salmon', 'lightgreen', 'orange', 'purple', 'cyan', 'magenta'])
plt.title("Survival Rate by siblings & spouses aboard")
plt.ylabel("Survival Rate")
plt.grid(axis='y')
plt.tight_layout()
plt.show()


parch.plot(kind='bar',color=['skyblue', 'salmon', 'lightgreen', 'orange', 'purple', 'cyan', 'magenta'])
plt.title("Survival Rate by parents & children aboard")
plt.ylabel("Survival Rate")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

