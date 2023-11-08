# parse_pass_from_cod
## Утилита для получения паролей от созаднных ВМ

На вход принимается текстовый файл urls.txt:
```
vm-name-01-00.00.00.00 [SRV0001] https://cod-portal-url/uniq_one_time_id
vm-name-02-00.00.00.00 [SRV0002] https://cod-portal-url/uniq_one_time_id
vm-name-03-00.00.00.00 [SRV0003] https://cod-portal-url/uniq_one_time_id
```
на выходе формируется out.csv:
```
hostname;login;password
```

# Инстуркция по использованию
```
git clone https://github.com/sky1su/parse_pass_from_cod.git
cd parse_pass_from_cod
poetry install
poetry shell
python3 main.py 
```

