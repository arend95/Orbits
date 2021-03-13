#include <iostream>
using namespace std;
#include <array>
#include <vector>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cmath>

#ifndef __Particle_h
#define __Particle_h

class Particle {
private:
    double m;
    double E;
    double Lz;
    
    array<double, 2> r;
    array<double, 2> v;
    array<double, 2> a;

public:
    Particle() {
        ReadInput();
    }
    
    void ReadInput();
    void UpdateParticle(double &dt);
    void CalcAcceleration();
    
    void GetAux();
    
    friend ostream &operator << (ostream &so, const Particle &pt) {
        so << pt.E << " " << pt.Lz << " " << pt.m << " " << pt.r[0] << " " << pt.r[1] << " " << 
            pt.v[0] << " " << pt.v[1] << endl;
        return so;
    }
};

#endif
    
