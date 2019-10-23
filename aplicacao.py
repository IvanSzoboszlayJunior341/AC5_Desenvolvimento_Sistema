from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
  
    return render_template('homepage.html')

@app.route('/Cursos')
def rounte():
    return render_template('listadecursos.html')

@app.route('/Detalhecurso')
def rounte1():
    return render_template('detalhedecurso.html')

@app.route('/Disciplina')
def rounte2():
    return render_template('disciplina.html')

@app.route('/Noticias')
def rounte3():
    return render_template('noticia.html')



app.run()