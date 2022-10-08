import tkinter as tk
import math
from simpletransformers.model import TransformerModel
from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pickle



window = tk.Tk()
window.title('FNC-2022TISF')
window.geometry('800x600')
window.configure(background='white')

def calculate_bmi_number():
    height = str(height_entry.get())
    weight = str(weight_entry.get())
    
    with open('D:/programing/programing_created-acer/fnc-1/train_/fnc_roberta_0115_self1.pkl', 'rb') as f:
        model = pickle.load(f)
    predictions, raw_outputs = model.predict([height, weight])
    
    

    result_label.configure(text=predictions)

header_label = tk.Label(window, text='FNC-2022TISF')
header_label.pack()
a = tk.Label(window, bg='white',text="")
a.pack(side=tk.TOP)
height_frame = tk.Frame(window, height=8)
height_frame.pack(side=tk.TOP)
height_label = tk.Label(height_frame, font=("Lucida Grande", 20), text='Sentence A')
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(height_frame, width=70)
height_entry.pack(side=tk.LEFT)
a = tk.Label(window, bg='white',text="")
a.pack(side=tk.TOP)
weight_frame = tk.Frame(window)
weight_frame.pack(side=tk.TOP)
weight_label = tk.Label(weight_frame, font=("Lucida Grande", 20), text='Sentence B')
weight_label.pack(side=tk.LEFT)
weight_entry = tk.Entry(weight_frame, width=70)
weight_entry.pack(side=tk.LEFT)

result_label = tk.Label(window, bg='white')
result_label.pack()

calculate_btn = tk.Button(window, text='RUN!!!', command=calculate_bmi_number)
calculate_btn.pack()

window.mainloop()