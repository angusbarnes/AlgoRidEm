import os
import shutil
import json
import uuid
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init()

def print_colored(text, color=Fore.WHITE, style=Style.NORMAL):
    print(f"{style}{color}{text}{Style.RESET_ALL}")

def get_input(prompt, color=Fore.CYAN):
    return input(f"{color}{prompt}{Style.RESET_ALL}")

def create_bot_directory(bot_name):
    source_dir = "client"
    target_dir = f"{bot_name}_bot"

    if os.path.exists(target_dir):
        print_colored(f"Warning: {target_dir} already exists.", Fore.YELLOW)
        overwrite = get_input("Do you want to overwrite it? (y/n): ").lower() == 'y'
        if not overwrite:
            print_colored("Operation cancelled.", Fore.RED)
            return False

    try:
        shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)
        print_colored(f"Successfully created {target_dir}", Fore.GREEN)
        return True
    except Exception as e:
        print_colored(f"Error creating bot directory: {e}", Fore.RED)
        return False

def create_bot_manifest(bot_name):
    manifest = {
        "bot_name": bot_name,
        "bot_id": str(uuid.uuid4()),
        "bot_description": "",
        "bot_author": ""
    }

    print_colored("\nLet's create your bot manifest:", Fore.MAGENTA)
    manifest["bot_description"] = get_input("Enter a brief description of your bot's strategy or philosophy: ")
    manifest["bot_author"] = get_input("Enter the developer's name: ")

    manifest_path = f"{bot_name}_bot/bot_manifest.json"
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=4)

    print_colored(f"\nBot manifest created at {manifest_path}", Fore.GREEN)
    print_colored("\nHere's your bot manifest:", Fore.MAGENTA)
    print(json.dumps(manifest, indent=4))

def main():
    print_colored("=== 🤖 Bot Creator Helper ===", Fore.MAGENTA, Style.BRIGHT)
    
    bot_name = get_input("Enter your bot name: ")
    
    if create_bot_directory(bot_name):
        create_bot_manifest(bot_name)
        print_colored("\nBot creation complete! 🎉", Fore.GREEN, Style.BRIGHT)
    else:
        print_colored("Bot creation failed.", Fore.RED, Style.BRIGHT)

if __name__ == "__main__":
    main()