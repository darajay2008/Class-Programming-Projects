JFLAGS = -g
JCC = javac

default: myBackoff.class 

myBackoff.class: myBackoff.java
	$(JCC) $(JFLAGS) myBackoff.java

clean: 
	$(RM) *.class received.txt