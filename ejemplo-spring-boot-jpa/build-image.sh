mvn clean install spring-boot:repackage -Dmaven.test.skip=true
#mvn spring-boot:build-image -Dmaven.test.skip=true
docker build -t angelsantander/ejemplo-java-jpa:0.1 .