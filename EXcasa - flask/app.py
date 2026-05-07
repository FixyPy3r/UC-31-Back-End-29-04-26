from flask import Flask, render_template
 
app = Flask(__name__)
 
sabores = ['calabresa', 'nordestina']


@app.route('/pizza/<sabor>')
def pizza(sabor):
    if sabor in sabores:
        return render_template(sabor + '.html')
    else:
        return render_template('Nencontrada.html', sabor=sabor)
 
if __name__ == '__main__':
    app.run(debug=True)