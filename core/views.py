from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from core.models import Enfermedad, Review, Suggestion, Mireview, Enfermedadmaes, Enfermedadmara, Reviewmaes, Reviewmara
from PIL import Image, ImageOps
import datetime
import os.path
import clips
import ast
import time
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from core.forms import EnfermedadmaizForm, EnfermedadmaesmaizForm, EnfermedadmaramaizForm

# ------------------------------------------------------------------------------
# Create your views here.

def index(request):
    return render(request, 'index.html')


#inicio codigofacilitoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

def enfermedadmaiz_view(request):
    if request.method == 'POST':
        form = EnfermedadmaizForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('enfermedadmaiz:index')
    else:
        form = EnfermedadmaizForm()
    return render(request, 'enfermedadmaiz_form.html', {'form':form})  


def enfermedadmaiz_edit(request,id_enfermedadmaiz):
    enfermedadmaiz = Enfermedad.objects.get(id=id_enfermedadmaiz)     
    if request.method == 'GET':
        form = EnfermedadmaizForm(instance=enfermedadmaiz)
    else:
        form = EnfermedadmaizForm(request.POST, instance=enfermedadmaiz)
        if form.is_valid():
            form.save()
        return redirect('accionesPage')
    return render(request, 'enfermedadmaiz_form.html', {'form':form}) 


def enfermedadmaiz_delete(request, id_enfermedadmaiz):
    enfermedadmaiz = Enfermedad.objects.get(id=id_enfermedadmaiz)
    if request.method == 'POST':
        enfermedadmaiz.delete()
        return redirect('accionesPage')
    return render(request,'enfermedadmaiz_delete.html', {'enfermedadmaiz':enfermedadmaiz}) 

#fin codigofacilitoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    


def preferencePage(request):
    return render(request, 'preferences.html')


def preferencemaesPage(request):
    return render(request, 'preferencesmaes.html')  


def preferencemaraPage(request):
    return render(request, 'preferencesmara.html')    

@login_required
def nuevoEnfermedadPage(request):
    return render(request, 'new.html')


def aboutUsPage(request):
    return render(request, 'about.html')

@login_required
def reportePage(request):
    mireviews = Mireview.objects.all()
    return render(request, 'reporte.html', {'mireviews':mireviews})

@login_required
def reportePageoct(request):
    mireviews = Mireview.objects.filter(createdTime__contains='10')
    return render(request, 'reporteoct.html', {'mireviews':mireviews})


@login_required
def reportePagesep(request):
    mireviews = Mireview.objects.filter(createdTime__contains='09')
    return render(request, 'reportesep.html', {'mireviews':mireviews})   

@login_required
def reportePageago(request):
    mireviews = Mireview.objects.filter(createdTime__contains='08')
    return render(request, 'reporteago.html', {'mireviews':mireviews})  


@login_required
def reportemaizPage(request):
    enfermedadmaiz = Enfermedad.objects.all()
    return render(request, 'reportemaiz.html', {'enfermedadmaiz':enfermedadmaiz})


@login_required
def reportecalificacionmaizPage(request):
    reviewmaiz = Review.objects.order_by('-stars')
    return render(request, 'reportecalificacionmaiz.html', {'reviewmaiz':reviewmaiz})


@login_required
def accionesPage(request):
    enfermedadmaiz = Enfermedad.objects.all()
    return render(request, 'acciones.html', {'enfermedadmaiz':enfermedadmaiz})    


@csrf_exempt
def escrituraPage(request):
    enfermedadmaiz = Enfermedad.objects.latest('id')
    return render(request, 'escritura.html', {'enfermedadmaiz':enfermedadmaiz})       


@csrf_exempt
def escritura(request):
  #  insertEscrituraIntoDatabase(request.POST)
  if request.method == "POST":
    insertEscrituraIntoClips()
    return render(request, 'escritura.html')        


# New Review, Assume Data is CORRECT
@csrf_exempt
def processReviews(request):
    if request.method == "POST":
        id = insertReviewIntoDatabase(request.POST)
        insertReviewIntoClips(request.POST, id)
        return HttpResponse('')
    else:
        response = []
        reviews = Review.objects.filter(enfermedadId=int(request.GET['enfermedadId'])).order_by("-id")
        for review in reviews:
            response.append({"id": review.id, "comment": review.comment, "reviewer": review.reviewer,
                    "createdTime": review.createdTime})
        return JsonResponse(response, safe=False)

