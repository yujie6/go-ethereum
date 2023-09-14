## Go Ethereum Dump
Experiment input generation for [The Locality of Memory Checking](https://eprint.iacr.org/2023/1358).
The code is modified from the official go-ethereum repository.

## Instructions
```
make geth
./build/bin/geth --datadir ./dumpdir import ~/Downloads/block00 >> eth00.txt
./build/bin/geth --datadir ./dumpdir import ~/Downloads/block01 >> eth01.txt
./build/bin/geth --datadir ./dumpdir import ~/Downloads/block02 >> eth02.txt
./build/bin/geth --datadir ./dumpdir import ~/Downloads/block03 >> eth03.txt
```
The output file has the following format that indicates the read/write operations of a certain block id.
```
new  1
read
0x05a56E2D52c817161883f50c441c3228CFe54d9f
read
0x05a56E2D52c817161883f50c441c3228CFe54d9f
write
0x05a56E2D52c817161883f50c441c3228CFe54d9f
[248 76 128 136 69 99 145 130 68 244 0 0 160 86 232 31 23 27 204 85 166 255 131 69 230 146 192 248 110 91 72 224 27 153 108 173 192 1 98 47 181 227 99 180 33 160 197 210 70 1 134 247 35 60 146 126 125 178 220 199 3 192 229 0 182 83 202 130 39 59 123 250 216 4 93 133 164 112] <nil>
```
