from app.etl import process

def test_etl():
    assert process('sample.csv') is not None
