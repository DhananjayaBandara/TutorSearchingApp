class Tutor:
    def __init__(self, name, subject, rate):
        self.name = name
        self.subject = subject
        self.rate = rate
    
    def __str__(self):
        return f"Name: {self.name}, Subject: {self.subject}, Rate: ${self.rate}/hr"
    
class TutorApp:
    def __init__(self):
        self.tutors = []
    
    def add_tutor(self):
        name = input("Enter tutor's name: ")
        subject = input("Enter subject taught by tutor: ")
        rate = float(input("Enter hourly rate: "))
        
        self.tutors.append(Tutor(name, subject, rate))
        print(f"Tutor {name}  added successfully.")
        
    def search_tutor(self):
        subject = input("Enter subject to search for: ")
        found_tutors = [tutor for tutor in self.tutors if tutor.subject.lower() == subject.lower()]
        if found_tutors:
            print("Tutors found:")
            for tutor in found_tutors:
                print(tutor)
        else:
            print("No tutors found for the given subject")
            
    def display_tutors(self):
        if self.tutors:
            print("All Tutors:")
            for tutor in self.tutors:
                print(tutor)
        else:
            print("No tutors available.")
    
    def run(self):
        while True:
            print("\n--- Tutor Search App ---")
            print("1. Add Tutor")
            print("2. Search Tutor")
            print("3. Display All Tutors")
            print("4. Exit")
            
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_tutor()
            elif choice == '2':
                self.search_tutor()
            elif choice == '3':
                self.display_tutors()
            elif choice == '4':
                print("Exiting the app.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = TutorApp()
    app.run()
            