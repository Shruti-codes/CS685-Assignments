#!/bin/bash
start=$SECONDS

sh clean.sh ; 
sh case-generator.sh ; 
sh edge-generator.sh ; 
sh neighbor-generator.sh ; 
sh state-generator.sh ; 
sh zscore-generator.sh ; 
sh method-spot-generator.sh ; 
sh top-generator.sh

end=$SECONDS

echo "duration: $((end-start)) seconds."