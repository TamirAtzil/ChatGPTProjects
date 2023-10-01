import openai

def get_fun_fact(topic):
    # Initialize the OpenAI API with your API key
    openai.api_key = "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"

    # Construct the prompt for GPT
    prompt_text = f"Tell me a fun fact about {topic}."

    # Make the API call to OpenAI
    response = openai.Completion.create(
      model="text-davinci-002",  # or whatever the model endpoint is when you're using it
      prompt=prompt_text,
      max_tokens=150  # adjust based on your requirements
    )

    # Extract the joke from the response
    fact = response.choices[0].text.strip()

    return fact

# Test the function
topic = input("Enter a topic: ")
print(get_fun_fact(topic))
