from pygame import display, event, font


class MainFont:
    def __init__(self, pos: tuple[int, int], color: str = '#BBBBBB', scale: int = 6):
        self.WIN = display.get_surface()
        self.font = font.Font('gameFont.woff', scale)
        self.w = self.font.size('n')[0]
        self.h = self.font.get_height()
        self.indicator_pos = 0
        self.x, self.y = pos
        self.color = color
        self.text = ""

    def text_input(self, key_in: event.Event, text_in: event.Event, lining: bool = True):
        key = key_in .__dict__["unicode"]
        char = text_in.__dict__["text"]
        if key == "\x08":
            self.text = self.text[:-1:]
        elif lining and key == "\r":
            self.text += "\n"
        elif char != "":
            self.text += char
        print(text_in, " ", char)

    def draw(self, text: str, antialias: bool, pos: tuple[int, int], centered: bool = False):
        self.WIN.blits([(self.font.render(text, antialias, self.color),
                        (pos[0] - (self.font.size(text)[0]//2 if centered else 0),
                         pos[1] + y*self.h))
                        for y, text in enumerate(text.split('\n'))])

    def blit(self, antialias: bool):
        self.WIN.blits([(self.font.render(text, antialias, self.color),
                        (self.x, self.y+y*self.h))
                        for y, text in enumerate(self.text.split('\n'))])
