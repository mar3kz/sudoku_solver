def sudoku_input():
    result = [
        [], [], [], [], [], [], [], [], [] 
    ]

    print("Zadejte vasi sudoku:\n")

    for radek in range(len(result)):
        for sloupec in range(0, 9):
            x = input(f"Cislo - {radek} {sloupec}: ")

            if x == "":
                result[radek].append("0")
            else:
                result[radek].append(x)

    return result

# pole = [
#     ["0", "0", "0", "3", "9", "0", "0", "5", "1"],
#     ["8", "5", "0", "1", "0", "2", "0", "0", "4"],
#     ["0", "1", "3", "0", "0", "0", "6", "0", "0"],
#     ["0", "0", "4", "0", "0", "0", "0", "0", "0"],
#     ["0", "3", "9", "7", "4", "6", "1", "2", "0"],
#     ["0", "0", "0", "0", "0", "0", "7", "0", "0"],
#     ["0", "0", "8", "0", "0", "5", "3", "6", "0"],
#     ["6", "0", "0", "8", "0", "3", "0", "1", "5"],
#     ["3", "4", "0", "0", "1", "9", "0", "0", "0"],
# ]

pole = sudoku_input()

def check(radek_i, sloupec_i, num_try, pole):
    # checking row
    if str(num_try) in pole[radek_i]:
        return 1
    
    for index in range(len(pole)):
        if pole[index][sloupec_i] == str(num_try):
            return 1
        
    #hranice 3x3
    min_radek = (radek_i // 3) * 3
    max_radek = min_radek + 2 # index => +1 protoze od x : do y - 1 (for loop)

    min_sloupec = (sloupec_i // 3) * 3
    max_sloupec = min_sloupec + 2 # # index => +1 protoze od x : do y - 1 (for loop)

    for radek_index in range(min_radek, max_radek + 1):
        for sloupec_index in range(min_sloupec, max_sloupec + 1):
            if pole[radek_index][sloupec_index] == str(num_try):
                return 1
            
    return 0

def volne_pozice(pole):
    pozice = []

    for index_radek in range(0, 9):
        for index_sloupec in range(0, 9):
            if str(pole[index_radek][index_sloupec]) == "0":
                x = [index_radek, index_sloupec]
                pozice.append(x)

    return pozice

pozice = volne_pozice(pole)
num_try = 1
i = 0
while(True):
    radek_i, sloupec_i = pozice[i]

    if num_try > 9:
        if (i - 1) < 0:
            print("sudoku asi nema reseni")
            exit(1)

        i -= 1
        radek_i, sloupec_i = pozice[i]
        num_try = int(pole[radek_i][sloupec_i]) + 1
        print(num_try)
        pole[radek_i][sloupec_i] = "0"

    if check(radek_i, sloupec_i, num_try, pole) == 0 and num_try < 10:
        pole[radek_i][sloupec_i] = str(num_try)
        i += 1
        num_try = 1
    else:
        num_try += 1

    if i == len(pozice):
        print("vase sudoku: \n")

        result = ""
        for array in pole:
            result += " ".join(array) + "\n"

        print(result)
        exit(0)