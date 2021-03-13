###########################################################
DIRSRC	= ./src/
###########################################################
COMP 	= g++
CFLAGS 	= -O3 -std=c++11
CC 	= $(COMP) $(CFLAGS) -c
CO	= $(COMP) $(CFLAGS) -o
###########################################################
Orbit.exe: Main.o Particle.o
	$(CO) Orbit.exe Main.o Particle.o
###########################################################
Main.o: $(DIRSRC)Main.cpp Particle.o
	$(CC) $(DIRSRC)Main.cpp -I$(DIRSRC)
Particle.o: $(DIRSRC)Particle.h $(DIRSRC)Particle.cpp
	$(CC) $(DIRSRC)Particle.cpp
###########################################################
clean:
	rm -f *~
	rm -f *.o
	rm -f *.exe
	rm -f *.out
