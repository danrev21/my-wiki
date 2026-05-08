===========================
# CMD
может быть только одна инструкция в Dockerfile. Если вы укажете более одного CMD, то только последний CMD вступит в силу.
  Имеет три формы:
  CMD ["executable","param1","param2"] (exec form, this is the preferred form)
  CMD ["param1","param2"] (as default parameters to ENTRYPOINT)
  CMD command param1 param2 (shell form)
  
  Основная цель CMD - предоставить значения по умолчанию для исполняемого контейнера. Эти значения по умолчанию могут включать исполняемый файл, или не включать исполняемый файл, и в этом случае в ENTRYPOINT также надо указать инструкцию.

  Если CMD используется для предоставления аргументов по умолчанию для ENTRYPOINT инструкции, обе инструкции CMD и ENTRYPOINT должны быть указаны в формате массива JSON.
 
  В отличие от формы shell, форма exec не вызывает командную оболочку. Это означает, что нормальной обработки оболочки не происходит. Например, CMD [ "echo", "$HOME" ] не будет делать подстановку переменных на $HOME. Если вам нужна обработка оболочки, используйте форму shell или запустите оболочку напрямую, например: CMD [ "sh", "-c", "echo $HOME" ]. При использовании формы exec и непосредственном выполнении оболочки, как и в случае с формой оболочки, расширение переменной среды выполняет оболочка, а не docker.

  Если вы хотите, чтобы ваш контейнер каждый раз запускал один и тот же исполняемый файл, вам следует рассмотреть возможность использования ENTRYPOINT в сочетании с CMD.

  Примечание:
  Не путайте RUN с CMD. RUN фактически запускает команду и фиксирует результат; CMD ничего не выполняет во время сборки, но указывает предполагаемую команду для образа.

====================================================================================================
И ENTRYPOINT, и CMD указывают, какой процесс (просто говоря, команда) должен запускаться в контейнере в качестве основного процесса.

Когда Dockerfile содержит несколько директив CMD, важно отметить, что вступят в силу только инструкции из последнего CMD, что позволяет четко и предсказуемо настроить поведение контейнера по умолчанию.

CMD инструкция будет выполнятся по умолчанию, но если при запуске контейнера указать другой аргумент, то он и поступит на вход ENTRYPOINT.
Если формы отличаются:
  ENTRYPOINT ["echo"] - exec
  CMD hello world     - shell
то по умолчанию вместе с аргументом 'hello world' на вход ENTRYPOINT поступит '/bin/sh -c', и в итоге output: 
/bin/sh -c hello world
А при указании аргумента 'hi there' при запуске контейнера ENTRYPOINT примет только указанный аргумент и output: 
hi there

Для обработки переменных - shell либо CMD [ "sh", "-c", "echo $HOME" ]

ENTRYPOINT Инструкция:
Похож на CMD, но основное отличие состоит в том, что он предоставляет исполняемый файл в качестве команды по умолчанию.
В отличие от CMD, команда и ее параметры не игнорируются, когда Docker запускает контейнер с помощью альтернативной команды.
Если файл Dockerfile содержит обе инструкции CMDи ENTRYPOINT, CMDаргументы инструкции добавляются к файлу ENTRYPOINT.

Инструкция CMD:
Используется для предоставления значений по умолчанию для исполняемого контейнера.
Указывает команду и/или параметры по умолчанию, которые будут выполняться при запуске контейнера.
Если a Dockerfile имеет несколько CMD инструкций, вступает в силу только последняя.
Инструкцию CMD можно переопределить во время выполнения, передав аргументы docker run.

Best Practices:
Используйте CMD для установки команды по умолчанию, которую можно легко переопределить.
Используйте ENTRYPOINT для установки основной команды для контейнера. Он часто используется CMD для предоставления аргументов по умолчанию.
Комбинируйте ENTRYPOINT и CMD разумно, чтобы сделать ваш образ более гибким и настраиваемым.
Если вам нужно запустить контейнер как исполняемый файл (например, docker run myimage arg1 arg2), используйте ENTRYPOINT.

# From tasks:
An ENTRYPOINT allows you to configure a container that will run as an executable
The main purpose of a CMD is to provide defaults for an executing container
If you would like your container to run the same executable every time, then you should consider using ENTRYPOINT in combination with CMD
ENTRYPOINT/CMD has 2 forms:
exec form: ["echo", "hello", "world"] - preferred form, but doesn’t support shell env variables
shell form: echo hello world - supports shell env variables
Both ENTRYPOINT and CMD specify what process (simply saying command) should run in the container as a main process.

CMD is an instruction designed for establishing a default command that users can conveniently modify based on their specific needs.
When a Dockerfile contains multiple CMD directives, it’s crucial to note that only the instructions from the last CMD will take effect, allowing for clear and predictable customization of the container’s default behavior.

