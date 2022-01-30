from flask import Flask, render_template
app = Flask(__name__)
from controllers.characters_controller import characters_blueprint
from controllers.items_controller import items_blueprint

@app.route('/home')
def home():
    return render_template('index.html')

# @app.route('/characters')
# def characters():
#     return render_template('/characters/index.html')

# @app.route('/items')
# def items():
#     return render_template('/items/index.html')

if __name__ == '__main__':
    app.run(debug=True)

app.register_blueprint(characters_blueprint)
app.register_blueprint(items_blueprint)
