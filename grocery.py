import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from docx import Document
from prompts import *
import io
# import os

# Load environment variables
load_dotenv()

st.title("Shopping List Wizard")

doc_file = st.file_uploader("Upload a file")  

def read_word_file_from_upload(uploaded_file):
    """Read Word document from Streamlit uploaded file"""
    doc = Document(uploaded_file)
    parts = []

    # Paragraphs
    for para in doc.paragraphs:
        if para.text.strip():
            parts.append(para.text)

    # Tables
    for table in doc.tables:
        for row in table.rows:
            row_data = [cell.text.strip() for cell in row.cells]
            parts.append(" | ".join(row_data))

    return "\n".join(parts)

# Process uploaded file
if doc_file is not None:
    # Read the uploaded file
    doc_text = read_word_file_from_upload(doc_file)
    
    st.write("📄 **File uploaded successfully!**")

    # Show processing status
    st.write("🔄 **Processing your menu...**")
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Raw list of ingredients - 3 rounds

    # Round 1
    with st.spinner("Raw list of ingredients 1/3 running..."):
        response = client.chat.completions.create(
            model="gpt-5",
            reasoning_effort="low", 
            messages=[
                {"role": "system", "content": raw_ingredients_system_prompt},
                {"role": "user", "content": doc_text}
            ]
        )
    
    raw_answer1 = response.choices[0].message.content
    
    # Round 2
    with st.spinner("Raw list of ingredients 2/3 running..."):
        response = client.chat.completions.create(
            model="gpt-5",
            reasoning_effort="low", 
            messages=[
                {"role": "system", "content": raw_ingredients_system_prompt},
                {"role": "user", "content": doc_text}
            ]
        )
    
    raw_answer2 = response.choices[0].message.content

    # Round 3
    with st.spinner("Raw list of ingredients 3/3 running..."):
        response = client.chat.completions.create(
            model="gpt-5",
            reasoning_effort="low", 
            messages=[
                {"role": "system", "content": raw_ingredients_system_prompt},
                {"role": "user", "content": doc_text}
            ]
        )

    raw_answer3 = response.choices[0].message.content

    # Final raw list of ingredients
    with st.spinner("Final raw list of ingredients running..."):
        response = client.chat.completions.create(
            model="gpt-5",
            reasoning_effort="low", 
            messages=[
                {"role": "system", "content": clean_raw_ingredients_system_prompt},
                {"role": "user", "content": f"Cписок 1: {raw_answer1}\nCписок 2: {raw_answer2}\nCписок 3: {raw_answer3}"}
            ]
        )
    final_raw_answer = response.choices[0].message.content
    
    # Normalized list of ingredients
    with st.spinner("Normalized list of ingredients running..."):
        response = client.chat.completions.create(
            model="gpt-5",
            reasoning_effort="low", 
            messages=[
                {"role": "system", "content": normalized_ingredients_system_prompt},
                {"role": "user", "content": final_raw_answer}
            ]
        )
    normalized_answer = response.choices[0].message.content


    # Grouped list of ingredients
    with st.spinner("Grouped list of ingredients running..."):
        response = client.chat.completions.create(
            model="gpt-5",
            reasoning_effort="low", 
            messages=[
                {"role": "system", "content": grouped_ingredients_system_prompt},
                {"role": "user", "content": normalized_answer}
            ]
        )
    grouped_answer = response.choices[0].message.content
      
    # Counts of ingredients
    with st.spinner("Counts of ingredients running..."):
        response = client.chat.completions.create(
            model="gpt-5",
            reasoning_effort="low", 
            messages=[
                {"role": "system", "content": counts_system_prompt},
                {"role": "user", "content": f"Menu: {doc_text}\nGrouped list of ingredients: {grouped_answer}"}
            ]
        )
    counts_answer = response.choices[0].message.content

    st.write("✅ **Counts of ingredients generated!**")
    st.text_area("Counts of ingredients", counts_answer, height=400)

else:
    st.write("👆 Please upload a Word document (.docx) to get started!")