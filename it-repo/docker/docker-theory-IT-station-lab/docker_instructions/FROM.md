===========================
# FROM
инициализирует новый этап сборки и устанавливает базовый образ для последующих инструкций.
 1. ARG единственная инструкция, которая может предшествовать FROM в Dockerfile. См . Как взаимодействуют ARG и FROM .
 2. FROM может появляться несколько раз в одном Dockerfile для создания нескольких образов или использования одного этапа сборки в качестве зависимости для другого. Simply make a note of the last image ID output by the commit before each new FROM instruction. Each FROM instruction clears any state created by previous instructions.
 3. При желании можно дать имя новому этапу сборки, добавив AS name в FROM инструкцию. Имя можно использовать в последующих FROM и COPY --from=<name> инструкциях для обращения к образу, созданному на этом этапе.
 4. Значения tag или digest являются необязательными. Если вы опустите любой из них, билдер примет latest тег по умолчанию. Билдер возвращает ошибку, если не может найти tag значение.

  FROM инструкции поддерживают переменные, объявленные любыми ARG инструкциями, предшествующими первой FROM.
  
ARG  CODE_VERSION=latest
FROM base:${CODE_VERSION}
CMD  /code/run-app

FROM extras:${CODE_VERSION}
CMD  /code/run-extras
 Объявленный ARG перед FROM находится за пределами стадии сборки, поэтому его нельзя использовать ни в какой инструкции после FROM. Чтобы использовать значение по умолчанию объявленного ARG перед первым FROM, используйте ARG инструкции без значения внутри этапа сборки:

ARG VERSION=latest
FROM busybox:$VERSION
ARG VERSION
RUN echo $VERSION > image_version

