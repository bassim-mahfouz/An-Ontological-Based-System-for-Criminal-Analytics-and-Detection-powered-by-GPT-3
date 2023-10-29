import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.Completion.create(
    engine ="text-davinci-003",
    prompt = prompt ,
    max_tokens =50,
    n =1 ,
    stop = None , 
    temperature =0.8 ,
    )
    return response.choices[0].text.strip()