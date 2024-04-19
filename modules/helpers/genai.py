import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyBACJs92EvOb_D_q9Awd43DRNbVTFrOTnM')

def textbased_model(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question, stream=True)
    return response

def imageandtextbased(img, text=None):
    model = genai.GenerativeModel('gemini-pro-vision')
    if not text:
        response = model.generate_content(img)
    else:
        response = model.generate_content([question, img], stream=True)
        response.resolve()
    return response

