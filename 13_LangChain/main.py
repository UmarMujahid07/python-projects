import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from local env file
load_dotenv()

# Initialize the Gemini chat model with the correct API parameters
language_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Initialize standard output parser to convert model responses into plain strings
output_parser = StrOutputParser()

# Define prompt template for initial story generation
story_prompt_template = ChatPromptTemplate.from_template("write a short story(of 100 words) on {topic}")

# Construct processing chain for story creation
story_generation_chain = story_prompt_template | language_model | output_parser

# Execute story generation chain for the given topic
selected_topic = "a robot learning to cook"
generated_story = story_generation_chain.invoke({"topic": selected_topic})
print("Generated Story:")
print(generated_story)
print()

# Define prompt template to summarize the generated text
summary_prompt_template = ChatPromptTemplate.from_template("summarize this in one sentence: {story_text}")

# Construct processing chain for summarization
summarization_chain = summary_prompt_template | language_model | output_parser

# Execute summarization chain using the generated story text
story_summary = summarization_chain.invoke({"story_text": generated_story})
print("Story Summary:")
print(story_summary)
print()

# Define prompt template to translate the summary into Roman Urdu
translation_prompt_template = ChatPromptTemplate.from_template("Translate into Roman Urdu: {summary_text}")

# Construct processing chain for translation
translation_chain = translation_prompt_template | language_model | output_parser

# Execute translation chain using the story summary
translated_summary = translation_chain.invoke({"summary_text": story_summary})
print("Roman Urdu Translation:")
print(translated_summary)