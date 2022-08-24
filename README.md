<h1>Firefly Pytest API Automation Project</h1>
This project is prepared for the Firefly recruitment process.
<h2>Tool stack</h2>

* Python
* Pytest
* Requests
* Faker

<h3>Requirements</h3>

* Python 3 or higher must be installed (Version 3 preferred) <a href="https://www.python.org/downloads/"> Python
  download page
* Pytest must be installed <a href="https://pypi.org/project/pytest/">Pytest download</a>,

<h3>Project Tree</h3>

```
.
├── README.md
├── config
│   ├── base_config.py
│   └── service
│       └── service_config.py
├── conftest.py
├── model
│   └── product.py
├── output
│   ├── assets
│   │   └── style.css
│   └── report.html
├── pytest.ini
├── requirements.txt
├── service
│   ├── carts
│   │   └── carts_service.py
│   └── products
│       └── products_service.py
├── tests
│   ├── test_customer.py
│   └── test_products.py
└── utils
    ├── api
    │   ├── api_commons.py
    │   └── api_utils.py
    ├── assertion
    │   └── assertion.py
    └── data
        └── data_generator.py

```

<h4>Config Folder</h4>
Used for environment variables. There are usually *_config.py files.

<h4>Model Folder</h4>
This will be used for variables implementation in the project. Variables should be defined in the class.

<h4>Service Folder</h4>
Requests to the service are managed here, methods are usually created using service utils.

<h4>Tests folder</h4>
Test files, that is, test cases in Pytest format will be located under this folder.

<h4>Utils Folder</h4>
The utils class and methods of the project will be defined in this folder.

<h4>conftest.py</h4>
File where decorators such as global fixtures are defined for pytest.
<h4>pytest.ini</h4>
Required file for pytest configuration.

<h4>requirements.txt</h4>
The file required for the installation of project necessary libraries.

<h4>output/*</h4>
Generates pytest-html reports after each execution.

<h2>Naming Convention</h2>

Conditions are requested when naming. Names should be short and meaningful.

``directory names = my_directory (snake case)``

``variable name = my_variable (snake case)``

``method name = my_method (snake case)``

``class name = MyClass (Pascal case)``

``tag name = @MyTag (Pascal case)``



<h2> Test Run </h2>

Python CLI command to run tests.

execution tests :

``
python3 -m pytest
``

execution tests via specific test file

``
python3 -m pytest 'file path'
``

execution tests via marks

@pytest.mark.smoke should be added in the test case

``
pytest -v -m smoke
``

execution tests via parallel

``
python3 -m pytest -n 4
``

