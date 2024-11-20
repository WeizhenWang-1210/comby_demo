#!/bin/bash
#Fixing the naming of object's field
comby ":[[object]].real" ":[object].re"  /home/weizhen/repo/comby_demo/lib/ComplexNumber.py -review;
comby ":[[object]].imaginary" ":[object].im"  /home/weizhen/repo/comby_demo/lib/ComplexNumber.py -review;