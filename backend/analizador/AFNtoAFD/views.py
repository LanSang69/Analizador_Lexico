import json
import traceback
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .logic import AFN, Operations as op, AFD, Analizador as A, simbolosEspeciales as s
afns_ids = []
afn_saved = []
descriptions = {}

@csrf_exempt
def get_session_data(request):
    if request.method == 'GET':
        try:
            global afns_ids
            global descriptions
            return JsonResponse({
                'status': 'success',
                'data': afns_ids,  # List of automata IDs
                'descriptions': descriptions, # ID-description pairs
            }, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt
def set_empty(request):
    if request.method == 'POST':
        try:
            global afn_saved
            afn_saved = []

            global afns_ids
            afns_ids = []

            global descriptions
            descriptions = {}

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

            afn = AFN.AFN()
            afn.crearAFNBasicoRange(inferior, superior)
            global afn_saved
            afn_saved.append(afn)

            random_id = op.generate_random_id()
            afn.set_idAFN(random_id)

            global afns_ids
            afns_ids.append(random_id)

            global descriptions
            descriptions[random_id] = op.print_afn_details(afn)
            
            message = op.print_afn_details(afn)
            return JsonResponse({'status': 'success', 'id': afn.get_idAFN(), 'message': f'Automata creado con id: {afn.get_idAFN()}', 'data': message, 'description': descriptions}, status=200)
        
        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Parametro faltante: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
@csrf_exempt
def concatenate_afns(request):
    if request.method == 'POST':
        try:
            global afn_saved
            global afns_ids
            global descriptions
            data = json.loads(request.body)
            id1 = data.get('id1')
            id2 = data.get('id2')

            # Find AFNs by IDs
            afn1 = next((a for a in afn_saved if a.get_idAFN() == id1), None)
            afn2 = next((a for a in afn_saved if a.get_idAFN() == id2), None)

            if not afn1 or not afn2:
                return JsonResponse({'status': 'error', 'message': 'Alguno de los automatas no se encontró'}, status=404)

            # Concatenate AFNs
            afn1.Concatenar(afn2)
            
            # Reassign IDs after removing the old ones
            afn_saved = [a for a in afn_saved if a.get_idAFN() not in (id1, id2)]
            
            random_id = op.generate_random_id()

            while random_id in afns_ids:
                random_id = op.generate_random_id()

            afn1.set_idAFN(random_id)
            afn_saved.append(afn1)
            afns_ids = []
            for afn in afn_saved:
                descriptions[afn.get_idAFN()] = op.print_afn_details(afn)
                afns_ids.append(afn.get_idAFN())

            print(afns_ids)
            print(op.print_afn_details(afn1))
            print(descriptions)

            desc = op.print_afn_details(afn1)
            # Return response with success message
            return JsonResponse({'status': 'success', 'id': afn1.get_idAFN(), 'description' : desc, 'message': f'Automata concatenado con id: {afn1.get_idAFN()}'}, status=200)

        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Parametro faltante: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)      
          

