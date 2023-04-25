# Дополнительные опции Codegen

Помимо указания url, сodegen может принимать еще несколько дополнительных атрибутов.

Общий синтаксический формат для записи сценария выглядит так:

`codegen [параметры] [url]`

Узнать доступные опции и краткое их описание можно, выполнив команду

```shell
playwright codegen --help
```

Рассмотрим несколько из них.

Вы можете указать размер открываемого окна браузера, указав аргумент `--viewport-size`

```shell
playwright codegen --viewport-size=800,600 https://playwright-todomvc.antonzimaiev.repl.co
```

При записи сценария вы можете сразу указать файл, в который будете сохранен записанный код, добавив аргумент `-о` или
`--output` и указав имя файла.

```shell
playwright codegen -o lesson.py https://playwright-todomvc.antonzimaiev.repl.co
```
