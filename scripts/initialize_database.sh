#! /bin/bash

#!/usr/bin/env bash

set -euo pipefail  

DB_USER="root"
DB_PASS="toor"

# Determine the directory where this script lives
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Execute scripts in order
mysql -u"${DB_USER}" -p"${DB_PASS}" < "${SCRIPT_DIR}/drop_and_make_schema.sql"
mysql -u"${DB_USER}" -p"${DB_PASS}" < "${SCRIPT_DIR}/create_tables.sql"
mysql -u"${DB_USER}" -p"${DB_PASS}" < "${SCRIPT_DIR}/insert_sample_data.sql"
echo "Database initialization completed successfully."
