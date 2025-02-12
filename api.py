from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'Título': 'O Alquimista ',
        'Autor': 'Paulo Coelho'
    },

    {
        'id': 2,
        'Título':'O Pequeno Príncipe',
        'Autor':'Antoine de Saint-Exupéry'
    },
    {
        'id': 3,
        'Título':'Dom Quixote',
        'Autor':'Manuel Cervantes'
    }
]
