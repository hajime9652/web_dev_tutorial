#! /usr/bin/env sh

set -e

until curl -sI http://main-store:7474 | grep "200 OK"; do
  >&2 echo "Neo4j isn't available. Let's wait for sometime"
  sleep 1
done

neomodel_install_labels ./app/models.py --db bolt://${NEO4J_USERNAME}:${NEO4J_PASSWORD}@${NEO4J_URI}

uvicorn --reload --host 0.0.0.0 --port 8888 --log-level info main:app
