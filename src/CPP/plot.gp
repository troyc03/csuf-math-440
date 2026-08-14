# Setup clean GIF engine
set terminal gif animate delay 5 size 1100,550 enhanced font 'Verdana,10'
set output 'kinematics_movie.gif'

# Manually count records cleanly without relying on column-guessing stats
stats 'trajectory.dat' using 1 nooutput
total_frames = STATS_records

# --- CUSTOMIZE BOX BOUNDS HERE ---
# Adjust these numbers to match your simulation area safely!
xmin = -5.0
xmax =  5.0
ymin = -5.0
ymax =  5.0
tmax = 7.0
vmax = 6.0
# ---------------------------------

set grid

do for [i=1:total_frames] {
    # Force multiplot initialization per frame explicitly
    set multiplot layout 1,2 title sprintf("Kinematics Simulation | Frame %d of %d", i, total_frames)
    
    # -------------------------------------------------------------
    # LEFT PANEL: Vector Position Plot
    # -------------------------------------------------------------
    set size ratio -1
    set xlabel "X Position"
    set ylabel "Y Position"
    
    # Hardcoded strict limits to stop axis jumping or loop breaking
    set xrange [xmin:xmax]
    set yrange [ymin:ymax]
    
    plot 'trajectory.dat' every ::0::i using 2:3 with lines lw 1.5 lc rgb "gray" title "Path Trail", \
         'trajectory.dat' every ::(i-1)::i using 2:3 with points pt 7 ps 2 lc rgb "black" title "Particle", \
         'trajectory.dat' every ::(i-1)::i using 2:3:($4*0.3):($5*0.3) with vectors head filled lw 2 lc rgb "red" title "Vel Vector", \
         'trajectory.dat' every ::(i-1)::i using 2:3:($6*0.3):($7*0.3) with vectors head filled lw 2 lc rgb "dark-green" title "Acc Vector"

    # -------------------------------------------------------------
    # RIGHT PANEL: Velocity Components vs Time
    # -------------------------------------------------------------
    set size ratio 0 # Clear square locks
    set xlabel "Time (s)"
    set ylabel "Velocity Magnitude"
    
    set xrange [0:tmax] 
    set yrange [-vmax:vmax]
    
    plot 'trajectory.dat' every ::0::i using 1:4 with lines lw 2 lc rgb "orange" title "Vx(t)", \
         'trajectory.dat' every ::0::i using 1:5 with lines lw 2 lc rgb "purple" title "Vy(t)"
         
    # Explicitly clear the layout buffer for the next loop execution
    unset multiplot
}

# Flush file stream safely to local machine
set output
