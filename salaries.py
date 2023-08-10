# Load modules
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import ElasticNet
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load dataset
df = pd.read_csv(r"Elastic Net Regression/salaries.csv")  # Enter Your Path of CSV file

label_encoder = LabelEncoder()
df['Job'] = label_encoder.fit_transform(df['Job'])

# Split into Features and Prediction Variable
X = df[['Age','Job']]
y = df['Salary']

# Create training and testing vars, It’s usually around 80/20 or 70/30.
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)


# Now we’ll fit the model on the training data
model = ElasticNet(random_state=0)
model.fit(X_train, Y_train)


# Make predictions on validation dataset
predictions = model.predict(X_test)

print("Accuracy: ", model.score(X_test, Y_test))
print("r2 Score: ", r2_score(Y_test, predictions))


# Take input from user
Age = float(input("Enter Age: "))
Job = float(input("Enter Job: "))


result = model.predict([[Age, Job]])  
print("Result: ", result) 