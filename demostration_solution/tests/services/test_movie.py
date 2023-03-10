from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='Йеллоустоун', year=2018, rating=8.6)
    movie_2 = Movie(id=1, title='Омерзительная восьмерка', year=2015, rating=7.8)
    movie_3 = Movie(id=1, title='Вооружен и очень опасен', year=1978, rating=6)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movie = self.movie_service.get_all()

        assert len(movie) > 0

    def test_create(self):
        movie_d = {
            "title": "Blue sky",
            "description": "Описание",
            "trailer": "https://www.youtube.com/watch?v=LVdRR6m5OdА",
            "year": "2020",
            "rating": "3.4",
            "genre_id": "2",
            "director_id": "3"
        }

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 3,
            "title": "Sky blue"
        }
        self.movie_service.update(movie_d)
