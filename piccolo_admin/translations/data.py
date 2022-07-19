"""
See https://github.com/piccolo-orm/piccolo_admin/issues/173 for more info.

NOTE: Flake8's line length warning has been disabled for this file - see
.flake8, so we don't have to worry about wrapping long translations.

NOTE: To validate the translations (to see if any are missing)::

    # At the root of the project
    cd scripts
    python get_translations.py validate

NOTE: One of the fastest ways to get the translations in bulk is using Google
Spreadsheets. For example, this function translates a value from English to
Portuguese `=GOOGLETRANSLATE(A1,"en","pt")`. A CSV file can be downloaded, and
then converted to JSON using a tool like this
https://www.convertcsv.com/csv-to-json.htm.

"""

import typing as t

from piccolo_admin.translations.models import Translation

# For now there aren't any words which are different between dialects, so we
# only need one form of English.
ENGLISH = Translation(
    language_name="English",
    language_code="en",
    translations={
        "About": "About",
        "Add Row": "Add Row",
        "Apply": "Apply",
        "Ascending": "Ascending",
        "Back to home page": "Back to home page",
        "Back": "Back",
        "Change password": "Change password",
        "Clear filters": "Clear filters",
        "Close": "Close",
        "Create": "Create",
        "Current password": "Current password",
        "Dark Mode": "Dark Mode",
        "Days": "Days",
        "Delete": "Delete",
        "Descending": "Descending",
        "Edit": "Edit",
        "Export CSV": "Export CSV",
        "Filter": "Filter",
        "Form submitted": "Form submitted",
        "Forms": "Forms",
        "Go to page": "Go to page",
        "Hide Filters": "Hide Filters",
        "Hide referencing tables": "Hide referencing tables",
        "Home": "Home",
        "Hours": "Hours",
        "Light Mode": "Light Mode",
        "Loading": "Loading",
        "Log out": "Log out",
        "Minutes": "Minutes",
        "New password confirmation": "New password confirmation",
        "New password": "New password",
        "New value": "New value",
        "No results found": "No results found",
        "of": "of",
        "page": "page",
        "result(s)": "result(s)",
        "rows": "rows",
        "Save": "Save",
        "Seconds": "Seconds",
        "Select a column to update": "Select a column to update",
        "Select a Column": "Select a Column",
        "Select a table in the sidebar to get started.": "Select a table in the sidebar to get started.",
        "selected result(s) on": "selected result(s) on",
        "Show Filters": "Show filters",
        "Show referencing tables": "Show referencing tables",
        "Showing": "Showing",
        "Sort by": "Sort by",
        "Sort": "Sort",
        "Tables": "Tables",
        "Thanks for using Piccolo Admin.": "Thanks for using Piccolo Admin.",
        "Update": "Update",
        "Use again": "Use again",
        "Version": "Version",
        "Weeks": "Weeks",
        "Welcome to": "Welcome to",
        "with a matching": "with a matching",
    },
)


WELSH = Translation(
    language_name="Welsh",
    language_code="cy",
    translations={
        "About": "Am",
        "Add Row": "Ychwanegu Rhes",
        "Apply": "Ymgeisiwch",
        "Ascending": "Esgynnol",
        "Back to home page": "Yn ôl i'r dudalen gartref",
        "Back": "Ol",
        "Change password": "Newid cyfrinair",
        "Clear filters": "Clirio hidlwyr",
        "Close": "Cau",
        "Create": "Creu",
        "Current password": "Cyfrinair cyfredol",
        "Dark Mode": "Modd Yywyll",
        "Days": "Dyddiau",
        "Delete": "Dileu",
        "Descending": "Disgyn",
        "Edit": "Golygu",
        "Export CSV": "Allforio CSV",
        "Filter": "Ffilter",
        "Form submitted": "Ffurflen wedi'i chyflwyno",
        "Forms": "Ffurflenni",
        "Go to page": "Ewch i'r dudalen",
        "Hide Filters": "Cuddio hidlwyr",
        "Hide referencing tables": "Cuddio tablau cyfeirio",
        "Home": "Cartref",
        "Hours": "Oriau",
        "Light Mode": "Modd Golau",
        "Loading": "Llwytho",
        "Log out": "Allgofnodi",
        "Minutes": "Munudau",
        "New password confirmation": "Cadarnhad cyfrinair newydd",
        "New password": "Cyfrinair newydd",
        "No results found": "Heb ganfod canlyniadau",
        "of": "o",
        "page": "tudalen",
        "rows": "rhesi",
        "Save": "Arbed",
        "Seconds": "Eiliadau",
        "Select a Column": "Dewiswch Golofn",
        "Select a table in the sidebar to get started.": "Dewiswch un o'r tablau yn y bar ochr i ddechrau.",
        "Show Filters": "Dangos hidlwyr",
        "Show referencing tables": "Dangos tablau cyfeirio",
        "Showing": "Yn dangos",
        "Sort by": "Trefnu yn ôl",
        "Sort": "Didoli",
        "Tables": "Tablau",
        "Thanks for using Piccolo Admin.": "Diolch am ddefnyddio Piccolo Admin.",
        "Update": "Diweddariad",
        "Use again": "Defnyddiwch eto",
        "Version": "Fersiwn",
        "Weeks": "Wythnosau",
        "Welcome to": "Croeso i",
        "with a matching": "gyda chyfateb",
        "New value": "Gwerth newydd",
        "Select a column to update": "Dewiswch golofn i'w diweddaru",
        "result(s)": "canlyniad(au)",
        "selected result(s) on": "canlyniad(au) dethol ymlaen",
    },
)

