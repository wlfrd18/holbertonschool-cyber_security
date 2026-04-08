#!/bin/bash
(
grep "useradd" auth.log | awk -F'name=' '{print $2}' | awk -F',' '{print $1}' | grep '^[A-Z]' | sort | uniq
grep "useradd" auth.log | awk -F'name=' '{print $2}' | awk -F',' '{print $1}' | grep '^[a-z]' | sort | uniq
) | paste -sd ","
