import allure
from pytest_voluptuous import S
from schemas.schemas import *


@allure.label('owner', 'Александр Санталов')
@allure.epic('Тесты reqres.in')
@allure.title('Создание пользователя')
def test_create_user(reqres):
    created_user = reqres.post('api/users', {'name': 'Alex', 'job': 'Tester'})

    assert created_user.status_code == 201
    assert S(create_user) == created_user.json()
    assert created_user.json()['name'] == 'Alex'
    assert created_user.json()['job'] == 'Tester'


@allure.label('owner', 'Александр Санталов')
@allure.epic('Тесты reqres.in')
@allure.title('Обновление пользователя через метод put')
def test_update_user_by_put(reqres):
    update_user = reqres.put('api/users/2', {'name': 'sant', 'job': 'aqa'})

    assert update_user.status_code == 200
    assert S(create_update_user) == update_user.json()
    assert update_user.json()['name'] == 'sant'
    assert update_user.json()['job'] == 'aqa'


@allure.label('owner', 'Александр Санталов')
@allure.epic('Тесты reqres.in')
@allure.title('Обновление пользователя через метод patch')
def test_update_user_by_patch(reqres):
    update_user = reqres.put('api/users/2', {'name': 'asantalov', 'job': 'manual_tester'})

    assert update_user.status_code == 200
    assert S(create_update_user) == update_user.json()
    assert update_user.json()['name'] == 'asantalov'
    assert update_user.json()['job'] == 'manual_tester'


@allure.label('owner', 'Александр Санталов')
@allure.epic('Тесты reqres.in')
@allure.title('Удаление пользователя')
def test_delete_user(reqres):
    delete_user = reqres.delete('api/users/2')

    assert delete_user.status_code == 204


@allure.label('owner', 'Александр Санталов')
@allure.epic('Тесты reqres.in')
@allure.title('Успешная регистрация')
def test_successful_register(reqres):
    user_register = reqres.post('api/register', {'email': 'eve.holt@reqres.in', 'password': 'pistol'})

    assert user_register.status_code == 200
    assert S(register_user) == user_register.json()
    assert user_register.json()['id']
    assert user_register.json()['token']


@allure.label('owner', 'Александр Санталов')
@allure.epic('Тесты reqres.in')
@allure.title('Неуспешная регистрация')
def test_unsuccessful_register(reqres):
    user_register = reqres.post('api/register', {'email': 'sydney@fife'})

    assert user_register.status_code == 400
    assert S(unregister_user) == user_register.json()
    assert user_register.json()['error'] == 'Missing password'
