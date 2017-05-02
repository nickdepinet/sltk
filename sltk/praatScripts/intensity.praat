form Command line Arguments
    text file_name
    positive intensity_time
    positive min_freq
    positive time_step
    text sub_mean
    text out_file
endform

Read from file: file_name$
do ("To Intensity...", min_freq, time_step, sub_mean$)
val = do ("Get value at time...", intensity_time, "Cubic")
writeFileLine: out_file$, val