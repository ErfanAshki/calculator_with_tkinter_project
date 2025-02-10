import tkinter as tk 

window = tk.Tk()

btn_calc_data = [
    {'text': '7',
    'command': lambda : print('7')
    }, 
    {'text': '8',
    'command': lambda : print('8')
    }, 
    {'text': '9',
    'command': lambda : print('9')
    },
    {'text': '+',
    'command': lambda : print('+')
    },
    {'text': '4',
    'command': lambda : print('4')
    },
    {'text': '5',
    'command': lambda : print('5')
    },
    {'text': '6',
    'command': lambda : print('6')
    },
    {'text': '-',
    'command': lambda : print('-')
    },
    {'text': '1',
    'command': lambda : print('1')
    },
    {'text': '2',
    'command': lambda : print('2')
    },
    {'text': '3',
    'command': lambda : print('3')
    },
    {'text': '*',
    'command': lambda : print('*')
    },
    {'text': '0',
    'command': lambda : print('0')
    },
    {'text': '.',
    'command': lambda : print('.')
    },
    {'text': 'C',
    'command': lambda : print('C')
    },
    {'text': '=',
    'command': lambda : print('=')
    },
]

btn_objects = []

for btn_data in btn_calc_data:
    button = tk.Button(
        master=window,
        text=btn_data['text'],
        command=btn_data['command'],
        height=3
    )
    btn_objects.append(button)
    
for i , btn_object in enumerate(btn_objects):
    btn_object.grid(row=(i//4) + 1 , column=i%4, sticky='nsew')


label_calc_result = tk.Label(master=window, text=0, width=30, height=3)

label_calc_result.grid(row=0, column=0, columnspan=4)



window.mainloop()
