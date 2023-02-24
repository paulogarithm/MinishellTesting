# MinishellTesting

## How to get it ?
Clone this repo in your minishell folder by using this command :<br/>
`git clone git@github.com:paulogarithm/MinishellTesting.git`

You should now have something like this
```
[minishell] $ ls
lib  Makefile  src

[minishell] $ git clone git@github.com:paulogarithm/MinishellTesting.git
...

[minishell] $ ls
lib  Makefile  MinishellTesting  src
```

## How does it works ?
To run the tests, simply do `./MinishellTesting/run`.

To made your own test, you can configure the **commands.txt**'s file in the **config** folder.<br/>
`./MinishellTesting/config/commands.txt`

## How can i code new tests

### Basics
Basically, your **commands.txt**'s file should look like this :
```
:: This is a comment

>>> Cathegory

> Test 1
Command

> Test 2
Command

>>> End
```

The way the line will be executed is as follow :<br/>
`Command | Terminal`

Terminal is replaced by `tcsh` and `./mysh`.<br/>
Then the result of both function are compared.

After all the tests are passed, you get a resume of all cathegories and an overall one.
```
75%  [===============>    ] Cathegory 1
25%  [=====>              ] Cathegory 2

50%  [==========>         ] Overall
```


### Sub-commands
You can also add sub-commands to your tests.


Basically, it will execute this command after the pipe but before the terminal command :<br/>
`Command | Subcommand Terminal`

To add them in your test, you can use the $ sign followed by a space like this in your **commands.txt**'s file.
```
> Test
$ Subcommand
Command
```
