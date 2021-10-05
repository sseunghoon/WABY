from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Result, Choice, Feedback
from django.urls import reverse


def index(request):
    total_num = Result.objects.count()
    army_num = Result.objects.filter(belong=1).count()
    navy_num = Result.objects.filter(belong=2).count()
    airforce_num = Result.objects.filter(belong=3).count()

    context = {
        'total_num': total_num,
        'army_num': army_num,
        'navy_num': navy_num,
        'airforce_num': airforce_num,
    }
    return render(request, 'mlic/index.html', context)


def form(request):
    questions = Question.objects.all()
    questions_count = Question.objects.count()

    context = {
        'questions': questions,
        'questions_count': questions_count,
    }
    return render(request, 'mlic/form.html', context)

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     selected_choice.votes += 1
#     selected_choice.save()
#     # POST data가 잘 처리되었으면 언제나 HttpResponseRedirect를 줘서
#     # 유저가 뒤로 가기 버튼을 눌렀을 때 2번 전송되는 것을 방지함
#     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def submit(request):
    question_cnt = Question.objects.count()
    intensity_sum = 0

    for i in range(1, question_cnt+1):
        intensity = int(request.POST[f'question-{i}'])
        intensity_sum = intensity_sum + intensity

    serial_num = int(request.POST[f'serial_num'])
    belong = int(request.POST[f'belong'])

    result = Result()
    result.intensity_sum = intensity_sum
    result.serial_num = serial_num
    result.belong = belong
    result.save()

    result_id = Result.objects.count()

    return redirect('mlic:result', result_id=result_id)


def result(request, result_id):
    result = Result.objects.get(pk=result_id)
    belong = result.belong
    serial_num = result.serial_num
    intensity_sum = result.intensity_sum

    #####################################################

    result_cnt = Result.objects.count()
    results = Result.objects.all()
    result_low_cnt = 0

    for r in results:
        if(r.intensity_sum <= intensity_sum):
            result_low_cnt += 1

    result_high_cnt = result_cnt - result_low_cnt

    rank = result_high_cnt+1
    percentage = round(rank / result_cnt * 100, 2)

    if(percentage <= 50):
        isTop = 1
    else:
        isTop = 0
        percentage = 100-percentage

    #####################################################

    belongs = {
        1: 1,
        2: 2,
        3: 3,
    }

    belongResult_cnt = Result.objects.filter(belong=belongs[belong]).count()
    belongResults = Result.objects.filter(belong=belongs[belong])

    belongResult_low_cnt = 0

    for br in belongResults:
        if(br.intensity_sum <= intensity_sum):
            belongResult_low_cnt += 1

    belongResult_high_cnt = belongResult_cnt - belongResult_low_cnt

    belongRank = belongResult_high_cnt + 1
    belongPercentage = round(belongRank / belongResult_cnt * 100, 2)

    if(belongPercentage <= 50):
        belongIsTop = 1
    else:
        belongIsTop = 0
        belongPercentage = 100-belongPercentage

    #####################################################

    serials = {
        21: 21,
        20: 20,
        19: 19,
        18: 18,
        17: 17,
        16: 16,
        15: 15,
        14: 14,
        13: 13,
        12: 12,
    }

    serialResult_cnt = Result.objects.filter(serial_num=serials[serial_num]).count()
    serialResults = Result.objects.filter(serial_num=serials[serial_num])

    serialResult_low_cnt = 0

    for sr in serialResults:
        if(sr.intensity_sum <= intensity_sum):
            serialResult_low_cnt += 1

    serialResult_high_cnt = serialResult_cnt - serialResult_low_cnt

    serialRank = serialResult_high_cnt + 1
    serialPercentage = round(serialRank / serialResult_cnt * 100, 2)

    if(serialPercentage <= 50):
        serialIsTop = 1
    else:
        serialIsTop = 0
        serialPercentage = 100-serialPercentage

    #####################################################

    customResult_cnt = Result.objects.filter(belong=belongs[belong], serial_num=serials[serial_num]).count()
    customResult = Result.objects.filter(belong=belongs[belong], serial_num=serials[serial_num])

    customResult_low_cnt = 0

    for cr in customResult:
        if(cr.intensity_sum <= intensity_sum):
            customResult_low_cnt += 1

    customResult_high_cnt = customResult_cnt - customResult_low_cnt

    customRank = customResult_high_cnt + 1
    customPercentage = round(customRank / customResult_cnt * 100, 2)

    if(customPercentage <= 50):
        customIsTop = 1
    else:
        customIsTop = 0
        customPercentage = 100-customPercentage

    #####################################################

    if(belong == 1):
        belong_str = "육군"
    elif(belong == 2):
        belong_str = "해군"
    else:
        belong_str = "공군"

    serial_str = str(serial_num)+"군번"

    summary = ""

    if intensity_sum <= 25:
        summary = "말랑 부대"
    elif intensity_sum <= 50:
        summary = "평균 K-ARMY 부대"
    elif intensity_sum <= 75:
        summary = "강철 부대"
    else:
        summary = "도대체 어떤 군생활을...?"

    percentage = format(percentage, '.2f')
    belongPercentage = format(belongPercentage, '.2f')
    serialPercentage = format(serialPercentage, '.2f')
    customPercentage = format(customPercentage, '.2f')

    #####################################################

    context = {
        'intensity_sum': intensity_sum,
        'result_cnt': result_cnt,
        'percentage': percentage,
        'rank': rank,
        'isTop': isTop,
        'belong': belong,
        'belongResult_cnt': belongResult_cnt,
        'belongPercentage': belongPercentage,
        'belongRank': belongRank,
        'belongIsTop': belongIsTop,
        'serial_num': serial_num,
        'serialResult_cnt': serialResult_cnt,
        'serialPercentage': serialPercentage,
        'serialRank': serialRank,
        'serialIsTop': serialIsTop,
        'belong_str': belong_str,
        'serial_str': serial_str,
        'customResult_cnt': customResult_cnt,
        'customPercentage': customPercentage,
        'customRank': customRank,
        'customIsTop': customIsTop,
        'summary': summary,
        'result_id': result_id,
    }

    return render(request, 'mlic/result.html', context=context)


def feedback(request):

    content = request.POST[f'feedback_content']
    result_id = request.POST[f'result_id']

    feedback = Feedback()
    feedback.content = content
    feedback.save()

    return redirect('mlic:result', result_id=result_id)

