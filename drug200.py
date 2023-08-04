# Load modules
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
#from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load dataset
df = pd.read_csv(r"Naive Bayes/drug200.csv")

label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])
df['BP'] = label_encoder.fit_transform(df['BP'])
df['Cholesterol'] = label_encoder.fit_transform(df['Cholesterol'])
print(df.head())

# Split into training data and test data
X = df[['Age','Sex','BP','Cholesterol', 'Na_to_K']]
y = df['Drug']

# Create training and testing vars, It’s usually around 80/20 or 70/30.
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# Now we’ll fit the model on the training data
model = GaussianNB()
model.fit(X_train, Y_train)

# Make predictions on validation dataset
predictions = model.predict(X_test)

print("Accuracy: ", accuracy_score(predictions, Y_test))

#Take input from user
Age = float(input("Enter Age (between 15 and 75): "))
Sex = float(input("Enter Sex (0 or 1): "))
BP = float(input("Enter BP (0 or 1 or 2): "))
Cholesterol = float(input("Enter Cholesterol (0 or 1): "))
Na_to_K = float(input("Enter Na_to_K (between 6.2 and 38.3): "))

result = model.predict([[Age, Sex, BP, Cholesterol, Na_to_K]])  
print("Result: ", result)