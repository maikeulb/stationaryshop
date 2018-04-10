import os
import click

from glob import glob
from subprocess import call
from app.extensions import db
from app.models import (
    CatalogItem,
    Category,
    Permission,
    Role,
    User
)
import config
from config import Config
from flask import current_app
from flask.cli import with_appcontext
from werkzeug.exceptions import MethodNotAllowed, NotFound

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)
TEST_PATH = os.path.join(PROJECT_ROOT, 'tests')


def register(app):
    @app.cli.command('seed-db')
    @click.command()
    def seed():
        print('Starting DB seed')
        db.drop_all()
        db.create_all()

        seed_users()
        seed_categories()
        seed_catalog()

        db.session.commit()
        print('DB seed complete')

    def seed_users():
        print('Adding roles, demo-user, demo-admin, and admin')
        Role.insert_roles()

        demo = User(
            username='demo',
            password=Config.DEMO_PASSWORD,
            email=Config.DEMO_EMAIL,
            role=Role.query.filter_by(permissions=Permission.GENERAL).first())
        demo_admin = User(
            username='demo_admin',
            password=Config.DEMO_ADMIN_PASSWORD,
            email=Config.DEMO_ADMIN_EMAIL,
            role=Role.query.filter_by(permissions=Permission.DEMO_ADMINISTER).first())
        admin = User(
            username='admin',
            password=Config.ADMIN_PASSWORD,
            email=Config.ADMIN_EMAIL,
            role=Role.query.filter_by(permissions=Permission.ADMINISTER).first())

        db.session.add(demo)
        db.session.add(demo_admin)
        db.session.add(admin)

    def seed_categories():
        print('Adding categories')
        Role.insert_roles()

        notebooks = Category(
            name='notebooks')
        pens = Category(
            name='pens and pencils')
        desk = Category(
            name='desk accessories')

        db.session.add(notebooks)
        db.session.add(pens)
        db.session.add(desk)

    def seed_catalog():
        print('Adding catalog')
        if config.DevelopmentConfig:
            baseurl = 'http://localhost:5000/static/'
        else:
            baseurl = 'http://localhost:5000/'

        paper_note = CatalogItem(
            name='Paper Note',
            description="120 sheets",
            image_url="{}images/products/paper_note.jpg".format(baseurl),
            price=20,
            category_id=1)

        double_ring = CatalogItem(
            name='Plantation Double Ring Note',
            description="80 sheets",
            image_url="{}images/products/plantation_double_ring_note.jpg".format(
                baseurl),
            price=2.5,
            category_id=1)

        paper_note_set = CatalogItem(
            name='Planation Paper Note 5PCS/Set',
            description="30 sheets/book",
            image_url="{}images/products/plantation_paper_note_set.jpg".format(
                baseurl),
            price=3.5,
            category_id=1)

        recyle_paper = CatalogItem(
            name='Recycle Paper Double Ring Note',
            description="80 sheets",
            image_url="{}images/products/recycle_paper_double_ring_note.jpg".format(
                baseurl),
            price=3,
            category_id=1)

        db.session.add(paper_note)
        db.session.add(double_ring)
        db.session.add(paper_note_set)
        db.session.add(recyle_paper)

        colored_pencils = CatalogItem(
            name='12 Colored Pencils',
            description="Material: Cedar",
            image_url="{}images/products/colored_pencils.jpg".format(baseurl),
            price=5,
            category_id=2)

        ballpoint_pens = CatalogItem(
            name='Gel-Ink BallPoint Pen 6PCS/SET',
            description="Pen Nib: 0.38mm",
            image_url="{}images/products/ballpoint_pen_set.jpg".format(
                baseurl),
            price=8,
            category_id=2)

        hexa_pen = CatalogItem(
            name='10 Colors Hexa Pen Set Minia',
            description="Material: Polyproplene",
            image_url="{}images/products/hexa_pen_set_minia.jpg".format(
                baseurl),
            price=5,
            category_id=2)

        db.session.add(colored_pencils)
        db.session.add(ballpoint_pens)
        db.session.add(hexa_pen)

        calculator = CatalogItem(
            name='Calculator',
            description="Color: Black",
            image_url="{}images/products/calculator.jpg".format(baseurl),
            price=25,
            category_id=3)

        correction_tape = CatalogItem(
            name='Correction Tape',
            description="Dimensions: 5mmx10cm",
            image_url="{}images/products/correction_tape.jpg".format(baseurl),
            price=8,
            category_id=3)

        hole_puncher = CatalogItem(
            name='2 Hole Puncher',
            description="Maximum Capacity:10c",
            image_url="{}images/products/hole_puncher.jpg".format(baseurl),
            price=5.5,
            category_id=3)

        db.session.add(calculator)
        db.session.add(correction_tape)
        db.session.add(hole_puncher)

    @click.command()
    @click.option('-f', '--fix-imports', default=False, is_flag=True,
                  help='Fix imports using isort, before linting')
    def lint(fix_imports):
        skip = ['node_modules', 'requirements']
        root_files = glob('*.py')
        root_directories = [
            name for name in next(os.walk('.'))[1] if not name.startswith('.')]
        files_and_directories = [
            arg for arg in root_files + root_directories if arg not in skip]

        def execute_tool(description, *args):
            """Execute a checking tool with its arguments."""
            command_line = list(args) + files_and_directories
            click.echo('{}: {}'.format(description, ' '.join(command_line)))
            rv = call(command_line)
            if rv != 0:
                exit(rv)

        if fix_imports:
            execute_tool('Fixing import order', 'isort', '-rc')
        execute_tool('Checking code style', 'flake8')

    @click.command()
    def clean():
        for dirpath, dirnames, filenames in os.walk('.'):
            for filename in filenames:
                if filename.endswith('.pyc') or filename.endswith('.pyo'):
                    full_pathname = os.path.join(dirpath, filename)
                    click.echo('Removing {}'.format(full_pathname))
                    os.remove(full_pathname)

    @click.command()
    @click.option('--url', default=None,
                  help='Url to test (ex. /static/image.png)')
    @click.option('--order', default='rule',
                  help='Property on Rule to order by (default: rule)')
    @with_appcontext
    def urls(url, order):
        rows = []
        column_length = 0
        column_headers = ('Rule', 'Endpoint', 'Arguments')

        if url:
            try:
                rule, arguments = (
                    current_app.url_map
                               .bind('localhost')
                               .match(url, return_rule=True))
                rows.append((rule.rule, rule.endpoint, arguments))
                column_length = 3
            except (NotFound, MethodNotAllowed) as e:
                rows.append(('<{}>'.format(e), None, None))
                column_length = 1
        else:
            rules = sorted(
                current_app.url_map.iter_rules(),
                key=lambda rule: getattr(rule, order))
            for rule in rules:
                rows.append((rule.rule, rule.endpoint, None))
            column_length = 2

        str_template = ''
        table_width = 0

        if column_length >= 1:
            max_rule_length = max(len(r[0]) for r in rows)
            max_rule_length = max_rule_length if max_rule_length > 4 else 4
            str_template += '{:' + str(max_rule_length) + '}'
            table_width += max_rule_length

        if column_length >= 2:
            max_endpoint_length = max(len(str(r[1])) for r in rows)
            # max_endpoint_length = max(rows, key=len)
            max_endpoint_length = (
                max_endpoint_length if max_endpoint_length > 8 else 8)
            str_template += '  {:' + str(max_endpoint_length) + '}'
            table_width += 2 + max_endpoint_length

        if column_length >= 3:
            max_arguments_length = max(len(str(r[2])) for r in rows)
            max_arguments_length = (
                max_arguments_length if max_arguments_length > 9 else 9)
            str_template += '  {:' + str(max_arguments_length) + '}'
            table_width += 2 + max_arguments_length

        click.echo(str_template.format(*column_headers[:column_length]))
        click.echo('-' * table_width)

        for row in rows:
            click.echo(str_template.format(*row[:column_length]))

    @app.cli.command("test")
    def test():
        import pytest
        rv = pytest.main([TEST_PATH, '--verbose'])
        exit(rv)

    @app.cli.group()
    def translate():
        pass

    @translate.command()
    @click.argument('lang')
    def init(lang):
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system(
                'pybabel init -i messages.pot -d app/translations -l ' + lang):
            raise RuntimeError('init command failed')
        os.remove('messages.pot')

    @translate.command()
    def update():
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system('pybabel update -i messages.pot -d app/translations'):
            raise RuntimeError('update command failed')
        os.remove('messages.pot')

    @translate.command()
    def compile():
        if os.system('pybabel compile -d app/translations'):
            raise RuntimeError('compile command failed')