# MI New Review, Assume Data is CORRECT hahahahahahahahahahahahahahahahahahahahahahahahahahahahaha
@csrf_exempt
def processMireviews(request):
    if request.method == "POST":
        id = insertMireviewIntoDatabase(request.POST)
        return HttpResponse('')


# Create New Dish, Assume Data is CORRECT!
@csrf_exempt
def crearEnfermedad(request):
    id = insertarNuevaEnfermedad(request.POST)
    insertIntoClips(id, request.POST)
    return HttpResponse('')


# A new preferences. Assume Data is CORRECT!
@csrf_exempt
def newPreference(request):
    result = clipsMatchPreference(request.POST)
    print(result)
    response = []
    if result != None:
        for val in result.split('---'):
            if "," in val:
                val2 = val.split(',')
                enfermedad = Enfermedad.objects.get(id=int(val2[0]))
                response.append({"id": enfermedad.id, "name": enfermedad.name, "images": enfermedad.images, "description": enfermedad.description,
#                    "cuisine": val2[1], "vegetarian": val2[2], "hasSoup": val2[3], 
#                    "spicyLevel": val2[8], "saltyLevel": val2[9], "sweetLevel": val2[11],
#                    "stars": float(val2[12])})
                    "planta": val2[1], "sintomaAAA": val2[2], "sintomaBB": val2[3], 
                    "sintomaCC": val2[4], "sintomaDD": val2[5], "sintomaEE": val2[6],
                    "stars": float(val2[7])})

    return JsonResponse(response, safe=False)


# LO MISMO DE ARRIBA PERO PARA Enfermedadmaes
@csrf_exempt
def newPreferencemaes(request):
    result = clipsMatchPreferencemaes(request.POST)
    print(result)
    response = []
    if result != None:
        for val in result.split('---'):
            if "," in val:
                val2 = val.split(',')
                enfermedadmaes = Enfermedadmaes.objects.get(id=int(val2[0]))
                response.append({"id": enfermedadmaes.id, "name": enfermedadmaes.name, "images": enfermedadmaes.images, "description": enfermedadmaes.description,
#                    "cuisine": val2[1], "vegetarian": val2[2], "hasSoup": val2[3], 
#                    "spicyLevel": val2[8], "saltyLevel": val2[9], "sweetLevel": val2[11],
#                    "stars": float(val2[12])})
                    "planta": val2[1], "sintomaAAA": val2[2], "sintomaBB": val2[3], 
                    "sintomaCC": val2[4],
                    "stars": float(val2[5])})

    return JsonResponse(response, safe=False)


# Lo mismo de arriba, pero para Enfermedadmara
@csrf_exempt
def newPreferencemara(request):
    result = clipsMatchPreferencemara(request.POST)
    print(result)
    response = []
    if result != None:
        for val in result.split('---'):
            if "," in val:
                val2 = val.split(',')
                enfermedadmara = Enfermedadmara.objects.get(id=int(val2[0]))
                response.append({"id": enfermedadmara.id, "name": enfermedadmara.name, "images": enfermedadmara.images, "description": enfermedadmara.description,
#                    "cuisine": val2[1], "vegetarian": val2[2], "hasSoup": val2[3], 
#                    "spicyLevel": val2[8], "saltyLevel": val2[9], "sweetLevel": val2[11],
#                    "stars": float(val2[12])})
                    "planta": val2[1], "sintomaAAA": val2[2], "sintomaBB": val2[3], 
                    "sintomaCC": val2[4], "sintomaDD": val2[5], "sintomaEE": val2[6],
                    "stars": float(val2[7])})

    return JsonResponse(response, safe=False)    


# A new preferences. Assume Data is CORRECT!
@csrf_exempt
def modify(request):
    insertSuggestionIntoDatabase(request.POST)
    insertSuggestionsIntoClips()
    return HttpResponse('')


# ------------------------------------------------------------------------------
# Utility Functions
def insertarNuevaEnfermedad(data):
    images = ast.literal_eval(data['images'])
    imageNum = 0;
    for image in images:
        imageNum = imageNum + (image != 'null')

    enfermedad = Enfermedad(name=data['name'],
                description=data['description'],
                images=imageNum,
                planta=data['planta'],
                sintomaAA=data['sintomaAA'],
                sintomaBB=data['sintomaBB'],
                sintomaCC=data['sintomaCC'],
                sintomaEE=data['sintomaEE'],
                sintomaDD=data['sintomaDD'])
    enfermedad.save()

    index = 0
    for image in images:
        if image != 'null':
            index = index + 1
            createImage(enfermedad.id, index, image)

    return enfermedad.id


