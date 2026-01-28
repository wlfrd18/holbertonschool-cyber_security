for i in {1..10}; do
  curl -s -I http://web0x01.hbtn/a1/hijack_session/ | awk '/hijack_session/ {print $2}';
done 
