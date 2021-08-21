import pygame
import numpy as np

import pygame.display

class Calculation:
    def __init__(self, cells, user_input_horizontal, user_input_vertical):
        self.neighs = 0
        self.cells = cells
        self.user_input_horizontal = user_input_horizontal
        self.user_input_vertical = user_input_vertical

    def is_neighbours(self, x, y):
        self.neighs = 0
        if x > 0 and y > 0 and self.cells[x - 1][y - 1] == 1:
            self.neighs += 1
        if y > 0 and self.cells[x][y - 1] == 1:
            self.neighs += 1
        if y > 0 and x < self.user_input_horizontal - 1 and self.cells[x + 1][y - 1] == 1:
            self.neighs += 1
        if x > 0 and self.cells[x - 1][y] == 1:
            self.neighs += 1
        if x < self.user_input_horizontal - 1 and self.cells[x + 1][y] == 1:
            self.neighs += 1
        if y < self.user_input_vertical - 1 and x > 0 and self.cells[x - 1][y + 1] == 1:
            self.neighs += 1
        if y < self.user_input_vertical - 1 and self.cells[x][y + 1] == 1:
            self.neighs += 1
        if y < self.user_input_vertical - 1 and x < self.user_input_horizontal - 1 and self.cells[x + 1][y + 1] == 1:
            self.neighs += 1
        return self.neighs

    def in_box_x(self):
        for i in range(self.user_input_horizontal):
            for j in range(self.user_input_vertical):
                if 1 + i * 20 <= GUI.mouseX < 1 + i * 20 + 20 - 2 * 1 and GUI.mouseY >= 1 + j * 20 + 80 and GUI.mouseY < 1 + j * 20 + 20 + 80 - 2 * 1:
                    return i
        return -1

    def in_box_y(self):
        for i in range(self.user_input_horizontal):
            for j in range(self.user_input_vertical):
                if 1 + i * 20 <= GUI.mouseX < 1 + i * 20 + 20 - 2 * 1 and GUI.mouseY >= 1 + j * 20 + 80 and GUI.mouseY < 1 + j * 20 + 20 + 80 - 2 * 1:
                    return j
        return -1

