import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu

ctk.set_appearance_mode("System") 

# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("dark-blue") 

appWidth, appHeight = 1200, 750

# App Class
class App(ctk.CTk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.title("Xforce assignment(Sahil Bhatia)")
		self.geometry(f"{appWidth}x{appHeight}")
		self.grid_columnconfigure(0, weight=0)
		self.grid_columnconfigure(1, weight=1)

		#Heading
		self.headLabel = ctk.CTkLabel(self, text="JIRA ISSUE CREATOR", font=("Arial", 40, "bold"))
		self.headLabel.grid(row = 0, column = 0, columnspan = 4, padx=50, pady=30)

		# Name Label
		self.nameLabel = ctk.CTkLabel(self,
									text="Email")
		self.nameLabel.grid(row=1, column=0,
							padx=20, pady=20)

		# Name Entry Field
		self.nameEntry = ctk.CTkEntry(self,
						placeholder_text="JohnDoe@example.com")
		self.nameEntry.grid(row=1, column=1,
							columnspan=3, padx=50,
							pady=20, sticky= "ew")
		
		# APIKEY Label
		self.apiLabel = ctk.CTkLabel(self,
									text="API Token")
		self.apiLabel.grid(row=2, column=0,
						padx=20, pady=20,
						sticky="ew")
		
		# APIKEY Entry Field
		self.apiEntry = ctk.CTkEntry(self,
							   show="⦿",
						       placeholder_text="API key comes here")
		self.apiEntry.grid(row=2, column=1,
							columnspan=3, padx=50,
							pady=20, sticky= "ew")
		# IssueType label
		self.issueTypeLabel = ctk.CTkLabel(self, text="Type of Issue")
		self.issueTypeLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

		issue_types = ["Task", "Sub-task", "Change", "Problem", "Incident", "Post-incident review", "Service request", "Service request with approvals"]
		self.issueTypeVar = StringVar(self)
		self.issueTypeVar.set("Select Issue Type")
		self.issueTypeMenu = OptionMenu(self, self.issueTypeVar, *issue_types)
		self.issueTypeMenu.grid(row=3, column=1, columnspan=3, padx=50, pady=20, sticky="w")
        

		# Subject Label
		self.subjectLabel = ctk.CTkLabel(self, 
									text="Subject")
		self.subjectLabel.grid(row=4, column=0, 
							padx=20, pady=20,
							sticky="ew")
		
        # Subject Entry Field
		self.subjectEntry = ctk.CTkEntry(self,
							placeholder_text="Service ticket for...")
		self.subjectEntry.grid(row=4, column=1,
						columnspan=3, padx=50,
						pady=20, sticky="ew")
		
        # Description Label
		self.desLabel = ctk.CTkLabel(self, 
									text="Description:")
		self.desLabel.grid(row=5, column=0, 
							padx=20, pady=20,
							sticky="ew")

		# Text Box
		self.displayBox = ctk.CTkTextbox(self, width=200, height=100)
		self.displayBox.grid(row=6, column=0, columnspan=4,
							padx=50, pady=20, sticky="nsew")

        # Submit Button
		self.submitButton = ctk.CTkButton(self, text="Submit Ticket", font=("Arial", 25, "bold"), command=self.submit_data, width=300, height=75)
		self.submitButton.grid(row = 7, column = 0, columnspan = 4, padx=50, pady=40)
		
        # Function to collect and store data
	def submit_data(self):
		self.name = self.nameEntry.get()
		self.api_token = self.apiEntry.get()  # Assuming you need the API token
		self.issue_type = self.issueTypeVar.get()
		self.subject = self.subjectEntry.get()
		self.description = self.displayBox.get("1.0", "end-1c")  # Get all text from textbox
		
        # collecting the data
		data = {
			"name": self.name,
			"api_token": self.api_token,
			"subject": self.subject,
			"description": self.description,
			"issue": self.issue_type
        }

        # Now you can use these variables for further processing or actions
		print("Collected data:")
		print("Name:", self.name)
		print("API Token:", self.api_token)
		print("issue type", self.issue_type)
		print("Subject:", self.subject)
		print("Description:", self.description)
		
		messagebox.showinfo("Service Request Sent!", "Your service request has been sent successfully!")

        # Clear the entries for the next submission
		self.nameEntry.delete(0, "end")
		self.apiEntry.delete(0, "end")
		self.subjectEntry.delete(0, "end")
		self.displayBox.delete("1.0", "end")
		
        # import json
		import json
		with open("service_request_data.json", "w") as f:
			json.dump(data, f)
		self.quit()

if __name__ == "__main__":
	app = App()
	app.mainloop()
