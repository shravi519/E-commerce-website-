import pandas as pd 
from sklearn import tree 
from sklearn.preprocessing import LabelEncoder 
from sklearn.naive_bayes import GaussianNB 
data = pd.read_csv('Downloads\data3.csv') 
print("The first 5 values of data is :\n",data.head()) 
X = data.iloc[:,:-1] 
print("\nThe First 5 values of train data is\n",X.head()) 
y = data.iloc[:,-1] 
print("\nThe first 5 values of Train output is\n",y.head()) 
le_outlook = LabelEncoder() 
X.Outlook = le_outlook.fit_transform(X.Outlook) 
le_temperature = LabelEncoder() 
X.Temperature = le_temperature.fit_transform(X.Temperature) 
le_humidity = LabelEncoder() 
X.Humidity = le_humidity.fit_transform(X.Humidity) 
le_wind = LabelEncoder() 
X.Wind = le_wind.fit_transform(X.Wind) 
print("\nNow the Train data is :\n",X.head()) 
le_PlayTennis = LabelEncoder() 
y = le_PlayTennis.fit_transform(y) 
print("\nNow the Train output is\n",y) 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20) 
classifier = GaussianNB() 
classifier.fit(X_train,y_train) 
from sklearn.metrics import accuracy_score 
print("Accuracy is:",accuracy_score(classifier.predict(X_test),y_test))