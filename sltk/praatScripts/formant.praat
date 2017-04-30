form Command line Arguments
    text file_name
    positive time_step
    natural max_num_formants
    positive max_formant
    positive window_length
    positive pre_emphasis
    natural formant
    positive time
    text out_file
endform

Read from file: file_name$
do ("To Formant (burg)...", time_step, max_num_formants, max_formant, window_length, pre_emphasis)
freq = do ("Get value at time...", formant, time, "Hertz", "Linear")
writeFileLine: out_file$, freq


