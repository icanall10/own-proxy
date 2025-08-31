#!/bin/bash

# Установка pproxy, если не установлен
if ! command -v pproxy &> /dev/null; then
    echo "Устанавливаем pproxy..."
    pip3 install pproxy
fi

# Запуск SOCKS5 прокси на порту 8080
echo "Запускаем SOCKS5 прокси на :8080..."
pproxy -l socks5://:8080 -v