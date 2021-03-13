#include "Particle.h"

void Particle::ReadInput() {
    ifstream inFile;
    string value;
    inFile.open("initial.in");
    vector<double> data;
    
    if (inFile) {
        while (inFile >> value) {
            double val = atof(value.c_str());
            data.push_back(val);
        }
    }
    inFile.close();
    cout << m << " " << r[0] << " " << r[1] << endl;
    
    m    = data[0];
    r[0] = data[1];
    r[1] = data[2];
    v[0] = data[3];
    v[1] = data[4];
}
        
void Particle::CalcAcceleration() {
    double common = 1 / (1 + r[0]*r[0] + r[1]*r[1]/2);
    
    a[0] = -2*common * r[0];
    a[1] = -common   * r[1];
}

void Particle::UpdateParticle(double &dt) {
    /* Step with Verlet scheme */
    array<double, 2> a0;
    for(int i=0; i<2; i++) {
        CalcAcceleration();
        r[i] += v[i]*dt + 0.5*a[i]*dt*dt;
        a0[i] = a[i];
        CalcAcceleration();
        v[i] += 0.5*(a0[i] + a[i])*dt;
    }
}

void Particle::GetAux() {
    E = 0;
    
    for(int i=0; i<2; i++) {
        E += 0.5*m*(v[i]*v[i]);
    }
    E += m * log(1 + r[0]*r[0] + r[1]*r[1]/2);
    
    Lz = m*(v[0]*r[1] - v[1]*r[0]);
}
