# Load modules
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import pandas as pd

# Load dataset
df = pd.read_csv(r"iris.csv")

# Split into training data and test data
X = df[['sepal_length','sepal_width','petal_length','petal_width']]
y = df['classification']

# Create training and testing vars, It’s usually around 80/20 or 70/30.
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# Now we’ll fit the model on the training data
model = SVC(gamma='auto')
model.fit(X_train, Y_train)

# Make predictions on validation dataset
predictions = model.predict(X_test)

print("Accuracy: ", accuracy_score(predictions, Y_test))

# Take input from user
sepal_length = float(input("Enter sepal_length (between 4 and 8): "))
sepal_width = float(input("Enter sepa_width (between 2 and 5): "))
petal_length = float(input("Enter petal_length (between 1 and 7): "))
petal_width = float(input("Enter petal_width (between 0.1 and 3): "))

result = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])  # input must be 2D array
print("Result: ", result)