from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from polls.models import Question, Choice    
from django.http.response import Http404
# Create your views here.
    
def index(request):
    poll_list = Question.objects.order_by('-pub_date') #[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_poll_list': poll_list,
    })
    return HttpResponse(template.render(context))

def detail(request, poll_id):
    # a page that gives the detail view of each Poll
    try:
        poll_view = Question.objects.get(pk=poll_id)
    except Question.DoesNotExist :
        raise Http404   
    context = {'poll' : poll_view}
    return render(request, 'polls/detail.html', context)

def results(request, poll_id):
    poll = get_object_or_404(Question, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
 
def vote(request, poll_id):
    poll_vote = get_object_or_404(Question, pk=poll_id)
    try:
        selected_choice = poll_vote.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': poll_vote,
            'error_message': "You didn't select a choice.",
        })      
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(poll_vote.id,)))

    
    return HttpResponse("You're voting on poll %s." % poll_id)