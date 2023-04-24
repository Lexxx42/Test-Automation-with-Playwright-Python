# Установка IDE

## Установка Visual Studio

VS Code - это бесплатный редактор кода, который работает в операционных системах macOS, Linux и Windows.

Системные требования:

Процессор с частотой 1,6 ГГц или выше
1 ГБ оперативной памяти
Платформы
VS Code поддерживается на следующих платформах:

OS X El Capitan (10.11+)
Windows 8.0, 8.1 и 10, 11 (32-разрядная и 64-разрядная версии)
Linux (Debian): Ubuntu Desktop 16.04, Debian 9
Linux (Red Hat): Red Hat Enterprise Linux 7, CentOS 7, Fedora 34

### Windows

Загрузите Visual Studio Code для Windows.

Дважды кликните по `VSCodeSetup.exe`, чтобы запустить процесс установки.

### Mac OS X

Загрузите Visual Studio Code для Mac OS X.
Дважды щелкните на `VSCode-osx.zip`, чтобы разархивировать содержимое.
Перетащите `Visual Studio Code.app` в папку `Applications(Программы)`

### Linux

Загрузите Visual Studio Code для Linux.
Разархивируйте `VSCode-linux-x64.zip` из этой папки.
Дважды щелкните `Code`, чтобы запустить Visual Studio Code.

> Совет: Если вы хотите запустить VS Code с терминала, создайте следующую ссылку
> `/path/to/vscode/Code`, заменив ее абсолютным путем к исполняемому файлу

```shell
sudo ln -s /path/to/vscode/Code /usr/local/bin/code
```

Теперь вы можете просто ввести `code .`

## Установка PyCharm

JetBrains PyCharm — это кроссплатформенная интегрированная среда разработки для языка программирования Python,
разработанная компанией JetBrains

### Windows

Скачайте и запустите программу установки и следуйте инструкциям мастера

Учтите следующие параметры в мастере установки

**64-bit launcher:** Добавляет значок запуска на Рабочий стол.

**Open Folder as Project:** Добавляет опцию в контекстное меню папки, которая позволит открыть выбранный каталог как
проект PyCharm.

**.py**: Устанавливает ассоциацию с файлами Python для их открытия в PyCharm.

**Add launchers dir to the PATH:** Позволяет запускать данный экземпляр PyCharm из консоли без указания пути к нему.

MacOS
Загрузите образ диска.

Смонтируйте образ и перетащите приложение PyCharm в Приложения.

Запустите приложение PyCharm из каталога Applications, Launchpad или Spotlight.
