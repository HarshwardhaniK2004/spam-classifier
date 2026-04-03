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

---

## 🙌 Author

Your Name

---

⭐ If you found this useful, consider giving it a star!
