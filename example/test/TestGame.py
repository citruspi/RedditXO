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

        # use a (r, g, b) tuple for color
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)

        self.subreddits = {
            'Science': 'science',
            'Technology': 'technology',
            'World News': 'news',
            'Money': 'money'
        }

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
        self.screen = screen

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

            # Print Title
            self.printText("RedditXO Client", 90, 450, 50, self.yellow)

            start_x_pos_subreddits = 150
            start_y_pos_subreddits = 150
            for key in self.subreddits:
                self.printText(key, 60, start_x_pos_subreddits, start_y_pos_subreddits, self.green)
                start_y_pos_subreddits += 100

            # Flip Display
            pygame.display.flip()
            # fill later

            # Try to stay at 30 FPS
            self.clock.tick(30)

    def printText(self, txtText, Textsize, Textx, Texty, Textcolor, text_font="MS Comic Sans"):
        # pick a font you have and set its size
        myfont = pygame.font.SysFont(text_font, Textsize)
        # apply it to text on a label
        label = myfont.render(txtText, 1, Textcolor)
        # put the label object on the screen at point Textx, Texty
        self.screen.blit(label, (Textx, Texty))
        # show the whole thing
        pygame.display.flip()


# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = TestGame()
    game.run()


if __name__ == '__main__':
    main()
