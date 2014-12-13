#!/usr/bin/python
import pygame
from gi.repository import Gtk


class TestGame:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.x = -100
        self.y = 100

        self.vx = 10
        self.vy = 0

        self.paused = False
        self.direction = 1

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    # The main game loop.
    def run(self):
        self.running = True

        screen = pygame.display.get_surface()

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.direction = -1
                    elif event.key == pygame.K_RIGHT:
                        self.direction = 1

            # pick a font you have and set its size
            myfont = pygame.font.SysFont("Comic Sans MS", 90)
            # apply it to text on a label
            yellow = (255, 255, 0)
            title = myfont.render("Python and Pygame are Fun!", 1, yellow)
            # put the label object on the screen at point x=100, y=100
            screen.blit(title, (130, 300))

            # Clear Display
            #screen.fill((255, 255, 255))  # 255 for white

            # Draw the ball
            #pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)

            # Flip Display
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)


# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = TestGame()
    game.run()

if __name__ == '__main__':
    main()
