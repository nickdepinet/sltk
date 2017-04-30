form Command line Arguments
    text file_name
    positive time_step
    positive pitch_floor
    positive pitch_ceil
    positive start_time
    positive end_time
    text out_file
endform

Read from file: file_name$
do ("To Pitch...", time_step, pitch_floor, pitch_ceil)
min = do ("Get minimum...", 0, 0, "Hertz", "Parabolic")
max = do ("Get maximum...", 0, 0, "Hertz", "Parabolic")
mean = do ("Get mean...", start_time, end_time, "Hertz")
writeFileLine: out_file$, min, ",", mean, ",", max


