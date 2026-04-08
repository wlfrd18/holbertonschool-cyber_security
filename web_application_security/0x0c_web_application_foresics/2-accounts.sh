#!/bin/bash
tail -1000 $1 | awk '
/Failed password for/ {
	for (i = 1; i <= NF; i++)
	{
		if ($i == "for")
		{
			if ($(i + 1) == "invalid")
				user = $(i + 3)
			else
				user = $(i + 1)
			failed[user]++
		}
	}
}
/Accepted password for/ || /Accepted publickey for/ {
	for (i = 1; i <= NF; i++)
	{
		if ($i == "for")
		{
			user = $(i + 1)
			success[user]++
		}
	}
}
END {
	for (user in success)
	{
		if (failed[user] > 0)
			print user
	}
}'
