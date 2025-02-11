import tkinter as tk 

window = tk.Tk()

label_calc_result = tk.Label(master=window, text='0', width=30, height=3)

label_calc_result.grid(row=0, column=0, columnspan=4)


def check_dot_in_decimal_numbers(current):
    for char in current[::-1]:
        if char == '.':
            return True
        elif char in ['+', '-', '*']:
            return False
        
    return False


def insert_number_in_label_calc_result(btn_text):
    current = label_calc_result['text'] 

    if btn_text == 'C':
        label_calc_result['text'] = '0'
        
    elif current == '0':
        label_calc_result['text'] = btn_text
        
    elif btn_text == '=':
        label_calc_result['text'] = str(eval(current))
        
    elif btn_text == '.':
        if not check_dot_in_decimal_numbers(current):
            label_calc_result['text'] += btn_text
    
    elif btn_text in ['+', '-', '*'] and current[-1] in ['+', '-', '*']:
        label_calc_result['text'] = current[: -1] + btn_text
            
    else:
        label_calc_result['text'] += btn_text
    
    

btn_calc_data = [
    {'text': '7',
    'command': lambda : insert_number_in_label_calc_result('7')
    }, 
    {'text': '8',
    'command': lambda : insert_number_in_label_calc_result('8')
    }, 
    {'text': '9',
    'command': lambda : insert_number_in_label_calc_result('9')
    },
    {'text': '+',
    'command': lambda : insert_number_in_label_calc_result('+')
    },
    {'text': '4',
    'command': lambda : insert_number_in_label_calc_result('4')
    },
    {'text': '5',
    'command': lambda : insert_number_in_label_calc_result('5')
    },
    {'text': '6',
    'command': lambda : insert_number_in_label_calc_result('6')
    },
    {'text': '-',
    'command': lambda : insert_number_in_label_calc_result('-')
    },
    {'text': '1',
    'command': lambda : insert_number_in_label_calc_result('1')
    },
    {'text': '2',
    'command': lambda : insert_number_in_label_calc_result('2')
    },
    {'text': '3',
    'command': lambda : insert_number_in_label_calc_result('3')
    },
    {'text': '*',
    'command': lambda : insert_number_in_label_calc_result('*')
    },
    {'text': '0',
    'command': lambda : insert_number_in_label_calc_result('0')
    },
    {'text': '.',
    'command': lambda : insert_number_in_label_calc_result('.')
    },
    {'text': 'C',
    'command': lambda : insert_number_in_label_calc_result('C')
    },
    {'text': '=',
    'command': lambda : insert_number_in_label_calc_result('=')
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


def modify_data(btn_text):
    current = label_calc_result['text']
    
    if btn_text == 'M':
        current = current[: -1]
        label_calc_result['text'] = current
        

btn_modify = tk.Button(master=window, text='M', height=3, command=lambda : modify_data('M'))

btn_modify.grid(row=5, column=0, columnspan=5, sticky='nsew')

window.mainloop()
