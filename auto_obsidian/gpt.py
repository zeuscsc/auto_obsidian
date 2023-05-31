from .llm import LLM_Base
import openai
from time import sleep
import os

GPT3_MODEL = "gpt-3.5-turbo"
GPT4_MODEL = "gpt-4"
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
TECKY_API_KEY = os.environ.get('TECKY_API_KEY')
class GPT(LLM_Base):
    gpt_error_delay=2

    def switch2tecky():
        openai.api_key = TECKY_API_KEY
        openai.api_base = "https://api.gpt.tecky.ai/v1"
    def switch2openai():
        openai.api_key = OPENAI_API_KEY
        openai.api_base = "https://api.openai.com/v1"

    def model_picker():
        if TECKY_API_KEY is not None and TECKY_API_KEY != "":
            return GPT4_MODEL
        elif OPENAI_API_KEY is not None and OPENAI_API_KEY != "":
            return GPT3_MODEL
        else:
            return None

    def get_response(self,system,assistant,user):
        model=GPT.model_picker()
        if model is None:
            raise Exception("No API key found for OpenAI or Tecky")
        chat_cache=LLM_Base.load_chat_cache(model,system,assistant,user)
        if chat_cache is not None:
            if "choices" in chat_cache and len(chat_cache["choices"])>0 and "message" in chat_cache["choices"][0] and \
                "content" in chat_cache["choices"][0]["message"]:
                return chat_cache["choices"][0]["message"]["content"]
            elif "on_tokens_oversized" in chat_cache:
                e=chat_cache["on_tokens_oversized"]
                return self.instant.on_tokens_oversized(e,system,assistant,user)
            elif "result_filtered" in chat_cache:
                return None
            elif "choices" in chat_cache and len(chat_cache["choices"])>0 and "message" in chat_cache["choices"][0] and \
                "content" not in chat_cache["choices"][0]["message"]:
                LLM_Base.delete_chat_cache(model,system,assistant,user)
        if model=="gpt-3.5-turbo":
            GPT.switch2openai()
        elif model=="gpt-4":
            GPT.switch2tecky()
        print(f"Connecting to {model} model...")
        try:
            completion = openai.ChatCompletion.create(
                model=model,
                messages=[
                        {"role": "system","content": system},
                        {"role": "assistant","content": assistant},
                        {"role": "user","content": user}
                    ],
                )
            LLM_Base.save_chat_cache(model,system,assistant,user,completion)
            return completion.choices[0].message.content
        except Exception as e:
            print(e)
            if LLM_Base.detect_if_tokens_oversized(e):
                LLM_Base.save_chat_cache(model,system,assistant,user,{"on_tokens_oversized":str(e)})
                return self.instant.on_tokens_oversized(e,system,assistant,user)
            elif LLM_Base.detect_if_result_filtered(e):
                LLM_Base.save_chat_cache(model,system,assistant,user,{"result_filtered":str(e)})
                return None
            else:
                sleep(self.gpt_error_delay)
                self.gpt_error_delay=self.gpt_error_delay*2
                return self.instant.get_response(system,assistant,user)
    pass