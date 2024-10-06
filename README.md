# Todo List Django Application

This project serves as a portfolio piece to demonstrate my Python programming skills.

This project primarily concentrates on Python and Django skills, with less emphasis on HTML/CSS. I see opportunities for enhancing the HTML/CSS elements, which I may explore in the future.

This project utilizes only fundamental Django concepts, with the possibility of incorporating more advanced features in the future.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Roadmap](#roadmap)

## Overview

A Todo list web application implemented using Python and the Django Framework.

## Features

- Todo list items (name, description, due date, done status)
- Supported Storage: Any database supported by the Django Framework

## Requirements

- Python, minimum version of `3.9`
- Django, minimum version of `4.2`

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/cthealljr/django-todo-list.git
   cd django-todo-list
   ```
2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install project:
    ```bash
    pip install .
    ```

## Usage

In your Django project:

1. Add app to Django settings `INSTALLED_APPS`:
    ```python
    # other settings
    INSTALLED_APPS = [
        "todo.apps.TodoConfig",
        # other apps
    ]
    # other settings
    ```

2. Add app urls to project urls:
    ```python
    from todo import urls as todo_urls

    urlpatterns = [
        # other urls
        path('todo/', include(todo_urls)), # this is just an example, you can use whatever path you want, even "/" if this is the only app.
        # other urls
    ]
    ```

3. Run database migrations:
    ```bash
    # Within the project directory containing the Django manage.py script
    python manage.py migrate
    ```

4. For local testing:
    ```bash
    # Within the project directory containing the Django manage.py script
    python manage.py runserver
    ```

### Templates

The templates included with the Todo App expect to extend a base template called `base.html`, a simple one is provided in this project at `test_site/templates/base.html` and a stylesheet is also provided at `test_site/static/css/index.css`, to use them add `test_site/templates` to the `TEMPLATES['DIRS']` setting and `test_site/static` to `STATICFILES_DIRS` in your Django project settings file, example:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # add path to test_site/templates here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATICFILES_DIRS = [
    # add path to test_site/static here
]
```

## License

This project is licensed under the Apache License Version 2.0.

## Roadmap

- Add support for displaying due dates in any timezone requested by the user
- Add proper testing of views/models
