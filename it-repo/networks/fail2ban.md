txt
# Полное руководство по установке и настройке Fail2Ban

## Что такое Fail2Ban?

Fail2Ban — это инструмент для защиты сервера от брутфорс-атак. Он анализирует логи сервисов (SSH, Nginx, Apache и др.) и временно блокирует IP-адреса, с которых происходит слишком много неудачных попыток входа или подозрительной активности[](https://tsecurity.de/de/2782528/IT+Programmierung/Using+Fail2Ban+to+Protect+Against+Brute+Force+Attacks/de/201468/Videos/de/21/IT+Server/Unix+Server/)[](https://tsecurity.de/de/2480667/IT+Programmierung/How+to+install+and+configure+Fail2ban+for+protecting+SSH+and+Nginx/de/18/IT+Downloads/de/155807/K%C3%BCnstliche+Intelligenz++Videos+%2F+AI/).

---

## Установка Fail2Ban

### Для Ubuntu/Debian:

bash

sudo apt update
sudo apt upgrade -y
sudo apt install fail2ban -y

После установки сервис запустится автоматически[](https://github.com/aqeelabpro/fail2ban-asterisk-configuration)[](https://help.time4vps.com/en/articles/401845-installing-fail2ban-for-protection-from-brute-force-attacks)[](https://www.scaleway.com/en/docs/tutorials/protect-server-fail2ban/).

### Для CentOS/RHEL:

bash

sudo yum update -y
sudo yum install epel-release -y
sudo yum install fail2ban -y

### Проверка установки:

bash

fail2ban-client --version
sudo systemctl status fail2ban

### Автозапуск:

bash

sudo systemctl enable fail2ban

---

## Конфигурационный файл: jail.local

**Важно:** Никогда не редактируйте `/etc/fail2ban/jail.conf` напрямую — он может быть перезаписан при обновлении. Все изменения вносятся в `jail.local`[](https://github.com/aqeelabpro/fail2ban-asterisk-configuration)[](https://www.scaleway.com/en/docs/tutorials/protect-server-fail2ban/).

Создайте файл:

bash

sudo nano /etc/fail2ban/jail.local

### Готовая конфигурация для большинства сценариев:

ini

[DEFAULT]
# IP-адреса, которые никогда не блокируются (белый список)
# Добавьте свои IP, локальные сети, VPN
ignoreip = 127.0.0.1/8 ::1
           10.0.0.0/8
           172.16.0.0/12
           192.168.0.0/16
# Время блокировки в секундах (1 час = 3600, 1 день = 86400)
bantime = 3600
# Временное окно для подсчёта неудачных попыток (10 минут = 600)
findtime = 600
# Количество неудачных попыток до блокировки
maxretry = 5
# Действие при блокировке (mwl = с email-уведомлением и логами)
action = %(action_mwl)s
# Email для уведомлений (если настроен почтовый сервер)
destemail = admin@example.com
sendername = Fail2Ban
# Тип блокировки (nftables для Ubuntu 24.04+, iptables для старых версий)
banaction = nftables[multiport]
# ============================================
# ЗАЩИТА SSH
# ============================================
[sshd]
enabled = true
port = ssh
logpath = %(sshd_log)s
backend = %(sshd_backend)s
maxretry = 3
bantime = 86400  # 24 часа для SSH
# ============================================
# ЗАЩИТА NGNIX (HTTP-авторизация)
# ============================================
[nginx-http-auth]
enabled = true
port = http,https
logpath = /var/log/nginx/error.log
maxretry = 3
bantime = 3600
# ============================================
# ЗАЩИТА NGNIX (ограничение запросов)
# ============================================
[nginx-limit-req]
enabled = true
port = http,https
logpath = /var/log/nginx/error.log
maxretry = 5
findtime = 60   # 5 попыток за 1 минуту
bantime = 600   # блокировка на 10 минут
# ============================================
# БОРЬБА С ПЛОХИМИ БОТАМИ
# ============================================
[nginx-badbots]
enabled = true
port = http,https
logpath = /var/log/nginx/access.log
findtime = 600
maxretry = 1    # Достаточно одной попытки от бота
bantime = 86400
# ============================================
# ЗАЩИТА WORDPRESS
# ============================================
[wordpress]
enabled = false  # Отключено по умолчанию, включите при необходимости
port = http,https
filter = wordpress
logpath = /var/log/nginx/access.log
maxretry = 3
bantime = 3600
# ============================================
# ЗАЩИТА ASTERISK (VoIP)
# ============================================
[asterisk]
enabled = false
port = 5060,5061
filter = asterisk
logpath = /var/log/asterisk/full
maxretry = 5
bantime = 600
action = iptables-allports[name=ASTERISK, protocol=all]

---

## Применение конфигурации

После редактирования `jail.local` перезагрузите Fail2Ban:

bash

# Полная перезагрузка сервиса
sudo systemctl restart fail2ban
# Или мягкая перезагрузка конфигурации
sudo fail2ban-client reload

---

## Основные команды для управления

bash

# Просмотр статуса всех джейлов
sudo fail2ban-client status
# Просмотр статуса конкретного джейла (например, sshd)
sudo fail2ban-client status sshd
# Ручная блокировка IP
sudo fail2ban-client set sshd banip 192.168.1.100
# Ручная разблокировка IP
sudo fail2ban-client set sshd unbanip 192.168.1.100
# Просмотр логов Fail2Ban
sudo tail -f /var/log/fail2ban.log
# Проверка конфигурации на ошибки
sudo fail2ban-client -d

---

## Настройка уведомлений в Telegram

Для получения мгновенных оповещений о блокировках можно настроить Telegram-бота[](https://github.com/crypto3301/Linux-host-Protection):

### 1. Создайте бота в Telegram через @BotFather

### 2. Получите chat_id:

bash

curl -s "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates" | jq

### 3. Создайте скрипт уведомлений:

bash

sudo mkdir -p /etc/fail2ban/telegram
sudo tee /etc/fail2ban/telegram/notify.sh <<'EOF'
#!/bin/bash
TELEGRAM_TOKEN="YOUR_BOT_TOKEN"
CHAT_ID="YOUR_CHAT_ID"
BAN_ACTION="$1"
IP="$2"
if [ "$BAN_ACTION" == "ban" ]; then
    MESSAGE="🚫 IP $IP был заблокирован Fail2Ban"
elif [ "$BAN_ACTION" == "unban" ]; then
    MESSAGE="✅ IP $IP был разблокирован"
else
    exit 0
fi
curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage" \
    -d chat_id="${CHAT_ID}" \
    -d text="${MESSAGE}" > /dev/null
EOF
sudo chmod +x /etc/fail2ban/telegram/notify.sh

### 4. Настройте действие в Fail2Ban:

bash

sudo tee /etc/fail2ban/action.d/telegram.conf <<'EOF'
[Definition]
actionban = /etc/fail2ban/telegram/notify.sh ban <ip>
actionunban = /etc/fail2ban/telegram/notify.sh unban <ip>
EOF

### 5. Добавьте в `jail.local`:

ini

[sshd]
action = iptables
         telegram

---

## Интеграция с IP2Location

IP2Location — это сервис, который позволяет определить географическое местоположение IP-адреса (страну, регион, город). Это полезно для анализа атакующих[](https://socket.dev/go/package/github.com/rdybing/iplocate?version=v0.0.0-20191031170346-57b6dd05d5b0)[](https://github.com/rdybing/iplocate).

### Варианты использования IP2Location с Fail2Ban:

#### 1. Анализ логов (инструмент iplocate)

Существует инструмент `iplocate`, который сканирует логи Fail2Ban и определяет географию атакующих IP[](https://github.com/rdybing/iplocate):

bash

# Установка Go (если не установлен)
sudo apt install golang-go -y
# Клонирование и сборка iplocate
git clone https://github.com/rDybing/iplocate.git
cd iplocate
go build iplocate.go
# Запуск (требует sudo)
sudo ./iplocate

Этот инструмент покажет:

- Страны, из которых приходят атаки
    
- Последние заблокированные IP с их геолокацией
    

#### 2. API IP2Location для автоматической блокировки по странам

Вы можете настроить Fail2Ban для автоматической блокировки IP из нежелательных стран. Пример скрипта:

bash

#!/bin/bash
# /usr/local/bin/check_ip_country.sh
IP="$1"
API_KEY="YOUR_IP2LOCATION_API_KEY"
# Запрос к API IP2Location
COUNTRY=$(curl -s "https://api.ip2location.com/v2/?ip=${IP}&key=${API_KEY}&package=WS3" | jq -r '.country_code')
# Блокировка IP из России, Китая, Северной Кореи
if [[ "$COUNTRY" == "RU" || "$COUNTRY" == "CN" || "$COUNTRY" == "KP" ]]; then
    /usr/bin/fail2ban-client set sshd banip ${IP}
    echo "$(date): Блокирован IP ${IP} из страны ${COUNTRY}" >> /var/log/country_blocks.log
fi

**Важно:** IP2Location предоставляет:

- **Бесплатный демо-ключ** — ограничение 20 запросов в день[](https://socket.dev/go/package/github.com/rdybing/iplocate?version=v0.0.0-20191031170346-57b6dd05d5b0)[](https://github.com/rdybing/iplocate)
    
- **Платные подписки** — для большого количества запросов
    

Подробная документация API: [https://www.ip2location.com/web-service/ip2location](https://www.ip2location.com/web-service/ip2location)

---

## Тестирование работы Fail2Ban

### 1. Проверка защиты SSH:

С другого компьютера выполните несколько неудачных попыток входа:

bash

ssh nonexistent@your-server-ip
# Повторите 3-5 раз

### 2. Проверьте статус блокировки:

bash

sudo fail2ban-client status sshd

Вы должны увидеть заблокированный IP в списке `Banned IP list`.

### 3. Разблокировка тестового IP:

bash

sudo fail2ban-client unban <IP_адрес>

---

## Дополнительные файлы конфигурации

Для лучшей организации можно использовать каталог `/etc/fail2ban/jail.d/`:

bash

# Создание отдельного конфига для SSH
sudo nano /etc/fail2ban/jail.d/sshd.local

Содержимое:

ini

[sshd]
enabled = true
port = 2222  # Если SSH на нестандартном порту
maxretry = 3
bantime = 86400

Этот подход удобен для разделения конфигураций разных сервисов[](https://github.com/fail2ban/fail2ban/issues/3877).

---

## Типичные проблемы и их решение

|Проблема|Решение|
|---|---|
|SSH на нестандартном порту|Укажите порт в конфиге: `port = 2222`|
|Не работают email-уведомления|Настройте Postfix или используйте Telegram|
|Слишком агрессивная блокировка|Увеличьте `maxretry` или уменьшите `findtime`|
|Не блокирует нужный сервис|Проверьте путь к логам в `logpath`|

После настройки Fail2Ban ваш сервер будет значительно лучше защищён от брутфорс-атак и автоматических сканеров уязвимостей[](https://tsecurity.de/de/2480667/IT+Programmierung/How+to+install+and+configure+Fail2ban+for+protecting+SSH+and+Nginx/de/18/IT+Downloads/de/155807/K%C3%BCnstliche+Intelligenz++Videos+%2F+AI/).