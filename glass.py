# Load modules
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load dataset
df = pd.read_csv(r"glass.csv")

# Split into training data and test data
X = df[['RI','Na','Mg','Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']]
y = df['Type']

# Create training and testing vars, It’s usually around 80/20 or 70/30.
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# Now we’ll fit the model on the training data
model = RandomForestClassifier(max_depth=3, random_state=0)
model.fit(X_train, Y_train)


# Make predictions on validation dataset
predictions = model.predict(X_test)

print("Accuracy: ", accuracy_score(predictions, Y_test))


# Take input from user
RI = float(input("Enter RI: "))
Na = float(input("Enter Na: "))
Mg = float(input("Enter Mg: "))
Al = float(input("Enter Al: "))
Si = float(input("Enter Si: "))
K = float(input("Enter K: "))
Ca = float(input("Enter Ca: "))
Ba = float(input("Enter Ba: "))
Fe = float(input("Enter Fe: "))

result = model.predict([[RI, Na, Mg, Al, Si, K, Ca, Ba, Fe]])  
print("Result: ", result) 