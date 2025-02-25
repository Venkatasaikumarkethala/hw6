"""
App package initializer for Homework 5.
Loads plugin commands and starts the REPL in App.
"""
from .plugin_manager import PluginManager

class App:
    """Main Application class implementing a REPL that uses the command pattern."""
    @staticmethod
    def start() -> None:
        print("Welcome to the Interactive Calculator!")
        print("Type 'menu' to see available commands or 'exit' to quit.\n")

        # Dynamically load all commands from the commands folder
        commands_dict = PluginManager.load_plugins()

        while True:
            user_input = input(">>> ").strip()
            if not user_input:
                continue

            tokens = user_input.split()
            command_name = tokens[0].lower()
            args = tokens[1:]

            if command_name == 'exit':
                print("Exiting the interactive calculator...")
                break

            command_class = commands_dict.get(command_name)
            if command_class:
                command_instance = command_class()
                try:
                    # Pass commands_dict as the second argument.
                    output = command_instance.execute(args, commands_dict)
                    if output is not None:
                        print(output)
                except ValueError as exc:
                    print(f"Error: {exc}")
                except Exception as exc:
                    print(f"Unexpected error: {exc}")
            else:
                print("Unknown command. Type 'menu' to see available commands, or 'exit' to quit.")
