from typing import Tuple
import pygame
from text import Text
from sys import exit

def drawLine(start, end):
    """Bresenham's Line Algorithm
    Produces a list of tuples from start and end
 
    >>> points1 = get_line((0, 0), (3, 4))
    >>> points2 = get_line((3, 4), (0, 0))
    >>> assert(set(points1) == set(points2))
    >>> print points1
    [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
    >>> print points2
    [(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
    """
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
 
    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)
 
    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
 
    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1
 
    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1
 
    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
 
    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points

class Point:
    def __init__(self):
        self.pos: list[Tuple[int]] = []
        self.indices: list[int] = []
        
class Main:
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.font.init()
        pygame.init()
        self.initialize_screen("Setup", 600, 600)

    def initialize_screen(self, title: str, width: int, height: int):
        self.window_size = (width, height)
        self.screen = pygame.display.set_mode(self.window_size, 0, 32)
        self.display = pygame.Surface((width // 2, height // 2))
        pygame.display.set_caption(title)

    def screen_background(self, color: str):
        self.screen.fill(pygame.color.THECOLORS[color])

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:
                    print(self.point.indices)
                
                if event.key == pygame.K_SPACE:
                    # Algorithm to make this [[[0], [1], [2]], [[..], [..], [..]], ...] and write it in txt file.
                    output = ""
                    if not self.point.pos: return
                    for index, tup in enumerate(self.point.pos):
                        temp = list(tup)
                        temp.insert(1, 0)
                        temp[2] = -temp[2]
                        output += "[{con1}]{temp_comma}".format(con1 = "{con2}".format(con2 = ", ".join("[{temp_x} + offset.{temp_coord}]".format(temp_x = t, temp_coord = coord) for t, coord in zip(temp, ("x", "z", "y")))), temp_comma = ', ' if index != len(self.point.pos) - 1 else '')
                        self.point.pos[index] = list([x] for x in temp)
                    with open("Plot/output.txt", "w") as f:
                        f.write(f"[{output}]")
                    print("Done")
                    
                    for index in range(len(self.drawn_blocks)):
                        self.drawn_blocks[index][1] = pygame.transform.scale(pygame.image.load(f"Plot/untouched.png"), (self.block_size, self.block_size))
                        self.drawn_blocks[index][2] = False
                        self.drawn_blocks[index][3] = False
                        
                    self.drawn_blocks.clear()
                    if self.point.pos: 
                        self.point.pos.clear()
                        self.point.indices.clear()
                    
                        
                if event.key == pygame.K_c:
                    if not self.drawn_blocks: return
                    for index in range(len(self.drawn_blocks)):
                        self.drawn_blocks[index][1] = pygame.transform.scale(pygame.image.load(f"Plot/untouched.png"), (self.block_size, self.block_size))
                        self.drawn_blocks[index][2] = False
                        self.drawn_blocks[index][3] = False
                    self.drawn_blocks.clear()
                    if self.point.pos: 
                        self.point.pos.clear()
                        self.point.indices.clear()
                    
                if event.key == pygame.K_z:
                    if not self.drawn_blocks: return
                    self.drawn_blocks[-1][1] = pygame.transform.scale(pygame.image.load(f"Plot/untouched.png"), (self.block_size, self.block_size))
                    self.drawn_blocks[-1][2] = False
                    self.drawn_blocks[-1][3] = False
                    self.drawn_blocks.pop()
                    if self.point.pos: 
                        self.point.pos.pop()
                        self.point.indices.pop()
                    
                if event.key == pygame.K_x:
                    if not self.point.pos: return
                    self.drawn_blocks[self.point.indices[-1]][1] = pygame.transform.scale(pygame.image.load(f"Plot/touched.png"), (self.block_size, self.block_size))
                    self.drawn_blocks[self.point.indices[-1]][3] = False
                    self.point.pos.pop()
                    self.point.indices.pop()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.blocks: return
                if not event.button == 3: return
                for index, block in enumerate(self.blocks):
                    if block[0].collidepoint(event.pos) and block[2]:
                        block[3] = True
                        if block[3] and block[2]:
                            self.point.pos.append(tuple((x - 310) // self.block_size for x in block[0].center))
                            self.point.indices.append(self.drawn_blocks.index(block))
                            block[1] = pygame.transform.scale(pygame.image.load(f"Plot/outline.png"), (self.block_size, self.block_size))
                        
                
    def key_input(self):
        key = pygame.key.get_pressed()
        
    def mouse_input(self):
        mouse = pygame.mouse
        if mouse.get_pressed()[0]:
            if not self.blocks: return
            for block in self.blocks:
                if block[0].collidepoint(mouse.get_pos()) and not block[2]:
                    block[2] = True
                    if block[2]:
                        self.drawn_blocks.append(block)
                        block[1] = pygame.transform.scale(pygame.image.load(f"Plot/touched.png"), (self.block_size, self.block_size))
        
    def initialize_code(self):
        self.columns = 30
        self.block_size = self.screen.get_width() // self.columns
        self.point = Point()
        self.blocks: list[list[pygame.Rect, pygame.Surface, bool, bool]] = []
        self.drawn_blocks: list[list[pygame.Rect, pygame.Surface, bool, bool]] = []
        
        for y in range(self.columns):
            for x in range(self.columns):
                self.blocks.append(
                    [
                        pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size),
                        pygame.transform.scale(pygame.image.load(f"Plot/untouched.png"), (self.block_size, self.block_size)),
                        False,
                        False
                    ]
                    )
    
    def loop_block(self):
        self.cursor = pygame.mouse.get_pos()

    def rendering_screen(self):
        for block in self.blocks:
            self.screen.blit(block[1], block[0])
        pygame.draw.rect(self.screen, pygame.color.THECOLORS["red"], pygame.Rect(self.screen.get_width() // 2 + 5, self.screen.get_height() // 2 + 5, self.block_size / 2, self.block_size / 2))
        if not self.blocks: return
        for block in self.blocks:
            if block[0].collidepoint(self.cursor):
                self.text = Text(self.screen, "white")
                self.text.Insert(40, f"X: {(block[0].x - 300) // self.block_size}", (self.block_size * 2), self.screen.get_height() - (self.block_size * 4))
                self.text.Insert(40, f"Y: {-((block[0].y - 300) // self.block_size)}", (self.block_size * 2), self.screen.get_height() - (self.block_size * 6))
                    
        # for p in get_line((0, 0), (10, 5)):
            # x, y = p
            # pygame.draw.rect(self.screen, pygame.color.THECOLORS["green"], pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size))
        
            
    def update_screen(self):
        pygame.display.update()
        self.dt = self.clock.tick(self.fps) / 1000

    def Run(self):
        self.fps = 60
        self.dt = self.clock.tick(self.fps) / 1000
        self.running = True
        self.initialize_code()

        while self.running:
            self.screen_background('white')
            self.event_handling()
            self.mouse_input()
            self.key_input()

            self.loop_block()
            self.rendering_screen()
            self.update_screen()

        pygame.quit()

if __name__ == '__main__':
    Main().Run()
