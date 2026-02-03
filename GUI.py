import customtkinter as ck
from password_manager import PasswordManager

class user_gui:

    def __init__(self):
        self.pm = PasswordManager()
        self.app = ck.CTk()
        ck.set_default_color_theme("green")
        self.app.title("PasSafe")
        self.app.geometry("250x300")

        self.login_key = {
            "Create a new key": (self.pm.create_key, "Enter the name of your new key file"),
            "Load an existing key": (self.pm.load_key, "Enter the path of your key file") }
        
        self.login_password = {
            "Create a passoword file": (self.pm.create_password_file, "Enter the name of your new password file") ,
            "Load a Password file":(self.pm.load_password_file, "Enter the path of your password file")}
        
        self.passwords = {
            "Add a new password": (self.pm.add_password, "Add the website", "Add your password"),
            "Get a passowrd": (self.pm.get_password,"Which website's password? ")}

        self.main()

    def user_input(self,button_text):
        dialog = ck.CTkInputDialog(text=button_text, title="continue")
        text = dialog.get_input()
        return text

    def add_buttons(self,dictionary): 
        #creates buttons from a dictionary: name of the button, command to run, and user input message  
        for index, (label, arg) in enumerate(dictionary.items()):
           
            func = arg[0]
            button_text = arg[1]
            command = lambda f=func, b=button_text: self.execute_and_refresh(f, b)
            
            button = ck.CTkButton(self.current_frame, text=label, command=command)
            button.grid(row=index, column=0, padx=30, pady=20)
            self.app.grid_columnconfigure(0, weight=1)

    def create_screen(self, dictionary):
        
        self.current_frame = ck.CTkFrame(self.app)
        self.current_frame .pack(expand=True, fill="both", padx=10, pady=10)

        self.add_buttons(dictionary)
    
    def clear_screen(self):
        self.current_frame.destroy()
    
    def execute_and_refresh(self, function, button_text):

        data = self.user_input(button_text)
        #runs the necessary Password Manager function if user does not click "cancel"
        if data:
            function(data)

            self.clear_screen()

    def main(self):

        self.create_screen(self.login_key)
        self.create_screen(self.login_password)



gui = user_gui()

gui.app.mainloop()





