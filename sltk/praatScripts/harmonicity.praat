form Command line Arguments
    text file_name
    positive harmonicity_time
    positive time_step
    positive min_pitch
    positive silence_threshold
    positive ppw
    text out_file
endform

Read from file: file_name$
do ("To Harmonicity (cc)...", time_step, min_pitch, silence_threshold, ppw)
val = do ("Get value at time...", harmonicity_time, "Cubic")
writeFileLine: out_file$, val