import pygame

#button class
class Button():
	def __init__(self, x, y, image, caption='', scale=1, color = '#9F71DB', color_back ='#354259'):
		self.width = image.get_width()
		self.height = image.get_height()
		self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False

		# caption
		self.caption = caption
		self.font = pygame.font.Font(None, 40)
		self.text = self.font.render(self.caption, 1, color)
		self.text_back = self.font.render(self.caption, 1, color_back)

	def draw(self, surface):

		action = False
		# get mouse position
		pos = pygame.mouse.get_pos()

		# draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))
		textx = self.rect.x + self.width // 2 - self.text.get_width() // 2
		texty = self.rect.y + self.height // 2 - self.text.get_height() // 2
		surface.blit(self.text_back, (textx - 2, texty + 2))
		surface.blit(self.text, (textx, texty))

		# check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return action