CROATIAN = Translation(
    language_name="Croatian",
    language_code="hr",
    translations={
        "About": "O",
        "Add Row": "Dodaj redak",
        "Apply": "Primijeni",
        "Ascending": "Uzlazno",
        "Back to home page": "Vrati se na početnu stranicu",
        "Back": "Natrag",
        "Change password": "Promijeni lozinku",
        "Clear filters": "Obriši filtere",
        "Close": "Zatvori",
        "Create": "Kreiraj",
        "Current password": "Trenutna lozinka",
        "Dark Mode": "Tamni način rada",
        "Days": "Dani",
        "Delete": "Izbriši",
        "Descending": "Silazno",
        "Edit": "Uredi",
        "Export CSV": "Izvezi CSV",
        "Filter": "Filtar",
        "Form submitted": "Obrazac poslan",
        "Forms": "Forme",
        "Go to page": "Idi na stranicu",
        "Home": "Početna",
        "Hours": "Sati",
        "Light Mode": "Svijetli način rada",
        "Loading": "Učitavanje",
        "Log out": "Odjava",
        "Minutes": "Minute",
        "New password confirmation": "Potvrda nove lozinke",
        "New password": "Nova lozinka",
        "New value": "Nova vrijednost:",
        "No results found": "Nema rezultata",
        "of": "od",
        "page": "stranici",
        "result(s)": "rezultat(a)",
        "rows": "redaka",
        "Save": "Spremi",
        "Seconds": "Sekunde",
        "Select a column to update": "Odaberite stupac za ažuriranje",
        "Select a Column": "Odaberite stupac",
        "Select a table in the sidebar to get started.": "Za početak odaberite jednu od tablica na bočnoj traci.",
        "selected result(s) on": "odabranih rezultat(a) na",
        "Show Filters": "Prikaži filtere",
        "Showing": "Pokazuje",
        "Sort by": "Sortiraj po",
        "Sort": "Sortiraj",
        "Tables": "Tablice",
        "Thanks for using Piccolo Admin.": "Hvala što koristite Piccolo Admin.",
        "Update": "Ažuriraj",
        "Use again": "Koristi ponovno",
        "Version": "Verzija",
        "Weeks": "Tjedni",
        "Welcome to": "Dobrodošli u",
        "with a matching": "s odgovarajućom kolumnom",
        "Hide Filters": "Sakrij filtre",
        "Hide referencing tables": "Sakrij referentne tablice",
        "Select a column to update": "Odaberite stupac za ažuriranje",
        "Show referencing tables": "Prikaži referentne tablice",
    },
)


