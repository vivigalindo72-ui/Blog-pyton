from flask import Flask, render_template_string

app = Flask(_name_)

posts = [
    {"titulo": "Bienvenidos a mi blog", "autor": "Vivi", "texto": "Este es mi primer post hecho en Python y Flask."},
    {"titulo": "Lo que aprendí", "autor": "Vivi", "texto": "Crear un repo en GitHub desde la compu es más fácil que en el cel."}
]

plantilla = """
<!DOCTYPE html>
<html>
<head><title>Blog-pyton</title></head>
<body style="font-family:Arial; max-width:600px; margin:auto;">
    <h1>Blog-pyton de Vivi</h1>
    <hr>
    {% for p in posts %}
        <h2>{{ p.titulo }}</h2>
        <small>Por {{ p.autor }}</small>
        <p>{{ p.texto }}</p>
        <hr>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def inicio():
    return render_template_string(plantilla, posts=posts)

if _name_ == "_main_":
    app.run(debug=True)
