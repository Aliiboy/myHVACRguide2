<!-- > Note -->

myHVACRguide
======
Application de gestion de projet en HVAC/R


## Django
https://docs.djangoproject.com/fr/2.2/
### Package de dev
#### Coverage https://coverage.readthedocs.io/en/coverage-5.3/#
surveillance du programme, pour determiner se qu'il doit etre testé
- coverage run --source='.' manage.py test
- coverage html (rapport)


## VSCODE & PY
### Commandes VS CODE
- IntelliSense HTML :
CTRL+Space
### Commandes PY
- creer fichier pip freeze :
py -m pip freeze > uninstall.txt
### Extensions
- Language
French language pack

- Icones
vscode-icons

- Doc pour Python et JS
Kite Autocomplete Plugin for Visual Studio Code

- HTML
IntelliSense for CSS class names in HTML
Django Templates

- github
### Raccourcis
- Copier une ligne : Alt+Shift+fleche du bas
- Prévisualisation : CTRL+Shit+V


## Heroku
### Commandes
- Creer la base de données
heroku addons:create
heroku-postgresql:hobby-dev

- Log
heroku logs --tail --app technibe

- Paramatres de base console
heroku config:set DISABLE_COLLECTSTATIC=1 --app technibe
heroku run python src/manage.pycollectstatic --app technibe

### Variables d'environnement
- Dans le env.
SECRET_KEY=kobl@t=yw9d*0y%jt2gjnq78=u!z_rrxb&w8e47l!(jz@m79zy
DEBUG=False
DB_NAME=your-db-name
DB_USER=your-db-user-name
DB_PASSWORD=your-db-password
DB_HOST=localhost
RECAPTCHA_PUBLIC_KEY=your-recaptcha-public-key
RECAPTCHA_PRIVATE_KEY=your-recaptcha-private-key

## Github
### Commandes
- Supprimer l'historique des validations avec les commandes git
https://gist.github.com/heiswayi/350e2afda8cece810c0f6116dadbe651


## TODOLIST
### GCU
https://www.legalplace.fr/contrats/conditions-generales-d-utilisation/creer/11
https://django-termsandconditions.readthedocs.io/en/latest/#
### Accounts
delete profile
### template
404
403
### dashboard
creation
### setting
mise en cache
### menu navigation en python

### HTML
Continuer sur dream w au plus simple
dream w : faire meme principe de andt sur edition du profil
    ajout ou changement d'email
    modification de mot de pass
    tout les templates accounts