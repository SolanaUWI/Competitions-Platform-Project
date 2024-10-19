import pytest
from App import create_app
from App.database import db
from sqlalchemy.sql import text  

@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  
    })

    with app.app_context():
        db.create_all()  
        yield app
        db.drop_all()  
        db.session.remove()

@pytest.fixture(scope='function', autouse=True)
def clean_db(test_app):
    with test_app.app_context():
        db.session.rollback()
        db.session.execute(text("DELETE FROM user"))
        db.session.execute(text("DELETE FROM student"))
        db.session.execute(text("DELETE FROM admin"))
        db.session.execute(text("DELETE FROM competitions"))
        db.session.execute(text("DELETE FROM results"))
        db.session.commit()

@pytest.fixture(scope='function')
def client(test_app):
    return test_app.test_client()
