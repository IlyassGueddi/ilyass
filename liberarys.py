import openai

# OpenRouter DeepSeek free model with hardcoded API key
openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

# Loop to ask multiple questions
while True:
    user_input = input("Ask a question (or type 'exit' to quit): ")

    if user_input.lower() in ["exit", "quit", "q"]:
        print("Goodbye!")
        break

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change the model if needed
            headers={
                "HTTP-Referer": "https://your-site-url.com",  # Optional
                "X-Title": "Your Site Name",  # Optional
            },
            messages=[
                {"role": "user", "content": user_input}
            ],
            max_tokens=1000,
        )

        print("\nAssistant:", completion.choices[0].message["content"], "\n")

    except Exception as e:
        print("Error:", e)
