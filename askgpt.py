import openai

def askGPT(gpt_prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.7,
        max_tokens=1200,
        top_p=1,
        frequency_penalty= 0.0,
        presence_penalty= 0.0
        #stop=["\n"]
    )
    return(response['choices'][0]['text'])

def askdalle(prompt):


    return("hello")