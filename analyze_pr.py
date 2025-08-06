from langchain.chat_models import init_chat_model
import getpass
import os
os.environ["LANGCHAIN_PROJECT"] = "langchain_test" # langsmith usage
if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")


# Ref: https://github.com/BurnyCoder/llm-pr-review-gh-action/blob/main/.github/workflows/analyze_pr_diff.yml
model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")


def run_prompt(prompt, context):
    response = model.invoke(f'{prompt} given this {context}')
    return response.content


context = 'print("X"'
print(run_prompt('What are the risks of this PR?', context))
