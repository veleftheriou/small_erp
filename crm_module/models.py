from django.db import models

# Create your models here.

LEAD = 'LEAD'
PROSPECT = 'PROS'
CLIENT = 'CLIE'
STATUT_CLIENT_CHOICES = (
    (LEAD, 'Lead'),
    (PROSPECT, 'Prospect'),
    (CLIENT, 'Client')
)


CONTACT_PYHSIQUE = 'PHYS'
APPEL = 'APPE'
EMAIL = 'MAIL'
DERNIERE_INTERRACTION_CHOICES = (
    (CONTACT_PYHSIQUE, 'Contact Physique'),
    (APPEL, 'Appel Téléphonique'),
    (EMAIL, 'Email')
)


FOURNISSEUR = 'FOUR'
PARTICULIER = 'PART'
TYPE_PROFESSIONNEL_CHOICES = (
    (FOURNISSEUR, 'Fournisseur'),
    (CLIENT, 'Client'),
    (PARTICULIER, 'Particulier')
)

class Contact(models.Model):
    nom = models.CharField(max_length=120)
    adresse = models.CharField(max_length=250)
    code_postal = models.CharField(max_length=10)
    localite = models.CharField(max_length=100)
    pays = models.CharField(max_length=40)
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    num_tva = models.CharField(max_length=20, blank=True)
    type_client = models.CharField(
        max_length=4,
        choices=TYPE_PROFESSIONNEL_CHOICES,
        default=CLIENT
    )
    statut_client = models.CharField(
        max_length=4,
        choices=STATUT_CLIENT_CHOICES,
        default=PROSPECT
    )
    interraction = models.CharField(
        max_length=4,
        choices=DERNIERE_INTERRACTION_CHOICES,
        default=EMAIL
    )