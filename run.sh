# docker run -it -v /Users/tangchao/projects:/root python:3.7 /bin/bash
# apt install -y libgl1-mesa-glx

python3 main.py \
    --config example_data/eng.py \
    --dataset img \
    --num_processes 0 \
    --log_period 10