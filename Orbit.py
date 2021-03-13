import os
import matplotlib.pyplot as pt
import matplotlib
matplotlib.rcParams.update({'font.size': 20})
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
pt.rcParams['xtick.top'] = True
pt.rcParams['ytick.right'] = True

def RunSim(t_begin, t_end, dt):
    os.system("./Orbit.exe {} {} {}".format(t_begin, t_end, dt))

def Convert(string):
    li = map(float, string.split(" "))
    line = []
    for lli in li:
        line.append(lli)
        
    return line

def ReadFile():
    x   = []
    y   = []
    
    vx  = []
    vy  = []
    
    t   = []
    E   = []
    Lz  = []

    y_check = 0
    x_check = 0
    y_s = []
    x_s = []
    with open("data.out","r") as dat:
        for line in dat:
            line = Convert(line)

            x.append( line[4] )
            y.append( line[5] )
            Lz.append(line[2] )
            E.append( line[1] )
            t.append( line[0] )
            
            # Save surface of sections for phase diagrams
            if(line[5]*y_check < 0 and line[5] > 0):
                vx.append(line[6])
                x_s.append(line[4])
                
            if(line[4]*x_check < 0 and line[4] < 0):
                vy.append(line[7])
                y_s.append(line[5])
                
            y_check = line[5]
            x_check = line[4]
            
    E = [abs((x - E[0])/E[0]) for x in E]
    meanLz = (max(Lz) + min(Lz))/2
    print("# Average Lz = %.16f" % meanLz)

    return x, y, vx, vy, x_s, y_s, t, E

def PlotOrbit(x, y, vx, vy, x_s, y_s, t, E):
    state0 = []
    with open("initial.in") as inp:
        for line in inp:
            line = Convert(line)
            for i in range(len(line)):
                state0.append(line[i])
    
    fig, ax = pt.subplots(2,2, figsize=(15,15), gridspec_kw={'wspace':0.25,'hspace':0.25})
    
    ax[0][0].plot(x, y)
    ax[0][0].tick_params(which="both", direction="in")
    ax[0][0].set_xlabel("$x$")
    ax[0][0].set_ylabel("$y$")
    ax[0][0].set_title(r"$m$ = {} $x_0$ = {} $y_0$ = {} $vx_0$ = {} $vy_0$ = {}".format(state0[0], state0[1], state0[2], state0[3], state0[4]))

    ax[1][0].plot(x_s, vx, 'b.')
    ax[1][0].tick_params(which="both", direction="in")
    ax[1][0].set_xlabel("$x$")
    ax[1][0].set_ylabel(r"$v_x$")

    ax[0][1].plot(y_s, vy, 'b.')
    ax[0][1].tick_params(which="both", direction="in")
    ax[0][1].set_xlabel("$y$")
    ax[0][1].set_ylabel(r"$v_y$")

    ax[1][1].plot(t, E)
    ax[1][1].tick_params(which="both", direction="in")
    ax[1][1].set_xlabel("$t$")
    ax[1][1].set_ylabel(r"$\vert E-E_0/E_0\vert$")
    ax[1][1].set_yscale("log")
    
    pt.show()
    
if __name__ == "__main__":
    
    # Time settings
    t_begin = 0
    t_end   = 500
    dt      = 0.01

    RunSim(t_begin, t_end, dt)
    x, y, vx, vy, x_s, y_s, t, E = ReadFile()
    PlotOrbit(x, y, vx, vy, x_s, y_s, t, E)
              
