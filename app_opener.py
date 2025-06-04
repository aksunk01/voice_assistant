import os
import google.generativeai as genai

#Need to validate the app name somehow
def opener(prompt):
    key = "AIzaSyAiofnQ6d84B7KeNFIYTuUVKjx_lvY-Xck"
    genai.configure(api_key= key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    ai_prompt = "What is the app being opened, and only give me the app name:",prompt
    response = model.generate_content(ai_prompt)
    message = str(response.text)
    
    
 
    #print(len((response.text)))
    
    return(response.text.strip())












