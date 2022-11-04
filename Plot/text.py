from pygame import font, color
class Text:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color

    def Insert(self,
               fontsize = 0,
               text = "",
               x = 0,
               y = 0,
               italic = False,
               bold = False):
        self.default_font = font.SysFont('Constantia', fontsize, italic, bold)
        self.render = self.default_font.render(str(text), False, color.THECOLORS[self.color])
        self.screen.blit(self.render, (x,y))
