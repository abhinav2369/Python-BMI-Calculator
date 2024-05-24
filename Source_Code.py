# Import
from tkinter import *
from PIL import Image, ImageTk

    
# Main Window
root = Tk()
root.title("BMI Calculator")
root.resizable(False, False)
root.geometry("650x420")


# Calcuate BMI
def calculate_bmi():
    weight = float(Input_weight.get())
    height = float(Input_height.get()) / 100
    bmi = weight / (height ** 2)
    Label_result.config(text=f"Your BMI: {bmi:.2f}")

# Top Frame
Top = Frame(root)
Top.pack(pady=10,expand=False)

# Image
Logo = Image.open("logo.png")
Logo = Logo.resize((50, 50))
Logo = ImageTk.PhotoImage(Logo)
Logo_label = Label(Top, image=Logo)
Logo_label.grid(row=0,column=0,padx=10,pady=10)

# Top Label
Label_heading = Label(Top, text="BMI  CALCULATOR", font=("Arial", 24),fg="red")
Label_heading.grid(row=0,column=1)

# Main Frame
main = Frame(root)
main.pack(pady=20,expand=True)

label_weight = Label(main, text="Enter your weight (kg):", font=("Arial", 12))
label_weight.grid(row=0,column=0,pady=20,padx=20)

Input_weight = Entry(main, font=("Arial", 12))
Input_weight.grid(row=0,column=1,pady=20,padx=20)

label_height = Label(main, text="Enter your height (cm):", font=("Arial", 12))
label_height.grid(row=1,column=0,pady=20,padx=20)

Input_height = Entry(main, font=("Arial", 12))
Input_height.grid(row=1,column=1,pady=20,padx=20)

Calculate_button = Button(root,text="Calculate",font=("Arial",12,"bold"),cursor="hand2",bg="red",fg="white",relief="groove",borderwidth=2)
Calculate_button.config(command=lambda: calculate_bmi())
Calculate_button.pack(pady=20)

Label_result = Label(root,text="Your BMI is: ",font=("Arial",12))
Label_result.pack(pady=20)

# Frame
root.mainloop()
