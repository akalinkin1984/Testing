import pytest
import requests

from main import check_auth, list_of_numbers, solve


# НЕОБХОДИМО ВВЕСТИ СВОЙ ТОКЕН ЯНДЕКС ДИСКА
TOKEN_YA_DISK = ''


@pytest.mark.parametrize(
    "login, password, expected",
    (
        ['user', 'password', 'Доступ ограничен'],
        ['admin', '123', 'Доступ ограничен'],
        ['admin', 'password', 'Добро пожаловать']
    )
)
def test_check_auth(login, password, expected):
    actual = check_auth(login, password)
    assert actual == expected


@pytest.mark.parametrize(
    "n, expected",
    (
        [1, [1]],
        [5, [1, 2, 3, 4, 5]],
        [9, [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    )
)
def test_list_of_numbers(n, expected):
    actual = list_of_numbers(n)
    assert actual == expected


@pytest.mark.parametrize(
    "receipts, expected",
    (
        [[123, 145, 346, 246, 235, 166, 112, 351, 436], ([346, 166, 436], 3)],
        [[123, 145], ([], 0)],
        [[111, 222, 333, 444, 555, 666, 777, 888, 999, 123, 124, 125], ([333, 666, 999, 125], 4)]
    )
)
def test_solve(receipts, expected):
    actual = solve(receipts)
    assert actual == expected


class TestYandexDisk:
    def setup_method(self):
        self.headers = {'Authorization': f'OAuth {TOKEN_YA_DISK}'}
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def test1(self):
        params = {'path': '123'}
        response = requests.put(self.url, headers=self.headers, params=params)
        assert response.status_code == 201

    def test2(self):
        params = {'path': '234'}
        response = requests.put(self.url, headers=self.headers, params=params)
        assert response.status_code == 201

    def test3(self):
        params = {'path': '123'}
        response = requests.put(self.url, headers=self.headers, params=params)
        assert response.status_code == 409

    def test4(self):
        response = requests.put(self.url, headers=self.headers)
        assert response.status_code == 400

    def test5(self):
        params = {'path': '123'}
        response = requests.put(self.url, params=params)
        assert response.status_code == 401

    @pytest.mark.xfail
    def test6(self):
        params = {'path': '123'}
        response = requests.put(self.url, headers=self.headers, params=params)
        assert response.status_code == 423

    def test7(self):
        params = {'path': '123'}
        response = requests.get(self.url, headers=self.headers, params=params)
        assert response.status_code == 200
