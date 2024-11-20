#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
bash $SCRIPT_DIR/fix_init.sh;
bash $SCRIPT_DIR/fix_property.sh;
bash $SCRIPT_DIR/fix_substract.sh;