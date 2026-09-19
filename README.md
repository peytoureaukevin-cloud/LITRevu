# LITRevu - étapes 0 à 2

Cette version contient uniquement le socle du projet : un environnement Django,
un modèle utilisateur personnalisé et les pages d’inscription, de connexion et
de déconnexion.

## Installation

Python 3.12 ou une version plus récente est requis.

```bash
git clone https://github.com/peytoureaukevin-cloud/LITRevu.git
cd LITRevu
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Ouvrez ensuite <http://127.0.0.1:8000/login/>.

Pour un environnement de production, définissez une valeur secrète pour
`DJANGO_SECRET_KEY` et positionnez `DJANGO_DEBUG=0`.

## Administration

Un superutilisateur est inclus dans la base SQLite fournie :

| Identifiant | Mot de passe |
| --- | --- |
| `admin` | `Admin!123456` |

L’administration est disponible sur <http://127.0.0.1:8000/admin/>.

## Accessibilité

Les formulaires disposent de labels visibles, d’un focus clavier contrasté,
d’un lien d’accès rapide au contenu principal et de titres explicites.
