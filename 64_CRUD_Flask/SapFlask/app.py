from flask import Flask, render_template, request, url_for, redirect
from database import db
from flask_migrate import Migrate

from models import Persona
from forms import PersonaForm

app = Flask(__name__)

# CONFIG DB
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'sap_flask_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# CONFIG flask-migrate
migrate = Migrate()
migrate.init_app(app, db)
# CONFIG flask-wtf
app.config['SECRET_KEY'] = 'my_secret_key'

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    # personas = Persona.query.all()
    personas = Persona.query.order_by('id')
    total_personas = Persona.query.count()

    app.logger.debug(f'Listado Personas: {personas}')
    app.logger.debug(f'Total Personas: {total_personas}')

    return render_template('index.html', personas=personas, total_personas=total_personas)
@app.route('/ver/<int:id>')
def verDetalle(id):
    # persona = Persona.query.get(id)
    persona = Persona.query.get_or_404(id)

    app.logger.debug(f'Ver persona: {persona}')

    return render_template('detalle.html', persona=persona)

@app.route('/agregar', methods=['GET','POST'])
def agregar():
    persona = Persona()
    persona_form = PersonaForm(obj=persona)

    if request.method == 'POST':
        if persona_form.validate_on_submit():
            persona_form.populate_obj(persona)
            app.logger.debug(f'Persona a insertar {persona}')

            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('agregar.html', form=persona_form)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    persona = Persona.query.get_or_404(id)
    persona_form = PersonaForm(obj=persona)

    if request.method == 'POST':
        if persona_form.validate_on_submit():
            persona_form.populate_obj(persona)
            app.logger.debug(f'Persona a modificar {persona}')

            db.session.commit()
            return redirect(url_for('index'))

    return render_template('editar.html', form=persona_form)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Persona a eliminar: {persona}')

    db.session.delete(persona)
    db.session.commit()

    return redirect(url_for('index'))

