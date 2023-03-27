## Проект API автотестов
### Используемые технологии
<p  align="center">
<code><img width="5%" title="Python" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1024px-Python.svg.png"></code>
<code><img width="5%" title="Pycharm" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1200px-PyCharm_Icon.svg.png"></code>
<code><img width="5%" title="Pytest" src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg"></code>
<code><img width="5%" title="Selene" src="https://fs.getcourse.ru/fileservice/file/download/a/159627/sc/264/h/e0cabcb69a2df1e6b1086292c020a4a7.png"></code>
<code><img width="5%" title="Requests" src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png"></code>
<code><img width="5%" title="Allure Report" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4"></code>
<code><img width="5%" title="Allure TestOps" src="https://marketplace-cdn.atlassian.com/files/92e2d8c3-2a30-46c0-bf21-2453a4a270d3?fileType=image&mode=full-fit"></code>
<code><img width="5%" title="Jira" src="https://logojinni.com/image/logos/jira-3.svg"></code>
<code><img width="5%" title="Selenoid" src="https://diginomica.com/sites/default/files/images/2017-09/docker-container.jpg"></code>
<code><img width="5%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"></code>
<code><img width="5%" title="GitHub" src="https://cdn-icons-png.flaticon.com/512/25/25231.png"></code>
<code><img width="5%" title="Telegram" src="https://cdn.icon-icons.com/icons2/923/PNG/256/telegram_icon-icons.com_72055.png"></code>
</p>
<br> 

### Проекст состоит из двух групп тестов:
<details><summary><b>reqres.in - только api тесты</b></summary>
<ul>
  <li>Создание пользователя</li>
  <li>Обновление пользователя через метод put</li>
  <li>Обновление пользователя через метод patch</li>
  <li>Удаление пользователя</li>
  <li>Успешная регистрация</li>
  <li>Неуспешная регистрация</li>
</ul>

</details>
<details><summary><b>demowebshop - комбинированные ui\api тесты</b></summary>
<br> 
<ul>
  <li>Успешная авторизация</li>
  <li>Удаление товара из списка желаемого</li>
  <li>Удаление товара из карзины</li>
  <li>Удаление адреса покупателя</li>
  <li>Логаут</li>
</ul>
</details>
<br>

### <img width="3%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"> [Запуск проекта в Jenkins](https://jenkins.autotests.cloud/job/asantalov_diplom_api/)
##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение на сервере Jenkins.
![Jenkins_run](/images/run.jpg)

### <img width="3%" title="Allure Report" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4"> Allure report
##### После прохождения тестов, результаты можно посмотреть в Allure отчете.
![Overview](images/all.jpg)

##### Во вкладке Behaviors находятся собранные тест кейсы, у которых описаны шаги. Для api методов реализованы вложения. Для комбинированных тестов по окончанию теста делается скриншот и сохраняется видеозапись теста.
![Behaviors](images/allure2.jpg)

<video width="320" height="240" controls>
  <source src="video.mov" type="video/mp4">
</video>

