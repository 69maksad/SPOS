import re

# Initialize all necessary tables and variables directly
def initialize_pass1():
    is_table = {
        "STOP": {"mnemonic": "STOP", "opcode": "00", "num": 0},
        "ADD": {"mnemonic": "ADD", "opcode": "01", "num": 0},
        "SUB": {"mnemonic": "SUB", "opcode": "02", "num": 0},
        "MULT": {"mnemonic": "MULT", "opcode": "03", "num": 0},
        "MOVER": {"mnemonic": "MOVER", "opcode": "04", "num": 0},
        "MOVEM": {"mnemonic": "MOVEM", "opcode": "05", "num": 0},
        "COMP": {"mnemonic": "COMP", "opcode": "06", "num": 0},
        "BC": {"mnemonic": "BC", "opcode": "07", "num": 0},
        "DIV": {"mnemonic": "DIV", "opcode": "08", "num": 0},
        "READ": {"mnemonic": "READ", "opcode": "09", "num": 0},
        "PRINT": {"mnemonic": "PRINT", "opcode": "10", "num": 0},
    }
    
    symtab = []
    symaddr = []
    littab = []
    litaddr = []
    pooltab = [0]
    LC = 0

    return is_table, symtab, symaddr, littab, litaddr, pooltab, LC

def generate_ic():
    # Open input and output files
    with open("ic.txt", "w") as wr, open("input.asm", "r") as br:
        # Initialize tables and variables
        is_table, symtab, symaddr, littab, litaddr, pooltab, LC = initialize_pass1()
        wr.write("---------------------\n  Intermediate Code\n---------------------\n")
        
        lines = br.readlines()

        # Process each line from the assembly code
        for line in lines:
            split = re.split(r'\s+', line.strip())  # Split by spaces
            if not split:
                continue

            if len(split) > 1:
                # Label Handling
                if len(split[0]) > 0:
                    if split[0] not in symtab:
                        symtab.append(split[0])
                        symaddr.append(LC)
                    else:
                        index = symtab.index(split[0])
                        symaddr[index] = LC

                # Process instructions
                if split[1] == "START":
                    LC = int(split[2])
                    wr.write(f"(AD,01)(C,{split[2]}) \n")
                elif split[1] == "ORIGIN":
                    if "+" in split[2] or "-" in split[2]:
                        LC = get_address(split[2], symtab, symaddr)
                    else:
                        LC = symaddr[symtab.index(split[2])]
                elif split[1] == "EQU":
                    addr = 0
                    if "+" in split[2] or "-" in split[2]:
                        addr = get_address(split[2], symtab, symaddr)
                    else:
                        addr = symaddr[symtab.index(split[2])]
                    if split[0] not in symtab:
                        symtab.append(split[0])
                        symaddr.append(addr)
                    else:
                        index = symtab.index(split[0])
                        symaddr[index] = addr
                elif split[1] in ["LTORG", "END"]:
                    if 0 in litaddr:
                        for i in range(pooltab[-1], len(littab)):
                            if litaddr[i] == 0:
                                litaddr[i] = LC
                                LC += 1
                        if split[1] != "END":
                            pooltab.append(len(littab))
                            wr.write("\n(AD,05)\n")
                        else:
                            wr.write("(AD,04) \n")
                elif "DS" in split[1]:
                    LC += int(split[2])
                    wr.write(f"(DL,01) (C,{split[2]}) \n")
                elif "DC" in split[1]:
                    LC += 1
                    wr.write(f"\n(DL,02) (C,{split[2].replace('', '')}) \n")
                elif split[1] in is_table:
                    wr.write(f"(IS,{is_table[split[1]]['opcode']}) ")
                    if len(split) > 2 and split[2] is not None:
                        reg = split[2].replace(",", "")
                        reg_map = {"AREG": "1", "BREG": "2", "CREG": "3", "DREG": "4"}
                        if reg in reg_map:
                            wr.write(f"({reg_map[reg]}) ")
                        else:
                            if reg in symtab:
                                wr.write(f"(S,{symtab.index(reg)})\n")
                            else:
                                symtab.append(reg)
                                symaddr.append(0)
                                wr.write(f"(S,{symtab.index(reg)}) \n")
                    if len(split) > 3 and split[3] is not None:
                        if "=" in split[3]:
                            norm = split[3].replace("=", "").replace("'", "")
                            if norm not in littab:
                                littab.append(norm)
                                litaddr.append(0)
                                wr.write(f"(L,{littab.index(norm)})")
                            else:
                                wr.write(f"(L,{littab.index(norm)})")
                        elif split[3] in symtab:
                            wr.write(f"(S,{symtab.index(split[3])}) \n")
                        else:
                            symtab.append(split[3])
                            symaddr.append(0)
                            wr.write(f"(S,{symtab.index(split[3])}) \n")
                    LC += 1
        write_tables(symtab, symaddr, littab, litaddr, pooltab)

def get_address(address_str, symtab, symaddr):
    if "+" in address_str:
        parts = address_str.split("+")
        return symaddr[symtab.index(parts[0])] + int(parts[1])
    elif "-" in address_str:
        parts = address_str.split("-")
        return symaddr[symtab.index(parts[0])] - int(parts[1])
    else:
        return symaddr[symtab.index(address_str)]

def write_tables(symtab, symaddr, littab, litaddr, pooltab):
    with open('sym.txt', 'w') as br1:
        br1.write("-------------------\n    Symbol Table\n-------------------\nSymbol    Address\n")
        for i in range(len(symtab)):
            br1.write(f"  {symtab[i]}       {symaddr[i]}\n")

    with open('lit.txt', 'w') as br2:
        br2.write("-----------------------\n    Literal Table\n-----------------------\nLiteral       Address\n")
        for i in range(len(littab)):
            br2.write(f"='{littab[i]}'           {litaddr[i]}\n")

    with open('pool.txt', 'w') as br3:
        br3.write("-----------------------------\n         Pool Table\n-----------------------------\nPool Index    Literal Index\n")
        for i in range(len(pooltab)):
            br3.write(f"     {i}              {pooltab[i]}\n")

def print_file(filename):
    with open(filename, 'r') as file:
        print(file.read())

if __name__ == "__main__":
    generate_ic()
    print_file("ic.txt")
    print_file("sym.txt")
    print_file("lit.txt")
    print_file("pool.txt")
