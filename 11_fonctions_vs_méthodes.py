# Exercice: introduire une classe Article
# pour éviter la répétition de paramètres
# titre, contenu, lien, résumé
def crée_page_web(titre, contenu):
    print("création de la page web")
    slug = titre.lower().replace(" ", "-")
    return "https://blog.e2li/" + slug


def envoi_email(titre, résumé, lien):
    print("envoi email à propos de", titre)


def envoi_tweet(titre, résumé, lien):
    print("envoi tweet à propos de", titre)


def publie_article(titre, résumé, contenu):
    lien = crée_page_web(titre, contenu)
    envoi_email(titre, résumé, lien)
    envoi_tweet(titre, résumé, lien)


titre = "Un super titre"
résumé = "Un super résumé"
contenu = "Du contenu de qualité"
publie_article(titre, résumé, contenu)
