# bonus
Приложение "Бонусный акаунт"
Функции админ панели:
	1. Добавлять новый аккаунт (Имя, Фамилия, Телефон, Номер карты, Баланс в балах). 
	2. Редактировать: имя, фамилию, телефон
	3. Поиск по номеру карты, фамилии, телефону
	4. Удаление бонусного аккаунта
	5. Добавить транзакции (тип, сумма, дата, чья транзакция)
	6. Фильтр транзакции по типу и дате

Функции REST API:
	1. Получение всех бонусных аккаунтов
	2. Получение информации о бонусном аккаунте и транзакциях по номеру карты
	3. Запрос на создание новой карты

Реализация:

	Исользуемые библиотеки находятся в файле requirements.txt

	Функции админ панели:
	Предусмотрена валидация поля Имя (только кириллица), Телефона (длина 10 символов) и Номера карты (длинна 6 символов). 


	Функции REST API:
	1. Получение всех бонусных аккаунтов - реализовано через views.get_account_all(request). Content-type: apllication\json
	2. Получение информации о бонусном аккаунте и транзакциях по номеру карты - Получение реализовано через передачу ID в url /bonus_account/get_account/:id/ (В отличии от условия ТЗ). 
	Дополнительно предусмотрено условие отсуствия данного id в базе. При необходимости можно дополнительно реализовать получение информации по номеру карты. Content-type: apllication\json
	3. Запрос на создание новой карты. Реализовано через views.add_tras(request). Предусмотрена валидация формата даты.


	Дополнительно:

	В приложении созданы две формы TrasactionForm и AccountForm, и два шаблона form_account.html, form_trasaction.html для дополнительной возможности добавления новых аккаунтов и транзакций.
	Добавлены тесты в test.py