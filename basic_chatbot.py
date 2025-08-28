
# Basic Chatbot


# Function to generate chatbot response
def chatbot_response(user_input):
    # convert input to lowercase for comparison
    user_input = user_input.lower()

    # Rule-based replies
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what are u doing":
        return "nothing!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

# Main chatbot function
def run_chatbot():
    print("Chatbot: Hello! You can talk to me. Type 'bye' to exit.")

    while True:
        # Take input from user
        user_input = input("You: ")

        # Get chatbot reply
        response = chatbot_response(user_input)

        # Display reply
        print("Chatbot:", response)

        # Exit if user says 'bye'
        if user_input.lower() == "bye":
            break

# Run chatbot
run_chatbot()

