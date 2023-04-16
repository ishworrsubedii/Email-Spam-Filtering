![image](https://user-images.githubusercontent.com/45705878/232320372-4515cf34-d8cc-4063-ae99-cd371f79c7d5.png)

# Email Spam Filter using Simple Logistic Regression and Django
This project aims to build a simple email spam filter using logistic regression and deploy it using the Django web framework. The project will help you learn how to:

- Build a simple email spam filter using logistic regression
- Train the model on a dataset of spam and non-spam emails
- Deploy the model using the Django web framework
- Build a simple web interface to test the spam prediction
# Requirements
To run this project, you need to have the following:

- Python 
- Django
- NumPy
- Pandas
- Scikit-learn
- Jupyter Notebook


# Building the Spam Filter
We will build the spam filter using logistic regression. First, we will preprocess the dataset by splitting it into training and testing sets, scaling the features, and creating a feature matrix and target vector.

Then, we will fit the logistic regression model to the training data and evaluate its performance on the testing data. We will use the area under the receiver operating characteristic (ROC) curve (AUC) as our evaluation metric.

# Deploying the Spam Filter using Django
Once we have built and trained our spam filter, we will deploy it using the Django web framework. We will create a simple web interface that allows users to input an email and get a prediction of whether it is spam or not.

The Django application will consist of two main parts: the view and the template. The view will handle the user input and make predictions using the logistic regression model, and the template will display the results.

# Conclusion
By the end of this project, i have built a simple email spam filter using logistic regression and deployed it using the Django web framework. This project will give you a good introduction to building machine learning models and deploying them using web frameworks.
