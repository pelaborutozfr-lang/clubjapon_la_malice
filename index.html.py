# --- Script Python ultra simple pour site local ---

# 🔹 Noms de fichiers (ils doivent être dans le même dossier que le script)
images = ["image1.jpg", "image2.jpg"]
background = "fond2.jpg"

# 🔹 HTML de la page
html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Mon site</title>
    <style>
        body {{
            background: url('{background}') no-repeat center center fixed;
            background-size: cover;
            font-family: Arial, sans-serif;
            color: black;
            text-align: center;
            padding-top: 50px;
        }}
        h1, h2, p {{
            margin: 20px;
        }}
        img {{
            width: 300px;
            margin: 15px;
            border-radius: 15px;
            box-shadow: 0 0 10px black;
        }}
    </style>
</head>
<body>
    <h1>Scénario :</h1>
    <p>C'est l'histoire de la malice le farfadet malicieux</p>
    <h2>chara design :</h2>
    {''.join(f"<img src='{img}' alt='image'>" for img in images)}
</body>
</html>
"""

# 🔹 Crée le fichier HTML
with open("mon_site.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Fichier 'mon_site.html' créé ! Ouvre-le avec ton navigateur.")
