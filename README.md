# AI_internship_project



# AI Virtual Career Counsellor 🤖🎓

## 📌 Project Overview

The **AI Virtual Career Counsellor** is an NLP-based chatbot that helps users identify suitable career paths based on their interests. It uses **Rasa** for intent classification, **NLTK** for text preprocessing, and **Streamlit** for a simple and interactive web interface.

---

## 🎯 Features

* Understands user interests using NLP
* Classifies inputs into career domains (Tech, Arts, Commerce)
* Recommends relevant career paths
* Interactive web-based chatbot UI
* Easy to train, test, and deploy

---

## 🛠️ Technologies Used

* Python
* Rasa
* NLTK
* Streamlit
* YAML

---

## 📂 Project Structure

```
├── app.py
├── requirements.txt
├── nltk_preprocessing.py
├── train_rasa.py
├── run_rasa.py
├── nlu.yml
├── domain.yml
├── stories.yml
├── config.yml
├── actions.py
├── credentials.yml
├── endpoints.yml
```

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Train Rasa Model

```bash
rasa train
```

### 3️⃣ Run Rasa Server

```bash
rasa run --enable-api --cors "*"
```

### 4️⃣ Start Streamlit App

```bash
streamlit run app.py
```

---

## 🧪 Sample Input

```
I like coding and computers
```

## 🧾 Sample Output

```
You might enjoy a career in Software Development, Data Science, or Engineering.
```

---

## 🌐 Deployment

* Streamlit frontend can be deployed using **Streamlit Cloud**
* Rasa backend can run locally or on a cloud server

---

## 👤 Author

**Made by Nikhil Kashmeeraben Rupala**