def createImage(id, index, image):
    imgCore = image.split(',')[1]
    imgFile = open(settings.DISH_IMAGE_DIR + "/" + str(id) + "_" + str(index) + ".jpeg", "wb")
    imgFile.write(imgCore.decode('base64'))
    imgFile.close()

    # Create square image
    img = Image.open(settings.DISH_IMAGE_DIR + "/" + str(id) + "_" + str(index) + ".jpeg")
    longer_side = max(img.size)
    thumb = Image.new('RGBA', (longer_side, longer_side), (255, 255, 255, 0))
    thumb.paste(
        img, ((longer_side - img.size[0]) / 2, (longer_side - img.size[1]) / 2)
    )
    thumb.save(settings.DISH_IMAGE_DIR + "/" + str(id) + "_" + str(index) + "_square.jpeg")


def insertIntoClips(id, data):
    # check if a fact-file exists
    FactsFile = settings.CLIPS_DIR + "/dishes.clp"
    if not os.path.isfile(FactsFile):
        file = open(FactsFile, 'w+')
        file.write("(deffacts enfermedades)\n")
        file.close()

    # modify facts
    lines = open(FactsFile, 'r+').readlines()
    n = len(lines)
    lines[n - 1] = lines[n-1][:-2] + "\n"
    lines.append('  (enfermedad '
                '(ID '+str(id)+')'
                '(name "'+data['name']+'") '
                '(planta "'+data['planta']+'") '
                '(sintoma-aa "'+data['sintomaAA']+'") '
                '(sintoma-bb "'+data['sintomaBB']+'") '
                '(sintoma-cc "'+data['sintomaCC']+'") '
                '(sintoma-ee "'+data['sintomaEE']+'") '
                '(sintoma-dd "'+data['sintomaDD']+'") '
                '(stars -1)))\n')

    # new facts
    open(FactsFile, 'w').writelines(lines)


attributeMap = { 'sintomaAA': 'sintoma-aa',
        'sintomaBB': 'sintoma-bb',
        'sintomaCC': 'sintoma-cc',
        'sintomaDD': 'sintoma-dd',
        'sintomaEE': 'sintoma-ee'};
def insertSuggestionIntoDatabase(data):
    suggestion = Suggestion(
                enfermedadName=data['enfermedadName'],
                enfermedadId=int(data['enfermedadId']),
                attribute=attributeMap[data['key']],
                value=data['value'],
                quantity=0)

    suggestions = Suggestion.objects.filter(enfermedadId=int(data['enfermedadId']), attribute=attributeMap[data['key']], value=data['value'])
    if (len(suggestions) != 0):
        suggestion = suggestions[0]

    suggestion.quantity = suggestion.quantity + 1
    suggestion.save()
    print(suggestion)


def insertSuggestionsIntoClips():
    # check if a fact-file exists
    FactsFile = settings.CLIPS_DIR + "/suggestions.clp"
    if not os.path.isfile(FactsFile):
        file = open(FactsFile, 'w+')
        file.write("(deffacts suggestions)\n")
        file.close()

    # modify facts
    suggestions = Suggestion.objects.all()
    lines = ['(deffacts suggestions\n']
    for suggestion in suggestions:
        lines.append('  (suggestion '
                     '(enfermedad-name "'+suggestion.enfermedadName+'")'
                     '(enfermedad-id '+str(suggestion.enfermedadId)+')'
                     '(attribute "'+suggestion.attribute+'")'
                     '(value "'+suggestion.value+'")'
                     '(quantity '+str(suggestion.quantity)+'))\n')

    lines.append(')\n')

    # new facts
    open(FactsFile, 'w').writelines(lines)


def insertReviewIntoDatabase(data):
    review = Review(reviewer=data['reviewer'],
                comment=data['comment'],
                stars=float(data['stars']),
                enfermedadName=data['enfermedadName'],
                enfermedadId=int(data['enfermedadId']),
                createdTime=datetime.datetime.now())
    print(review)
    review.save()
    return review.id


