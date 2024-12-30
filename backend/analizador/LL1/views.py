import json
import traceback
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from .logic.LL1 import gGramaticas as G
from .logic.lexico import AFN, Operations as op, AFD, Analizador as A, simbolosEspeciales as s, EvaluadorExpr as E, regex as R
from .logic.LL1 import LR0, Operations as Op

shared_lr0 = None

@csrf_exempt
def getLexico(request):
     if request.method == 'POST':
        try:
            data = json.loads(request.body)
            sigma = data.get('sigma')

            lr0 = LR0.LR0()
            lexicAnalisis = lr0.generarLexico(sigma)
            
            return JsonResponse({
                    'status': 'success',
                    'message': 'Analisis lexico creado',
                    'data': {
                       'descripcion': lexicAnalisis
                    }
                }, status=200)

    
        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Parametro faltante: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        

@csrf_exempt
def getReglas(request):
    global shared_lr0 

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            gramatica = data.get('gramatica')

            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(base_dir, 'LL1', 'gramaticas.txt')

            with open(file_path, 'r') as file:
                table = file.read()

            afd = AFD.AFD()
            afd.leerString(table)
            ll1 = G.GramaticaGramaticas()

            lines = gramatica.split("\n")
            for line in lines:
                ll1.initWithAFD(line, afd)
                ll1.G()
            ll1.AnalizarGramatica()

            lr0 = LR0.LR0()
            lr0.init(ll1)
            lr0.crearTablaLR0()
            lr0.generarTabla()
            details = lr0.imprimirAnalisis()

            shared_lr0 = lr0

            return JsonResponse({
                'status': 'success',
                'message': 'Gramatica creada',
                'data': {
                    'terminals': lr0.Vt,
                    'nonTerminals': lr0.Vn,
                    'details': details,
                    'table': lr0.TablaLR0,
                    'renglones': lr0.NumRenglonesTabla
                }
            }, status=200)

        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Parametro faltante: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt
def getTablaAnalisis(request):
    global shared_lr0 
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            matrix = data.get('matrix')
            sigma = data.get('sigma')

            if shared_lr0 is None:
                raise Exception("Gramatica no inicializada. Por favor, cree una gramatica primero.")

            print("tablaLR0")
            print(shared_lr0.TablaLR0)
            result, tabla = shared_lr0.analizarSigma(sigma, matrix)

            return JsonResponse({
                'status': 'success',
                'message': 'Tabla de análisis creada',
                'data': {
                    'valid': result,
                    'tabla': tabla
                }
            }, status=200)

        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Parametro faltante: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
