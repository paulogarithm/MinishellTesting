# MinishellTesting

## How to get it ?
Clone this repo in your minishell folder by using this command :
`git clone git@github.com:paulogarithm/MinishellTesting.git`

You should now have something like this
```
minishell/ $> ls
lib  Makefile  MinishellTesting  src
```

## How does it works ?
To run the tests, simply do `./MinishellTesting/run`.

## How can i code new tests

### Basics
Basically, your __commands.txt__'s file should look like this :
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
`Command | tcsh`<br/>
`Command | ./mysh`

Then the result of both function are compared.

After all the tests in a cathegory are passed, the result is showed with a progress bar.
```
75%  [===============>    ] Cathegory
```


### Sub-commands
You can also add 
