from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/analysis')
def analysis():
    articles = [
        {"id": 1, "title": "Introdução à Análise de Dados", "description": "Aprenda os conceitos básicos de análise de dados.", "image": "https://via.placeholder.com/300x200"},
        {"id": 2, "title": "Ferramentas de Análise de Dados", "description": "Uma visão geral das ferramentas mais usadas.", "image": "https://via.placeholder.com/300x200"},
        {"id": 3, "title": "Técnicas Avançadas de Análise", "description": "Explore técnicas avançadas de análise de dados.", "image": "https://via.placeholder.com/300x200"},
    ]
    return render_template('category.html', category="Análise de Dados", articles=articles)

@app.route('/rpa')
def rpa():
    articles = [
        {"id": 1, "title": "Introdução ao RPA", "description": "Conheça os conceitos básicos de RPA.", "image": "https://via.placeholder.com/300x200"},
        {"id": 2, "title": "Ferramentas de RPA", "description": "Veja as ferramentas mais utilizadas no mercado.", "image": "https://via.placeholder.com/300x200"},
        {"id": 3, "title": "Implementação de RPA", "description": "Saiba como implementar RPA na sua empresa.", "image": "https://via.placeholder.com/300x200"},
    ]
    return render_template('category.html', category="RPA", articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = {
        "title": "Exemplo de Artigo",
        "date": "01/07/2024",
        "author": "Autor Exemplo",
        "image": "https://via.placeholder.com/600x400",
        "content": "Conteúdo do artigo aqui..."
    }
    return render_template('article.html', article=article)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
