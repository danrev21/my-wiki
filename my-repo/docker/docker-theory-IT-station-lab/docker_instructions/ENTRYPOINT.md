===========================
# ENTRYPOINT
позволяет настроить контейнер, который будет работать как исполняемый файл.
has two forms:
  The exec form, which is the preferred form:
ENTRYPOINT ["executable", "param1", "param2"]
  The shell form:
ENTRYPOINT command param1 param2

  Например, следующий код запускает nginx с содержимым по умолчанию, прослушивая порт 80:

docker run -i -t --rm -p 80:80 nginx
  
  Аргументы командной строки docker run <image>будут добавлены после всех элементов в форме exec ENTRYPOINT и переопределяют все элементы, указанные с помощью CMD. Это позволяет передавать аргументы в точку входа, т. е. аргумент docker run <image> -d передает аргумент -d в точку входа. Вы можете переопределить ENTRYPOINT инструкцию, используя docker run --entrypoint флаг.

  Форма shell не позволяет использовать какие-либо аргументы CMD или аргументы командной строки, но имеет тот недостаток, что your ENTRYPOINT будет запускаться как подкоманда /bin/sh -c, которая не передает сигналы. Это означает, что исполняемый файл не будет принадлежать контейнеру и не будет получать сигналы Unix, поэтому ваш исполняемый файл не получит сообщение from .runENTRYPOINT/bin/sh -cPID 1SIGTERMdocker stop <container>

Только последняя ENTRYPOINT инструкция в файле Dockerfileбудет иметь эффект.

Пример исполнительной формы ENTRYPOINT 
Вы можете использовать форму execENTRYPOINT для установки довольно стабильных команд и аргументов по умолчанию, а затем использовать любую форму CMDдля установки дополнительных значений по умолчанию, которые, скорее всего, будут изменены.

FROM ubuntu
ENTRYPOINT ["top", "-b"]
CMD ["-c"]
Когда вы запустите контейнер, вы увидите, что это topединственный процесс:


 docker run -it --rm --name test  top -H
Для дальнейшего изучения результата вы можете использовать docker exec:


 docker exec -it test ps aux
И вы можете изящно запросить topвыключение, используя docker stop test.

Ниже Dockerfileпоказано использование ENTRYPOINTдля запуска Apache на переднем плане (т. е. как PID 1):


FROM debian:stable
RUN apt-get update && apt-get install -y --force-yes apache2
EXPOSE 80 443
VOLUME ["/var/www", "/var/log/apache2", "/etc/apache2"]
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
Если вам нужно написать начальный сценарий для одного исполняемого файла, вы можете убедиться, что окончательный исполняемый файл получает сигналы Unix, используя команды execи :gosu


#!/usr/bin/env bash
set -e

if [ "$1" = 'postgres' ]; then
    chown -R postgres "$PGDATA"

    if [ -z "$(ls -A "$PGDATA")" ]; then
        gosu postgres initdb
    fi

    exec gosu postgres "$@"
fi

exec "$@"
Наконец, если вам нужно выполнить дополнительную очистку (или связаться с другими контейнерами) при выключении или координировать более одного исполняемого файла, вам может потребоваться убедиться, что сценарий получает сигналы Unix, передает их, а затем ENTRYPOINTвыполняет еще немного работы:


#!/bin/sh
# Note: I've written this using sh so it works in the busybox container too

# USE the trap if you need to also do manual cleanup after the service is stopped,
#     or need to start multiple services in the one container
trap "echo TRAPed signal" HUP INT QUIT TERM

# start service in background here
/usr/sbin/apachectl start

echo "[hit enter key to exit] or run 'docker stop <container>'"
read

# stop service and clean up here
echo "stopping apache"
/usr/sbin/apachectl stop

echo "exited $0"
Если вы запустите этот образ с помощью docker run -it --rm -p 80:80 --name test apache, вы можете затем проверить процессы контейнера с помощью docker exec, или docker top, а затем попросить сценарий остановить Apache:


 docker exec -it test ps aux
 docker top test
 /usr/bin/time docker stop test
Примечание

Вы можете переопределить ENTRYPOINTнастройку с помощью --entrypoint, но это может только установить двоичный файл в exec (no sh -cбудет использоваться).

Примечание

Форма exec анализируется как массив JSON, что означает, что вы должны использовать двойные кавычки (") вокруг слов, а не одинарные кавычки (').

В отличие от формы оболочки, форма exec не вызывает командную оболочку. Это означает, что нормальной обработки оболочки не происходит. Например, ENTRYPOINT [ "echo", "$HOME" ]не будет делать подстановку переменных на $HOME. Если вам нужна обработка оболочки, используйте форму оболочки или запустите оболочку напрямую, например: ENTRYPOINT [ "sh", "-c", "echo $HOME" ]. При использовании формы exec и непосредственном выполнении оболочки, как и в случае с формой оболочки, расширение переменной среды выполняет оболочка, а не docker.

Пример шелл-формы ENTRYPOINT 
Вы можете указать обычную строку для , ENTRYPOINTи она будет выполняться в формате /bin/sh -c. Эта форма будет использовать обработку оболочки для замены переменных среды оболочки и будет игнорировать любые аргументы CMDили docker runаргументы командной строки. Чтобы убедиться, что docker stopлюбой долго работающий исполняемый файл будет ENTRYPOINTправильно сигнализировать, вам нужно не забыть запустить его с помощью exec:


FROM ubuntu
ENTRYPOINT exec top -b
Когда вы запустите этот образ, вы увидите один PID 1процесс:


 docker run -it --rm --name test top
Который выходит чисто на docker stop:


 /usr/bin/time docker stop test
Если вы забыли добавить execв начало вашего ENTRYPOINT:


FROM ubuntu
ENTRYPOINT top -b
CMD -- --ignored-param1
Затем вы можете запустить его (указав имя для следующего шага):


 docker run -it --name test top --ignored-param2
Из вывода видно, topчто указанное ENTRYPOINTне является PID 1.

Если вы затем запустите docker stop test, контейнер не завершится корректно — stopкоманда будет вынуждена отправить SIGKILLпо истечении тайм-аута:


 docker exec -it test ps waux
 /usr/bin/time docker stop test


