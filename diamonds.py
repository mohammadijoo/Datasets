# Load modules
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load dataset
df = pd.read_csv(r"Lasso Regression/diamonds.csv")  # Enter Your Path of CSV file

label_encoder = LabelEncoder()
df['cut'] = label_encoder.fit_transform(df['cut'])
df['color'] = label_encoder.fit_transform(df['color'])
df['clarity'] = label_encoder.fit_transform(df['clarity'])


# Split into Features and Prediction Variable
X = df[['carat','cut','color','clarity', 'depth', 'table', 'x', 'y', 'z']]
y = df['price']

# Create training and testing vars, It’s usually around 80/20 or 70/30.
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)


# Now we’ll fit the model on the training data
model = linear_model.Lasso(alpha=0.1)
model.fit(X_train, Y_train)


predictions = model.predict(X_test)

print("Accuracy: ", model.score(X_test, Y_test))
print("r2 Score: ", r2_score(Y_test, predictions))


# Take input from user
carat = float(input("Enter carat: "))
cut = float(input("Enter cut: "))
color = float(input("Enter color: "))
clarity = float(input("Enter clarity: "))
depth = float(input("Enter depth: "))
table = float(input("Enter table: "))


result = model.predict([[carat, cut, color, clarity, depth, table]])  
print("Result: ", result) 