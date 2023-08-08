# Load modules
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import pandas as pd

# Load dataset
df = pd.read_csv(r"house-prices.csv")

label_encoder = LabelEncoder()
df['Brick'] = label_encoder.fit_transform(df['Brick'])    # Yes --> 1 , No --> 0
df['Neighborhood'] = label_encoder.fit_transform(df['Neighborhood'])   # East --> 0 , North --> 1 , West --> 2 


# Split into training data and test data
X = df[['SqFt','Bedrooms','Bathrooms','Offers', 'Brick', 'Neighborhood']]
y = df['Price']

# Create training and testing vars, It’s usually around 80/20 or 70/30.
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)


# Now we’ll fit the model on the training data
model = LinearRegression()
model.fit(X_train, Y_train)

predictions = model.predict(X_test)

print("Accuracy: ", model.score(X_test, Y_test))
print("r2 Score: ", r2_score(Y_test, predictions))


# Take input from user
SqFt = float(input("Enter SqFt: "))
Bedrooms = float(input("Enter Bedrooms: "))
Bathrooms = float(input("Enter Bathrooms: "))
Offers = float(input("Enter Offers: "))
Brick = float(input("Enter Brick: "))
Neighborhood = float(input("Enter Neighborhood: "))


result = model.predict([[SqFt, Bedrooms, Bathrooms, Offers, Brick, Neighborhood]])  
print("Result: ", result) 