def insertReviewIntoClips(data, id):
    # check if a fact-file exists
    FactsFile = settings.CLIPS_DIR + "/reviews.clp"
    if not os.path.isfile(FactsFile):
        file = open(FactsFile, 'w+')
        file.write("(deffacts reviews)\n")
        file.close()

    # modify facts
    lines = open(FactsFile, 'r+').readlines()
    n = len(lines)
    lines[n - 1] = lines[n-1][:-2] + "\n"
    lines.append('  (review '
                '(ID '+str(id)+')'
                '(enfermedad-name "'+data['enfermedadName']+'")'
                '(enfermedad-id '+data['enfermedadId']+')'
                '(reviewer "'+data['reviewer']+'")'
                '(comment "'+data['comment']+'")'
                '(stars '+data['stars']+')))\n')

    # new facts
    open(FactsFile, 'w').writelines(lines)


# INICIO NUEVO BONJOUR-----------------------------------------------------------------

def insertEscrituraIntoClips():
    FactsFile = settings.CLIPS_DIR + "/dishes.clp"
    if not os.path.isfile(FactsFile):
        file = open(FactsFile, 'w+')
        file.write("(deffacts enfermedades)\n")
        file.close()

    # modify facts
    #dishes = Dish.objects.all()
    #nuevalinea
    suggestions = Enfermedad.objects.all()
    #finnuevalinea
    lines = ['(deffacts enfermedades\n']
    for suggestion in suggestions:
        lines.append('    (enfermedad '
                        '(ID '+str(suggestion.id)+')'
           #             '(dish-name "'+dish.hasSoup+'")'
                        '(name "'+str(suggestion.name)+'") '
                        '(planta "'+str(suggestion.planta)+'") '
                        '(sintoma-aa "'+str(suggestion.sintomaAA)+'") '
                        '(sintoma-bb "'+str(suggestion.sintomaBB)+'") '
                        '(sintoma-cc "'+str(suggestion.sintomaCC)+'") '
                        '(sintoma-dd "'+str(suggestion.sintomaDD)+'") '
                        '(sintoma-ee "'+str(suggestion.sintomaEE)+'") '
                        '(stars -1))\n')

    lines.append(')\n')

    # new facts
#    open(FactsFile, 'w').writelines(lines)  
    open(FactsFile, 'w').writelines(lines)   

# FIN NUEVO BONJOUR--------------------------------------------------------------------


#MIO hahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha
def insertMireviewIntoDatabase(data):
    review = Mireview(reviewer=data['reviewer'],
                comment=data['comment'],
                createdTime=datetime.datetime.now())
    print(review)
    review.save()
    return review.id      


def clipsMatchPreference(data):
    # Preference
    preference = '(preference ' +\
                 '(planta "'+data['planta']+'") ' +\
                 '(sintoma-aa "'+data['sintomaAA']+'") ' +\
                 '(sintoma-bb "'+data['sintomaBB']+'") ' +\
                 '(sintoma-cc "'+data['sintomaCC']+'") ' +\
                 '(sintoma-ee "'+data['sintomaEE']+'") ' +\
                 '(sintoma-dd "'+data['sintomaDD']+'"))'

    # CLIPS
    clips.Clear()
    clips.BatchStar(settings.CLIPS_DIR + "/templates.clp")
    if os.path.isfile(settings.CLIPS_DIR + "/dishes.clp"):
        clips.BatchStar(settings.CLIPS_DIR + "/dishes.clp")
    if os.path.isfile(settings.CLIPS_DIR + "/reviews.clp"):
        clips.BatchStar(settings.CLIPS_DIR + "/reviews.clp")
    if os.path.isfile(settings.CLIPS_DIR + "/suggestions.clp"):
        clips.BatchStar(settings.CLIPS_DIR + "/suggestions.clp")
    clips.BatchStar(settings.CLIPS_DIR + "/rules.clp")
    clips.Reset()
    clips.Assert(preference)
    clips.Run()
    return clips.StdoutStream.Read()


def clipsMatchPreferencemaes(data):
    # Preference
    preference = '(preference ' +\
                 '(planta "'+data['planta']+'") ' +\
                 '(sintoma-aa "'+data['sintomaAA']+'") ' +\
                 '(sintoma-bb "'+data['sintomaBB']+'") ' +\
                 '(sintoma-cc "'+data['sintomaCC']+'"))'                                  

    # CLIPS
    clips.Clear()
    clips.BatchStar(settings.CLIPS_DIR + "/templatesmaes.clp")
    if os.path.isfile(settings.CLIPS_DIR + "/dishesmaes.clp"):
        clips.BatchStar(settings.CLIPS_DIR + "/dishesmaes.clp")
    if os.path.isfile(settings.CLIPS_DIR + "/reviewsmaes.clp"):
        clips.BatchStar(settings.CLIPS_DIR + "/reviewsmaes.clp")
    if os.path.isfile(settings.CLIPS_DIR + "/suggestionsmaes.clp"):
        clips.BatchStar(settings.CLIPS_DIR + "/suggestionsmaes.clp")
    clips.BatchStar(settings.CLIPS_DIR + "/rulesmaes.clp")
    clips.Reset()
    clips.Assert(preference)
    clips.Run()
    return clips.StdoutStream.Read()


