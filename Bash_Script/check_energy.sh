 #!/bin/bash
 echo "Process ID : $$"
 echo "File name : $0"
 echo "Began checking energy!"

 # Get energy data
 rm file.csv
 for element in $(ls .)
 do
     if [ -d "$element" ];then
         grep 'reached required accuracy' ./$element/STEP2/vaspout
         energy="`grep 'sigma' ./$element/STEP2/OUTCAR | tail -1`"
         energy=${energy#*->0) =}
         echo $energy
         echo $energy >> data_energy.csv
     fi
 done
