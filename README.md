# DES Process (Dark Energy Survey Portal Process)
[![Coverage Status](https://coveralls.io/repos/github/linea-it/des-process/badge.svg?branch=master)](https://coveralls.io/github/linea-it/des-process?branch=master)

---

## What is it?
**[DES Process](https://github.com/linea-it/des-process)** is a collection of functions for fetching processes and products from DES portal.

---

## Installation
The source code is currently hosted on GitHub at: **[https://github.com/linea-it/des-process](https://github.com/linea-it/des-process)**

Binary installers for the latest released version are available at the **[Python package index](https://pypi.org/project/des-process/)**.

---

## How to use it?
This application has two classes _Process_ and _Product_.

### Process

#### Import Process
```
from des_process import process
```

#### Get all processes
```
process.all()
```
  - _`limit: Number` (optional)_: property to limit the output.

#### Get process by its process id:
```
process.by_id(process_id: Number)
```

### Product

#### Import Product
```
from des_process import product
```

#### Get all products
```
product.all()
```
  - _`limit: Number` (optional)_: property to limit the output.

#### Get product by its product id
```
product.by_id(product_id: Number)
```

#### Get all products by their process id
```
product.by_process_id(process_id: Number)
```

#### Get product by its display name
```
product.by_name(displayName: String)
```

#### Get products by their tag id:
```
product.by_tag_id(tag_id: Number)
```

#### Get products by their field id:
```
product.by_field_id(field_id: Number)
```

#### Get products by their type id:
```
product.by_type_id(type_id: Number)
```

#### Get products by their class id:
```
product.by_class_id(class_id: Number)
```

---

## Dependencies
The requests of this application depend on the **[Centaurus API](https://github.com/linea-it/centaurus)**.
