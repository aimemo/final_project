[![Python package](https://github.com/aimemo/final_project/actions/workflows/python-publish.yml/badge.svg)](https://github.com/aimemo/final_project/actions/workflows/python-publish.yml)

# Final UI-test Student's Project
#### Innopolis University 

Final Student's Project for the QA Automation Python Course

Purpose of Project:
- Auto-testing of UI the app https://berpress.github.io/online-grocery-store/ using framework **Pytest**

Tasks:
- writing autotests:
  - searching of products (positive and negative);
  - adding products in the basket;
  - in the basket: adding and removing product, deleting product, buying;
- configuring and running test in CI;
- writing test cases;
- receiving reports on tests results.


### Testing app
```
https://berpress.github.io/online-grocery-store/
```

### Use python 3.8 +

Create and activate virtual environments

#### For Mac OS
```
python3 -m venv env

source env/bin/activate
```

#### For Windows
```
python3 -m venv env

env\Scripts\activate
```

#### Run in terminal for install used packages
```
pip install -r requirements.txt
```

### Pre-commit
https://pre-commit.com
```
pre-commit run --all-files
```

### CI - GitHub Actions
[python-publish.yml](https://github.com/aimemo/final_project/blob/master/.github/workflows/python-publish.yml)

[test.py](https://github.com/aimemo/final_project/blob/master/test.py)


### Report - pytest-html
For testing with getting report run in terminal
```
pytest --html=report.html --self-contained-html
```
[Open the actual report (Ctrl+leftclick for opening in other page)](https://htmlpreview.github.io/?https://github.com/aimemo/final_project/blob/master/report.html)
