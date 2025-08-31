#!/bin/bash

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

git reset --hard && git pull

if ! command -v python3 &> /dev/null; then
    echo "Устанавливаем python3"
    brew install python
fi

if ! command -v pproxy &> /dev/null; then
    echo "Устанавливаем pproxy"
    pip3 install pproxy
fi

echo "Запускаем SOCKS5 прокси"
pproxy -l socks5://USER:PASS@:8080 -v

