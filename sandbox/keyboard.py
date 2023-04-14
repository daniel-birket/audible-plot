
import keyboard

# Define a generator function that yields the next 20 items
def generator_function():
    for i in range(20):
        yield i

# Define a function to print the next 20 items from the generator function
def print_next_20():
    generator = generator_function()
    for i in generator:
        print(i)

# Define a function to exit the program
def exit_program():
    print("Exiting program...")
    quit()

# Create a dictionary that maps keys to functions
key_functions = {
    "space": print_next_20,
    "q": exit_program,
}

# Start listening for keyboard events
keyboard.start_recording()

# Loop forever, processing each keyboard event as it occurs
while True:
    events = keyboard.stop_recording()
    for event in events:
        if event.event_type == "down":
            key = event.name
            function = key_functions.get(key)
            if function is not None:
                function()
    keyboard.start_recording()
