import openai
import webbrowser


def askGPT(gpt_prompt):
    """

    Args:
        gpt_prompt: User questions, text prompts etc.

    Returns: the response from gpt - the default model is davinci-003

    """
    tokenlimit = 1200
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.7,
        max_tokens=tokenlimit,
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

    # storetopath = r"D:\OneDrive\DALLEImageStorage"
    return (response['data'][0]['url'])


def chatwithGPT(gpt_prompt):
    """

    This is a new development for chatting with the latest model, 3.5

    Args:
        gpt_prompt: User questions, text prompts etc.

    Returns: the response from gpt - the default model is davinci-003

    """
    tokenlimit = 1200
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.7,
        max_tokens=tokenlimit,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0
        # stop=["\n"]
    )
    return (response['choices'][0]['text'])