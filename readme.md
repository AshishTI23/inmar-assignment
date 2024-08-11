# Stock Keeping Unit Management API

## Overview

This Django project provides a REST API for managing meta-data related to locations, departments, categories, subcategories, and Stock Keeping Units (SKUs). The API allows for the creation, retrieval, updating, and deletion of these entities. The project is structured around various models representing the hierarchical relationship between locations, departments, categories, and subcategories.

## Features

- **CRUD Operations**: Supports Create, Fetch, Update, and Delete operations for locations, departments, categories, subcategories, and SKUs.
- [**UUID-based Identification**](https://github.com/AshishTI23/inmar-assignment/blob/main/base/models.py): Each entity is identified by a universally unique identifier (UUID).
- **Hierarchical Data Representation**: The API supports nested resource queries, such as retrieving all categories within a department at a specific location.
- [**Seed Data**](https://github.com/AshishTI23/inmar-assignment/blob/main/sku/management/commands/seed.py): This functionality is achieved by implementing a management command that accepts arguments to specify the type of operations. The command handles both seeding and deletion processes in a structured manner, ensuring accurate and efficient data management.
- [**Pre-Commit Integration**](https://github.com/AshishTI23/inmar-assignment/blob/main/.pre-commit-config.yaml): By integrating pre-commit into development process, Devs can significantly enhance code quality, streamline your workflow, and ensure a more consistent and maintainable codebase.
- [**Custome Response format**](https://github.com/AshishTI23/inmar-assignment/blob/main/base/http.py): This implementation ensures consistency in the response body structure across all APIs.
## Setup Instructions

### Prerequisites

- Python 3.11.6+
- Django 5.0+
- PostgreSQL

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AshishTI23/inmar-assignment.git
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

    - Create of Delete seed data:
    ```bash
    python manage.py seed --type=add
    python manage.py seed --type=delete
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Locations
- **GET** `/api/v1/locations/` - List all locations.
- **POST** `/api/v1/locations/` - Create a new location.
- **PATCH, DELETE** `/api/v1/locations/<uuid:location_id>/` - Retrieve, update, or delete a specific location.

### Departments
- **GET** `/api/v1/locations/<uuid:location_id>/departments/` - List all departments at a specific location.
- **POST** `/api/v1/locations/<uuid:location_id>/departments/` - Create a new Department.
- **PATCH, DELETE** `/api/v1/departments/<uuid:department_id>/` - Retrieve, update, or delete a specific department.

### Categories
- **GET** `/api/v1/locations/<uuid:location_id>/departments/<uuid:department_id>/categories/` - List all categories within a specific department at a given location.
- **POST** `/api/v1/locations/<uuid:location_id>/departments/<uuid:department_id>/categories/` - Create a new Category.
- **PATCH, DELETE** `/api/v1/categories/<uuid:category_id>/` - Retrieve, update, or delete a specific category.

### Subcategories
- **GET** `/api/v1/locations/<uuid:location_id>/departments/<uuid:department_id>/categories/<uuid:category_id>/sub_categories/` - List all subcategories within a specific category in a given department and location.
- **POST** `/api/v1/locations/<uuid:location_id>/departments/<uuid:department_id>/categories/<uuid:category_id>/sub_categories/` - Create a new SubCategory.
- **PATCH, DELETE** `/api/v1/subcategories/<uuid:subcategory_id>/` - Retrieve, update, or delete a specific subcategory.

### SKUs
- **GET** `/api/v1/skus/` - List all SKUs.
<!-- - **POST** `/api/v1/skus/` - Create a new SKU. -->

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.


