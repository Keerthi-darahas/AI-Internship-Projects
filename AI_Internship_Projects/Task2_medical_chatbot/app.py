import streamlit as st
import os
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Store questions and answers
questions = []
answers = []

# Dataset folder
folder_path = "MedQuAD-master"

# Read all XML files
for root, dirs, files in os.walk(folder_path):

    for file in files:

        if file.endswith(".xml"):

            file_path = os.path.join(root, file)

            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:

                    data = f.read()

                # Parse XML
                soup = BeautifulSoup(data, "xml")

                qas = soup.find_all("QAPair")

                for qa in qas:

                    q = qa.find("Question")
                    a = qa.find("Answer")

                    if q and a:

                        q_text = q.text.strip()
                        a_text = a.text.strip()

                        if q_text != "" and a_text != "":

                            questions.append(q_text)
                            answers.append(a_text)

            except:
                pass

# Check dataset loaded
if len(questions) == 0:

    st.error("Dataset not loaded properly!")
    st.stop()

# Reduce size for speed
questions = questions[:5000]
answers = answers[:5000]

# Create vectorizer
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(questions)

# Chatbot function
def medical_chatbot(user_question):

    user_vec = vectorizer.transform([user_question])

    similarity = cosine_similarity(user_vec, X)[0]

    idx = similarity.argmax()

    # If similarity too low
    if similarity[idx] < 0.1:

        return "Sorry, I could not find a matching medical answer."

    return answers[idx]

# Streamlit UI
st.title("Medical Chatbot 🏥")

st.write("Ask any medical question below.")

user_input = st.text_input("Enter your question:")

if st.button("Submit"):

    if user_input:

        response = medical_chatbot(user_input)

        st.success(response)