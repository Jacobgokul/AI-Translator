from flask import Flask, render_template, request
from features.translator import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    languages = translator.list_of_lang()

    return render_template('index.html', languages=languages)

@app.route('/translate', methods=['Post'])
def translate():
    text = request.form['text']
    selected_lang = request.form['language']

    languages = translator.list_of_lang()
    translated_text = translator.text_translator(text, selected_lang)

    context = {
        'translated_text': translated_text,
        'languages': languages,
        'selected_lang': selected_lang
    }
    print(context['selected_lang'])
    return render_template('index.html', **context)

if __name__ == "__main__":
    app.run(debug=True)