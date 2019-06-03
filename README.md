# code2json
Convert code to JSON format. Useful when creating VSCode snippets.

# Emvironment
Python3.x

# How to use
## Example
1.) You create `input.py` which you want to convert to JSON format strings for making VSCode snippets.

```python
class Hoge():
    def __init__(self, V):
        """ hogehoge
        This is hoge class.
        """
        pass

    def hoge(self):
        """ hoge method """
        pass
```

2.) Run `main.py`

```sh
> python main.py input.py
```

3.) Generate `output.json`.

```json
"class Hoge():",
"    def __init__(self, V):",
"        \"\"\" hogehoge",
"        This is hoge class.",
"        \"\"\"",
"        pass",
"",
"    def hoge(self):",
"        \"\"\" hoge method \"\"\"",
"        pass",
```

4.) Copy and paste them to your VSCode snippet file.

```json
    "Hoge": {
        "prefix": ["hoge"],
        "body":[
            "class Hoge():",
            "    def __init__(self, V):",
            "        \"\"\" hogehoge",
            "        This is hoge class.",
            "        \"\"\"",
            "        pass",
            "",
            "    def hoge(self):",
            "        \"\"\" hoge method \"\"\"",
            "        pass",
        ]
    },
```

## Option Arguments
### -tab2sp n
It can convert indents of tabs to n spaces.

input.py(tab indents):
```python
class Hoge():
	def __init__(self, V):
		""" hogehoge
		This is hoge class.
		"""
		pass

	def hoge(self):
		""" hoge method """
		pass
```

Run like following:
```sh
> python main.py input.py -tab2sp 2
```

output.json:
```json
"class Hoge():",
"  def __init__(self, V):",
"    \"\"\" hogehoge",
"    This is hoge class.",
"    \"\"\"",
"    pass",
"",
"  def hoge(self):",
"    \"\"\" hoge method \"\"\"",
"    pass",
```

### -sp2tab n
It can convert indents of n spaces to "\t" strings.

input.py(indents of 4 spaces)
```python
class Hoge():
    def __init__(self, V):
        """ hogehoge
        This is hoge class.
        """
        pass

    def hoge(self):
        """ hoge method """
        pass
```

Run like following:
```sh
> python main.py input.py -sp2tab 4
```

output.json:
```json
"class Hoge():",
"\tdef __init__(self, V):",
"\t\t\"\"\" hogehoge",
"\t\tThis is hoge class.",
"\t\t\"\"\"",
"\t\tpass",
"",
"\tdef hoge(self):",
"\t\t\"\"\" hoge method \"\"\"",
"\t\tpass",
```

# License
MIT
