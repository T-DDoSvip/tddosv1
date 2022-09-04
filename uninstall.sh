#!/usr/bin/env bash
# This code write by T-DDoS 
# T-DDoS v1
if [[ "$(id -u)" -ne 0 ]]; then
  echo "
Please Run This Programm as Root!
"
  exit 1
fi
main() {
      clear
      echo "Đang Gỡ Cài Đặt..."
      sleep 2
      cd .. && rm -r DDos-Attack
      echo ""
      echo "Xong...!"
      echo "
Tạm Biệt :(
"
      exit 1
}
main
