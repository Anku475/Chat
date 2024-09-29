import requests
import json



# API endpoint
api_url = "https://llama.us.gaianet.network/v1/chat/completions"  # Ensure this is correct

# Chatbot function
def chatbot(message):
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ],
        "model": "model_name"  # Replace with your actual model name
    }

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    try:
        # POST request using requests
        response = requests.post(api_url, headers=headers, data=json.dumps(payload), verify=False)

        # Debugging: Print the response status and text
        print(f"Response Status: {response.status_code}")
        print(f"Response Text: {response.text}")

        # Check if the response is successful
        if response.status_code == 200:
            return response.json().get("choices")[0]["message"]["content"]
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except requests.exceptions.SSLError as e:
        print(f"SSL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage: Chatbot interaction
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    bot_response = chatbot(user_input)
    print(f"Bot: {bot_response}")



