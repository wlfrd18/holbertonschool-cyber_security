#!/bin/bash
ps -u "$1" --no-headers | grep -v ' 0 0 '
