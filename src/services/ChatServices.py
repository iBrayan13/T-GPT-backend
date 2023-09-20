import openai
from decouple import config

openai.api_key = config("OPENAI_API_KEY")

class ChatService:
    GPT_ENGINE = config("GPT_ENGINE")

    @classmethod
    def make_question(cls, question: str) -> str:
        """Make a question to chat gpt and get its answer.

        Args:
            question (str): Question to make to chatgpt.

        Returns:
            str: answer by chatgpt.
        """
        try:
            completion = openai.Completion.create(
                engine= cls.GPT_ENGINE,
                prompt= question,
                max_tokens= 2048
            )

            return completion.choices[0].text
            
        except Exception as ex:
            print(ex)
            return ""