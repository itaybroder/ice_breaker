from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup
if __name__ == "__main__":
    linkedin_profile_url = lookup(name="Lior Lubek")

    summery_template = """
        given the Linkedin information {information} about a person want you to create:
        1. a short summery
        2. two interesting facts about them
    """

    summery_prompt_template = PromptTemplate(
        input_variables=["information"], template=summery_template
    )

    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
        openai_api_key="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",
    )

    chain = LLMChain(llm=llm, prompt=summery_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)

    print(chain.run(information=linkedin_data))
