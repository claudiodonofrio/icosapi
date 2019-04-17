

java -jar openapi-generator-cli-3.3.4.jar validate -i ../icos-cp-api.json

java -jar openapi-generator-cli-3.3.4.jar generate -g html2 -o docu -i ../icos-cp-api.json
java -jar openapi-generator-cli-3.3.4.jar generate -g scala -o scala -i ../icos-cp-api.json
java -jar openapi-generator-cli-3.3.4.jar generate -g python -o python -i ../icos-cp-api.json

