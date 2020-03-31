from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic
from .forms import NameForm
import logging

logger = logging.getLogger(__name__)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = '<br>'.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello, world. You're at the polls index.")
    # loader 旧版本模板渲染
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    # render 模板渲染 -- 比较快捷
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    logger.info("首页展示...")
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # 上面的代码 等同于
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', args=(question.id,))
        # 等同于下面这条代码
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def get_name(request):
    # 如果form通过POST方法发送数据
    if request.method == 'POST':
        # 接受request.POST参数构造form类的实例
        form = NameForm(request.POST)
        # 验证数据是否合法
        if form.is_valid():
            # 处理form.cleaned_data中的数据
            # ...
            # 重定向到一个新的URL
            return redirect('polls:thanks')

    # 如果是通过GET方法请求数据，返回一个空的表单
    else:
        form = NameForm()
    return render(request, 'polls/name.html', {'form': form})

def thanks(request):
    return HttpResponse("OK!")