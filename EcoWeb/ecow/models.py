from django.contrib.auth.models import AbstractUser
from django.db import models



# Choices for User
AMBASSADEUR = 'EC'
HONNEUR = 'HO'

TITLE_CHOICES = [
    (AMBASSADEUR, 'Eco-Ambassadeur'),
    (HONNEUR, "Eco-Ambassadeur d'Honneur"),
]

ELEVE = 'EL'
PROF = 'PR'
ASSISTANT_DE_LABORATOIRE = 'AS'
VIE_SCOLAIRE = "VS"
CPE = "CP"
AUTRE = "AU"

STATUS_CHOICES = [
    (ELEVE, 'élève'),
    (PROF, "professeur"),
    (ASSISTANT_DE_LABORATOIRE, "assistant de laboratoire"),
    (VIE_SCOLAIRE, "Vie scolaire"),
    (CPE, "C.P.E."),
    (AUTRE, "Autre"),
]


class User(AbstractUser):
    bio = models.TextField(max_length=1000, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    public = models.BooleanField(default=False)
    pdp = models.ImageField(null=True, blank=True, upload_to='images/')
    seniority = models.IntegerField(default=2020)
    title = models.CharField(
        max_length=2,
        choices=TITLE_CHOICES,
        default=AMBASSADEUR,
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=AUTRE,
    )

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    URL_image = models.URLField(default="https://www.westernheights.k12.ok.us/wp-content/uploads/2020/01/No-Photo-Available.jpg") # Credit : https://www.westernheights.k12.ok.us/resources/special-services/no-photo-available/
    date = models.DateTimeField(auto_now=True)

    GENERAL = 'GE'
    CHANGEMENT_CLIMATIQUE = 'CH'
    ENERGIE_RENOUVELABLES= 'EN'
    RECYCLAGE = 'RE'
    SANTE = 'SA'

    CATEGORIES_CHOICES = [
        (GENERAL, 'General'),
        (CHANGEMENT_CLIMATIQUE, 'Changement climatique'),
        (ENERGIE_RENOUVELABLES, 'Energies renouvelables'),
        (RECYCLAGE, 'Recyclage'),
        (SANTE, 'Sante'),
    ]

    categories = models.CharField(
        max_length=2,
        choices=CATEGORIES_CHOICES,
        default=GENERAL,
    )

class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    URL_image = models.URLField(default="https://www.westernheights.k12.ok.us/wp-content/uploads/2020/01/No-Photo-Available.jpg") # Credit : https://www.westernheights.k12.ok.us/resources/special-services/no-photo-available/
    URL_video = models.URLField(default="not_available")
    date = models.DateTimeField(auto_now=True)

    GENERAL = 'GE'
    DIY = 'DI'
    HOME = 'HO'
    TOYS = 'TO'
    DECO = 'DE'

    CATEGORIES_CHOICES = [
        (GENERAL, 'General'),
        (DIY, 'DIY'),
        (HOME, 'Home'),
        (TOYS, 'Jouets'),
        (DECO, 'Déco'),
    ]

    categories = models.CharField(
        max_length=2,
        choices=CATEGORIES_CHOICES,
        default=GENERAL,
    )

class Comment_Article(models.Model):
    comment = models.CharField(max_length=1500)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class Comment_Idea(models.Model):
    comment = models.CharField(max_length=1500)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
