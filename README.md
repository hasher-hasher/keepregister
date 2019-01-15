### Keep Register

A tiny terminal app that helps you to keep track of your development journey with date and hour of each entry.

### Instasllation

For now the only place where the app is available is on pip. The plan is to make it available on apt and other package managers.

```bash
  $ pip install keepregister
```

### Usage

First argument is the file name, which if not exists will be created. The second argument is the message to register, between quotes.

```bash
$ keepregister example.txt "Today i had some problem with the database and i'm waiting the DB manager to fix this."
```

and the output will be ...

> 14/01/2019 08:00 - Today i had some problem with the database and i'm waiting the DB manager to fix this.

Simple as that!!!
