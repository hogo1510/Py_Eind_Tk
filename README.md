# Py_Eind_Tk

### Use-Case Diagram
![image](https://github.com/hogo1510/Py_Eind_Tk/assets/55227884/c8415a25-1ac3-45dd-88c7-168bc0b936f4)


### Beschrijving van Use-Case Diagram
Use Case 1: Login

    Doel: Gebruiker Kan zich aanmelden.
    Acteur: Acteur
    Beschrijving:
        De gebruiker start de applicatie.
        De gebruiker voert zijn inloggegevens in.
        App checkt of login klopt.
        Correct ? -> doorgestuurd naar het menu.
        Niet ? ->outmelding.

Use Case 2: Menu

    Doel: Toegang tot verschillende functies van app.
    Acteur: Acteur
    Beschrijving:
        Na correcte login wordt de gebruiker naar het hoofdmenu geleid.
        Gebruiker heeft keuze tussen verschillende opties: 'Dobbelsteen', 'Cirkul Berekening' en 'Exit'.
        Afhankelijk van keuze, wordt de functie gestart.

Use Case 3: Dobbelsteen

    Doel: Hiermee kan de gebruiker een dobbelsteen gooien.
    Acteur: Acteur
    Beschrijving:
        De gebruiker start 'Dobbelsteen' in het menu.
        De app toont een interface voor het gooien van een dobbelsteen.
        De gebruiker klikt op "gooi" zodat er een dobbelsteenworp wordt gedaan.
        App toont hierna een "random" getal.
        De gebruiker kan terugkeren naar het menu na het zien van het resultaat.

Use Case 4: Cirkul Berekening

    Doel: Hiermee kan de gebruiker een cirkelberekening uitvoeren.
    Acteur: Acteur
    Beschrijving:
        De gebruiker start 'Cirkul Berekening' in het menu.
        De app toont een interface voor het invoeren van cirkelgegevens.
        De gebruiker voert gegevens in.
        De app berekent de omtrek en oppervlakte van de cirkel en laat dit zien.
        De gebruiker kan terugkeren naar het menu na het zien van de resultaten.

Use Case 5: Exit

    Doel: Hiermee kan de gebruiker de applicatie afsluiten.
    Acteur: Acteur
    Beschrijving:
        De gebruiker start 'Exit' in het menu.
        De app sluit.
