#!/bin/bash
grep "iptables" $1 | grep " -A " | wc -l
