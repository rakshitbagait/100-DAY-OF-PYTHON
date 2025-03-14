# 72. Function with outputs

def format_name (f_name,l_name):
    formated_f_name= f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")

    formated_f_name= f_name.capitalize()
    formated_l_name = l_name.capitalize()

    print(f"{formated_f_name} {formated_l_name}")
 
    return (f"{formated_f_name} {formated_l_name}")
a=format_name("rakshit","bAGait")

print(a)