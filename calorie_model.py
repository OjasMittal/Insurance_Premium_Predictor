import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import r2_score

df = pd.read_csv('data.csv')
X = df[['Gender','Age','Height','Weight','Duration','Heart_Rate','Body_Temp']]
y = df['Calories']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2)
model = RandomForestRegressor()
model.fit(X_train,y_train)
# y_pred = model.predict(X_test)
# r2_score(y_test,y_pred)
pickle.dump(model,open('model.pkl','wb'))