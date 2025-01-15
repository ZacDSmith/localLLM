import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "codellama"
while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    retries = 0

    while retries < 3:
        try:
            # Send the query to the model
            response = client.generate(model=model, prompt=prompt)

            # Print the response from the model
            print("Response from Ollama:")
            print(response.response)
            break
        except Exception as e:
            retries +=1
            print("Error occurred: ", e)
        if retries >= 3:
            print("Unable to process request, try again...")
            continue