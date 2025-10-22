#!/usr/bin/env bash

if ! which ffmpeg > /dev/null; then
    echo "ffmpeg is not installed!"
    exit 1
fi

if [[ ! -e badapple.webm ]]; then
    echo "badapple video not found!"
    if ! which yt-dlp > /dev/null; then
        echo "yt-dlp is not installed!"
        exit 1
    fi

    yt-dlp --no-mtime -o badapple.webm -f bv https://www.youtube.com/watch?v=FtutLA63Cp8
fi

if [[ -d ./images ]]; then
    rm ./images/*
else
    mkdir images
fi

ffmpeg -i badapple.webm -vf "scale=24:-1,fps=16" ./images/badapple-%04d.png

python build.py
