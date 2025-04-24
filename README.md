# SheetGPT
This Python application enables you to upload a CSV file and ask questions about its content in natural language. It leverages a large language model (LLM) to generate responses based solely on the information within the document. Questions unrelated to the CSV will not be answered.

## How it works
The application processes the CSV by breaking its text into smaller chunks suitable for input into a large language model (LLM). It utilizes OpenAI embeddings to convert these chunks into vector representations. When a user asks a question, the app identifies the chunks most semantically relevant to the query and provides them to the LLM to generate a response.

The graphical interface is built with Streamlit, while Langchain is used to manage interactions with the LLM.

## Installation
To install the repository, please clone this repository and install the requirements:
```sh
pip install requirements.txt
```
You will also need to add your OpenAI API key to the ```.env``` file.

## Usage
To use the application, run the main.py file with the streamlit CLI (after having installed streamlit):
```sh
streamlit run app.py
```