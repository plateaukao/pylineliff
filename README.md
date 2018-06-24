## pylineliff ##

LIFF(LINE Front-end Framework) command line tool, plus a server api wrapper in python
https://developers.line.me/en/docs/liff/overview/

## Usage ##

#### init ####
to save access token locally for later use
```
$ pylineliff init {LINE_LIFF_ACCESS_TOKEN}
```

#### list ####
list all registered LINE LIFF apps
```
$ pytlineliff list
```


#### add ####
register a new LINE LIFF app 

(type can be: full, tall, compact)
```
$ pytlineliff add <url> <type>
```

#### delete ####
delete an existing LINE LIFF app
```
$ pylineliff delete <liff-id>
```

#### update ####
```
$ pylineliff update <liff-id> <json_string>
```


