import time
from base.customCommands import elementPage
import utilities.CustomLogger as cl


class dragAndDropPage(elementPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    dragAndDropButton = "com.code2lead.kwad:id/drag"  # id
    dragLogoKLO = "com.code2lead.kwad:id/ingvw"  # id
    blueSquare = "com.code2lead.kwad:id/layout2"  # id
    greenSquare = "com.code2lead.kwad:id/layout3"  # id
    dragText = "com.code2lead.kwad:id/lbl"  # id
    dragButton = "com.code2lead.kwad:id/btnDrag"  # id

    def scrollToTheDNDButton(self):
        self.swipe(997, 1764, 956, 326)

    def clickDragAndDropButton(self):
        self.clickElement(self.dragAndDropButton, "id")
        cl.allureLogs("Click on Tab Drag And Drop Button")

    def dragLogoAndDropItToTheBlueSquare(self):
        self.dragAndDropByElements(self.dragLogoKLO, self.blueSquare, "id")

    def dragLogoFromTheBlueSquareAndDropItToTheGreenSquare(self):
        self.dragAndDropByElements(self.dragLogoKLO, self.greenSquare, "id")

    def dragTextAndDropItToTheBlueSquare(self):
        self.dragAndDropByElements(self.dragText, self.blueSquare, "id")

    def dragTextFromTheBlueSqareAndDropItToTheGreenSquare(self):
        self.dragAndDropByElements(self.dragText, self.greenSquare, "id")

    def dragButtonAndDropItToTheBlueSquare(self):
        self.dragAndDropByElements(self.dragButton, self.blueSquare, "id")

    def dragButtonFromTheBlueSquareAndDropItToTheGreenSquare(self):
        self.dragAndDropByElements(self.dragButton, self.greenSquare, "id")


