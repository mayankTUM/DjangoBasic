from polls.models import Question, Choice
from django.utils import timezone

# created already
#p = Question(question_text="What's your favorite color?", pub_date = timezone.now())
#p = Question.objects.get(id=1)

# Give the Poll a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a poll's choices) which can be accessed via the API.


# created already
#p.choice_set.create(choice_text = "red", votes = 0)
#p.choice_set.create(choice_text = "blue", votes = 0)
#p.choice_set.create(choice_text = "green", votes = 0)


#q = Choice(question_id=1,choice_text = "orange", votes=0)
#q.save()
#q = Choice.objects.filter(question__question_text__startswith = "what")
#print q

q = Choice.objects.filter(question_id = 1)
print q