def clipsMatchPreferencemara(data):
    # Preference
    preference = '(preference ' +\
                 '(planta "'+data['planta']+'") ' +\
                 '(sintoma-aa "'+data['sintomaAA']+'") ' +\
                 '(sintoma-bb "'+data['sintomaBB']+'") ' +\
                 '(sintoma-cc "'+data['sintomaCC']+'") ' +\
                 '(sintoma-ee "'+data['sintomaEE']+'") ' +\
                 '(sintoma-dd "'+data['sintomaDD']+'"))'

    # CLIPS
    clips.Clear()
    clips.BatchStar(settings.CLIPS_DIR + "/templatesmara.clp")
    if os.path.isfile(settings.CLIPS_DIR + "/dishesmara.clp"):
        clips.BatchStar(settings.CLIPS_DIR + "/dishesmara.clp")
    if os.path.isfile(settings.CLIPS_DIR + "/reviewsmara.clp"):
        clips.BatchStar(settings.CLIPS_DIR + "/reviewsmara.clp")
    if os.path.isfile(settings.CLIPS_DIR + "/suggestionsmara.clp"):
        clips.BatchStar(settings.CLIPS_DIR + "/suggestionsmara.clp")
    clips.BatchStar(settings.CLIPS_DIR + "/rulesmara.clp")
    clips.Reset()
    clips.Assert(preference)
    clips.Run()
    return clips.StdoutStream.Read()

#MAES--------------------------------------------------------------

@login_required
def nuevomaesEnfermedadPage(request):
    return render(request, 'newmaes.html')


# Create New Dish, Assume Data is CORRECT!
@csrf_exempt
def crearmaesEnfermedad(request):
    id = insertarmaesNuevaEnfermedad(request.POST)
#    insertIntoClips(id, request.POST)
    return HttpResponse('')


# Utility Functions
def insertarmaesNuevaEnfermedad(data):
    images = ast.literal_eval(data['images'])
    imageNum = 0;
    for image in images:
        imageNum = imageNum + (image != 'null')

    enfermedadmaes = Enfermedadmaes(name=data['name'],
                description=data['description'],
                images=imageNum,
                planta=data['planta'],
                sintomaAA=data['sintomaAA'],
                sintomaBB=data['sintomaBB'],
                sintomaCC=data['sintomaCC'])
    enfermedadmaes.save()

    index = 0
    for image in images:
        if image != 'null':
            index = index + 1
            createmaesImage(enfermedadmaes.id, index, image)

    return enfermedadmaes.id


def createmaesImage(id, index, image):
    imgCore = image.split(',')[1]
    imgFile = open(settings.DISHMAES_IMAGE_DIR + "/" + str(id) + "_" + str(index) + ".jpeg", "wb")
    imgFile.write(imgCore.decode('base64'))
    imgFile.close()

    # Create square image
    img = Image.open(settings.DISHMAES_IMAGE_DIR + "/" + str(id) + "_" + str(index) + ".jpeg")
    longer_side = max(img.size)
    thumb = Image.new('RGBA', (longer_side, longer_side), (255, 255, 255, 0))
    thumb.paste(
        img, ((longer_side - img.size[0]) / 2, (longer_side - img.size[1]) / 2)
    )
    thumb.save(settings.DISHMAES_IMAGE_DIR + "/" + str(id) + "_" + str(index) + "_square.jpeg")


@csrf_exempt
def escrituramaesPage(request):
    enfermedadmaesmaiz = Enfermedadmaes.objects.latest('id')
    return render(request, 'escrituramaes.html', {'enfermedadmaesmaiz':enfermedadmaesmaiz})       


@csrf_exempt
def escrituramaes(request):
  #  insertEscrituraIntoDatabase(request.POST)
  if request.method == "POST":
    insertEscrituramaesIntoClips()
    return render(request, 'escrituramaes.html')


# INICIO NUEVO BONJOUR---------

