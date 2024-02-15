  
# **SMS Spam Classification Using Machine Learning**  


# **Introduction**

**Welcome to the SMS Spam Classification project, my first task at CodTech IT Solutions during my internship. In this project, I aim to develop a machine learning model that can classify SMS messages as spam or ham (non-spam) accurately.**

# **Objective**
**The main objective of this project is to build a robust classification model that can automatically identify spam messages, thus helping users filter out unwanted or potentially harmful content.**

# **Deployment**

**The model is deployed using Streamlit and hosted on Render. You can access it here**.[ https://sms-spam-classification-kj65.onrender.com/]

# **Technologies Used**
**Python**
**pandas**
**scikit-learn
**nltk**
**seaborn
**matplotlib
**pickle**
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
git clone https://github.com/you/sms-spam-classification.git

# **Install the required dependencies:**
pip install -r requirements.txt
