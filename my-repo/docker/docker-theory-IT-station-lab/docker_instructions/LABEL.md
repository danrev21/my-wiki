===========================
# LABEL
добавляет метаданные к образу. Это пара ключ-значение:

LABEL "com.example.vendor"="ACME Incorporated"
LABEL com.example.label-with-value="foo"
LABEL version="1.0"
LABEL description="This text illustrates \
that label-values can span multiple lines."
LABEL multi.label1="value1" multi.label2="value2" other="value3"
LABEL multi.label1="value1" \
      multi.label2="value2" \
      other="value3"

  Если метка уже существует, но с другим значением, последнее примененное значение переопределяет любое ранее установленное значение.
  Чтобы просмотреть метки изображения, используйте docker image inspect команду. Вы можете использовать --format опцию, чтобы показать только метки;

  docker image inspect --format='{{json .Config.Labels}}' myimage

{
  "com.example.vendor": "ACME Incorporated",
  "com.example.label-with-value": "foo",
  "version": "1.0",
  "description": "This text illustrates that label-values can span multiple lines.",
  "multi.label1": "value1",
  "multi.label2": "value2",
  "other": "value3"
}
