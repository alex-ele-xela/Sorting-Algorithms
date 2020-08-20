import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((800, 290))
pygame.display.set_caption("Bubble Sort Visualizer")

arial = pygame.font.SysFont("Arial", 27)

array = [randint(1, 50) for i in range(10)]
sortedArray = sorted(array)


# Function to check whether the given array is the sorted version of original array
def checkSorted(array):
    if array == sortedArray:
        return True
    return False


# Generator to update the array in each iteration
def bubbleSort(array):
    sortedArray = array[:]

    # Outer loop which specifies the position to put the bubbled element
    for i in range(len(sortedArray)-1, 0, -1):

        # Loop for bubbling the greatest element to the i'th position
        for j in range(i):
            change = False
            if sortedArray[j] > sortedArray[j+1]:
                sortedArray[j], sortedArray[j +
                                            1] = sortedArray[j+1], sortedArray[j]
                change = True

            # Yielding values (bool = if the original array is sorted, 1st index being compared, 2nd index being compared, bool = if the two are changed, value of outer array)
            yield (checkSorted(sortedArray), j, j+1, change, i)

# Stores the generator function which provides the next array
getArray = bubbleSort(array)


class Box():
    def __init__(self, x, y, width, height, num):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.num = num

        if self.num > 9:
            self.xSpace = 15
        else:
            self.xSpace = 21
    
    def draw(self, window):
        pygame.draw.rect(window, (255,255,255), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(window, (150, 150, 150), (self.x, self.y, self.width, self.height), 5)

        number = arial.render(str(self.num), True, (0,0,0))
        window.blit(number, (self.x + self.xSpace, self.y + 16))


class Dot():
    def __init__(self, x):
        self.x = x
    
    def draw(self, window):
        pygame.draw.circle(window, (255,0,0), (self.x, 200), 6)


arrayGUI = []
for i in range(10):
    x = 50 + (i * 70) + 5
    y = 110
    width = 60
    height = 60

    arrayGUI.append(Box(x, y, width, height, array[i]))


def redrawWindow():
    window.fill((255,255,255))

    for i in range(10):
        arrayGUI[i].draw(window)

    if not(isSorted):
        for i in range(len(dots)):
            dots[i].draw(window)
    
    pygame.display.update()


dots = []

run = True
isSorted = False
changing = False
timeDelay = 1000
sortedElements = 9
while run:
    pygame.time.delay(timeDelay)
    redrawWindow()

    if not(isSorted) and not(changing):
        isSorted, i, j, changing, sortedSide = next(getArray)

        if sortedSide < sortedElements:
            sortedElements -= 1
            dots.append(Dot(arrayGUI[sortedSide+1].x + 35))

        finalPos = arrayGUI[j].x
    
    if changing:
        timeDelay = 100

        if arrayGUI[i].x < finalPos :
            arrayGUI[i].x += 5
            arrayGUI[j].x -= 5
        else:
            timeDelay = 1000
            changing = False

            arrayGUI[i], arrayGUI[j] = arrayGUI[j], arrayGUI[i]



    for event in pygame.event.get():
        # Closing the window
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
