#!/bin/sh
FILE=$1
ENC=UTF32BE

for ENC in 'UTF32BE' 'UTF32LE'
echo iconv $FILE -t $ENC # -o out/greek-$ENC
 iconv $FILE -t $ENC -o out/greek-$ENC
od -tx4 out/greek-$ENC
done
