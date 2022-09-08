
import impr
import exprt
import UI

var, format_out = UI.input_()
if var == 1:
    if format_out == 1:
        impr.read_file_1()

    if format_out == 2:
        impr.read_file_2()

elif var == 2:
    if format_out == 1:
        exprt.write_file_1()

    if format_out == 2:
        exprt.write_file_2()