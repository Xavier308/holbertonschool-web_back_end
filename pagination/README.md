# Pagination Project

## Description
This project focuses on implementing various pagination techniques for handling large datasets. It covers simple pagination, hypermedia pagination, and deletion-resilient hypermedia pagination.

## Learning Objectives

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Setup
Use the provided `Popular_Baby_Names.csv` data file for this project.

## Tasks

### 0. Simple helper function
Implement a function `index_range` that takes `page` and `page_size` parameters and returns a tuple of start and end indexes.

### 1. Simple pagination
Implement a `Server` class with a `get_page` method that paginates the dataset.

### 2. Hypermedia pagination
Extend the `Server` class with a `get_hyper` method that returns pagination information including page size, current page, data, next page, previous page, and total pages.

### 3. Deletion-resilient hypermedia pagination
Implement a `get_hyper_index` method in the `Server` class that handles pagination even when items are deleted from the dataset between queries.

## Files
- `0-simple_helper_function.py`
- `1-simple_pagination.py`
- `2-hypermedia_pagination.py`
- `3-hypermedia_del_pagination.py`
