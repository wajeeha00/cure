import openai
class ChatBot:
    def __init__(self):
        openai.api_key = "sk-8"
   
    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150,
            #diversity but sacrificing accuracy
            temperature=0.5
        ).choices[0].text.strip()
        return response
 
if __name__ == "__main__":
    chatbot = ChatBot()
    while True:
        user_input = "hello"
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")