def insertEscrituramaesIntoClips():
    FactsFile = settings.CLIPS_DIR + "/dishesmaes.clp"
    if not os.path.isfile(FactsFile):
        file = open(FactsFile, 'w+')
        file.write("(deffacts enfermedades)\n")
        file.close()

    # modify facts
    #dishes = Dish.objects.all()
    #nuevalinea
    suggestions = Enfermedadmaes.objects.all()
    #finnuevalinea
    lines = ['(deffacts enfermedades\n']
    for suggestion in suggestions:
        lines.append('    (enfermedad '
                        '(ID '+str(suggestion.id)+')'
           #             '(dish-name "'+dish.hasSoup+'")'
                        '(name "'+str(suggestion.name)+'") '
                        '(planta "'+str(suggestion.planta)+'") '
                        '(sintoma-aa "'+str(suggestion.sintomaAA)+'") '
                        '(sintoma-bb "'+str(suggestion.sintomaBB)+'") '
                        '(sintoma-cc "'+str(suggestion.sintomaCC)+'") '
           #             '(sintoma-dd "'+str(suggestion.sintomaDD)+'") '
           #             '(sintoma-ee "'+str(suggestion.sintomaEE)+'") '
                        '(stars -1))\n')

    lines.append(')\n')

    # new facts
#    open(FactsFile, 'w').writelines(lines)  
    open(FactsFile, 'w').writelines(lines)   

# FIN NUEVO BONJOUR----------

@login_required
def reportemaesmaizPage(request):
    enfermedadmaesmaiz = Enfermedadmaes.objects.all()
    return render(request, 'reportemaesmaiz.html', {'enfermedadmaesmaiz':enfermedadmaesmaiz})


#inicio codigofacilitoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

def enfermedadmaesmaiz_view(request):
    if request.method == 'POST':
        form = EnfermedadmaesmaizForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('enfermedadmaesmaiz:index')
    else:
        form = EnfermedadmaesmaizForm()
    return render(request, 'enfermedadmaesmaiz_form.html', {'form':form})  


def enfermedadmaesmaiz_edit(request,id_enfermedadmaesmaiz):
    enfermedadmaesmaiz = Enfermedadmaes.objects.get(id=id_enfermedadmaesmaiz)     
    if request.method == 'GET':
        form = EnfermedadmaesmaizForm(instance=enfermedadmaesmaiz)
    else:
        form = EnfermedadmaesmaizForm(request.POST, instance=enfermedadmaesmaiz)
        if form.is_valid():
            form.save()
        return redirect('accionesmaesPage')
    return render(request, 'enfermedadmaesmaiz_form.html', {'form':form}) 


def enfermedadmaesmaiz_delete(request, id_enfermedadmaesmaiz):
    enfermedadmaesmaiz = Enfermedadmaes.objects.get(id=id_enfermedadmaesmaiz)
    if request.method == 'POST':
        enfermedadmaesmaiz.delete()
        return redirect('accionesmaesPage')
    return render(request,'enfermedadmaesmaiz_delete.html', {'enfermedadmaesmaiz':enfermedadmaesmaiz}) 

#fin codigofacilitoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo        

# New Review, Assume Data is CORRECT
@csrf_exempt
def processReviewsmaes(request):
    if request.method == "POST":
        id = insertReviewmaesIntoDatabase(request.POST)
        insertReviewmaesIntoClips(request.POST, id)
        return HttpResponse('')
    else:
        response = []
        reviews = Reviewmaes.objects.filter(enfermedadId=int(request.GET['enfermedadId'])).order_by("-id")
        for review in reviews:
            response.append({"id": review.id, "comment": review.comment, "reviewer": review.reviewer,
                    "createdTime": review.createdTime})
        return JsonResponse(response, safe=False)


def insertReviewmaesIntoDatabase(data):
    review = Reviewmaes(reviewer=data['reviewer'],
                comment=data['comment'],
                stars=float(data['stars']),
                enfermedadName=data['enfermedadName'],
                enfermedadId=int(data['enfermedadId']),
                createdTime=datetime.datetime.now())
    print(review)
    review.save()
    return review.id


