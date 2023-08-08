# Load modules
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load dataset
df = pd.read_csv(r"stars.csv")

label_encoder = LabelEncoder()

df['Color'] = label_encoder.fit_transform(df['Color'])
df['Spectral_Class'] = label_encoder.fit_transform(df['Spectral_Class'])
#print(df.head())

# Split into training data and test data
X = df[['Temperature','L','R','A_M', 'Color', 'Spectral_Class']]
y = df['Type']

# Create training and testing vars, It’s usually around 80/20 or 70/30.
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# Now we’ll fit the model on the training data
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, Y_train)


# Make predictions on validation dataset
predictions = model.predict(X_test)

print("Accuracy: ", accuracy_score(predictions, Y_test))


#Take input from user
Temperature = float(input("Enter Temperature: "))
L = float(input("Enter L: "))
R = float(input("Enter R: "))
A_M = float(input("Enter A_M : "))
Color = float(input("Enter Color: "))
Spectral_Class = float(input("Enter Spectral_Class: "))

result = model.predict([[Temperature, L, R, A_M, Color, Spectral_Class]])  
print("Result: ", result)