from langchain_experimental.agents import create_csv_agent
from langchain_community.llms import OpenAI
from dotenv import load_dotenv

class Processing():

    def get_answer(self, doc, question):
        load_dotenv()
        llm = OpenAI(temperature=0)
        agent = create_csv_agent(llm, doc, verbose = False, allow_dangerous_code=True)

        return agent.run(question)
