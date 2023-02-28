import openai
import webbrowser


def askGPT(gpt_prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.7,
        max_tokens=1200,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0
        # stop=["\n"]
    )
    return (response['choices'][0]['text'])


def askdalle(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    dalleurl = response['data'][0]['url']
    webbrowser.open(dalleurl, new=0, autoraise=True)

    storetopath = r"D:\OneDrive\DALLEImageStorage"
    return (response['data'][0]['url'])
