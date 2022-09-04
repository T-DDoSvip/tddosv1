#!/usr/bin/bash
# This code write by T-DDoS
# T-DDoS v1
if [[ "$(id -u)" -ne 0 ]]; 
then
  echo "
Please, Run This programm as Root!
"
  exit 1
fi
function main() {
        printf '\033]2;Installing\a'
	clear
	echo ""
	echo "Installing... "
	chmod +x DDos.py
	sleep 1
echo"╔╦╗ ╔╦╗╔╦╗┌─┐╔═╗"
echo" ║───║║ ║║│ │╚═╗"
echo" ╩  ═╩╝═╩╝└─┘╚═╝"
	echo ""
        echo "   Version: 1.0"
        echo ""
	sleep 1
	apt install python
        apt install python3
	apt install python3-pip
	pip install --upgrade pip3
	chmod +x uninstall.sh
	echo "
Đã Setup Xong Chúc Bạn Chạy Mượt Nhé<3...!

"
	echo ""
	echo "Sử dụng: python t-ddosv1.py Để Chạy Tool"
	echo ""
	exit 1
}
main
