from requests import api
from decouple import config

class ChatService:

    @classmethod
    def make_question(cls, question: str) -> str:
        """Make a question to chat gpt and get its answer.

        Args:
            question (str): Question to make to chatgpt.

        Returns:
            str: answer by chatgpt.
        """
        try:
            res = api.post(
                url= "https://api.openai.com/v1/chat/completions",
                headers= {
                    "Authorization": f"Bearer {config('OPENAI_API_KEY')}",
                    "Content-Type": "application/json",
                },
                json= {
                    "model": "gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": question}],
                }
            )
            if res.status_code == 200:
                data = res.json()
                answer = data["choices"][0]["message"]["content"]

                return f"{answer} \n\nObtenido por #T-GPT"
            else:
                print("Something wrong with response")
                return ""
            
        except Exception as ex:
            print(ex)
            print(type(ex))
            return ""