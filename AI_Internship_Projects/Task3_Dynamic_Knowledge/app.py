import streamlit as st
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load knowledge files
documents = []
file_names = []

folder_path = "knowledge_base"

# Read all text files
for file in os.listdir(folder_path):

    if file.endswith(".txt"):

        file_path = os.path.join(folder_path, file)

        with open(file_path, "r", encoding="utf-8") as f:

            content = f.read()

            documents.append(content)

            file_names.append(file)

# Check if knowledge exists
if len(documents) == 0:

    st.error("No knowledge files found in knowledge_base folder!")

    st.stop()

# Create vectorizer
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(documents)

# Chatbot function
def chatbot(user_question):

    user_vec = vectorizer.transform([user_question])

    similarity = cosine_similarity(user_vec, X)[0]

    idx = similarity.argmax()

    return documents[idx]

# Streamlit UI
st.title("Dynamic Knowledge Chatbot 📚")

st.write("This chatbot updates automatically when new files are added.")

user_input = st.text_input("Ask a question:")

if st.button("Submit"):

    if user_input:

        response = chatbot(user_input)

        st.success(response)