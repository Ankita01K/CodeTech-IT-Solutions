  
# 1-**SMS Spam Classification Using Machine Learning**  
![Screenshot 2024-02-18 000925](https://github.com/Ankita01K/CodeTech-IT-Solutions/assets/123232024/993877e1-2420-493e-8774-0d67ea060ee6)


# **Introduction**

**Welcome to the SMS Spam Classification project, my first task at CodTech IT Solutions during my internship. In this project, I aim to develop a machine learning model that can classify SMS messages as spam or ham (non-spam) accurately.**

# **Objective**

**The main objective of this project is to build a robust classification model that can automatically identify spam messages, thus helping users filter out unwanted or potentially harmful content.**

# **Deployment**

**The model is deployed using Streamlit and hosted on Render. You can access it here**. [https://sms-spam-classification-kj65.onrender.com/](https://sms-spam-classification-deploy.onrender.com)

# **Technologies Used**
**Python**

**pandas**

**scikit-learn**

**nltk**

**seaborn**

**matplotlib**

**Streamlit** 

**Render**

# **Dataset Description**

**The dataset used for this project, obtained from Kaggle, consists of labeled SMS messages categorized as 'ham' (non-spam) or 'spam'. It comprises 5572 messages with associated labels.**

# **Exploratory Data Analysis (EDA)**

**Investigated the distribution of 'ham' and 'spam' instances.**

**Generated word clouds for both spam and ham messages.**

**Analyzed the top 30 most common words in the spam and ham corpora.**

# **Text Preprocessing**
**Lowercased all text for consistency.**

**Tokenized messages into individual words.**

**Removed special characters, punctuation, and stopwords.**

**Applied stemming to reduce words to their root form.**

# **Model Building**
**Explored various classification algorithms including Gaussian Naive Bayes, Multinomial Naive Bayes, Bernoulli Naive Bayes, Support Vector Classifier (SVC), and Logistic Regression (LR).**

**Evaluated models based on accuracy, precision, and confusion matrices.**

**Selected the Multinomial Naive Bayes classifier as the optimal model due to its high accuracy and precision.**

# **Saving the Model**

**Saved the trained Multinomial Naive Bayes model using the pickle library for future use.**

# **Usage**

# **Clone the repository:**

**git clone** https://github.com/Ankita01K/CodeTech-IT-Solutions.git

# **Install the required dependencies:**

pip install -r requirements.txt






# 2-**Credit Card Fraud Detection Using Machine Learning**

![Screenshot 2024-02-19 224119](https://github.com/Ankita01K/CodeTech-IT-Solutions/assets/123232024/be3bf946-d106-471b-9366-e7bc44c8bff1)


## **Overview**

**This project focuses on building a model to detect fraudulent credit card transactions. It utilizes a dataset containing information about credit card transactions and experiments with algorithms like Logistic Regression, Decision Trees, and Random Forests to classify transactions as fraudulent or legitimate. This is the second  task of my internship on CodTech IT Solutions.**


# **Dataset Information**

**Features**: **The dataset consists of various features derived from PCA transformation.**

**Target** Variable: **'Class' denotes the transaction class, with 1 representing fraud and 0 representing legitimate transactions.**

# **Methodology**

**Data Preprocessing**: Checking for null values, handling duplicates, and standardizing the 'Amount' feature.

**Handling Imbalanced Datasets**: Using Synthetic Minority Oversampling Technique (SMOTE) to oversample the minority class.

**Model Building**: Training Logistic Regression, Decision Tree, and Random Forest classifiers.

**Model Evaluation**: Evaluating the performance of each model using accuracy, classification report, and confusion matrix.

**Feature Importance**: Analyzing feature importance using Random Forest classifier.

**Model Deployment**: Model Deployment: Deployed the selected model on the Streamlit using Render.

# **Model Evaluation Results**

|Model|Training Accuracy|Testing Accuracy|Precision (Class 0)|Precision (Class 1)|Recall (Class 0)|Recall (Class 1)|F1-Score (Class 0)|F1-Score (Class 1)|
|-|-|-|-|-|-|-|-|-|
|Logistic Regression	|95.87%|95.87%|0.94|0.98|0.98|0.94|0.96|0.96|
|Decision Tree|100.00%|99.82%|1.00|1.00|1.00|1.00|1.00|1.00|
|Random Forest|100.00%|99.99%|1.00|1.00|1.00|1.00|1.00|1.00|
|Random Forest (with Feature Importance)|100.00%|99.98%|1.00|1.00|1.00|1.00|1.00|1.00|

# **Deployment**
**The model is deployed on Render. You can access it here.**  [https://sms-spam-classification-kj65.onrender.com/](https://creditcarddetection.onrender.com/)

# **Technologies Used**

**Python**

**pandas**

**NumPy**

**scikit-learn**

**seaborn**

**Matplotlib**

# **Usage**

## **Clone the repository**

**git clone** https://github.com/Ankita01K/CodeTech-IT-Solutions.git

**Install the required dependencies**

**pip install** -r requirements.txt

**Run the Streamlit App**

streamlit run app.py






# 3-**Movie Genre Classification**

# **Introduction**

**This project aims to classify movie genres based on their descriptions using various machine learning algorithms. The classification of movie genres can be beneficial for content recommendation systems, movie databases, and streaming platforms**

# **Overview**

**The project involves preprocessing the movie descriptions, exploring different machine learning models, and evaluating their performance. The models considered include Multinomial Naive Bayes, Gaussian Naive Bayes, Bernoulli Naive Bayes, Logistic Regression.**

# **Dataset Information**

**The dataset used for this project is sourced from Kaggle and contains movie titles, genres, and descriptions.**

**Dataset Source**: Movie Genre Classification Dataset on Kaggle

**Description**: This dataset comprises movie titles, genres, and descriptions.

**Features**:

**Title**: Title of the movie.

**Genre**: Genre(s) of the movie.

**Description**: Description of the movie.


# **Methodology**

**Data Preprocessing**: The movie descriptions are preprocessed to remove noise, including special characters, stopwords, and stemming to normalize the text data.

**Feature Engineering**: Text features are extracted using the Term Frequency-Inverse Document Frequency (TF-IDF) vectorization technique to represent the textual information numerically.

**Model Selection**: Several machine learning algorithms are explored for genre classification, including Multinomial Naive Bayes, Gaussian Naive Bayes, Bernoulli Naive Bayes, Logistic Regression.

**Model Evaluation**: The models are evaluated based on their accuracy scores on both training and validation datasets, with confusion matrices providing additional insights into model performance.

# **Tools Used**

**Python**: Programming language used for data preprocessing and model implementation.

**NLTK (Natural Language Toolkit)**: Library for natural language processing tasks such as text preprocessing.

**Scikit-learn**: Python library for machine learning tasks including model implementation and evaluation.






