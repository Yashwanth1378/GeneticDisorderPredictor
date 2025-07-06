import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib

# Load dataset
df = pd.read_csv('Training_set.csv')

# Strip column names of extra spaces
df.columns = df.columns.str.strip()

# Drop irrelevant columns
df.drop(['Patient Id', 'Patient First Name', 'Family Name'], axis=1, inplace=True)

# Encode categorical columns
label_encoders = {}
for column in df.columns:
    if df[column].dtype == 'object':
        le = LabelEncoder()
        df[column] = df[column].astype(str).str.strip()  # clean strings
        df[column] = le.fit_transform(df[column])

        label_encoders[column] = le

# Features and target
X = df.drop('Birth defects', axis=1)  #  Changed from 'Genetic Disorder'
y = df['Birth defects']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, 'model.pkl')
joblib.dump(label_encoders, 'encoders.pkl')

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
