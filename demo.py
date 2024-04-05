import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + ", You are destined to greatness"+"!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
    server_name="0.0.0.0"
)

demo.launch()