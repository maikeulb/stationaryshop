import os
from glob import glob
from subprocess import call

import click
from flask import current_app
from flask.cli import with_appcontext
from werkzeug.exceptions import MethodNotAllowed, NotFound
from app.extensions import db
from app.models import Category, CatalogItem, Role, User, Permission
from config import Config

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

        print('Complete DB seed')

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

        light = Category(
            name='light')
        medium = Category(
            name='medium')
        dark = Category(
            name='dark')

        db.session.add(light)
        db.session.add(medium)
        db.session.add(dark)

    def seed_catalog():
        print('Adding catalog')
        espresso_roast = CatalogItem(
            name='Expresso Roast',
            description="Smoothe",
            image_url="https://qph.fs.quoracdn.net/main-qimg-26af24cca0015cdfd309f496aee6ce4e.webp",
            price=20,
            category_id=1)

        bali_blue_moon = CatalogItem(
            name='Bali Blue Moon',
            description="Bitter",
            image_url="https://qph.fs.quoracdn.net/main-qimg-26af24cca0015cdfd309f496aee6ce4e.webp",
            price=20,
            category_id=2)

        sumatra_mandheling = CatalogItem(
            name='Sumatra Mandheling',
            description="Sweet",
            image_url="https://qph.fs.quoracdn.net/main-qimg-26af24cca0015cdfd309f496aee6ce4e.webp",
            price=20,
            category_id=2)

        guatamala_antigua = CatalogItem(
            name='Guatamala Antigua',
            description="Decaf",
            image_url="https://qph.fs.quoracdn.net/main-qimg-26af24cca0015cdfd309f496aee6ce4e.webp",
            price=20,
            category_id=3)

        mocha_java = CatalogItem(
            name='Mocha Java',
            description="Nice",
            image_url="https://qph.fs.quoracdn.net/main-qimg-26af24cca0015cdfd309f496aee6ce4e.webp",
            price=20,
            category_id=3)

        db.session.add(espresso_roast)
        db.session.add(bali_blue_moon)
        db.session.add(sumatra_mandheling)
        db.session.add(guatamala_antigua)
        db.session.add(mocha_java)

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

    @click.command()
    def test():
        import pytest
        rv = pytest.main([TEST_PATH, '--verbose'])
        exit(rv)
