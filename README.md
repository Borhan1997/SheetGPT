# SheetGPT
**SheetGPT** is an application that enables you to upload a CSV file and ask questions about its content in natural language. It leverages a large language model (LLM) to generate responses based solely on the information within the document. Questions unrelated to the CSV will not be answered.

## How it works
The application reads the CSV file and processes the data. It utilizes OpenAI LLMs alongside with Langchain Agents in order to answer your questions. The CSV agent then uses tools to find solutions to your questions and generates an appropriate response with the help of a LLM.

The application employs **Streamlit** to create the graphical user interface (GUI) and utilizes **Langchain** to interact with the LLM.

## Installation
To install the repository, please clone this repository and install the requirements:
```sh
pip install -r requirements.txt
```
You will also need to add your OpenAI API key to the ```.env``` file.

## Usage
To use the application, run the main.py file with the streamlit CLI (after having installed streamlit):
```sh
streamlit run app.py
```
