#include <iomanip>

#include "Particle.h"

int main(int argc, char* argv[]) {
    Particle prt;
    
    double t_begin = atof(argv[1]);
    double t_end   = atof(argv[2]);
    double dt      = atof(argv[3]);
    
    double t = t_begin;
    
    int prec = 16; // Machine precision
    ofstream outFile;
    outFile.open("data.out");
    prt.GetAux();
    
    outFile << t << std::setprecision(prec) << " " << prt;
    
    /* Evolution loop */
    while(t < t_end) {
        prt.UpdateParticle(dt);
        prt.GetAux();
        
        outFile << t << std::setprecision(prec) << " " << prt;
        cerr << t << "/" << t_end << endl;
        
        t += dt;
        if(t > t_end) t = t_end;
    }
    outFile.close();
    cerr << "# Simulation finished!" << endl;
}


