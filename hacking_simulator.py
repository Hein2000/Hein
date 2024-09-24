import random
import time
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class HackingSimulator:
    def __init__(self):
        self.score = 0
        self.typing_paragraphs = [
            "The Omnissiah guides the machine spirits of Mars.",
            "It is through his divine will that the Imperium's technology persists.",
            "The blessed STC designs are coveted relics of a bygone era, held in the vaults of the Adeptus Mechanicus.",
            "To tamper with the sanctity of a machine is heresy, and only the ordained Tech-Priests may commune with their sacred code.",
            "The Machine God watches over all technology, from the smallest cog to the greatest Titan.",
            "Tech-Priests invoke rites and prayers before engaging with any piece of technology.",
            "The Cult Mechanicus seeks to recover the lost knowledge of the ancient Standard Template Constructs."
        ]
        self.time_up = False
        self.caesar_cipher_text = "glory to the omnissiah for the machines will endure"
        self.mitre_stages = [
            {"name": "Data Exfiltration", "challenge": self.pattern_challenge},
            {"name": "Code Manipulation", "challenge": self.typing_challenge},
            {"name": "Circuit Break", "challenge": self.math_challenge},
            {"name": "Memory Coil", "challenge": self.memory_challenge},
            {"name": "Cogitator Uplift", "challenge": self.logic_challenge},
            {"name": "Cipher Shunt", "challenge": self.typing_challenge},
            {"name": "Access Subversion", "challenge": self.typing_challenge},
            {"name": "Data Stream Parsing", "challenge": self.pattern_challenge},
            {"name": "Multinode Hacking", "challenge": self.memory_challenge},
            {"name": "Core Overload", "challenge": self.typing_challenge}
        ]

    def clear_screen(self):
        """Clear the terminal screen based on the OS."""
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For macOS/Linux
            os.system('clear')

    def print_ascii_welcome(self):
        """Print ASCII art for the Adeptus Mechanicus welcome screen."""
        ascii_art = Fore.RED + r"""
   //\\
  //  \\  .------------.  
 ||    || |            |  
 ||    || |  Omnissiah  |  
 ||    || |------------|  
 ||    || |            |  
  \\  //  '------------'  
   \\//    Tech-Priest Login
=============================
""" + Style.RESET_ALL
        print(ascii_art)

    def print_ascii_stage_complete(self, stage_number):
        """Print ASCII art for a stage completion."""
        ascii_art = Fore.GREEN + r"""
   ______  _      _        ____  __  __ 
  |  ____|| |    | |      / __ \|  \/  |
  | |__   | |    | |     | |  | | \  / |
  |  __|  | |    | |     | |  | | |\/| |
  | |     | |____| |____ | |__| | |  | |
  |_|     |______|______(_)____(_)___|_|
""" + Style.RESET_ALL
        print(ascii_art)
        print(f"{Fore.CYAN}\nStage {stage_number} complete!\n{Style.RESET_ALL}")

    def print_ascii_hack_in_progress(self):
        """Print ASCII art to indicate hacking progress."""
        ascii_art = Fore.YELLOW + r"""
      ___               __      __  __ 
     / _ \_______ __ __/ /_____/ /_/ /
    / ___/ __/ _ \\ \ / __/ __/ __/ / 
   /_/  /_/  \___/_\_\\__/\__/\__/_/  
   Initiating Data Extraction...
""" + Style.RESET_ALL
        print(ascii_art)

    def login(self):
        """Prompt the user for a username and password. Allow 3 attempts."""
        correct_username = "Cawl"
        correct_password = "Cog"
        attempts = 3

        self.print_ascii_welcome()

        for attempt in range(attempts):
            print(f"{Fore.CYAN}Accessing the terminal... Please log in. (Attempt {attempt + 1}/{attempts})")
            
            username = input("Enter username: ")
            password = input("Enter password: ")

            if username == correct_username and password == correct_password:
                print(f"{Fore.GREEN}\nLogin successful. Welcome, Tech-Priest.\n{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED}\nLogin failed! Unauthorized access.\n{Style.RESET_ALL}")

            if attempt < attempts - 1:
                print(f"{Fore.YELLOW}Try again.\n{Style.RESET_ALL}")
        
        print(f"{Fore.RED}\nToo many failed attempts! Access denied.\n{Style.RESET_ALL}")
        return False

    def typing_challenge(self):
        challenge_paragraph = " ".join(random.sample(self.typing_paragraphs, 2))  # Select 2 random sentences
        self.print_ascii_hack_in_progress()
        print(f"\nTyping Challenge: Type the following paragraph within 30 seconds:\n'{challenge_paragraph}'")

        user_input = input("\nYour input: ")
        if user_input == challenge_paragraph:
            print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Wrong!{Style.RESET_ALL}")
            return False

    def math_challenge(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-', '*'])
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        else:  # operation == '*'
            correct_answer = num1 * num2

        self.print_ascii_hack_in_progress()
        print(f"\nCircuit Break Challenge: Solve {num1} {operation} {num2}")

        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED}Wrong!{Style.RESET_ALL}")
                return False
        except ValueError:
            print(f"{Fore.RED}Invalid input! Please enter a number.{Style.RESET_ALL}")
            return False

    def memory_challenge(self):
        sequence = [random.randint(0, 9) for _ in range(5)]
        self.print_ascii_hack_in_progress()
        print(f"\nMemory Coil Challenge: Memorize this sequence: {sequence}")
        time.sleep(3)  # Give the player time to memorize

        self.clear_screen()  # Clear the screen after showing the sequence
        user_input = input("Enter the sequence: ")

        user_sequence = list(map(int, user_input.strip().split()))
        if user_sequence == sequence:
            print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Wrong!{Style.RESET_ALL}")
            return False

    def pattern_challenge(self):
        pattern = "".join([random.choice(['#', '*', '@', '%']) for _ in range(4)])
        self.print_ascii_hack_in_progress()
        print(f"\nData Exfiltration Challenge: Memorize this pattern: {pattern}")
        time.sleep(3)

        self.clear_screen()  # Clear the screen after showing the pattern
        user_input = input("Enter the pattern: ")

        if user_input == pattern:
            print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Wrong!{Style.RESET_ALL}")
            return False

    def logic_challenge(self):
        logic_questions = [
            {"question": "Which is bigger: 5 or 3?", "answer": "5"},
            {"question": "Which comes first in the alphabet: A or Z?", "answer": "A"},
            {"question": "Is 10 divisible by 2?", "answer": "yes"},
        ]
        question = random.choice(logic_questions)
        self.print_ascii_hack_in_progress()
        print(f"\nCogitator Uplift Challenge: {question['question']}")

        user_input = input("Your answer: ").lower().strip()
        if user_input == question["answer"].lower():
            print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Wrong!{Style.RESET_ALL}")
            return False

    def hacking_sequence(self):
        """Complete 10 stages with a score of 15 points per stage."""
        for stage_number, stage in enumerate(self.mitre_stages, 1):
            print(f"{Fore.CYAN}\nStage {stage_number} - {stage['name']}:{Style.RESET_ALL}")

            success = stage["challenge"]()

            if success:
                self.score += 15
                self.print_ascii_stage_complete(stage_number)
            else:
                print(f"{Fore.RED}Stage {stage_number} failed.{Style.RESET_ALL}")

            print(f"{Fore.YELLOW}Current score: {self.score}/150{Style.RESET_ALL}")

    def reset_game(self):
        """Reset the game if the player doesn't get a perfect score."""
        print(f"{Fore.YELLOW}\nYour score is not perfect. Restarting the hacking sequence.{Style.RESET_ALL}")
        self.score = 0
        self.hacking_sequence()

    def generate_caesar_cipher(self, shift=3):
        """Generate a Caesar cipher with a given shift."""
        cipher_text = ""
        for char in self.caesar_cipher_text:
            if char.isalpha():
                shifted = ord(char) + shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    cipher_text += chr(shifted)
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    cipher_text += chr(shifted)
            else:
                cipher_text += char  # Keep spaces and punctuation the same
        return cipher_text

    def end_game(self):
        """End the game after all stages are complete."""
        while True:
            if self.score == 150:
                print(f"{Fore.GREEN}\nCongratulations! You achieved a perfect score.{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Final Cipher Text: {self.generate_caesar_cipher()}{Style.RESET_ALL}")
            else:
                self.reset_game()

            action = input(f"{Fore.CYAN}\nType 'exit' to quit or 'retry' to try again: {Style.RESET_ALL}").lower().strip()
            if action == 'exit':
                print(f"{Fore.RED}Exiting the game.{Style.RESET_ALL}")
                break
            elif action == 'retry':
                self.score = 0
                self.hacking_sequence()

    def start(self):
        print(f"{Fore.CYAN}Welcome, Tech-Priest!{Style.RESET_ALL}")

        if not self.login():
            print(f"{Fore.RED}Access denied. Exiting...{Style.RESET_ALL}")
            return

        self.hacking_sequence()
        self.end_game()

if __name__ == "__main__":
    simulator = HackingSimulator()
    simulator.start()





















