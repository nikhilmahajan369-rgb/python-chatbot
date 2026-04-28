def chatbot():

    print("🤖 AI Bot started...")
    print("Type 'bye' to exit\n")

    responses = {
        "hello": "Hi! कैसे हो?",
        "hi": "Hello😊",
        "python": "Python is a powerful language",
        "joke": "Why programmers hate nature? because it has too many bugs"
    }

    while True:
        user = input("You: ").lower().strip()

        if user == "bye":
            print("Bot: Bye! Take care 👋")
            break

        matched = False

        for key in responses:
            if key in user:
                print("Bot:", responses[key])
                matched = True
                break

        if not matched:
            print("Bot: Sorry, मैं समझ नहीं पाया 😕")

chatbot()