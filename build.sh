#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# This command will run the Python code to create the database tables
python -c "from inventory_api.database import Base, engine; Base.metadata.create_all(bind=engine)"