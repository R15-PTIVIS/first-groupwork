**How to run the project**

1. Minulla oli repo koneella (joka on kytketty tähän repoon https://github.com/R15-PTIVIS/first-groupwork), mutta lokaali repossa ei ollut django projektin koodia (se oli remote repossa). Menin main-haaraan ja suoritin `git pull`

2. Menin projektin kansioon `cd group_work_one`

3. Epäonnistuin suorittamaan komento `python manage.py runserver`
   ModuleNotFoundError: No module named 'django'
   ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?

4. Suoritin komento `virtual env` ja komento `env\Scripts\activate.ps1`

5. Epäonnistuin suorittamaan komento `python manage.py runserver` samoilla virheilmoituksilla kun askelella 3.

6. Suoritin `python -m pip install django`

7. Komento `python manage.py runserver` meni läpi ja projekti aukeni selaimessa osoitteella http://127.0.0.1:8000

**Jira** https://kirill-nikolaev.atlassian.net/jira/software/projects/ERR/boards/3

#tehty
Kokeilen, jos githubin commit näkyy Jirassa - näyttää toimivalta

Kokeilen, seuraako Jira githubin haaraan tehtyjä muutoksia - näyttää toimivalta

Kokeilen, seuraako Jira githubin haaraan tehtyjä muutoksia ILMAN maininta Jira-avaimesta commitin tekstissä - ei seuraa

Loin toimivan django-projektin:

1. Avasin PyCharmissa New project "first-django"
2. Suoritin kommento `python -m pip install django`
3. Suoritin kommento `django-admin startproject group-one-work`
4. Siirryin group-one-work kansioon ja siinä suoritin kommento `python manage.py runserver`

...ja laitoin sen repoon.

#workflow
Ensin loin kortin Jirassa, sitten tein muutoksia koodiin, commitin ne githubissa ja vein ne etärepoon.
Lopuksi merkitsin kortin tehdyksi.
