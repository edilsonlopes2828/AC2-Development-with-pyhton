
from models import Series


def create_series(db, title, genre, seasons):
    series = Series(
        title=title,
        genre=genre,
        seasons=seasons
    )
    db.add(series)
    db.commit()
    db.refresh(series)
    return series


def list_series(db):
    return db.query(Series).order_by(Series.id).all()


def get_series(db, series_id):
    return db.query(Series).filter(Series.id == series_id).first()


def update_series(db, series_id, title=None, genre=None, seasons=None):
    series = get_series(db, series_id)

    if series is None:
        return None

    if title is not None:
        series.title = title
    if genre is not None:
        series.genre = genre
    if seasons is not None:
        series.seasons = seasons

    db.commit()
    db.refresh(series)
    return series


def delete_series(db, series_id):
    series = get_series(db, series_id)

    if series is None:
        return False

    db.delete(series)
    db.commit()
    return True
