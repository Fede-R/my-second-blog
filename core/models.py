from django.db import models

# Create your models here.
class Enfermedad(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    images = models.IntegerField()
    planta = models.CharField(max_length=50)
    sintomaAA = models.CharField(max_length=50)
    sintomaBB = models.CharField(max_length=50)
    sintomaCC = models.CharField(max_length=50)
    sintomaDD = models.CharField(max_length=50)
    sintomaEE = models.CharField(max_length=50)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'name: ' + self.name + '\n' +\
            'description: ' + self.description + '\n' +\
            'images: ' + str(self.images) + '\n' +\
            'planta: ' + self.planta + '\n' +\
            'sintomaAA: ' + self.sintomaAA + '\n' +\
            'sintomaBB: ' + self.sintomaBB + '\n' +\
            'sintomaCC: ' + self.sintomaCC + '\n' +\
            'sintomaDD: ' + self.sintomaDD + '\n' +\
            'sintomaEE: ' + self.sintomaEE + '\n' 

class Review(models.Model):
    enfermedadName = models.CharField(max_length=50)
    enfermedadId = models.IntegerField()
    comment = models.TextField()
    reviewer = models.CharField(max_length=50)
    stars = models.IntegerField()
    createdTime =  models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'enfermedad-name: ' + self.enfermedadName + '\n' +\
            'enfermedad-id: ' + str(self.enfermedadId) + '\n' +\
            'reviewer: ' + self.reviewer + '\n' +\
            'comment: ' + self.comment + '\n' +\
            'stars: ' + str(self.stars) + '\n' +\
            'createdTime: ' + str(self.createdTime) + '\n'


class Suggestion(models.Model):
    enfermedadName = models.CharField(max_length=50)
    enfermedadId = models.IntegerField()
    attribute = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'enfermedad-name: ' + self.enfermedadName + '\n' +\
            'enfermedad-id: ' + str(self.enfermedadId) + '\n' +\
            'attribute: ' + self.attribute + '\n' +\
            'value: ' + self.value + '\n' +\
            'quantity: ' + str(self.quantity) + '\n'

#Este es mi nuevo modelo de prueba
class Mireview(models.Model):
    comment = models.TextField()
    reviewer = models.CharField(max_length=50)
    createdTime =  models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'reviewer: ' + self.reviewer + '\n' +\
            'comment: ' + self.comment + '\n' +\
            'createdTime: ' + str(self.createdTime) + '\n'


class Enfermedadmaes(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    images = models.IntegerField()
    planta = models.CharField(max_length=50)
    sintomaAA = models.CharField(max_length=50)
    sintomaBB = models.CharField(max_length=50)
    sintomaCC = models.CharField(max_length=50)
    
    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'name: ' + self.name + '\n' +\
            'description: ' + self.description + '\n' +\
            'images: ' + str(self.images) + '\n' +\
            'planta: ' + self.planta + '\n' +\
            'sintomaAA: ' + self.sintomaAA + '\n' +\
            'sintomaBB: ' + self.sintomaBB + '\n' +\
            'sintomaCC: ' + self.sintomaCC + '\n'  


class Enfermedadmara(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    images = models.IntegerField()
    planta = models.CharField(max_length=50)
    sintomaAA = models.CharField(max_length=50)
    sintomaBB = models.CharField(max_length=50)
    sintomaCC = models.CharField(max_length=50)
    sintomaDD = models.CharField(max_length=50)
    sintomaEE = models.CharField(max_length=50)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'name: ' + self.name + '\n' +\
            'description: ' + self.description + '\n' +\
            'images: ' + str(self.images) + '\n' +\
            'planta: ' + self.planta + '\n' +\
            'sintomaAA: ' + self.sintomaAA + '\n' +\
            'sintomaBB: ' + self.sintomaBB + '\n' +\
            'sintomaCC: ' + self.sintomaCC + '\n' +\
            'sintomaDD: ' + self.sintomaDD + '\n' +\
            'sintomaEE: ' + self.sintomaEE + '\n' 


class Enfermedadsoho(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    images = models.IntegerField()
    planta = models.CharField(max_length=50)
    sintomaAA = models.CharField(max_length=50)
    sintomaBB = models.CharField(max_length=50)
    sintomaCC = models.CharField(max_length=50)
    sintomaDD = models.CharField(max_length=50)
    sintomaEE = models.CharField(max_length=50)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'name: ' + self.name + '\n' +\
            'description: ' + self.description + '\n' +\
            'images: ' + str(self.images) + '\n' +\
            'planta: ' + self.planta + '\n' +\
            'sintomaAA: ' + self.sintomaAA + '\n' +\
            'sintomaBB: ' + self.sintomaBB + '\n' +\
            'sintomaCC: ' + self.sintomaCC + '\n' +\
            'sintomaDD: ' + self.sintomaDD + '\n' +\
            'sintomaEE: ' + self.sintomaEE + '\n' 


class Enfermedadsota(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    images = models.IntegerField()
    planta = models.CharField(max_length=50)
    sintomaAA = models.CharField(max_length=50)
    sintomaBB = models.CharField(max_length=50)
    sintomaCC = models.CharField(max_length=50)
    sintomaDD = models.CharField(max_length=50)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'name: ' + self.name + '\n' +\
            'description: ' + self.description + '\n' +\
            'images: ' + str(self.images) + '\n' +\
            'planta: ' + self.planta + '\n' +\
            'sintomaAA: ' + self.sintomaAA + '\n' +\
            'sintomaBB: ' + self.sintomaBB + '\n' +\
            'sintomaCC: ' + self.sintomaCC + '\n' +\
            'sintomaDD: ' + self.sintomaDD + '\n' 


class Enfermedadsora(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    images = models.IntegerField()
    planta = models.CharField(max_length=50)
    sintomaAA = models.CharField(max_length=50)
    sintomaBB = models.CharField(max_length=50)
    sintomaCC = models.CharField(max_length=50)
    sintomaDD = models.CharField(max_length=50)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'name: ' + self.name + '\n' +\
            'description: ' + self.description + '\n' +\
            'images: ' + str(self.images) + '\n' +\
            'planta: ' + self.planta + '\n' +\
            'sintomaAA: ' + self.sintomaAA + '\n' +\
            'sintomaBB: ' + self.sintomaBB + '\n' +\
            'sintomaCC: ' + self.sintomaCC + '\n' +\
            'sintomaDD: ' + self.sintomaDD + '\n' 


class Enfermedadtriho(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    images = models.IntegerField()
    planta = models.CharField(max_length=50)
    sintomaAA = models.CharField(max_length=50)
    sintomaBB = models.CharField(max_length=50)
    sintomaCC = models.CharField(max_length=50)
    
    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'name: ' + self.name + '\n' +\
            'description: ' + self.description + '\n' +\
            'images: ' + str(self.images) + '\n' +\
            'planta: ' + self.planta + '\n' +\
            'sintomaAA: ' + self.sintomaAA + '\n' +\
            'sintomaBB: ' + self.sintomaBB + '\n' +\
            'sintomaCC: ' + self.sintomaCC + '\n'  


class Reviewmaes(models.Model):
    enfermedadName = models.CharField(max_length=50)
    enfermedadId = models.IntegerField()
    comment = models.TextField()
    reviewer = models.CharField(max_length=50)
    stars = models.IntegerField()
    createdTime =  models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'enfermedad-name: ' + self.enfermedadName + '\n' +\
            'enfermedad-id: ' + str(self.enfermedadId) + '\n' +\
            'reviewer: ' + self.reviewer + '\n' +\
            'comment: ' + self.comment + '\n' +\
            'stars: ' + str(self.stars) + '\n' +\
            'createdTime: ' + str(self.createdTime) + '\n'


class Reviewmara(models.Model):
    enfermedadName = models.CharField(max_length=50)
    enfermedadId = models.IntegerField()
    comment = models.TextField()
    reviewer = models.CharField(max_length=50)
    stars = models.IntegerField()
    createdTime =  models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'enfermedad-name: ' + self.enfermedadName + '\n' +\
            'enfermedad-id: ' + str(self.enfermedadId) + '\n' +\
            'reviewer: ' + self.reviewer + '\n' +\
            'comment: ' + self.comment + '\n' +\
            'stars: ' + str(self.stars) + '\n' +\
            'createdTime: ' + str(self.createdTime) + '\n'


class Reviewsoho(models.Model):
    enfermedadName = models.CharField(max_length=50)
    enfermedadId = models.IntegerField()
    comment = models.TextField()
    reviewer = models.CharField(max_length=50)
    stars = models.IntegerField()
    createdTime =  models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'enfermedad-name: ' + self.enfermedadName + '\n' +\
            'enfermedad-id: ' + str(self.enfermedadId) + '\n' +\
            'reviewer: ' + self.reviewer + '\n' +\
            'comment: ' + self.comment + '\n' +\
            'stars: ' + str(self.stars) + '\n' +\
            'createdTime: ' + str(self.createdTime) + '\n'


class Reviewsota(models.Model):
    enfermedadName = models.CharField(max_length=50)
    enfermedadId = models.IntegerField()
    comment = models.TextField()
    reviewer = models.CharField(max_length=50)
    stars = models.IntegerField()
    createdTime =  models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'enfermedad-name: ' + self.enfermedadName + '\n' +\
            'enfermedad-id: ' + str(self.enfermedadId) + '\n' +\
            'reviewer: ' + self.reviewer + '\n' +\
            'comment: ' + self.comment + '\n' +\
            'stars: ' + str(self.stars) + '\n' +\
            'createdTime: ' + str(self.createdTime) + '\n'


class Reviewsora(models.Model):
    enfermedadName = models.CharField(max_length=50)
    enfermedadId = models.IntegerField()
    comment = models.TextField()
    reviewer = models.CharField(max_length=50)
    stars = models.IntegerField()
    createdTime =  models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'enfermedad-name: ' + self.enfermedadName + '\n' +\
            'enfermedad-id: ' + str(self.enfermedadId) + '\n' +\
            'reviewer: ' + self.reviewer + '\n' +\
            'comment: ' + self.comment + '\n' +\
            'stars: ' + str(self.stars) + '\n' +\
            'createdTime: ' + str(self.createdTime) + '\n'


class Reviewtriho(models.Model):
    enfermedadName = models.CharField(max_length=50)
    enfermedadId = models.IntegerField()
    comment = models.TextField()
    reviewer = models.CharField(max_length=50)
    stars = models.IntegerField()
    createdTime =  models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'enfermedad-name: ' + self.enfermedadName + '\n' +\
            'enfermedad-id: ' + str(self.enfermedadId) + '\n' +\
            'reviewer: ' + self.reviewer + '\n' +\
            'comment: ' + self.comment + '\n' +\
            'stars: ' + str(self.stars) + '\n' +\
            'createdTime: ' + str(self.createdTime) + '\n'


class Enfermedadtripla(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    images = models.IntegerField()
    planta = models.CharField(max_length=50)
    sintomaAA = models.CharField(max_length=50)
    sintomaBB = models.CharField(max_length=50)
    sintomaCC = models.CharField(max_length=50)
    sintomaDD = models.CharField(max_length=50)
    sintomaEE = models.CharField(max_length=50)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'name: ' + self.name + '\n' +\
            'description: ' + self.description + '\n' +\
            'images: ' + str(self.images) + '\n' +\
            'planta: ' + self.planta + '\n' +\
            'sintomaAA: ' + self.sintomaAA + '\n' +\
            'sintomaBB: ' + self.sintomaBB + '\n' +\
            'sintomaCC: ' + self.sintomaCC + '\n' +\
            'sintomaDD: ' + self.sintomaDD + '\n' +\
            'sintomaEE: ' + self.sintomaEE + '\n' 


class Reviewtripla(models.Model):
    enfermedadName = models.CharField(max_length=50)
    enfermedadId = models.IntegerField()
    comment = models.TextField()
    reviewer = models.CharField(max_length=50)
    stars = models.IntegerField()
    createdTime =  models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'ID: '+ str(self.id) + '\n' +\
            'enfermedad-name: ' + self.enfermedadName + '\n' +\
            'enfermedad-id: ' + str(self.enfermedadId) + '\n' +\
            'reviewer: ' + self.reviewer + '\n' +\
            'comment: ' + self.comment + '\n' +\
            'stars: ' + str(self.stars) + '\n' +\
            'createdTime: ' + str(self.createdTime) + '\n'