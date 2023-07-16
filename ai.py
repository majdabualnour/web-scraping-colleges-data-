import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"quit",
        ["Bye! Take care."]
    ],
    [
        r"(.*)",
        ["Sorry, I can only respond to predefined patterns."]
    ]
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)
print("ChatBot: Hi, How can I assist you today?")
while True:
    user_input = input("User: ")
    response = chatbot.respond(user_input)
    print("ChatBot:", response)
