# pwd-generator

<br/>

You can **use different types of generators** and **define the length** of your password for each of them:
- Uppercase-only
- Lowercase-only
- Letter-only
- Digit-only
- Special character only
- Custom : select options you want or not for you password

<br/>

## Installation
```commandline
pip install git+ssh://git@github.com/Zepolimer/pwd-generator.git@main#pwd-generator
```

```commandline
rm build/ pwd_generator.egg-info dist -Rf
python3 setup.py bdist_wheel
pip3 install -I dist/pwd_generator-*-py3-none-any.whl
```

## Unittests
```commandline
python3 -m unittest
```