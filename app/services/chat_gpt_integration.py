import openai

from settings import settings


class ChatGPTIntegration:
    """
    Class to integrate with the OpenAI API.
    """
    @classmethod
    def chat_response(self, question):
        """
        Method to get the response from the OpenAI API.

        :param question: The question to ask the OpenAI API.
        """

        openai.api_key = settings.GPT_API_KEY

        response = openai.ChatCompletion.create(
            model=settings.GPT_MODEL_ENGINE,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "system", "content": "I am here to assist you with any questions you have."},
                {"role": "user", "content": question},
            ],
            max_tokens=settings.GPT_MAX_TOKENS,
            temperature=settings.GPT_TEMPERATURE,
        )

        return response["choices"][0]["message"]