class GUI:

    mouseX = -1
    mouseY = -1
    
    #initialisation
    def __init__(self):
        self.running = False
        self.main_page_running = True
        self.rule_page_running = False
        self.game_running = True

        self.pause = True
        self.option = False
        self.textfield_active_1 = False
        self.textfield_active_2 = False
        self.user_text_1 = ''
        self.user_text_2 = ''
        self.text_field_actived_1 = 0
        self.text_field_actived_2 = 0

        self.color_active = (255, 255, 255)
        self.color_passive = (153, 153, 153)
        self.display_color_1 = self.color_passive
        self.display_color_2 = self.color_passive

        self.input_Horizontal = "30"
        self.input_Vertical = "30"
        self.user_input_horizontal = 64
        self.user_input_vertical = 64

        self.cells = np.zeros((self.user_input_horizontal, self.user_input_vertical))
        self.neighbours = np.zeros((self.user_input_horizontal, self.user_input_vertical))
        self.new_cells = np.zeros((self.user_input_horizontal, self.user_input_vertical))

        self.screen_y = self.user_input_vertical * 20 + 2 + 80
        self.screen_x = self.user_input_horizontal * 20 + 2

        self.mech = Calculation(self.cells, self.user_input_horizontal, self.user_input_vertical)
    #GUI
    def game(self):
        while self.game_running:
            while self.main_page_running:
                self.main_screen = pygame.display.set_mode((720, 400))
                pygame.display.set_caption("Settings")
                self.user_input_horizontal = 30
                self.user_input_vertical = 30

                GUI.mouseX = pygame.mouse.get_pos()[0]
                GUI.mouseY = pygame.mouse.get_pos()[1]

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.main_page_running = False
                        self.game_running = False
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if not self.option:
                            if 235 < GUI.mouseX < 485 and 250 < GUI.mouseY < 300:
                                self.running = True
                                self.main_page_running = False
                            elif 235 < GUI.mouseX < 485 and 175 < GUI.mouseY < 225:
                                self.rule_page_running = True
                                self.main_page_running = False
                            if 235 < GUI.mouseX < 485 and 100 < GUI.mouseY < 150:
                                self.option = True
                        elif self.option:
                            if 0 < GUI.mouseX < 130 and 0 < GUI.mouseY < 40:
                                self.option = False
                            if 280 < GUI.mouseX < 530 and 100 < GUI.mouseY < 150:
                                self.textfield_active_1 = True
                                self.text_field_actived_1 += 1
                            else:
                                self.textfield_active_1 = False
                            if 280 < GUI.mouseX < 530 and 250 < GUI.mouseY < 300:
                                self.textfield_active_2 = True
                                self.text_field_actived_2 += 1
                            else:
                                self.textfield_active_2 = False
                    if self.option:
                        if self.textfield_active_1:
                            if event.type == pygame.KEYDOWN:
                                if event.type != pygame.K_BACKSPACE:
                                    self.user_text_1 += event.unicode
                                else:
                                    self.user_text_1 = self.user_text_1[:-1]
                        if self.textfield_active_2:
                            if event.type == pygame.KEYDOWN:
                                if event.type != pygame.K_BACKSPACE:
                                    self.user_text_2 += event.unicode
                                else:
                                    self.user_text_2 = self.user_text_2[:-1]

                #main screen layout
                self.main_screen.fill((255, 255, 255))
                if GUI.mouseX > 235 and GUI.mouseX < 485 and GUI.mouseY > 100 and GUI.mouseY < 150:
                    pygame.draw.rect(self.main_screen, (153, 153, 153), [235, 100, 250, 50])
                else:
                    pygame.draw.rect(self.main_screen, (255, 255, 255), [235, 100, 250, 50])
                if GUI.mouseX > 235 and GUI.mouseX < 485 and GUI.mouseY > 250 and GUI.mouseY < 300:
                    pygame.draw.rect(self.main_screen, (153, 153, 153), [235, 250, 250, 50])
                else:
                    pygame.draw.rect(self.main_screen, (255, 255, 255), [235, 250, 250, 50])
                if GUI.mouseX > 235 and GUI.mouseX < 485 and GUI.mouseY > 175 and GUI.mouseY < 225:
                    pygame.draw.rect(self.main_screen, (153, 153, 153), [235, 175, 250, 50])
                else:
                    pygame.draw.rect(self.main_screen, (255, 255, 255), [235, 175, 250, 50])

                self.option_font = pygame.font.SysFont(None, 60)

                self.title_img = pygame.image.load("img/GOL.png")
                self.title_img_resize = pygame.transform.scale(self.title_img, (240, 60))
                self.main_screen.blit(self.title_img_resize, (240, 10))

                self.option_img = self.option_font.render("SETTINGS", True, (0, 0, 0))
                self.main_screen.blit(self.option_img, (255, 105))
                self.generate_img = self.option_font.render("GENERATE", True, (0, 0, 0))
                self.main_screen.blit(self.generate_img, (245, 258))
                self.rules_img = self.option_font.render("RULES", True, (0, 0, 0))
                self.main_screen.blit(self.rules_img, (285, 182))

                #Settings page
                if self.option == True:
                    if self.textfield_active_1:
                        self.display_color_1 = self.color_active
                    else:
                        self.display_color_1 = self.color_passive
                    if self.textfield_active_2:
                        self.display_color_2 = self.color_active
                    else:
                        self.display_color_2 = self.color_passive
                    self.main_screen.fill((255, 255, 0))
                    pygame.draw.rect(self.main_screen, self.display_color_1, [280, 100, 250, 50])
                    pygame.draw.rect(self.main_screen, self.display_color_2, [280, 250, 250, 50])
                    pygame.draw.rect(self.main_screen, (255, 255, 255), [0, 0, 130, 40])
                    self.arrow_font = pygame.font.SysFont(None, 60)
                    self.arrow_img = self.arrow_font.render("BACK", True, (0, 0, 0))
                    self.main_screen.blit(self.arrow_img, (0, 0))

                    self.width_font = pygame.font.SysFont(None, 60)
                    self.width_img = self.width_font.render("WIDTH", True, (0, 0, 0))
                    self.main_screen.blit(self.width_img, (100, 108))
                    self.length_font = pygame.font.SysFont(None, 60)
                    self.length_img = self.length_font.render("LENGTH", True, (0, 0, 0))
                    self.main_screen.blit(self.length_img, (100, 258))

                    self.user_input_font =pygame.font.SysFont(None, 60)
                    self.user_input_img_1 = self.user_input_font.render(self.user_text_1, True, (0, 0, 0))
                    self.main_screen.blit(self.user_input_img_1, (285, 105))
                    self.user_input_img_2 = self.user_input_font.render(self.user_text_2, True, (0, 0, 0))
                    self.main_screen.blit(self.user_input_img_2, (285, 255))

                    self.input_Horizontal = self.user_text_1
                    self.input_Vertical = self.user_text_2
                    # validation
                    if self.input_Horizontal.isdigit():
                        pygame.draw.rect(self.main_screen, (255, 255, 0), [150, 150, 400, 100])
                        self.user_input_horizontal = int(self.input_Horizontal)
                        if self.user_input_horizontal > 64 or self.user_input_horizontal < 15:
                            self.user_input_horizontal = 30
                    elif self.text_field_actived_1 >= 2:
                        self.valid_img_h = self.user_input_font.render("Please input an integer!", True, (0, 0, 0))
                        self.main_screen.blit(self.valid_img_h, (235, 150))
                    if self.input_Vertical.isdigit():
                        pygame.draw.rect(self.main_screen, (255, 255, 0), [150, 300, 400, 100])
                        self.user_input_vertical = int(self.input_Vertical)
                        if self.user_input_vertical > 64 or self.user_input_vertical < 5:
                            self.user_input_vertical = 30
                    elif self.text_field_actived_2 >= 2:
                        self.valid_img_v = self.user_input_font.render("Please input an integer!", True, (0, 0, 0))

                    self.input_rule_font = pygame.font.SysFont(None, 20)
                    self.rule_size = self.input_rule_font.render("Please note that the game will function at 30x30 if the input is either lower than 15x5 or higher than 64x64", True, (0, 0, 0))
                    self.main_screen.blit(self.rule_size, (20, 350))
                pygame.display.update()
                # explain rules
            while self.rule_page_running:
                '''
                1.	Any live cell with two or three live neighbours survives.
                2.	Any dead cell with three live neighbours becomes a live cell.
                3.	All other live cells die in the next generation. Similarly, all other dead cells stay dead.
                '''
                self.rule_screen = pygame.display.set_mode((720, 400))
                pygame.display.set_caption("Rules")
                self.rule_screen.fill((255, 255, 255))
                for self.event in pygame.event.get():
                    if self.event.type == pygame.QUIT:
                        self.main_page_running = True
                        self.rule_page_running = False
                self.rules_font = pygame.font.SysFont(None, 30)

                self.rule_one = self.rules_font.render("1. Any live cell with two or three live neighbours survives.", True, (0, 0, 0))
                self.rule_two = self.rules_font.render("2. Any dead cell with three live neighbours becomes a live cell.", True, (0, 0, 0))
                self.rule_three = self.rules_font.render("3. All other live cells die in the next generation. Similarly, all other", True, (0, 0, 0))
                self.rule_three_part2 = self.rules_font.render(" dead cells stay dead.", True, (0, 0, 0))
                self.rule_screen.blit(self.rule_one, (30, 50))
                self.rule_screen.blit(self.rule_two, (30, 150))
                self.rule_screen.blit(self.rule_three, (30, 250))
                self.rule_screen.blit(self.rule_three_part2, (45, 280))

                pygame.display.update()

            while self.running:
                # set up window
                self.screen_x = self.user_input_horizontal * 20 + 2
                self.screen_y = self.user_input_vertical * 20 + 2 + 80
                self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))
                pygame.display.set_caption("Game Of Life")

                # get mouse position
                GUI.mouseX = pygame.mouse.get_pos()[0]
                GUI.mouseY = pygame.mouse.get_pos()[1]

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        self.game_running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if self.mech.in_box_x() != -1 and self.mech.in_box_y() != -1:
                            if self.cells[self.mech.in_box_x()][self.mech.in_box_y()] == 0:
                                self.cells[self.mech.in_box_x()][self.mech.in_box_y()] = 1
                            elif self.cells[self.mech.in_box_x()][self.mech.in_box_y()] == 1:
                                self.cells[self.mech.in_box_x()][self.mech.in_box_y()] = 0

                        if 5 < GUI.mouseX < 285 and 10 < GUI.mouseY < 70:
                            if self.pause:
                                self.pause = False
                            elif not self.pause:
                                self.pause = True

                # initialize background
                self.screen.fill((158, 205, 250))


                # setup cells gui
                for x in range(self.user_input_horizontal):
                    for y in range(self.user_input_vertical):
                        pygame.draw.rect(self.screen, (249, 251, 175), [1 + x * 20, 1 + y * 20 + 80, 20 - 2 * 1, 20 - 2 * 1])
                        if self.cells[x][y] == 1:
                            pygame.draw.rect(self.screen, (240, 162, 249), [1 + x * 20, 1 + y * 20 + 80, 18, 18])

                # calculation
                if not self.pause:
                    for x in range(self.user_input_horizontal):
                        for y in range(self.user_input_vertical):
                            self.neighbours[x][y] = self.mech.is_neighbours(x, y)
                            if self.cells[x][y] == 1:
                                if int(self.neighbours[x][y]) < 2 or int(self.neighbours[x][y]) > 3:
                                    self.new_cells[x][y] = 0
                            if self.cells[x][y] == 0:
                                if int(self.neighbours[x][y]) == 3:
                                    self.new_cells[x][y] = 1
                    self.cells[:] = self.new_cells[:]

                # draw pause button
                pygame.draw.rect(self.screen, (153, 153, 153), [5, 10, 280, 60])
                self.pause_font = pygame.font.SysFont(None, 60)

                if self.pause:
                    self.pause_start_img = self.pause_font.render("START", True, (255, 255, 255))
                    self.screen.blit(self.pause_start_img, (75, 22))
                elif not self.pause:
                    self.pause_stop_img = self.pause_font.render("STOP", True, (255, 255, 255))
                    self.screen.blit(self.pause_stop_img, (75, 22))

                self.new_cells[:] = self.cells[:]

                pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    gui = GUI()
    gui.game()
