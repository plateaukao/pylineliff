## pylineliff ##

LIFF(LINE Front-end Framework) command line tool, plus a server api wrapper in python
https://developers.line.me/en/docs/liff/overview/

## Usage ##

#### init ####
to save access token locally for later use
```
$ liff.py init {LINE_LIFF_ACCESS_TOKEN}
```

#### list ####
list all registered LINE LIFF apps
```
$ liff.py list
```


#### add ####
register a new LINE LIFF app 

(type can be: full, tall, compact)
```
$ liff.py  add <url> <type>
```

#### delete ####
delete an existing LINE LIFF app
```
$ liff.py delete <liff-id>
```

#### update ####
```
$ liff.py update <liff-id> <json_string>
```


