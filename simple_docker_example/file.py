docker run --rm \
    --mount type=bind,source="$(PWD)/data",target=/mnt/data
    --mount type=bind,source="$(PWD)/src/digit_recognition",target=/mnt/digit_recognition \
    --workdir /mnt \
    digit_recognition:latest \
    python digit_recognition/train.py --epochs 8 --batch_size 32 --data_path "./data"




docker run --rm \
    --mount type=bind,source="${PWD}/.",target=/mnt \
    --workdir /mnt \
    tutorial:v1 python app.py -f "./data/target.csv" -n 5

