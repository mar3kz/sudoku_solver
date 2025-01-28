rules:
1. no same number in column/row
2. no same number in 3x3
3. when num_try > 9 => return 1 position back to last correct position and set set num_try to previous value + 1 (because 1-previous_value are 100% wrong numbers and should not be there, hence the +1 and continuing the search)
4. num_try has to be under 10 => 1-9
