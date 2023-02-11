import os
import openai
import gradio as gr

# Cole sua API da openAI aqui
openai.api_key = ""


start_sequence = "\nAI:"
restart_sequence = "\nHuman:"

prompt = " Fale com a inteligência artificial\nHuman:"

def openai_create(prompt):
        response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        temperature = 0.9,
        max_tokens = 3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["Human:", "AI:"]
        )
        return response.choices[0].text


def chatbot_clone(input, history):
    history = history or []
    s = list(sum(history,()))
    s.append(input)
    inp = ''.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>Criando chatBot com API Openai e usando Gradio</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("ENVIAR")
    submit.click(chatbot_clone, inputs = [message,state], outputs=[chatbot,state])

block.launch(debug=True)
