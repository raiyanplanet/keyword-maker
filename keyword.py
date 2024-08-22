import time
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_welcome_message():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for better UX
    welcome_text = '''
  __          __  _                            _                __
  \ \        / / | |                          | |              / _|
   \ \  /\  / /__| | ___ ___  _ __ ___   ___| |_ ___  _ __  | |_ ___  ___
    \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ __/ _ \| '__| |  _/ _ \/ __|
     \  /\  /  __/ | (_| (_) | | | | | |  __/ || (_) | |    | ||  __/\__ \\
      \/  \/ \___|_|\___\___/|_| |_| |_|\___|\__\___/|_|    |_| \___||___/
    '''
    ascii_cat = '''
       /\\_/\\
      ( o.o )
       > ^ <
    '''
    print(Fore.CYAN + Style.BRIGHT + welcome_text + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + ascii_cat + Style.RESET_ALL)

def get_valid_input(prompt, validate=lambda x: True, error_message="Invalid input", color=Fore.CYAN):
    while True:
        print(color + prompt, end=' ')
        user_input = input().strip()
        if validate(user_input):
            return user_input
        print(Fore.RED + error_message + Style.RESET_ALL)

def is_valid_date(year, month, day):
    try:
        import datetime
        datetime.datetime(int(year), int(month), int(day))
        return True
    except ValueError:
        return False

