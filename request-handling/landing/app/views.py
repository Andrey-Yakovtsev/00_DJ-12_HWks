from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()

index_counter = 1
i = 0
j = 0

def index(request):
    # counter = {}
    from_landing = request.GET.get('from-landing')
    global j
    global i
    global index_counter
    if from_landing == 'test':
        i += 1
        counter = {'test': i}
        print(counter)
    else:
        j += 1
        counter = {'landing': j}
        print(counter)
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    index_counter += 1
    return render_to_response('index.html')


def landing(request):
    from_landing = request.GET.get('from-landing')
    if from_landing == 'test':
        return render_to_response('landing_alternate.html')
    else:
        return render_to_response('landing.html')

# Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов




def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    return render_to_response('stats.html', context={
        'index_counter': index_counter,
        'test_conversion':  i / index_counter,
        'original_conversion': j / index_counter,
    })
