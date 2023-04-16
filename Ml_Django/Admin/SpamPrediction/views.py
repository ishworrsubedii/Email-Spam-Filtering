from django.shortcuts import render
from joblib import load
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load and preprocess the dataset
dataset = pd.read_csv(
    'C:/Users/ACER/Desktop/Spam/spam.csv', encoding='ISO-8859-1')
dataset = dataset.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1)
dataset = dataset.rename(columns={'v1': 'category', 'v2': 'message'})
dataset.loc[dataset['category'] == 'spam', 'category'] = 1
dataset.loc[dataset['category'] == 'ham', 'category'] = 0

X_train = dataset.message
Y_train = dataset.category

# Create a TfidfVectorizer object and transform the input messages
vectorizer = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
x_train_tfidf = vectorizer.fit_transform(X_train)

# Load the pre-trained model
model = load(
    "C:/Users/ACER/Desktop/Spam Filtering Using Classification/model.joblib")

# Define the views


def index(request):
    return render(request, 'index.html')


def modeleprediction(request):
    if request.method == 'POST':
        message = request.POST['message']
        message_list = [message]  # Create a list containing the message
        # Pass the list to the transform method
        namee = vectorizer.transform(message_list)
        model_prediction = model.predict(namee)
        if model_prediction[0] == 1:
            model_prediction = 'Spam'
            print(model_prediction)
        else:
            model_prediction = 'Not Spam '
            print(model_prediction)

        return render(request, 'index.html', {'result': model_prediction})

    return render(request, 'index.html')
