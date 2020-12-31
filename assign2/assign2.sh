#!/bin/bash
start=$SECONDS

sh Q1.sh ; 
sh Q2.sh ; 
sh Q3.sh ; 
sh Q4.sh ;
sh Q5.sh ; 
sh Q6.sh ; 
sh Q7.sh ; 
sh Q8.sh ;
sh Q9.sh ;
sh Q10.sh ;
sh Q11.sh ;

end=$SECONDS

echo "duration: $((end-start)) seconds."