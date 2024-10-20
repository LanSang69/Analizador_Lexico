import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .logic import AFN, Operations as op

afn_saved = []
count = 0

@csrf_exempt
def set_empty(request):
    if request.method == 'POST':
        try:
            global afn_saved
            afn_saved = []

            global count
            count = 0

            return JsonResponse({'status': 'success', 'message': 'Automatas reiniciados'}, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
@csrf_exempt
def crear_basico(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            inferior = data.get('inferior')
            superior = data.get('superior')
            print("elements")
            print(inferior)
            print(superior)

            afn = AFN.AFN()
            afn.crearAFNBasicoRange(inferior, superior)
            global count
            count += 1
            afn.set_idAFN(count)

            if 'automatas' not in request.session:
                request.session['automatas'] = []

            afn_saved.append(afn)
            request.session['automatas'].append(afn.get_idAFN())

            message = op.print_afn_details(afn)

            return JsonResponse({'status': 'success', 'message': f'Automata creado con id: {afn.get_idAFN()}', 'data': message}, status=200)
        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Missing parameter: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)