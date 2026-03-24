import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

SUMMARIZER_MODEL = os.getenv("GROQ_SUMMARIZER_MODEL", "llama-3.3-70b-versatile")
RESPONSE_MODEL = os.getenv("GROQ_RESPONSE_MODEL", "llama-3.3-70b-versatile")


def _get_client_from_env(key_name: str) -> Groq:
    api_key = os.getenv(key_name) or os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError(
            f"{key_name} environment variable is not set (or set GROQ_API_KEY as fallback)"
        )
    return Groq(api_key=api_key)


def summarize_text(text: str) -> str:
    """
    Summarize the given text using Groq API (Summarizer)
    
    Args:
        text: The text to summarize
        
    Returns:
        The summarized text
    """
    try:
        summarizer_client = _get_client_from_env("GROQ_SUMMARIZER_API_KEY")
        message = summarizer_client.chat.completions.create(
            model=SUMMARIZER_MODEL,
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
        response_client = _get_client_from_env("GROQ_RESPONSE_API_KEY")
        prompt = f"Generate a helpful and relevant response to the following:\n\n{text}"
        if context:
            prompt = f"Context: {context}\n\n{prompt}"
        
        message = response_client.chat.completions.create(
            model=RESPONSE_MODEL,
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