PORTUGUESE = Translation(
    language_name="Portuguese",
    language_code="pt",
    translations={
        "Add Row": "Adicionar linha",
        "Apply": "Aplicar",
        "Ascending": "Ascendente",
        "Back": "De volta",
        "Back to home page": "Voltar à página inicial",
        "Change password": "Mudar senha",
        "Clear filters": "Filtros claros",
        "Close": "Perto",
        "Create": "Crio",
        "Current password": "Senha atual",
        "Dark Mode": "Modo escuro",
        "Days": "Dias",
        "Delete": "Excluir",
        "Descending": "descendente",
        "Edit": "Editar",
        "Export CSV": "Exportar CSV",
        "Filter": "Filtro",
        "Form submitted": "Formulário enviado",
        "Forms": "Formulários",
        "Go to page": "Vá para página",
        "Hide Filters": "Ocultar filtros",
        "Hide referencing tables": "Ocultar tabelas de referência",
        "Home": "Casa",
        "Hours": "Horas",
        "Light Mode": "Modo de luz",
        "Loading": "Carregando",
        "Log out": "Sair",
        "Minutes": "Minutos",
        "New password": "Nova Senha",
        "New password confirmation": "Nova confirmação de senha",
        "New value": "Novo valor",
        "No results found": "Nenhum resultado encontrado",
        "Save": "Salvar",
        "Seconds": "Segundos",
        "Select a Column": "Selecione uma coluna",
        "Select a column to update": "Selecione uma coluna para atualizar",
        "Select a table in the sidebar to get started.": "Selecione uma tabela na barra lateral para começar.",
        "Show Filters": "Mostrar filtros",
        "Show referencing tables": "Mostrar tabelas de referência",
        "Showing": "Mostrando",
        "Sort": "Ordenar",
        "Sort by": "Ordenar por",
        "Tables": "Mesas",
        "Thanks for using Piccolo Admin.": "Obrigado por usar o Piccolo Admin.",
        "Update": "Atualizar",
        "Use again": "Use novamente",
        "Version": "Versão",
        "Weeks": "Semanas",
        "Welcome to": "Bem-vindo ao",
        "of": "do",
        "page": "página",
        "result(s)": "resultados)",
        "rows": "linhas",
        "selected result(s) on": "Resultados selecionados (s) em",
        "with a matching": "com uma correspondência",
    },
)


GERMAN = Translation(
    language_name="German",
    language_code="de",
    translations={
        "Add Row": "Zeile hinzufügen",
        "Apply": "Sich bewerben",
        "Ascending": "Aufsteigend",
        "Back": "Der Rücken",
        "Back to home page": "Zurück zur Startseite",
        "Change password": "Passwort ändern",
        "Clear filters": "Klare Filter",
        "Close": "Nah dran",
        "Create": "Schaffen",
        "Current password": "Jetziges Passwort",
        "Dark Mode": "Dunkler Modus",
        "Days": "Tage",
        "Delete": "Löschen",
        "Descending": "Absteigend",
        "Edit": "Bearbeiten",
        "Export CSV": "Exportieren Sie CSV",
        "Filter": "Filter",
        "Form submitted": "Formular eingereicht",
        "Forms": "Formen",
        "Go to page": "Gehen Sie zur Seite",
        "Hide Filters": "Filter ausblenden",
        "Hide referencing tables": "Referenzierungstabellen ausblenden",
        "Home": "Heim",
        "Hours": "Std",
        "Light Mode": "Lichtmodus",
        "Loading": "Wird geladen",
        "Log out": "Ausloggen",
        "Minutes": "Protokoll",
        "New password": "Neues Passwort",
        "New password confirmation": "Neues Passwort bestätigen",
        "New value": "Neuer Wert",
        "No results found": "keine Ergebnisse gefunden",
        "Save": "Speichern",
        "Seconds": "Sekunden",
        "Select a Column": "Wählen Sie eine Spalte aus",
        "Select a column to update": "Wählen Sie eine Spalte aus, um zu aktualisieren",
        "Select a table in the sidebar to get started.": "Wählen Sie eine Tabelle in der Seitenleiste aus, um loszulegen.",
        "Show Filters": "Filter anzeigen",
        "Show referencing tables": "Referenzierungstabellen anzeigen",
        "Showing": "Zeigen",
        "Sort": "Sortieren",
        "Sort by": "Sortieren nach",
        "Tables": "Tische",
        "Thanks for using Piccolo Admin.": "Vielen Dank für die Verwendung von Piccolo Admin.",
        "Update": "Aktualisieren",
        "Use again": "Wiederbenutzen",
        "Version": "Ausführung",
        "Weeks": "Wochen",
        "Welcome to": "Willkommen zu",
        "of": "von",
        "page": "Seite",
        "result(s)": "Ergebnisse)",
        "rows": "Reihen",
        "selected result(s) on": "ausgewählte Ergebnisse (en) auf",
        "with a matching": "mit einem Matching",
    },
)