def generate_wordlist():
    # Display the welcome message
    print_welcome_message()

    # Record start time
    start_time = time.time()

    # Get basic user information
    first_name = get_valid_input(Fore.GREEN + "Enter your first name:" + Style.RESET_ALL, lambda x: x.isalpha(), "Please enter a valid name.")
    last_name = get_valid_input(Fore.GREEN + "Enter your last name:" + Style.RESET_ALL, lambda x: x.isalpha(), "Please enter a valid name.")
    nickname = get_valid_input(Fore.GREEN + "Enter your nickname:" + Style.RESET_ALL)
    birth_year = get_valid_input(Fore.GREEN + "Enter your birth year:" + Style.RESET_ALL, lambda x: x.isdigit() and len(x) == 4, "Please enter a valid year.")
    birth_month = get_valid_input(Fore.GREEN + "Enter your birth month (as a number):" + Style.RESET_ALL, lambda x: x.isdigit() and 1 <= int(x) <= 12, "Please enter a valid month.")
    birth_day = get_valid_input(Fore.GREEN + "Enter your birth day:" + Style.RESET_ALL, lambda x: x.isdigit() and 1 <= int(x) <= 31, "Please enter a valid day.")

    while not is_valid_date(birth_year, birth_month, birth_day):
        print(Fore.RED + "Invalid date. Please enter a valid date." + Style.RESET_ALL)
        birth_year = get_valid_input(Fore.GREEN + "Enter your birth year:" + Style.RESET_ALL, lambda x: x.isdigit() and len(x) == 4, "Please enter a valid year.")
        birth_month = get_valid_input(Fore.GREEN + "Enter your birth month (as a number):" + Style.RESET_ALL, lambda x: x.isdigit() and 1 <= int(x) <= 12, "Please enter a valid month.")
        birth_day = get_valid_input(Fore.GREEN + "Enter your birth day:" + Style.RESET_ALL, lambda x: x.isdigit() and 1 <= int(x) <= 31, "Please enter a valid day.")

    favorite_color = get_valid_input(Fore.GREEN + "Enter your favorite color:" + Style.RESET_ALL)

    # Get partner information
    partner_first_name = get_valid_input(Fore.GREEN + "Enter your partner's first name:" + Style.RESET_ALL, lambda x: x.isalpha(), "Please enter a valid name.")
    partner_last_name = get_valid_input(Fore.GREEN + "Enter your partner's last name:" + Style.RESET_ALL, lambda x: x.isalpha(), "Please enter a valid name.")
    partner_birth_year = get_valid_input(Fore.GREEN + "Enter your partner's birth year:" + Style.RESET_ALL, lambda x: x.isdigit() and len(x) == 4, "Please enter a valid year.")
    partner_birth_month = get_valid_input(Fore.GREEN + "Enter your partner's birth month (as a number):" + Style.RESET_ALL, lambda x: x.isdigit() and 1 <= int(x) <= 12, "Please enter a valid month.")
    partner_birth_day = get_valid_input(Fore.GREEN + "Enter your partner's birth day:" + Style.RESET_ALL, lambda x: x.isdigit() and 1 <= int(x) <= 31, "Please enter a valid day.")

    while not is_valid_date(partner_birth_year, partner_birth_month, partner_birth_day):
        print(Fore.RED + "Invalid date. Please enter a valid date." + Style.RESET_ALL)
        partner_birth_year = get_valid_input(Fore.GREEN + "Enter your partner's birth year:" + Style.RESET_ALL, lambda x: x.isdigit() and len(x) == 4, "Please enter a valid year.")
        partner_birth_month = get_valid_input(Fore.GREEN + "Enter your partner's birth month (as a number):" + Style.RESET_ALL, lambda x: x.isdigit() and 1 <= int(x) <= 12, "Please enter a valid month.")
        partner_birth_day = get_valid_input(Fore.GREEN + "Enter your partner's birth day:" + Style.RESET_ALL, lambda x: x.isdigit() and 1 <= int(x) <= 31, "Please enter a valid day.")

    # Get hobbies, games, sports, subjects, and movies
    hobbies = get_valid_input(Fore.GREEN + "Enter favorite hobbies separated by commas:" + Style.RESET_ALL).split(',')
    games = get_valid_input(Fore.GREEN + "Enter favorite games separated by commas:" + Style.RESET_ALL).split(',')
    sports = get_valid_input(Fore.GREEN + "Enter favorite sports separated by commas:" + Style.RESET_ALL).split(',')
    subjects = get_valid_input(Fore.GREEN + "Enter favorite subjects separated by commas:" + Style.RESET_ALL).split(',')
    movies = get_valid_input(Fore.GREEN + "Enter favorite movies separated by commas:" + Style.RESET_ALL).split(',')

    # Get additional keywords
    additional_keywords = get_valid_input(Fore.GREEN + "Enter additional keywords separated by commas:" + Style.RESET_ALL)
    keywords = [keyword.strip() for keyword in additional_keywords.split(',') if keyword.strip()]

    # Get minimum and maximum word length
    min_length = int(get_valid_input(Fore.GREEN + "Enter the minimum word length:" + Style.RESET_ALL, lambda x: x.isdigit() and int(x) > 0, "Please enter a valid number."))
    max_length = int(get_valid_input(Fore.GREEN + "Enter the maximum word length:" + Style.RESET_ALL, lambda x: x.isdigit() and int(x) > min_length, "Please enter a valid number."))

    # Base words list
    words = [
                first_name, last_name, nickname, favorite_color,
                partner_first_name, partner_last_name
            ] + keywords + hobbies + games + sports + subjects + movies

    # Remove any empty entries
    words = [word.strip() for word in words if word.strip()]

    # Generate combinations
    combinations = set()

    # Add base words
    combinations.update(words)

    # Add year, month, day for user and partner
    combinations.update([
        birth_year, birth_month, birth_day,
        partner_birth_year, partner_birth_month, partner_birth_day
    ])

    # Create basic combinations
    for word in words:
        combinations.add(word + birth_year)
        combinations.add(word + birth_month + birth_day)
        combinations.add(word + birth_day + birth_month)
        combinations.add(word + partner_birth_year)
        combinations.add(word + partner_birth_month + partner_birth_day)
        combinations.add(word + partner_birth_day + partner_birth_month)

    # Combine all possible pairs
    for word1 in words:
        for word2 in words:
            if word1 != word2:
                combinations.add(word1 + word2)
                combinations.add(word1 + birth_year + word2)
                combinations.add(word1 + word2 + birth_year)
                combinations.add(word1 + birth_month + birth_day + word2)
                combinations.add(word1 + partner_birth_year + word2)
                combinations.add(word1 + word2 + partner_birth_year)
                combinations.add(word1 + partner_birth_month + partner_birth_day + word2)

    # Generate variations with numbers
    for word in words:
        for number in range(1, 1000):  # Number range from 1 to 999
            number_str = str(number)
            combinations.add(word + number_str)
            combinations.add(number_str + word)
            if len(number_str) < 3:  # Add variations with padded numbers
                combinations.add(word + number_str.zfill(3))  # e.g., '1' -> '001'
                combinations.add(number_str.zfill(3) + word)

    # Filter combinations by length
    filtered_combinations = {word for word in combinations if min_length <= len(word) <= max_length}

    # Sort combinations alphabetically
    wordlist = sorted(filtered_combinations)

    # Output the generated wordlist
    print(Fore.CYAN + "\nGenerated Wordlist:" + Style.RESET_ALL)
    for word in wordlist:
        print(Fore.GREEN + word + Style.RESET_ALL)

    # Optionally, write to a file
    save_to_file = get_valid_input(Fore.CYAN + "\nDo you want to save the wordlist to a file? (y/n): " + Style.RESET_ALL,
                                   lambda x: x in ['y', 'n'], "Please enter 'y' or 'n'.")
    if save_to_file == 'y':
        filename = get_valid_input(Fore.GREEN + "Enter the filename (include path if needed):" + Style.RESET_ALL)
        try:
            with open(filename, 'w') as file:
                for word in wordlist:
                    file.write(f"{word}\n")
            file_size = os.path.getsize(filename)
            # Record end time
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(Fore.GREEN + f"Wordlist saved to {filename}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Number of words generated: {len(wordlist)}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"File size: {file_size} bytes" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Time taken: {elapsed_time:.2f} seconds" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error saving file: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    generate_wordlist()
