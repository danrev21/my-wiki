================================================================
# Docker is running as a service (daemon), what unit file is used for this? Enter absolute real path.
The unit file used for running the Docker service (daemon) on systems with systemd is typically located at /lib/systemd/system/docker.service for systems using the traditional package installation method. 

You can check the absolute real path of the Docker service unit file by running the following command:

systemctl show --property=FragmentPath docker


This command will display the absolute real path of the unit file associated with the Docker service.

# разница между /usr/lib/systemd/system/ и /lib/systemd/system/
Основное различие между `/usr/lib/systemd/system/` и `/lib/systemd/system/` заключается в месте хранения файлов модулей systemd.

- `/usr/lib/systemd/system/`: этот каталог обычно содержит юнит-файлы, которые устанавливаются пакетами из менеджера пакетов дистрибутива. Эти модульные файлы обычно считаются некритическими компонентами и управляются менеджером пакетов.

- `/lib/systemd/system/`: этот каталог содержит файлы модулей, предоставляемые самой операционной системой или системным администратором. Эти юнит-файлы считаются важными для работы системы и не управляются менеджером пакетов. Системные администраторы могут изменять или добавлять файлы модулей в этот каталог, чтобы настроить поведение systemd.

Таким образом, `/usr/lib/systemd/system/` содержит установленные пакетом юнит-файлы, а `/lib/systemd/system/` содержит важные юнит-файлы, управляемые системным администратором.


# почему docker.service находится и в /usr/lib/systemd/system/ и в /lib/systemd/system/
Присутствие файла `docker.service` как в `/usr/lib/systemd/system/`, так и в `/lib/systemd/system/` связано с тем, как systemd обрабатывает файлы модулей в разных местах.

Systemd позволяет размещать юнит-файлы в нескольких каталогах, чтобы обеспечить совместимость между различными дистрибутивами. `/usr/lib/systemd/system/` — это основное местоположение для юнит-файлов, а `/lib/systemd/system/` — это резервный каталог, который может использоваться некоторыми дистрибутивами.

Наличие файла docker.service в обоих местах гарантирует, что его можно будет найти и использовать независимо от конкретной используемой конфигурации или дистрибутива systemd.

# расположить по приоритету директории храннения unit файлов: /etc/systemd/system/, /lib/systemd/system/, /usr/lib/systemd/system/
CHAT GPT FREE bot, [2/9/24 5:10 PM]
Рекомендуемый порядок определения приоритетов каталогов хранения юнит-файлов в Systemd следующий:

1. /etc/systemd/система/
2. /lib/systemd/система/
3. /usr/lib/systemd/system/

Каталог /etc/systemd/system/ имеет приоритет над другими каталогами, поскольку он допускает локальную настройку и переопределение. Каталог /lib/systemd/system/ содержит юнит-файлы, предоставляемые операционной системой, а в каталоге /usr/lib/systemd/system/ хранятся юнит-файлы, предоставляемые установленными пакетами.
