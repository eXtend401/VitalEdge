import google.generativeai as genai

genai.configure(api_key="AIzaSyA0Et1r6CVnYTBCfooa2AeELSxwtDFFSSE")

for model in genai.list_models():
    print(model.name, model.supported_generation_methods)