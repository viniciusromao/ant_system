set terminal postscript eps color "ArialMT" 20
set encoding iso_8859_1
set grid ytics lt 0 lw 1 lc rgb "#cccccc"
set grid xtics lt 0 lw 1 lc rgb "#cccccc"
set style line 1 lt 1 lw 3 lc 1 
set style line 2 lt 2 lw 3 lc 7
set style line 3 lt 1 lw 1 lc 3
set style line 4 lt 2 lw 1 lc 1
set pointsize 1.5 

set xrange [1:500]
#set yrange [0.5:1]
set xtics 50
#set ytics 0.1
set xlabel "Iterações"
set ylabel "Melhor solução"
set key box width 2
set key right top

plot "car1.dat" using 1:2 smooth csplines title "car1" with lines ls1, \
	"car2.dat" using 1:2 smooth csplines title "car2" with lines ls2, \
	"car3.dat" using 1:2 smooth csplines title "car3" with lines ls3, \
	"car4.dat" using 1:2 smooth csplines title "car4" with lines ls4, \
	"car6.dat" using 1:2 smooth csplines title "car6" with lines ls5
#	"car7.dat" using 1:2 smooth csplines title "car7" with lines ls6, \
#	"car8.dat" using 1:2 smooth csplines title "car8" with lines ls7, \
#	"rec01.dat" using 1:2 smooth csplines title "rec01" with lines ls8, \
#	"rec03.dat" using 1:2 smooth csplines title "rec03" with lines ls9
#%	"rec05.dat" using 1:2 smooth csplines title "rec05" with lines ls10;
