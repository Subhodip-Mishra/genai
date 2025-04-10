import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyDzN-U1gVESxHn0m6PaAUg0s0k8w2tEkNQ")

# Load the Gemini model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",  # Use gemini-1.5-pro if your account has access
    generation_config={
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    },
    safety_settings=[
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": 2},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": 2},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": 2},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": 2},
    ],
)

# Prompt
prompt = (
    "List the top 5 San Francisco news from the past week. "
    "You must include the date of each article."
)

# Generate content
response = model.generate_content(prompt)

# Print result
print("Generated Text:\n", response.text)

# Optional: Metadata (grounding / safety ratings not always available in client SDK)
print("\nMetadata:\n", response.prompt_feedback)
