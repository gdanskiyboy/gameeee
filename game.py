import pygame
import os

import cv2
from emoapi import emotionimg, detect_faces

emotion=8

_image_library = {}


def get_emot():
    
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    a = detect_faces(frame)*4
    if len(a) > 0:
        for f in a:
            emo_label, _ = emotionimg(frame[f[1]:f[1] + f[3], f[0]:f[0] + f[2]])
        emo_labels = dict(zip(list({0:'angry',1:'disgust',2:'fear',3:'happy',
                4:'sad',5:'surprise',6:'neutral'}.values()), range(7)))
        print(emo_labels[emo_label])
        return emo_labels[emo_label]
    return -1



def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


pygame.init()
screen = pygame.display.set_mode((1079, 620))
done = False
clock = pygame.time.Clock()
emotion = 0
while emotion != 3 or done != True:
    emotion = get_emot()
    print(emotion)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    screen.blit(get_image('deva2.png'), (0, 0))

    pygame.display.flip()
    clock.tick(6)

    if emotion == 3:
        break

    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

pygame.init()
screen = pygame.display.set_mode((1079, 620))
done = False
clock = pygame.time.Clock()
emotion = 1
while emotion != 5 or done != True:
    emotion = get_emot()
    print(emotion)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    screen.blit(get_image('deva3.png'), (0, 0))

    pygame.display.flip()
    clock.tick(6)

    if emotion == 5:
        break


    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

pygame.init()
screen = pygame.display.set_mode((1079, 620))
done = False
clock = pygame.time.Clock()
emotion = 1
while emotion != 0 or done != True:
    emotion = get_emot()
    print(emotion)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    screen.blit(get_image('deva4.png'), (0, 0))

    pygame.display.flip()
    clock.tick(6)

    if emotion == 0:
        break


    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

pygame.init()
screen = pygame.display.set_mode((1079, 620))
done = False
clock = pygame.time.Clock()
emotion = 1
while emotion != 0 or done != True:
    emotion = get_emot()
    print(emotion)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    screen.blit(get_image('deva1.png'), (0, 0))

    pygame.display.flip()
    clock.tick(6)

    if emotion == 0:
        break


    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

pygame.init()
screen = pygame.display.set_mode((1079, 620))
done = False
clock = pygame.time.Clock()
emotion = 1
while emotion != 0 or emotion !=6 or done != True:
    emotion = get_emot()
    print(emotion)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    screen.blit(get_image('deva6.png'), (0, 0))

    pygame.display.flip()
    clock.tick(6)

    if emotion == 0 or emotion ==6:
        break


    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)
pygame.init()
screen = pygame.display.set_mode((1079, 620))
done = False
clock = pygame.time.Clock()
emotion = 1
while emotion != 3 or done != True:
    emotion = get_emot()
    print(emotion)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    screen.blit(get_image('deva7.png'), (0, 0))

    pygame.display.flip()
    clock.tick(6)

    if emotion == 3:
        break


    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

pygame.init()
screen = pygame.display.set_mode((1079, 620))
done = False
clock = pygame.time.Clock()
emotion = 1
while emotion != 4 or done != True:
    emotion = get_emot()
    print(emotion)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    screen.blit(get_image('deva8.png'), (0, 0))

    pygame.display.flip()
    clock.tick(6)

    if emotion == 4:
        break


    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

pygame.init()
screen = pygame.display.set_mode((1079, 620))
done = False
clock = pygame.time.Clock()
emotion = 1
while emotion != 3 or done != True:
    emotion = get_emot()
    print(emotion)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    screen.blit(get_image('deva9.png'), (0, 0))

    pygame.display.flip()
    clock.tick(6)

    if emotion == 3:
        break


    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

pygame.init()
screen = pygame.display.set_mode((1079, 620))
done = False
clock = pygame.time.Clock()
