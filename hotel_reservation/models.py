import datetime

from django.db import models
from django.db.models import Count

def attachment_path(instance, filename):
    return "Pokoj/" + str(instance.pokoj.id_pokoje_cislo) + "/attachments/" + filename


class Vybaveni(models.Model):

    STANDARD = (
        ('standard', 'standard'),
        ('nadstandard', 'nadstandard'),
    )

    # Pole s definovanými předvolbami pro uložení typu přílohy
    standard = models.CharField(max_length=20, choices=STANDARD, blank=True, default='standard',
                                help_text='Zvolte standard, nadstandard', verbose_name="Standard")

    dvojluzka = models.IntegerField(blank=True, null=True, help_text="Zadejte počet jednolůžek na pokoji",
                                             verbose_name="Jednolůžka")

    jednoluzka = models.IntegerField(blank=True, null=True, help_text="Zadejte počet dvojlůžek na pokoji",
                                             verbose_name="Dvojlůžka")

    BALKON = (
        ('ano', 'ano'),
        ('ne', 'ne'),
    )

    # Pole s definovanými předvolbami pro uložení typu přílohy
    balkon = models.CharField(max_length=5, choices=BALKON, blank=True, default='ne',
                                help_text='Zvolte zda pokoj obsahuje balkon', verbose_name="Balkón")
    def __str__(self):
        return f"Vybaveni č. {self.pk}"

class Cenik(models.Model):
    cena_dospeli = models.FloatField(blank=False, null=False, help_text=" Zadejte cenu za dospělého",
                                     verbose_name="Cena za dospělého")

    cena_student = models.FloatField(blank=False, null=False, help_text=" Zadejte cenu za studenta",
                                     verbose_name="Cena za studenta")

    cena_dite = models.FloatField(blank=False, null=False, help_text=" Zadejte cenu za dítě",
                                     verbose_name="Cena za dítě")

    cena_duchodce = models.FloatField(blank=False, null=False, help_text=" Zadejte cenu za důchodce",
                                     verbose_name="Cena za důchodce")
    def __str__(self):
        return f"cenik č. {self.pk}"
class Pokoj(models.Model):
    poschodi = models.IntegerField(blank=True, null=False, help_text="Zadejte poschodí",
                                   verbose_name="Poschodí")

    foto = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, verbose_name="Fotografie")
    cenik_pokoje = models.ForeignKey(Cenik, on_delete=models.CASCADE, default="2")
    vybaveni_pokoje = models.ForeignKey(Vybaveni, help_text="Přiřaďte vybaveni", default="2", on_delete=models.CASCADE)

    def __str__(self):
        return f"Pokoj č. {self.pk}"

class Kontakt(models.Model):
    osobni_telefon = models.IntegerField(unique=True, blank=False, null=True, help_text="Zadejte osobni telefon",
                             verbose_name="Osobni telefon")
    sluzebni_telefon = models.IntegerField(unique=True, blank=False, null=True, help_text="Zadejte služební telefon",
                             verbose_name="Služební telefon")
    email = models.CharField(unique=True, max_length=30, blank=False, null=False, help_text="Zadejte email",
                                 verbose_name="Email")
    def __str__(self):
        return f"Kontakt č. {self.pk}"

class Mesto(models.Model):
    PSC = models.IntegerField(unique=True, blank=False, null=False, help_text="Zadejte PSČ",
                             verbose_name="poštovní směrovací číslo")
    mesto = models.CharField(max_length=150, blank=False, null=False, help_text="Zadejte název Města",
                             verbose_name="Město")
    def __str__(self):
        return f"Mesto č. {self.pk}"
class Osoba(models.Model):
    cislo_obcanskeho_prukazu = models.IntegerField(primary_key=True,blank=True, null=False, help_text="Zadejte číslo ob. průkazu",
                                   verbose_name="Číslo průkazu")

    jmeno = models.CharField(max_length=200, blank=False, null=False, help_text="Zadejte jméno",
                             verbose_name="Jméno")
    prijmeni = models.CharField(max_length=200, blank=False, null=False, help_text="Zadejte příjmení",
                             verbose_name="Příjmeni")
    adresa = models.CharField(max_length=200, blank=False, null=False, help_text="Zadejte adresu",
                             verbose_name="Adresa")

    osoba_kontakt = models.ManyToManyField(Kontakt, help_text="Přiřaďte kontakt", verbose_name="Kontakt")

    osoba_bydliste = models.ManyToManyField(Mesto, help_text="Přiřaďte město", verbose_name="město")
    def __str__(self):
        return f"Osoba č. {self.pk}"

class Ubytovani(models.Model):
    ubytovani_duchodce = models.IntegerField(blank=True, null=True, help_text="Zadejte počet ubytovaných důchodců",
                                             verbose_name="Důchodci")
    ubytovani_student = models.IntegerField(blank=True, null=True, help_text="Zadejte počet ubytovaných studentů",
                                             verbose_name="Studenti")
    ubytovani_dospeli = models.IntegerField(blank=True, null=True, help_text="Zadejte počet ubytovaných dospělých",
                                             verbose_name="Dospělí")
    ubytovani_deti = models.IntegerField(blank=True, null=True, help_text="Zadejte počet ubytovaných dětí",
                                             verbose_name="Děti")
    def __str__(self):
        return f"Ubytovani č. {self.pk}"
class Rezervace(models.Model):

    current_datetime = datetime.datetime.now()

    datum_prijezdu = models.DateField(blank=True, null=False, help_text="Prosím použijte tenhle formát: <em>YYYY-MM-DD</em>.",
                                      verbose_name="Datum příjezdu")

    pocet_noci = models.IntegerField(blank=True, null=False, help_text="Prosím zadejte počet nocí v celém čísle",
                                     verbose_name="Počet nocí")

    cas_vyhotoveni = models.DateTimeField(blank=True, null=True, help_text="Prosím zadejte čas vyhodnocení", default = current_datetime,
                                     verbose_name="Čas vyhotovení")

    osoba_cislo_obcanskeho_prukazu = models.ManyToManyField(Osoba, help_text="Zadejte cislo prukazu")

    pokoj = models.ManyToManyField(Pokoj, help_text="Zadejte číslo pokoje", verbose_name="přiřaďte pokoj")

    ubytovani= models.ForeignKey(Ubytovani, on_delete=models.CASCADE)
    def __str__(self):
        return f"Rezervace č. {self.pk}"










