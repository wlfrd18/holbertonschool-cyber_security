#!/bin/bash
grep "iptables" auth.log | grep " -A " | wc -l
