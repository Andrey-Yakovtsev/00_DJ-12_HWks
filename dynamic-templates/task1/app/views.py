import csv


from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'
    with open("inflation_russia.csv", encoding="utf-8") as fo:
        read_csv = list(csv.reader(fo))
    table = [x.split(';') for b in read_csv for x in b]

    for array in table:
        for i in range(len(array)):
            old_value = array[i]
            try:
                if old_value == '':
                    new_value = '-'
                    array[i] = new_value
            except:
                pass

    context = {
        'table_header': table[0],
        'table': table[1:]
    }

    return render(request, template_name, context)