#!/bin/bash
tail -1000 auth.log | grep "Accepted password" | awk '{print $9}' | sort -u
