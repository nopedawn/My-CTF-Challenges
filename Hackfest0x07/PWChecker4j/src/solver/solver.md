1. Clone & Download JAR
[jd-cli Github Repo](https://github.com/intoolswetrust/jd-cli) & 
[jd-cli-1.2.1.jar](https://libraries.io/maven/com.github.kwart.jd:jd-cli/1.2.1)

2. Add `jd-cli` to `.bashrc` environment
```sudo nano ~/.bashrc```
```
#jd-cli
function dec() {
        java -jar ~/jd-cli-1.2.1/jd-cli.jar "$@";
}
```

3. Decompile & Run
```
dec PWChecker4j.jar -od decompiled -oc
```

4. Static analyzing source-code