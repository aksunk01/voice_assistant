import google.generativeai as genai
import os



#Goes to gemini and gets ai generated answers.
def general(prompt):
    key = #enter in your own password for google gemini password
    genai.configure(api_key= key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    ai_prompt = prompt
    response = model.generate_content(ai_prompt)
    message = str(response.text)
    
    
 
    #print(len((response.text)))
    return(response.text.strip())
