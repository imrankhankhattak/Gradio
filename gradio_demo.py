import gradio as gr
from huggingface_hub import HfFolder

def add_numbers(Num1, Num2):
    return Num1 + Num2

def add_str(str1, str2):
    return str1 +" "+ str2

# Define the interface
demo = gr.Interface(
    fn=add_numbers, 
    inputs=[gr.Number(), gr.Number()], # Create two numerical input fields where users can enter numbers
    outputs=gr.Number() # Create numerical output fields
)
# Define the interface
demostr = gr.Interface(
    fn=add_str, 
    inputs=[gr.Textbox(), gr.Textbox()], # Create two string input fields where users can enter numbers
    outputs=gr.Textbox() # Create string output fields
)


# Launch the interface
demostr.launch(server_name="127.0.0.1", server_port= 7860)
