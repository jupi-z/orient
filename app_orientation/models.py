from django.db import models
from django.contrib.postgres.fields import IntegerRangeField


class Test(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    # Autres champs spécifiques à votre modèle Test
    # ...


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


PERSONALITY_TYPES = [
    ('type1', 'Type 1'),
    ('type2', 'Type 2'),
    # Ajoute d'autres choix ici si nécessaire
]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    interests = models.TextField()
    personality = models.CharField(choices=PERSONALITY_TYPES, max_length=20)
    # Autres champs de ton modèle UserProfile
    # ...


class Curriculum(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()


class School(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    curriculums = models.ManyToManyField(Curriculum)


class Career(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    entry_requirements = models.TextField()
    curriculums = models.ManyToManyField(Curriculum)
    employment_rate = models.FloatField()
    salary_range = IntegerRangeField()


class Alumni(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    experience = models.TextField()


class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    major = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Answer(models.Model):
    questionnaire = models.ForeignKey('Questionnaire', on_delete=models.CASCADE)
    content = models.TextField()
    is_correct = models.BooleanField()


class UserTestScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.FloatField()


class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')


class Resource(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    document = models.ForeignKey(Document, null=True, on_delete=models.SET_NULL)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()


class Filiere(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom


class Note(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    valeur = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.etudiant} - {self.filiere} : {self.valeur}"


class Questionnaire(models.Model):
    # Définissez les champs de votre modèle ici
    nom = models.CharField(max_length=100)
    age = models.IntegerField()
    genre = models.CharField(max_length=100)
    satisfaction = models.IntegerField()
