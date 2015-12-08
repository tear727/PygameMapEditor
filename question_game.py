class QuestionBank(object):
    def __init__(self):
        self.question1 = "question 1?"
        self.question2 = "question 2?"
        self.question3 = "question 3?"
        self.question4 = "question 4?"
        self.default_question = self.question1


class Background(object):
    def __init__(self, path_to_image):
        self.background_image = path_to_image


class Scene(object):
    def __init__(self,question_bank, background):
        self.question = question_bank.default_question
        self.answer = raw_input(self.question)
        self.background = background

    def update(self, question_bank):
        if self.answer == "a":
            self.question = question_bank.question2
            print self.question
        elif self.answer == "b":
            self.question = question_bank.question3
            print self.question
        elif self.answer == "c":
            self.question = question_bank.question3
            print self.question
        elif self.answer == "d":
            self.question = question_bank.question4
            print self.question
        else:
            print "please choose a or b!"


def main():
    """ Below are the instantiations of classess.  They are the actual objects.
    Classes alone are only 'object factories' and need to have corresponding
    instantiations to be used! """

    scene_1_bank = QuestionBank()
    background1 = Background("This is the image path")
    scene1 = Scene(scene_1_bank, background1)

    """ Scene1.update(Questions) calls the Scene1 method '.update'
    It is passed the 'Questions' instantiation as the 'question_bank' argument
    so that it has access to the data stored in 'Questions'.  In this case,
    that is how Scene1 'updates' the question."""
    scene1.update(scene_1_bank)

    """In reality, this is a poor example of a question game engine because
    it does not fully support modularity of classes.  In other words, it could
    be done much cleaner.  First of all, QuestionBank() is hard-coded.  Instead
    of seeting variables like 'self.question1 = "question1"', we would instead
    want to put multiple questions for a scene into a DATA STRUCTURE that can
    hold multiple questions.

    For example, if you wanted to add more scenes, you would need to make new
    instantiation of Scene() and QuestionBank() with their own different properties.
    Let's say you named them scene2 and scene_2_bank.

    The scene2 object would perhaps have a new background.  But, if you wanted
    the scene2 object to have DIFFERENT QUESTIONS than the scene1 object,
    you could ONLY achieve this if you get rid of the hard coded questions in the
    scene_1_bank object or if you made the scene_2_bank object and then OVERRIDE
    the question variables b ysetting them to new questions manually.
    THAT IS BAD DESIGN.

    There is a better way to do all this and that involves using data structures
    to hold data."""


    """
    Ready for the easiest "challenge" of your life? Try and print the 'background'
    variables value by accessing it THROUGH scene1.  It's super easy... I
    basically showed you how.  If you do it then you will see the relationships
    being made between the Scene()class and Background class.

    Hint: use '.' notation... lol

    The output in your terminal should be: This is the image path
    """


main()
