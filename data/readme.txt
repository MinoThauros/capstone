master_data is the data from run1 that will be stored in a txt file, no rush on cleaning this up cuz we can do it before run2.

run2_list_example shows how the lists will be sent to ur mino_compare() function. They are sent in real time :
mino_compare should take a list [] and an index representing Scan #.

mino_compare(scan_data, scan_number) - takes scan_data *live* from run2 aswell as the current scan number and compares it to the master_data from run1

scan_data is shown in the txt file : smthg like ['theta:0.01 dist:14 Q:47', 'theta:3.32 dist:11 Q:47', 'theta:60.01 dist:11 Q:47'] <- data from scan
scan_number is an int going from 1 to however many scans we take.

in the text file there are 8 scans in run 2 ( can see this if u search how many [] pairs there are )
there might be more scans in run 1 than run 2 or vice versa, if that happens just drop the last scan which doesnt exist in the other run.