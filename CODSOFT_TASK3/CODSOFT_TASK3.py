from tkinter import *
from tkinter import messagebox

cart = {}

appetizers = {
    "Fruit Salad": 12,
    "Cocktails": 11,
    "Nuggets": 14,
    "Sandwich": 15,
    "Salad": 13
}

maincourse = {
    "Biryani": 20,
    "Kizhi parotta": 30,
    "Fried Rice": 18,
    "Sambar Rice": 24,
    "Non-veg Thali": 35
}

beverages = {
    "Milk shake": 3,
    "Iced Tea": 2,
    "Lemon Tea": 3,
    "Coffee": 5
}

# Function to add or increment items in the cart
def add_to_cart(item, item_dict):
    if item in cart:
        cart[item] += 1
    else:
        cart[item] = 1
    update_item_labels(item_dict)

# Function to decrement items in the cart
def remove_from_cart(item, item_dict):
    if item in cart:
        if cart[item] > 1:
            cart[item] -= 1
        else:
            del cart[item]
    update_item_labels(item_dict)

# Function to update item labels displaying the number of selected items
def update_item_labels(item_dict):
    for item, (label, _) in item_dict.items():
        if item in cart:
            label.config(text=str(cart[item]))
        else:
            label.config(text="0")

# Function to calculate total bill amount
def calculate_bill():
    total_bill = 0
    for item, quantity in cart.items():
        if item in appetizers:
            total_bill += appetizers[item] * quantity
        elif item in maincourse:
            total_bill += maincourse[item] * quantity
        elif item in beverages:
            total_bill += beverages[item] * quantity
    return total_bill

# Function to handle "View Cart" button click
def view_cart():
    cart_window = Toplevel(root)
    cart_window.title("Your Cart")
    cart_window.geometry("400x500")
    cart_window.resizable(False, False)
    
    # Load and place the background image
    food_image = PhotoImage(file='bgimg2.png')
    background_label = Label(cart_window, image=food_image)
    background_label.place(x=0, y=0)
    
    if not cart:
        Label(cart_window, text="Your cart is empty.", bg='orange', font=('Calibri', 30, 'bold')).pack(pady=50)
    else:
        Label(cart_window, text="Your Cart Items:", font=('Calibri', 20)).pack(pady=20)
        
        for item, quantity in cart.items():
            Label(cart_window,bg='black',fg='white',font=('Calibri',12),text=f"{item} - Quantity: {quantity}").pack()
        
        total_bill = calculate_bill()
        Label(cart_window, text=f"Total Bill: ${total_bill}", font=('Calibri', 20, 'bold')).pack(pady=20)
        
        def place_order():
            order_details = "\n".join([f"{item} - Quantity: {quantity}" for item, quantity in cart.items()])
            messagebox.showinfo("Order Placed", f"Order placed successfully!\n\n{order_details}\nTotal Bill: ${total_bill}")
            cart.clear()
            cart_window.destroy()
            update_item_labels(item_appetizer)
            update_item_labels(item_maincourse)
            update_item_labels(item_beverages)
        
        place_order_button = Button(cart_window,bg='orange',fg='white',cursor='hand2',text="Place Order",font=('Calibri', 20),command=place_order)
        place_order_button.pack(pady=20)

    cart_window.mainloop()

    
root = Tk()
root.title('Food Menu')
root.geometry('700x900+300+200')
root.configure(bg='black')
root.resizable(False, False)

img = PhotoImage(file='bgimg.png')
Label(root, image=img, bg='white').place(x=0, y=0)

heading = Label(root, text='WELCOME TO NS FOODS', fg='white', bg='black', font=('Calibri', 30, 'bold'))
heading.place(x=150, y=20)

heading1 = Label(root, text='A Multicuisine restaurant', fg='white', bg='orange', font=('Calibri', 12))
heading1.place(x=253, y=80)

heading2 = Label(root, text='APPETIZERS', fg='black', bg='orange', font=('Calibri', 15, 'bold'))
heading2.place(x=50, y=130)

heading3 = Label(root, text='MAIN COURSE', fg='black', bg='orange', font=('Calibri', 15, 'bold'))
heading3.place(x=380, y=380)

heading4 = Label(root, text='BEVERAGES', fg='black', bg='orange', font=('Calibri', 15, 'bold'))
heading4.place(x=50, y=645)

frame = Frame(root, width=250, height=170, bg='black')
frame.place(x=40, y=170)

item_appetizer = {}

for item, price in appetizers.items():
    item_frame = Frame(frame, bg='black')
    item_frame.pack(pady=5, fill='x')

    item_label = Label(item_frame, text=f"{item} - ${price:.2f}", bg='black', fg='white', width=18)
    item_label.pack(side='left', padx=(10, 5))

    decrement_button = Button(item_frame, bg='white', text="-", command=lambda item=item: remove_from_cart(item, item_appetizer))
    decrement_button.pack(side='left')

    count_label = Label(item_frame, text="0", width=3, bg='white')
    count_label.pack(side='left')

    increment_button = Button(item_frame, bg='white', text="+", command=lambda item=item: add_to_cart(item, item_appetizer))
    increment_button.pack(side='left')

    # Store the count label in the item_labels dictionary
    item_appetizer[item] = (count_label, item_frame)

frame1 = Frame(root, width=250, height=170, bg='black')
frame1.place(x=370, y=420)

item_maincourse = {}

for item, price in maincourse.items():
    item_frame = Frame(frame1, bg='black')
    item_frame.pack(pady=5, fill='x')

    item_label = Label(item_frame, text=f"{item} - ${price:.2f}", bg='black', fg='white', width=18)
    item_label.pack(side='left', padx=(10, 5))

    decrement_button = Button(item_frame, bg='white', text="-", command=lambda item=item: remove_from_cart(item, item_maincourse))
    decrement_button.pack(side='left')

    count_label = Label(item_frame, text="0", width=3, bg='white')
    count_label.pack(side='left')

    increment_button = Button(item_frame, bg='white', text="+", command=lambda item=item: add_to_cart(item, item_maincourse))
    increment_button.pack(side='left')

    # Store the count label in the item_labels dictionary
    item_maincourse[item] = (count_label, item_frame)

frame2 = Frame(root, width=250, height=150, bg='black')
frame2.place(x=40, y=680)

item_beverages = {}

for item, price in beverages.items():
    item_frame = Frame(frame2, bg='black')
    item_frame.pack(pady=5, fill='x')

    item_label = Label(item_frame, text=f"{item} - ${price:.2f}", bg='black', fg='white', width=18)
    item_label.pack(side='left', padx=(10, 5))

    decrement_button = Button(item_frame, bg='white', text="-", command=lambda item=item: remove_from_cart(item, item_beverages))
    decrement_button.pack(side='left')

    count_label = Label(item_frame, text="0", width=3, bg='white')
    count_label.pack(side='left')

    increment_button = Button(item_frame, bg='white', text="+", command=lambda item=item: add_to_cart(item, item_beverages))
    increment_button.pack(side='left')

    # Store the count label in the item_labels dictionary
    item_beverages[item] = (count_label, item_frame)

view_cart_button = Button(root,bg='orange',fg='black',text="VIEW CART",cursor='hand2',font=('Calibri', 17, 'bold'), command=view_cart)
view_cart_button.place(x=170,y=835)

root.mainloop()