def insertReviewmaesIntoClips(data, id):
    # check if a fact-file exists
    FactsFile = settings.CLIPS_DIR + "/reviewsmaes.clp"
    if not os.path.isfile(FactsFile):
        file = open(FactsFile, 'w+')
        file.write("(deffacts reviews)\n")
        file.close()

    # modify facts
    lines = open(FactsFile, 'r+').readlines()
    n = len(lines)
    lines[n - 1] = lines[n-1][:-2] + "\n"
    lines.append('  (review '
                '(ID '+str(id)+')'
                '(enfermedad-name "'+data['enfermedadName']+'")'
                '(enfermedad-id '+data['enfermedadId']+')'
                '(reviewer "'+data['reviewer']+'")'
                '(comment "'+data['comment']+'")'
                '(stars '+data['stars']+')))\n')

    # new facts
    open(FactsFile, 'w').writelines(lines)


@login_required
def reportecalificacionmaizmaesPage(request):
    reviewmaiz = Reviewmaes.objects.order_by('-stars')
    return render(request, 'reportecalificacionmaizmaes.html', {'reviewmaiz':reviewmaiz})

#MARA-----------------------------------------------------------------


@login_required
def nuevomaraEnfermedadPage(request):
    return render(request, 'newmara.html')


# Create New Dish, Assume Data is CORRECT!
@csrf_exempt
def crearmaraEnfermedad(request):
    id = insertarmaraNuevaEnfermedad(request.POST)
#    insertIntoClips(id, request.POST)
    return HttpResponse('')


# Utility Functions
def insertarmaraNuevaEnfermedad(data):
    images = ast.literal_eval(data['images'])
    imageNum = 0;
    for image in images:
        imageNum = imageNum + (image != 'null')

    enfermedadmara = Enfermedadmara(name=data['name'],
                description=data['description'],
                images=imageNum,
                planta=data['planta'],
                sintomaAA=data['sintomaAA'],
                sintomaBB=data['sintomaBB'],
                sintomaCC=data['sintomaCC'],
                sintomaEE=data['sintomaEE'],
                sintomaDD=data['sintomaDD'])
    enfermedadmara.save()

    index = 0
    for image in images:
        if image != 'null':
            index = index + 1
            createmaraImage(enfermedadmara.id, index, image)

    return enfermedadmara.id


def createmaraImage(id, index, image):
    imgCore = image.split(',')[1]
    imgFile = open(settings.DISHMARA_IMAGE_DIR + "/" + str(id) + "_" + str(index) + ".jpeg", "wb")
    imgFile.write(imgCore.decode('base64'))
    imgFile.close()

    # Create square image
    img = Image.open(settings.DISHMARA_IMAGE_DIR + "/" + str(id) + "_" + str(index) + ".jpeg")
    longer_side = max(img.size)
    thumb = Image.new('RGBA', (longer_side, longer_side), (255, 255, 255, 0))
    thumb.paste(
        img, ((longer_side - img.size[0]) / 2, (longer_side - img.size[1]) / 2)
    )
    thumb.save(settings.DISHMARA_IMAGE_DIR + "/" + str(id) + "_" + str(index) + "_square.jpeg")


@csrf_exempt
def escrituramaraPage(request):
    enfermedadmaramaiz = Enfermedadmara.objects.latest('id')
    return render(request, 'escrituramara.html', {'enfermedadmaramaiz':enfermedadmaramaiz})       


@csrf_exempt
def escrituramara(request):
  #  insertEscrituraIntoDatabase(request.POST)
  if request.method == "POST":
    insertEscrituramaraIntoClips()
    return render(request, 'escrituramara.html')


# INICIO NUEVO BONJOUR---------

def insertEscrituramaraIntoClips():
    FactsFile = settings.CLIPS_DIR + "/dishesmara.clp"
    if not os.path.isfile(FactsFile):
        file = open(FactsFile, 'w+')
        file.write("(deffacts enfermedades)\n")
        file.close()

    # modify facts
    #dishes = Dish.objects.all()
    #nuevalinea
    suggestions = Enfermedadmara.objects.all()
    #finnuevalinea
    lines = ['(deffacts enfermedades\n']
    for suggestion in suggestions:
        lines.append('    (enfermedad '
                        '(ID '+str(suggestion.id)+')'
           #             '(dish-name "'+dish.hasSoup+'")'
                        '(name "'+str(suggestion.name)+'") '
                        '(planta "'+str(suggestion.planta)+'") '
                        '(sintoma-aa "'+str(suggestion.sintomaAA)+'") '
                        '(sintoma-bb "'+str(suggestion.sintomaBB)+'") '
                        '(sintoma-cc "'+str(suggestion.sintomaCC)+'") '
                        '(sintoma-dd "'+str(suggestion.sintomaDD)+'") '
                        '(sintoma-ee "'+str(suggestion.sintomaEE)+'") '
                        '(stars -1))\n')

    lines.append(')\n')

    # new facts
