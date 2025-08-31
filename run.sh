#!/bin/bash

git reset --hard && git pull

if ! command -v brew &> /dev/null; then
    echo "Устанавливаем Homebrew"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    if [ -d /opt/homebrew/bin ]; then
        eval "$(/opt/homebrew/bin/brew shellenv)"
    elif [ -d /usr/local/bin ]; then
        eval "$(/usr/local/bin/brew shellenv)"
    fi
fi

if ! command -v git &> /dev/null; then
    echo "Устанавливаем git"
    brew install git
fi

if ! command -v python3 &> /dev/null; then
    echo "Устанавливаем python3"
    brew install python
fi

if ! command -v pproxy &> /dev/null; then
    echo "Устанавливаем pproxy"
    pip3 install pproxy
fi


CONFIG_FILE="./.config"

# Если конфиг существует, считываем данные
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
fi



while [ -z "$PORT" ]; do
    echo
    read -p "Введите порт для прокси [по-умолчанию 8080]: " PORT
    PORT=${PORT:-8080}
done

while [ -z "$USERNAME" ]; do
    echo
    read -p "Введите логин для прокси: " USERNAME
done

while [ -z "$PASSWORD" ]; do
    echo
    read -p "Введите пароль для прокси: " PASSWORD
    echo
done

# Сохраняем данные в конфиг
cat > "$CONFIG_FILE" <<EOL
PORT="$PORT"
USERNAME="$USERNAME"
PASSWORD="$PASSWORD"
EOL


IP=$(curl -s https://ifconfig.me)

echo ""
echo -e "\033[90mip:\033[0m \033[32m$IP\033[0m"
echo -e "\033[90mport:\033[0m \033[32m$PORT\033[0m"
echo -e "\033[90musername:\033[0m \033[32m$USERNAME\033[0m"
echo -e "\033[90mpassword:\033[0m \033[32m$PASSWORD\033[0m"
echo ""

echo "SOCKS5 готов принимать подключения. Не закрывайте терминал"
"$HOME/Library/Python/3.9/bin/pproxy" -l socks5://127.0.0.1:8080#$USERNAME:$PASSWORD -v