@csrf_exempt
def cerradura_p(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data.get('id')

            global afn_saved
            afn = next((a for a in afn_saved if a.get_idAFN() == id), None)

            if not afn:
                return JsonResponse({'status': 'error', 'message': 'Automata no encontrado'}, status=404)

            afn.CerraduraPositiva()

            global afns_ids
            global descriptions

            descriptions[id] = op.print_afn_details(afn)

            desc = op.print_afn_details(afn)
            print(desc)
            return JsonResponse({'status': 'success', 'id': afn.get_idAFN(), 'description' : desc, 'message': f'Cerradura Positiva aplicada al automata de id: {afn.get_idAFN()}'}, status=200)
        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Parametro faltante: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
@csrf_exempt
def cerradura_k(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data.get('id')

            global afn_saved
            afn = next((a for a in afn_saved if a.get_idAFN() == id), None)

            if not afn:
                return JsonResponse({'status': 'error', 'message': 'Automata no encontrado'}, status=404)

            afn.CerraduraKleene()

            global afns_ids
            global descriptions

            descriptions[id] = op.print_afn_details(afn)

            desc = op.print_afn_details(afn)
            print(desc)
            return JsonResponse({'status': 'success', 'id': afn.get_idAFN(), 'description' : desc, 'message': f'Cerradura de Kleene aplicada al automata de id: {afn.get_idAFN()}'}, status=200)
        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Parametro faltante: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@csrf_exempt
def opcional(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data.get('id')

            global afn_saved
            afn = next((a for a in afn_saved if a.get_idAFN() == id), None)

            if not afn:
                return JsonResponse({'status': 'error', 'message': 'Automata no encontrado'}, status=404)

            afn.Opcional()

            global afns_ids
            global descriptions

            descriptions[id] = op.print_afn_details(afn)

            desc = op.print_afn_details(afn)
            print(desc)
            return JsonResponse({'status': 'success', 'id': afn.get_idAFN(), 'description' : desc, 'message': f'Cerradura Opcional aplicada al automata de id: {afn.get_idAFN()}'}, status=200)
        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Parametro faltante: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
@csrf_exempt
def unir_automatas(request):
   if request.method == 'POST':
        try:
            global afn_saved
            global afns_ids
            global descriptions
            data = json.loads(request.body)
            ids_array = data.get('ids')

            afn = next((a for a in afn_saved if a.get_idAFN() == ids_array[0]), None)
            if not afn:
                return JsonResponse({'status': 'error', 'message': f'Automata no encontrado: {ids_array[0]}'}, status=404)
            
            for i in range(1, len(ids_array)):
                afnAux = next((a for a in afn_saved if a.get_idAFN() == ids_array[i]), None)
                if not afnAux:
                    return JsonResponse({'status': 'error', 'message': f'Automata no encontrado: {ids_array[i]}'}, status=404)
                afn.Unir(afnAux)

            
            # Reassign IDs after removing the old ones
            afn_saved = [a for a in afn_saved if a.get_idAFN() not in ids_array]
            afns_ids = [a for a in afns_ids if a not in ids_array]

            random_id = op.generate_random_id()

            while random_id in afns_ids:
                random_id = op.generate_random_id()

            afn.set_idAFN(random_id)
            afn_saved.append(afn)

            descriptions[afn.get_idAFN()] = op.print_afn_details(afn)
            afns_ids.append(afn.get_idAFN())

            # Return response with success message
            return JsonResponse({'status': 'success', 'id': afn.get_idAFN(), 'description' : op.print_afn_details(afn), 'message': f'Automata unido con id: {afn.get_idAFN()}'}, status=200)

        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Parametro faltante: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)      
        
@csrf_exempt
def RegexToAFN(request):
   if request.method == 'POST':
        try:

            data = json.loads(request.body)
            regex = data.get('regex')
            
            if not regex:
                return JsonResponse({'status': 'error', 'message': 'Regex parameter missing'}, status=400)
            afn = AFN.AFN()
            afn = op.expToAFN(regex)

            global afn_saved
            afn_saved.append(afn)

            random_id = op.generate_random_id()
            afn.set_idAFN(random_id)

            global afns_ids
            afns_ids.append(random_id)

            global descriptions
            descriptions[random_id] = op.print_afn_details(afn)

            return JsonResponse({
                'status': 'success',
                'id': afn.get_idAFN(),
                'description': op.print_afn_details(afn),
                'message': f'Automata creado con id: {afn.get_idAFN()}'
            }, status=200)

        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Parametro faltante: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt
def createAFD(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data.get('id')

            global afn_saved
            afn = next((a for a in afn_saved if a.get_idAFN() == id), None)

            if not afn:
                return JsonResponse({'status': 'error', 'message': 'Automata no encontrado'}, status=404)

            Sj, queue = afn.EstadoSi()
            afd = AFD.AFD()
            afd.initTabla(queue)
            afd.guardarEnString()

            return JsonResponse({'status': 'success', 'id': afd.getIdAFD(), 'txt' : afd.getArchivo(), 'message': f'Transformacion completada al AFD id: {afd.getIdAFD()}'}, status=200)
        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Parametro faltante: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt
def analizar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            table = data.get('table')
            sigma = data.get('sigma')
            aux = ""
            afd = AFD.AFD()
            afd.leerString(table)
            analisis = A.AnalizadorLexico()
            analisis.initWithTable(sigma, afd)

            while True:
                token = analisis.yylex()
                if token == s.Simbolos.FIN:
                    break  
                aux = aux + " ".join([str(analisis.Lexema), "\t", str(token), "\n"])
            
            print(aux)
            final_table = aux

            return JsonResponse({'status': 'success', 'analisis': final_table, 'message': f'Transformacion completada al AFD id: {afd.getIdAFD()}'}, status=200)

        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Parametro faltante: {str(e)}'}, status=400)
        except Exception as e:
            error_message = traceback.format_exc()
            return JsonResponse({'status': 'error', 'message': str(e), 'traceback': error_message}, status=500)
