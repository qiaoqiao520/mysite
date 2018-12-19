from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic   # 从数据库中取数据前台渲染列表的操作比较简单，重复，Django封装了一个过程并提供统一的模板
from django.http import Http404

# Create your views here.


# def index(request):
#     """
#     展示问题列表
#     :param request:
#     :return:
#     """
#     question_list = Question.objects.all().order_by('-pub_date')[0:5]
#     # print(question_list)
#     # output = ''
#     # for q in question_list:
#     #     print(q.id, q.question_text, q.pub_date)
#     #     output = output + q.question_text + '，'
#     # print(output)
#     # 下面一行列表生成式代替上面四五行
#     # output = ','.join([q.question_text for q in question_list])
#     template = loader.get_template('polls/index.html')
#     context = {
#         'question_list': question_list
#     }
#     return HttpResponse(template.render(context, request))


def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'question_list': question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """
    显示一个问题的详细信息，问题内容，问题发布时间，选项内容，每个选项投票数
    :param request:
    :param question_id:
    :return:
    """
    """
    # 写法一
    try:
        question = Question.objects.filter(id=question_id)
    except Question.DoesNotExist:
        raise Http404("404,此id的问题不存在")
    print(question)
    context = {
       'question': question
   }
    # 写法二
    # question = Question.objects.filter(id=question_id)
    # if not question:
    #     raise Http404()
    return render(request, 'polls/detail.html', context)
    """

    # 写法三
    question = get_object_or_404(Question, id=question_id)
    # 由于orm代劳，question直接带出对应的choices
    # choices = question.choice_set.all()
    # 由于前端模板语言本质是后端代码，可以把上一句放在html中写，有助于降低后端复杂度
    # choices = Choice.objects.filter(question_id=question.id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    """
    投票结果
    :param request:
    :param question_id:
    :return:
    """
    question = Question.objects.get(id=question_id)
    context = {
        'question': question,
    }

    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    """
    投票
    :param request:
    :param question_id:
    :return:
    """
    try:
        question = Question.objects.get(id=question_id)
        choices = question.choice_set.all()
        choice_id = request.POST['choice']
        selected_choice = question.choice_set.get(id=choice_id)
    except Question.DoesNotExist as e:
        error_message = '问题内容不存在，请检查问题id'
    except Choice.DoesNotExist as e:
        error_message = '问题对应的选项不存在'
        return render(request, 'polls/detail.html', context={
            'question': question,
            'error_message': error_message
        })
    else:
        # sql  update choice set votes=votes+1 where id=2
        selected_choice.votes += 1
        selected_choice.save()
        # 投票完重定向到 views.results(qid)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# 通用模板示例，跟def index 类比着看，比较适合单调的增删查改
class SimpleView(generic.ListView):
    template_name = 'polls/index.html '
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()




