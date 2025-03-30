import os
import google.generativeai as genai  

# Get API key from environment variable  
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure API
genai.configure(api_key=API_KEY)  

def get_gemini_response(user_query):  
    model = genai.GenerativeModel("gemini-pro")  
    response = model.generate_content(user_query)  
    return response.text  
