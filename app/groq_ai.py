import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq clients with separate API keys
SUMMARIZER_API_KEY = os.getenv("GROQ_SUMMARIZER_API_KEY")
RESPONSE_API_KEY = os.getenv("GROQ_RESPONSE_API_KEY")

if not SUMMARIZER_API_KEY:
    raise ValueError("GROQ_SUMMARIZER_API_KEY environment variable is not set")

if not RESPONSE_API_KEY:
    raise ValueError("GROQ_RESPONSE_API_KEY environment variable is not set")

summarizer_client = Groq(api_key=SUMMARIZER_API_KEY)
response_client = Groq(api_key=RESPONSE_API_KEY)


def summarize_text(text: str) -> str:
    """
    Summarize the given text using Groq API (Summarizer)
    
    Args:
        text: The text to summarize
        
    Returns:
        The summarized text
    """
    try:
        message = summarizer_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"Please summarize the following text concisely:\n\n{text}"
                }
            ]
        )
        return message.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error summarizing text: {str(e)}")


def generate_ai_response(text: str, context: str = None) -> str:
    """
    Generate an AI response to the given text using Groq API (Response)
    
    Args:
        text: The text to respond to
        context: Optional context for better response generation
        
    Returns:
        The AI-generated response
    """
    try:
        prompt = f"Generate a helpful and relevant response to the following:\n\n{text}"
        if context:
            prompt = f"Context: {context}\n\n{prompt}"
        
        message = response_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return message.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error generating response: {str(e)}")


def analyze_email_content(email_text: str) -> dict:
    """
    Analyze email content and provide summary + suggested response
    
    Args:
        email_text: The email content to analyze
        
    Returns:
        Dictionary with summary and suggested response
    """
    try:
        summary = summarize_text(email_text)
        response = generate_ai_response(email_text, context="This is an email. Generate an appropriate response.")
        
        return {
            "summary": summary,
            "suggested_response": response
        }
    except Exception as e:
        raise Exception(f"Error analyzing email: {str(e)}")
