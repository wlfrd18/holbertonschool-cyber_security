#!/bin/bash
ps aux | grep "^$1" | grep -v "USER" | awk '$5 > 0' | awk '$6 > 0'
