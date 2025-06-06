#!/bin/bash

echo "==> Running tests..."

# locate pytest
_pytest=$(which pytest)
_EXIT_CODE=$?
if [ $_EXIT_CODE -ne 0 ]; then
  exit $_EXIT_CODE
fi
printf "pytest found in %s\n" ${_pytest}

eval "${_pytest} -q"
TEST_EXIT_CODE=$?

if [ $TEST_EXIT_CODE -ne 0 ]; then
  echo "==> Tests failed (exit code: $TEST_EXIT_CODE). Container wird beendet."
  exit $TEST_EXIT_CODE
fi

echo "==> Tests passed. Starte Flask-App..."

python flask_todo.py
