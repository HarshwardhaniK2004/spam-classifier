
# 📩 Spam Message Classifier

A simple Machine Learning project that classifies SMS messages as **Spam 🚫** or **Not Spam ✅** using Natural Language Processing.

---

## 🚀 Features

* Clean and simple UI using Streamlit
* Text preprocessing and vectorization using TF-IDF
* Machine Learning model using Logistic Regression
* Real-time prediction of messages

---

## 🧠 How it Works

1. Dataset of SMS messages is loaded
2. Text is cleaned (lowercase, remove symbols)
3. Converted into numerical form using TF-IDF
4. Logistic Regression model is trained
5. Model predicts whether a message is spam or not

---

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```
spam-classifier/
│── app.py
│── model.py
│── model.pkl
│── vectorizer.pkl
│── spam.csv
```

---

## ▶️ How to Run

1. Clone the repository

```
git clone https://github.com/your-username/spam-classifier.git
```

2. Go to project folder

```
cd spam-classifier
```

3. Install dependencies

```
python -m pip install pandas scikit-learn streamlit
```

4. Run the app

```
python -m streamlit run app.py
```

---

## 📊 Model Accuracy

* Achieved around **95% accuracy** on test data

---

## 📸 Output Screenshot

(Add your Streamlit app screenshot here)

---

## 📌 Future Improvements

* Add deep learning model (LSTM)
* Improve UI design
* Deploy the app online
* Add probability/confidence score

--Harshwardhani kewate

---
## Screenshot
<img width="1919" height="886" alt="Screenshot 2026-04-04 005034" src="https://github.com/user-attachments/assets/5a49d666-673d-48fb-a93b-1deb2bfe7f5c" />
<img width="1880" height="908" alt="Screenshot 2026-04-04 005144" src="https://github.com/user-attachments/assets/5801b76c-5a1d-419a-8367-c2a93189e9cd" />

⭐ If you found this useful, consider giving it a star!


## 🧠Approach

I built a Spam Message Classifier using a basic Natural Language Processing pipeline. First, I loaded the SMS dataset using pandas and performed preprocessing on the text data by converting it to lowercase and removing unnecessary symbols.

Next, I transformed the text into numerical features using TF-IDF vectorization, which helps represent the importance of words in each message.

I then trained a Logistic Regression model on the processed data to classify messages as spam or not spam. After training, I evaluated the model on test data and achieved around 95% accuracy.

Finally, I deployed the model using Streamlit, where users can input a message and get real-time predictions.
