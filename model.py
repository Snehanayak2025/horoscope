
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text i-mport TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# Step 3: Load Dataset
df = pd.read_csv('horoscope.csv')

# Step 4: Prepare Input & Labels
X = df['description']  # Horoscope description (NLP text)
y = df['sign']         # Target label (zodiac sign)

# Step 5: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Build NLP Pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer()),       # Convert text to TF-IDF features
    ('clf', MultinomialNB())            # Naive Bayes Classifier
])

# Step 7: Train Model
model.fit(X_train, y_train)

# Step 8: Evaluate Model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Step 9: Save Model to model.pkl
joblib.dump(model, 'model.pkl')
print("✅ Model saved as model.pkl")
