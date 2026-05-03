import pygame          # Import pygame for graphics and game features
import sys             # Import sys to allow program exit

pygame.init()          # initializes pygame; to start all pygame modules

class Question:
    def __init__(self, text, options, answer):
        self.text = text              # Store the question text (String)
        self.options = options        # Store answer choices in a list
        self.answer = answer          # Store the correct answer

    def is_correct(self, choice):
        return choice == self.answer  # Return True if user's choice matches correct answer

class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text                              # Text displayed on the button
        self.rect = pygame.Rect(x, y, width, height)  # Create rectangle for button position/size
        self.color = (180, 180, 180)                  # Default button color (gray)

    def draw(self, screen, font):
        # Draw button rectangle on screen
        pygame.draw.rect(screen, self.color, self.rect)

        # Render button text
        text_surface = font.render(self.text, True, (0, 0, 0))

        # Center text inside button rectangle
        text_rect = text_surface.get_rect(center=self.rect.center)

        # Draw text onto screen
        screen.blit(text_surface, text_rect)

    def is_hovered(self, mouse_pos):
        # Check if mouse is over the button
        return self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos):
        # Check if button is clicked (mouse inside rectangle)
        return self.rect.collidepoint(mouse_pos)

class QuizGame:
    def __init__(self):
        self.width = 800                              # Set window width
        self.height = 600                             # Set window height
        self.screen = pygame.display.set_mode((self.width, self.height))  # Create game window
        pygame.display.set_caption("Trivia Quiz Game")  # Set window title

        self.font = pygame.font.Font(None, 36)        # Set normal font
        self.big_font = pygame.font.Font(None, 48)    # Set larger font for titles

        self.score = 0                                # Initialize score to 0
        self.current_index = 0                        # Track current question index

        self.questions = self.load_questions()        # Load questions into list
        self.buttons = []                             # Create empty list for buttons

    def load_questions(self):
        # Return a list of Question objects
        return [
            Question(
                "What is the capital of France?",              # Question text
                ["Berlin", "Madrid", "Paris", "Rome"],         # Answer choices
                "Paris"                                        # Correct answer
            ),
            Question(
                "What is 6 x 2?",
                ["8", "12", "10", "14"],
                "12"
            ),
            Question(
                "Which language is this?",
                ["Java", "Python", "C++", "Swift"],
                "Python"
            )
        ]

    def create_buttons(self, options):
        self.buttons = []  # Reset button list for each question

        # Loop through each answer option
        for i, option in enumerate(options):
            # Create button with position based on index
            button = Button(option, 200, 200 + i * 70, 400, 50)

            # Add button to list
            self.buttons.append(button)

    def draw_text(self, text, x, y, font):
        # Render text into a surface
        surface = font.render(text, True, (0, 0, 0))

        # Draw text on screen at (x, y)
        self.screen.blit(surface, (x, y))

    def save_score(self):
        try:
            # Open file in append mode
            with open("scores.txt", "a") as file:
                # Write score to file
                file.write(f"Score: {self.score}\n")
        except Exception as e:
            # Print error if something goes wrong
            print("Error:", e)

    def run(self):
        running = True  # Control variable for loop

        # Main game loop (runs until game ends)
        while running:
            self.screen.fill((255, 255, 255))  # Clear screen with white background

            # Check if all questions are done
            if self.current_index >= len(self.questions):
                # Display game over text
                self.draw_text("Game Over!", 300, 200, self.big_font)

                # Display final score
                self.draw_text(f"Score: {self.score}", 320, 260, self.font)

                pygame.display.flip()  # Update screen

                self.save_score()      # Save score to file
                pygame.time.wait(3000)  # Wait 3 seconds
                break                 # Exit loop

            # Get current question
            current_q = self.questions[self.current_index]

            # Create buttons for current question
            self.create_buttons(current_q.options)

            # Draw question text
            self.draw_text(current_q.text, 100, 100, self.font)

            # Get current mouse position
            mouse_pos = pygame.mouse.get_pos()

            # Loop through buttons
            for button in self.buttons:
                # Check if mouse is hovering over button
                if button.is_hovered(mouse_pos):
                    button.color = (150, 200, 255)  # Change color when hovered
                else:
                    button.color = (180, 180, 180)  # Default color

                # Draw button
                button.draw(self.screen, self.font)

            pygame.display.flip()  # Update screen

            # Handle events (input)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close pygame
                    sys.exit()     # Exit program

                # Check for mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        # Check if clicked button
                        if button.is_clicked(mouse_pos):
                            # Check if answer is correct
                            if current_q.is_correct(button.text):
                                self.score += 1  # Increase score

                            # Move to next question
                            self.current_index += 1

# main program
if __name__ == "__main__":
    game = QuizGame()  # Create game object
    game.run()         # Start the game
