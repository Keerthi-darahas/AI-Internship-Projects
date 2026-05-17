import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load papers
documents = []
titles = []

folder_path = "research_papers"

for file in os.listdir(folder_path):

    if file.endswith(".txt"):

        path = os.path.join(folder_path, file)

        with open(path, "r", encoding="utf-8") as f:

            content = f.read()

            documents.append(content)

            titles.append(file)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(documents)

# Chatbot function
def expert_chatbot(question):

    user_vec = vectorizer.transform([question])

    similarity = cosine_similarity(user_vec, X)[0]

    idx = similarity.argmax()

    return idx, similarity

# Streamlit UI
st.title("Domain Expert Research Chatbot 📘")

st.write("Ask advanced Computer Science questions.")

question = st.text_input("Enter your question:")

if st.button("Search"):

    if question:

        idx, similarity = expert_chatbot(question)

        st.subheader("Most Relevant Research Paper")

        st.success(titles[idx])

        st.subheader("Paper Summary")

        summary = documents[idx][:400]

        st.write(summary + "...")

        st.subheader("Detailed Explanation")

        st.write(documents[idx])

        # Similarity chart
        st.subheader("Concept Visualization")

        df = pd.DataFrame({
            "Paper": titles,
            "Similarity": similarity
        })

        fig, ax = plt.subplots()

        ax.bar(df["Paper"], df["Similarity"])

        plt.xticks(rotation=15)

        st.pyplot(fig)