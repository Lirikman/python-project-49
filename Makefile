install: #запустить после первого клонирования или удаления зависмостей
	poetry install

brain-games: #вывод на экран приветствия
	poetry run brain-games

build: #сборка пакета
	poetry build

publish: #публикация проекта
	poetry publish --dry-run

package-install: #установка пакетов
	python3 -m pip install --user dist/*.whl
