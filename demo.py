import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + ", You are destined to greatness"+"!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch(share=True, share_server_address="estelinasbuffet.com:7000")