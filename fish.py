# Load modules
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Load dataset
df = pd.read_csv(r"fish.csv")

# Split into training data and test data
X = df[['Weight','Length1','Length2','Length3', 'Height', 'Width']]
y = df['Species']

# Create training and testing vars, It’s usually around 80/20 or 70/30.
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# Now we’ll fit the model on the training data
model = DecisionTreeClassifier(random_state=0)
model.fit(X_train, Y_train)


# Make predictions on validation dataset
predictions = model.predict(X_test)

print("Accuracy: ", accuracy_score(predictions, Y_test))


# Take input from user
Weight = float(input("Enter Weight: "))
Length1 = float(input("Enter Length1: "))
Length2 = float(input("Enter Length2: "))
Length3 = float(input("Enter Length3: "))
Height = float(input("Enter Height: "))
Width = float(input("Enter Width: "))


result = model.predict([[Weight, Length1, Length2, Length3, Height, Width]])  
print("Result: ", result) 