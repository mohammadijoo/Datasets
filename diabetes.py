# Load modules
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Load dataset
df = pd.read_csv(r"diabetes.csv")

# Split into training data and test data
X = df[['Pregnancies','Glucose','BloodPressure','SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
y = df['Outcome']

# Create training and testing vars, It’s usually around 80/20 or 70/30.
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# Now we’ll fit the model on the training data
model = LogisticRegression(max_iter=100000)
model.fit(X_train, Y_train)

# Make predictions on validation dataset
predictions = model.predict(X_test)

print("Accuracy: ", accuracy_score(predictions, Y_test))


# Take input from user
Pregnancies = float(input("Enter Pregnancies: "))
Glucose = float(input("Enter Glucose: "))
BloodPressure = float(input("Enter BloodPressure: "))
SkinThickness = float(input("Enter SkinThickness: "))
Insulin = float(input("Enter Insulin: "))
BMI = float(input("Enter BMI: "))
DiabetesPedigreeFunction = float(input("Enter DiabetesPedigreeFunction: "))
Age = float(input("Enter Age: "))

result = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])  
print("Result: ", result) 