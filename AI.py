import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium", padding_side="left")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

def generate_response(user_input, chat_history=""):
  try:
        # Encode the new user input and concatenate with the chat history
        new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        # Append the new user input to the chat history if there is one
        if chat_history != "":
            chat_history_ids = tokenizer.encode(chat_history, return_tensors='pt')
            input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)
        else:
            input_ids = new_input_ids

        # Generate response by passing input_ids through the model
        output = model.generate(input_ids=input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        # Decode the model's output and extract the generated response
        response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

        # Return the response or a default response
        if response.strip() != '':
            return response
        else:
            return "Sorry, I don't understand."
  except Exception as e:
    print("An error occurred while generating the bot's response:")
    print(str(e))
    return "Sorry, an error occurred while generating my response. Please try again later."

# Start the conversation loop
print("Hello! I am a Dictator. You can ask me anything.")
print("Enter quit if you want to stop the Conversation!!!! ")
chat_history = ""
while True:
    user_input = input("You: ")
    if user_input == "quit":
      break
    bot_response = generate_response(user_input, chat_history)
    print("Bot: " + bot_response)
    chat_history += user_input + tokenizer.eos_token + bot_response + tokenizer.eos_token