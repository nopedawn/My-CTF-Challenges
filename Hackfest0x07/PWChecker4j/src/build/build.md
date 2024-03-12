## Build step:

1. Compile Java source code (PWChecker4j.java):
```
javac PWChecker4j.java
```

2. Create a manifest file named `MANIFEST.MF` with the following content:
```
Manifest-Version: 1.0
Main-Class: PWChecker4j
```

3. Create the JAR file using the following command:
```
jar cfm PWChecker4j.jar MANIFEST.MF *.class
```


## Run program:

```
java -jar PWChecker4j.jar
```
