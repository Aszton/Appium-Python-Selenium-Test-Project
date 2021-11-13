import unittest
import pytest
import utilities.CustomLogger as cl
from pages.dragAndDropPage import dragAndDropPage

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class tabActivityTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.dnd = dragAndDropPage(self.driver)

    @pytest.mark.run(order=1)
    def test_dragAndDrop(self):
        cl.allureLogs("App Opened")
        self.dnd.scrollToTheDNDButton()
        self.dnd.clickDragAndDropButton()
        self.dnd.dragLogoAndDropItToTheBlueSquare()
        self.dnd.dragLogoFromTheBlueSquareAndDropItToTheGreenSquare()
        self.dnd.dragTextAndDropItToTheBlueSquare()
        self.dnd.dragTextFromTheBlueSqareAndDropItToTheGreenSquare()
        self.dnd.dragButtonAndDropItToTheBlueSquare()
        self.dnd.dragButtonFromTheBlueSquareAndDropItToTheGreenSquare()