#!/bin/bash

echo

echo 'CASE 1'
curl localhost:5000/items
echo

echo 'CASE 2'
curl localhost:5000/item/1
echo

echo 'CASE 3'
curl -XPOST -H "Content-Type: application/json" -d '{"items": [5, "test", "test"]}' localhost:5000/add_item
echo

echo 'DONE'