#    open(FactsFile, 'w').writelines(lines)  
    open(FactsFile, 'w').writelines(lines)   

# FIN NUEVO BONJOUR----------

@login_required
def reportemaramaizPage(request):
    enfermedadmaramaiz = Enfermedadmara.objects.all()
    return render(request, 'reportemaramaiz.html', {'enfermedadmaramaiz':enfermedadmaramaiz})


@login_required
def accionesmaesPage(request):
    enfermedadmaesmaiz = Enfermedadmaes.objects.all()
    return render(request, 'accionesmaes.html', {'enfermedadmaesmaiz':enfermedadmaesmaiz}) 


@login_required
def accionesmaraPage(request):
    enfermedadmaramaiz = Enfermedadmara.objects.all()
    return render(request, 'accionesmara.html', {'enfermedadmaramaiz':enfermedadmaramaiz}) 


#inicio codigofacilitoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

def enfermedadmaramaiz_view(request):
    if request.method == 'POST':
        form = EnfermedadmaramaizForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('enfermedadmaramaiz:index')
    else:
        form = EnfermedadmaramaizForm()
    return render(request, 'enfermedadmaramaiz_form.html', {'form':form})  


def enfermedadmaramaiz_edit(request,id_enfermedadmaramaiz):
    enfermedadmaramaiz = Enfermedadmara.objects.get(id=id_enfermedadmaramaiz)     
    if request.method == 'GET':
        form = EnfermedadmaramaizForm(instance=enfermedadmaramaiz)
    else:
        form = EnfermedadmaramaizForm(request.POST, instance=enfermedadmaramaiz)
        if form.is_valid():
            form.save()
        return redirect('accionesmaraPage')
    return render(request, 'enfermedadmaramaiz_form.html', {'form':form}) 


def enfermedadmaramaiz_delete(request, id_enfermedadmaramaiz):
    enfermedadmaramaiz = Enfermedadmara.objects.get(id=id_enfermedadmaramaiz)
    if request.method == 'POST':
        enfermedadmaramaiz.delete()
        return redirect('accionesmaraPage')
    return render(request,'enfermedadmaramaiz_delete.html', {'enfermedadmaramaiz':enfermedadmaramaiz}) 

#fin codigofacilitoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo


# New Review, Assume Data is CORRECT
@csrf_exempt
def processReviewsmara(request):
    if request.method == "POST":
        id = insertReviewmaraIntoDatabase(request.POST)
        insertReviewmaraIntoClips(request.POST, id)
        return HttpResponse('')
    else:
        response = []
        reviews = Reviewmara.objects.filter(enfermedadId=int(request.GET['enfermedadId'])).order_by("-id")
        for review in reviews:
            response.append({"id": review.id, "comment": review.comment, "reviewer": review.reviewer,
                    "createdTime": review.createdTime})
        return JsonResponse(response, safe=False)


def insertReviewmaraIntoDatabase(data):
    review = Reviewmara(reviewer=data['reviewer'],
                comment=data['comment'],
                stars=float(data['stars']),
                enfermedadName=data['enfermedadName'],
                enfermedadId=int(data['enfermedadId']),
                createdTime=datetime.datetime.now())
    print(review)
    review.save()
    return review.id


def insertReviewmaraIntoClips(data, id):
    # check if a fact-file exists
    FactsFile = settings.CLIPS_DIR + "/reviewsmara.clp"
    if not os.path.isfile(FactsFile):
        file = open(FactsFile, 'w+')
        file.write("(deffacts reviews)\n")
        file.close()

    # modify facts
    lines = open(FactsFile, 'r+').readlines()
    n = len(lines)
    lines[n - 1] = lines[n-1][:-2] + "\n"
    lines.append('  (review '
                '(ID '+str(id)+')'
                '(enfermedad-name "'+data['enfermedadName']+'")'
                '(enfermedad-id '+data['enfermedadId']+')'
                '(reviewer "'+data['reviewer']+'")'
                '(comment "'+data['comment']+'")'
                '(stars '+data['stars']+')))\n')

    # new facts
    open(FactsFile, 'w').writelines(lines)     


@login_required
def reportecalificacionmaizmaraPage(request):
    reviewmaiz = Reviewmara.objects.order_by('-stars')
    return render(request, 'reportecalificacionmaizmara.html', {'reviewmaiz':reviewmaiz})