#!/usr/bin/python3
for idx in range(ord('a'), ord('z') +1):
    if idx == 101 or idx == 113:
        continue
    else:
     print(chr(idx), end="")
