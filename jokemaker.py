import random
import time


quotes = [
    "What's the best thing about Switzerland? The flag is a big plus",
    "I went to the aquarium this weekend, but I didn’t stay long. There’s something fishy about that place",
    "I found a lion in my closet the other day! When I asked what it was doing there, it said Narnia business.",
    "What's a cat's favorite instrument? Purr-cussion.",
    "Why did the snail paint a giant S on his car? So when he drove by, people could say: Look at that S car go!"
    "What do you call a happy cowboy? A jolly rancher."
    ]

def generate_random_quote():
    """Select a random quote from the database."""
    return random.choice(quotes)

def display_quote(quote):
    """Display the quote."""
    print("Random Quote: from david")
    print(quote)
    print()

if __name__ == "__main__":
    print("Random Quote Generator")
    try:
        while True:
            quote = generate_random_quote()
            display_quote(quote)
            time.sleep(10)  # Display a new quote every 10 seconds
    except KeyboardInterrupt:
        print("\nProgram terminated by user")