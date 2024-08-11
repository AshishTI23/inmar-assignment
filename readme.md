# Meta-Data Management API

## Overview

This Django project provides a REST API for managing meta-data related to locations, departments, categories, subcategories, and Stock Keeping Units (SKUs). The API allows for the creation, retrieval, updating, and deletion of these entities. The project is structured around various models representing the hierarchical relationship between locations, departments, categories, and subcategories.

## Features

- **CRUD Operations**: Supports Create, Fetch, Update, and Delete operations for locations, departments, categories, subcategories, and SKUs.
- **UUID-based Identification**: Each entity is identified by a universally unique identifier (UUID).
- **Hierarchical Data Representation**: The API supports nested resource queries, such as retrieving all categories within a department at a specific location.

## Setup Instructions

### Prerequisites

- Python 3.11.6+
- Django 5.0+
- PostgreSQL (or any preferred relational database)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AshishTI23/inmar-assignment.git
    cd metadata-management-api
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    - Create a PostgreSQL database and update the `DATABASES` settings in `settings.py` accordingly.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

    - Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Locations
- **GET** `/api/v1/locations/` - List all locations.
- **POST** `/api/v1/locations/` - Create a new location.
- **PUT, DELETE** `/api/v1/locations/<uuid:location_id>/` - Retrieve, update, or delete a specific location.

### Departments
- **GET** `/api/v1/locations/<uuid:location_id>/departments/` - List all departments at a specific location.
- **POST** `/api/v1/locations/<uuid:location_id>/departments/` - Create a new Department.
- **PUT, DELETE** `/api/v1/departments/<uuid:department_id>/` - Retrieve, update, or delete a specific department.

### Categories
- **GET** `/api/v1/locations/<uuid:location_id>/departments/<uuid:department_id>/categories/` - List all categories within a specific department at a given location.
- **POST** `/api/v1/locations/<uuid:location_id>/departments/<uuid:department_id>/categories/` - Create a new Category.
- **PUT, DELETE** `/api/v1/categories/<uuid:category_id>/` - Retrieve, update, or delete a specific category.

### Subcategories
- **GET** `/api/v1/locations/<uuid:location_id>/departments/<uuid:department_id>/categories/<uuid:category_id>/sub_categories/` - List all subcategories within a specific category in a given department and location.
- **POST** `/api/v1/locations/<uuid:location_id>/departments/<uuid:department_id>/categories/<uuid:category_id>/sub_categories/` - Create a new SubCategory.
- **PUT, DELETE** `/api/v1/subcategories/<uuid:subcategory_id>/` - Retrieve, update, or delete a specific subcategory.

### SKUs
- **GET** `/api/v1/skus/` - List all SKUs.
<!-- - **POST** `/api/v1/skus/` - Create a new SKU. -->

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.


