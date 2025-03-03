"""
App package initializer for Homework 6.
Builds on Homework 5 by adding environment variables and logging.
"""
import os  
import logging  
import logging.config  
from dotenv import load_dotenv  
from .plugin_manager import PluginManager

class App:
    """Main Application class implementing a REPL that uses the command pattern,
       plus environment variables and logging."""
    
    def __init__(self):  
        self.configure_logging()
        
       
        load_dotenv()
        self.env_name = os.getenv("ENV_NAME", "unknown")  
        logging.info(f"Environment: {self.env_name}")


        self.commands_dict = PluginManager.load_plugins()
        logging.info("Plugin commands loaded.")

    def configure_logging(self):
        """Set up logging via logging.conf if available, else basic config."""

        os.makedirs('logs', exist_ok=True)

        if os.path.exists("logging.conf"):
            logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
            logging.info("Loaded logging configuration from logging.conf")
        else:
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
            )
            logging.info("Default logging configuration applied.")


    def start(self) -> None:
        logging.info("Starting the Interactive Calculator REPL...")  
        print("Welcome to the Interactive Calculator!")
        print("Type 'menu' to see available commands or 'exit' to quit.\n")

        while True:
            user_input = input(">>> ").strip()
            if not user_input:
                continue

            tokens = user_input.split()
            command_name = tokens[0].lower()
            args = tokens[1:]

            if command_name == 'exit':
                logging.info("User requested 'exit'. Shutting down.")
                print("Exiting the interactive calculator...")
                break

            command_class = self.commands_dict.get(command_name)
            if command_class:
                command_instance = command_class()
                try:
                    output = command_instance.execute(args, self.commands_dict)
                    if output is not None:
                        print(output)
                except ValueError as exc:
                    logging.error(f"ValueError in command '{command_name}': {exc}")  
                    print(f"Error: {exc}")
                except Exception as exc:
                    logging.exception(f"Unexpected error in command '{command_name}'.")  
                    print(f"Unexpected error: {exc}")
            else:
                logging.warning(f"Unknown command: {command_name}")
                print("Unknown command. Type 'menu' to see available commands, or 'exit' to quit.")
