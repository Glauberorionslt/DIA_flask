from flask import Flask, render_template, jsonify, request
import os
import json


app = Flask(__name__)

def load_articles():
    try:
        # Verifique o caminho do arquivo e abra o arquivo
        file_path = os.path.join(os.path.dirname(__file__), 'articles.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

@app.route('/')
def home():
    analysis_image = 'https://via.placeholder.com/600x400?text=Analise+de+Dados'
    rpa_image = 'https://via.placeholder.com/600x400?text=RPA'
    return render_template('home.html', analysis_image=analysis_image, rpa_image=rpa_image)

@app.route('/analysis')
def analysis():
    articles = [
        {"id": 1, "title": "Introdução à Análise de Dados", "description": "Aprenda os conceitos básicos de análise de dados.", "image": "\static\img\capa_card_subject\ANALISE DE DADOS\DATA_ANALYSIS.jpg"},
        {"id": 2, "title": "Ferramentas de Análise de Dados", "description": "Uma visão geral das ferramentas mais usadas.", "image": "\static\img\capa_card_subject\ANALISE DE DADOS\DATA_ANALYSIS.jpg"},
        {"id": 3, "title": "Técnicas Avançadas de Análise", "description": "Explore técnicas avançadas de análise de dados.", "image": "\static\img\capa_card_subject\ANALISE DE DADOS\DATA_ANALYSIS.jpg"},
    ]
    return render_template('category.html', category="Análise de Dados", articles=articles)

@app.route('/rpa')
def rpa():
    articles = [
        {"id": 4, "title": "Introdução ao RPA", "description": "Conheça os conceitos básicos de RPA.", "image": "\static\img\capa_card_subject\RPA\RPA.jpeg"},
        {"id": 5, "title": "Ferramentas de RPA", "description": "Veja as ferramentas mais utilizadas no mercado.", "image": "\static\img\capa_card_subject\RPA\RPA.jpeg"},
        {"id": 6, "title": "Implementação de RPA", "description": "Saiba como implementar RPA na sua empresa.", "image": "\static\img\capa_card_subject\RPA\RPA.jpeg"},
    ]
    return render_template('category.html', category="RPA", articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    articles = load_articles()
    article = next((a for a in articles if a['id'] == article_id), None)
    if article is None:
        return "Artigo não encontrado", 404

    return render_template('article.html', article=article)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/all_articles')
def all_articles():
    articles = [
        {"id": 1, "title": "Introdução à Análise de Dados", "description": "Aprenda os conceitos básicos de análise de dados.", "image": "/static/img/capa_card_subject/ANALISE DE DADOS/DATA_ANALYSIS.jpg"},
        {"id": 2, "title": "Ferramentas de Análise de Dados", "description": "Uma visão geral das ferramentas mais usadas.", "image": "/static/img/capa_card_subject/ANALISE DE DADOS/DATA_ANALYSIS.jpg"},
        {"id": 3, "title": "Técnicas Avançadas de Análise", "description": "Explore técnicas avançadas de análise de dados.", "image": "/static/img/capa_card_subject/ANALISE DE DADOS/DATA_ANALYSIS.jpg"},
        {"id": 4, "title": "Introdução ao RPA", "description": "Conheça os conceitos básicos de RPA.", "image": "/static/img/capa_card_subject/RPA/RPA.jpeg"},
        {"id": 5, "title": "Ferramentas de RPA", "description": "Veja as ferramentas mais utilizadas no mercado.", "image": "/static/img/capa_card_subject/RPA/RPA.jpeg"},
        {"id": 6, "title": "Implementação de RPA", "description": "Saiba como implementar RPA na sua empresa.", "image": "/static/img/capa_card_subject/RPA/RPA.jpeg"},
    ]
    return render_template('all_articles.html', articles=articles)

# Rota para processar a pesquisa
@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    articles = load_articles()
    filtered_articles = [article for article in articles if query in article['title'].lower()]
    return render_template('all_articles.html', articles=filtered_articles)

# Nova rota para a página "Contrate Freelancer"
@app.route('/contrate_freelancer')
def contrate_freelancer():
    return render_template('contrate_freelancer.html')

if __name__ == '__main__':
    app.run(debug=True)
