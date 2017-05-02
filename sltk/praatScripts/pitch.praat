form Command line Arguments
    text file_name
    positive time_step
    positive pitch_floor
    positive pitch_ceil
    positive pitch_time
    text out_file
endform

Read from file: file_name$
do ("To Pitch...", time_step, pitch_floor, pitch_ceil)
val = do ("Get value at time...", pitch_time, "Hertz", "Linear")
writeFileLine: out_file$, val