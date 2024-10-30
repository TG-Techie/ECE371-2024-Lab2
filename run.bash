#!/bin/bash

# clears previous outputs and then runs the python program

# HOW TO USE
# run `./run.bash` to run main
# run `./run.bash --test` to run test_all_keys.py
# run `./run.bash --clean` to only clear the previous outputs


rm penguin_decrypted.jpg &> /dev/null
rm penguin_encrypted.bin &> /dev/null

rm output/*.jpg &> /dev/null
rm output/*.bin &> /dev/null


if [[ $1 == "--clean" ]]; then
    echo "clean complete"
elif [[ $1 == "--test" ]]; then
    python3 test_all_pq_values.py
else
    python3 main.py
fi