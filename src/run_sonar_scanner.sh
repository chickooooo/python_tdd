#!/bin/sh

# run pytest with coverage
coverage run -m pytest

# generate coverage.xml
coverage xml

# run sonar scanner
"C:\Software\sonar-scanner-5.0.1.3006-windows\bin\sonar-scanner.bat" \
  -Dsonar.host.url=http://localhost:9000/ \
  -Dsonar.projectKey=python_tdd -Dsonar.language=py \
  -Dsonar.sourceEncoding=UTF-8 \
  -Dsonar.sources=./ \
  -Dsonar.python.coverage.reportPaths=coverage.xml \
  -Dsonar.login=admin \
  -Dsonar.password=5999

# generate coverage report
coverage report