FRENCH = Translation(
    language_name="French",
    language_code="fr",
    translations={
        "Add Row": "Ajouter une rangée",
        "Apply": "Appliquer",
        "Ascending": "Ascendant",
        "Back": "Retour",
        "Back to home page": "Retour à la page d'accueil",
        "Change password": "Changer le mot de passe",
        "Clear filters": "Filtres à claire",
        "Close": "proche",
        "Create": "Créer",
        "Current password": "Mot de passe actuel",
        "Dark Mode": "Mode sombre",
        "Days": "Journées",
        "Delete": "Effacer",
        "Descending": "Descendant",
        "Edit": "Éditer",
        "Export CSV": "Exporter CSV",
        "Filter": "Filtre",
        "Form submitted": "Formulaire soumis",
        "Forms": "Formes",
        "Go to page": "Aller à la page",
        "Hide Filters": "Masquer les filtres",
        "Hide referencing tables": "Masquer les tables de référence",
        "Home": "Maison",
        "Hours": "Heures",
        "Light Mode": "Mode léger",
        "Loading": "Chargement",
        "Log out": "Se déconnecter",
        "Minutes": "Minutes",
        "New password": "Nouveau mot de passe",
        "New password confirmation": "Confirmation du nouveau mot de passe",
        "New value": "Nouvelle valeur",
        "No results found": "Aucun résultat trouvé",
        "Save": "sauvegarder",
        "Seconds": "Secondes",
        "Select a Column": "Sélectionnez une colonne",
        "Select a column to update": "Sélectionnez une colonne à mettre à jour",
        "Select a table in the sidebar to get started.": "Sélectionnez une table dans la barre latérale pour commencer.",
        "Show Filters": "Montrer les filtres",
        "Show referencing tables": "Afficher les tables de référence",
        "Showing": "Projection",
        "Sort": "Trier",
        "Sort by": "Trier par",
        "Tables": "les tables",
        "Thanks for using Piccolo Admin.": "Merci d'utiliser PicColo Admin.",
        "Update": "Mise à jour",
        "Use again": "Utiliser à nouveau",
        "Version": "Version",
        "Weeks": "Semaines",
        "Welcome to": "Bienvenue à",
        "of": "de",
        "page": "page",
        "result(s)": "résultats)",
        "rows": "Lignes",
        "selected result(s) on": "Résultats sélectionnés sur",
        "with a matching": "avec une correspondance",
    },
)


SPANISH = Translation(
    language_name="Spanish",
    language_code="es",
    translations={
        "Add Row": "Añadir fila",
        "Apply": "Aplicar",
        "Ascending": "Ascendente",
        "Back": "atrás",
        "Back to home page": "Volver a la página de inicio",
        "Change password": "Cambia la contraseña",
        "Clear filters": "Filtros claros",
        "Close": "Cerca",
        "Create": "Crear",
        "Current password": "Contraseña actual",
        "Dark Mode": "Modo oscuro",
        "Days": "Días",
        "Delete": "Borrar",
        "Descending": "Descendente",
        "Edit": "Editar",
        "Export CSV": "CSV de exportación",
        "Filter": "Filtrar",
        "Form submitted": "Formulario enviado",
        "Forms": "Formularios",
        "Go to page": "Ir a la página",
        "Hide Filters": "Ocultar filtros",
        "Hide referencing tables": "Ocultar tablas de referencia",
        "Home": "Hogar",
        "Hours": "Horas",
        "Light Mode": "Modo de luz",
        "Loading": "Cargando",
        "Log out": "Cerrar sesión",
        "Minutes": "Minutos",
        "New password": "Nueva contraseña",
        "New password confirmation": "Nueva confirmación de contraseña",
        "New value": "Nuevo valor",
        "No results found": "No se han encontrado resultados",
        "Save": "Ahorrar",
        "Seconds": "Segundos",
        "Select a Column": "Seleccione una columna",
        "Select a column to update": "Seleccione una columna para actualizar",
        "Select a table in the sidebar to get started.": "Seleccione una tabla en la barra lateral para comenzar.",
        "Show Filters": "Mostrar filtros",
        "Show referencing tables": "Mostrar tablas de referencia",
        "Showing": "Demostración",
        "Sort": "Clasificar",
        "Sort by": "Ordenar por",
        "Tables": "Mesas",
        "Thanks for using Piccolo Admin.": "Gracias por usar Piccolo Admin.",
        "Update": "Actualizar",
        "Use again": "Usar de nuevo",
        "Version": "Versión",
        "Weeks": "Semanas",
        "Welcome to": "Bienvenido a",
        "of": "de",
        "page": "página",
        "result(s)": "resultados)",
        "rows": "hilera",
        "selected result(s) on": "Resultados seleccionados en",
        "with a matching": "con un juego",
    },
)


TRANSLATIONS: t.List[Translation] = [
    CROATIAN,
    ENGLISH,
    FRENCH,
    GERMAN,
    PORTUGUESE,
    SPANISH,
    WELSH,
]
