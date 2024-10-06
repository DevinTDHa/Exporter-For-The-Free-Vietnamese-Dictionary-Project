# Exporter For The Free Vietnamese Dictionary Project

This repository contains scripts to convert the dictionary files from [The Free Vietnamese Dictionary Project](https://www.informatik.uni-leipzig.de/~duc/Dict/install.html).
The script `convert.py` will convert the files to jsonl.

Currently only Vietnamese-English and vice versa dictionaries are supported (and tested, might work for the others).

## Usage

1. First, download the zip files from the [Manual Installation](https://www.informatik.uni-leipzig.de/~duc/Dict/install.html#manual).
Each zip file will contain a `*.dz` file. Extract this file to the [data/](data/) folder.
2. Run the `convert.py` script. This will convert each `*.dz` file in the data folder.

The resulting jsonl files will also be located in the data folder.

## Notes about the raw data

Special characters at the start of the line indicate the field for a dictionary entry. Namely:

| Character | Description                                             |
|-----------|---------------------------------------------------------|
| `@`       | Current Word of the Dict                                |
| `*`       | Part Of Speech (POS) Tag                                      |
| `#Syn`    | Synonyms                                                |
| `-`       | Indicator for text of the last field/Translation for current POS tag                    |
| `=`       | Example, split with `+` between text and translation    |
| `!`       | Idioms                                                  |

Examples:

```text
@cam
* noun
- Orange
=cam thuộc giống cam quít+the orange belongs to the citrus genus
=rượu cam+orange-flavoured liqueur
-Children's disease due to malnutrition
#Syn
- quả cam
-Cam
=trục cam+a cam-shaft
- Xem máu cam
* verb
- To content oneself with, to resign oneself to
=không cam làm nô lệ+not to resign oneself to servitude
=có nhiều nhặn gì cho cam
```

| Field       | Content                                             |
|-------------|-----------------------------------------------------|
| `@` Word         | cam                                                 |
| `*` POS  | noun                                              |
| `-` Translation         | Orange                                              |
| `=` Example         | cam thuộc giống cam quít (the orange belongs to the citrus genus) |
| `=` Example         | rượu cam (orange-flavoured liqueur)                 |
| `-` TODO?         | Children's disease due to malnutrition              |
| `#Syn`      | Synonyms                                            |
| `-` Synonym         | quả cam                                              |
| `-` Synonym        | Cam                                                 |
| `=` Example         | trục cam (a cam-shaft)                              |
| `-` See Also         | Xem máu cam                                         |
| `*` POS  | Verb       |
| `-` Translation         | To content oneself with, to resign oneself to       |
| `=` Example         | không cam làm nô lệ (not to resign oneself to servitude) |
| `=` Example         | có nhiều nhặn gì cho cam                            |

```text
@chuột
* noun
- Rat, mouse
=ướt như chuột lột+drenched to the bone, like a drowned rat
!chuột chạy cùng sào
-to be at the end of one's tether
!cháy nhà ra mặt chuột
-xem cháy
!chuột sa chĩnh gạo
-xem chĩnh
```

| Field       | Content                                             |
|-------------|-----------------------------------------------------|
| `@` Word         | chuột                                                |
| `*` POS  | noun                                              |
| `-` Translation         | Rat, mouse                                              |
| `=` Example         | ướt như chuột lột (drenched to the bone, like a drowned rat) |
| `!` Idiom         | chuột chạy cùng sào (to be at the end of one's tether) |
| `!` Idiom         | cháy nhà ra mặt chuột (xem cháy) |
| `!` Idiom         | chuột sa chĩnh gạo (xem chĩnh) |
