# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 09:43:39 2020

@author: jonathan
"""

# DROP TABLES
drop_customer_table = "DROP TABLE IF EXISTS customers"

drop_product_table = "DROP TABLE IF EXISTS products"

drop_material_table = "DROP TABLE IF EXISTS materials"

drop_color_table = "DROP TABLE IF EXISTS colors"

drop_description_table = "DROP TABLE IF EXISTS desription"

# CREATE TABLES
create_customer_table = """
CREATE TABLE IF NOT EXISTS customers
(
     customer_id    BIGINT PRIMARY KEY,
     first_name     VARCHAR(20),
     last_name      VARCHAR(20),
     email_address  VARCHAR(50),
     dob            DATE,
     gender         VARCHAR(8),
     street_address VARCHAR(50),
     state          VARCHAR(50),
     date_created   DATE,
     create_source  VARCHAR(50)
 )
"""

create_product_table = """
CREATE TABLE IF NOT EXISTS products
(
     product_id       BIGINT PRIMARY KEY,
     material_id      INT,
     color_id         INT,
     description_id   INT,
     pieces           INT,
     cost             NUMERIC
 )
"""

create_material_table = """
CREATE TABLE IF NOT EXISTS material
(
     material_id      BIGINT PRIMARY KEY,
     material_desc    VARCHAR(100)
 )
"""

create_color_table = """
CREATE TABLE IF NOT EXISTS color
(
     color_id       BIGINT PRIMARY KEY,
     color_desc     VARCHAR(100)
 )
"""

create_description_table = """
CREATE TABLE IF NOT EXISTS description
(
     description_id          BIGINT PRIMARY KEY,
     product_description     VARCHAR(100)
 )
"""

# INSERT QUERIES
insert_customer_table = """
INSERT INTO customers (customer_id, first_name, last_name, email_address, \
dob, gender, street_address, state, date_created, create_source)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

insert_product_table = """
INSERT INTO products (product_code, manufacturer_id, brand_id, material_id, \
material_type_id, color_id, state_id, state, description, number_of_pieces, cost)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

insert_material_table = """
INSERT INTO material (material_id, material_desc)
VALUES (%s, %s)
"""

insert_color_table = """
INSERT INTO color (color_id, color_desc)
VALUES (%s, %s)
"""

insert_description_table = """
INSERT INTO description (description_id, product_description)
VALUES (%s, %s)
"""

# QUERY LISTS
drop_table_queries = [drop_customer_table, drop_product_table, drop_material_table, drop_color_table, drop_description_table]
create_table_queries = [create_customer_table, create_product_table, create_material_table, create_color_table, create_description_table]
insert_table_queries = [insert_customer_table, insert_product_table, insert_material_table, insert_color_table, insert_description_table]
