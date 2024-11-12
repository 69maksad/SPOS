import os

class TableRow:
    def __init__(self, symbol, address, index=None):
        self.symbol = symbol
        self.address = address
        self.index = index

    def get_index(self):
        return self.index

    def set_index(self, index):
        self.index = index

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address


class Pass2:
    def __init__(self):
        self.SYMTAB = []
        self.LITTAB = []

    def read_tables(self):
        try:
            with open("SYMTAB.txt", "r") as br:
                for line in br:
                    parts = line.split()
                    self.SYMTAB.append(TableRow(parts[1], int(parts[2]), int(parts[0])))

            with open("LITTAB.txt", "r") as br:
                for line in br:
                    parts = line.split()
                    self.LITTAB.append(TableRow(parts[1], int(parts[2]), int(parts[0])))
        except Exception as e:
            print(e)

    def generate_code(self, filename):
        self.read_tables()
        with open(filename, "r") as br, open("PASS2.txt", "w") as bw:
            for line in br:
                parts = line.split()
                if "AD" in parts[0] or "DL,02" in parts[0]:
                    bw.write("\n")
                    continue
                elif len(parts) == 2:
                    if "DL" in parts[0]:
                        parts[0] = ''.join(filter(str.isdigit, parts[0]))
                        if int(parts[0]) == 1:
                            constant = int(''.join(filter(str.isdigit, parts[1])))
                            code = f"00\t0\t{constant:03d}\n"
                            bw.write(code)
                    elif "IS" in parts[0]:
                        opcode = int(''.join(filter(str.isdigit, parts[0])))
                        if opcode == 10:
                            if "S" in parts[1]:
                                sym_index = int(''.join(filter(str.isdigit, parts[1])))
                                code = f"{opcode:02d}\t0\t{self.SYMTAB[sym_index - 1].get_address():03d}\n"
                                bw.write(code)
                            elif "L" in parts[1]:
                                sym_index = int(''.join(filter(str.isdigit, parts[1])))
                                code = f"{opcode:02d}\t0\t{self.LITTAB[sym_index - 1].get_address():03d}\n"
                                bw.write(code)
                elif len(parts) == 1 and "IS" in parts[0]:
                    opcode = int(''.join(filter(str.isdigit, parts[0])))
                    code = f"{opcode:02d}\t0\t{0:03d}\n"
                    bw.write(code)
                elif "IS" in parts[0] and len(parts) == 3:  # All OTHER IS INSTR
                    opcode = int(''.join(filter(str.isdigit, parts[0])))
                    regcode = int(parts[1])

                    if "S" in parts[2]:
                        sym_index = int(''.join(filter(str.isdigit, parts[2])))
                        code = f"{opcode:02d}\t{regcode}\t{self.SYMTAB[sym_index - 1].get_address():03d}\n"
                        bw.write(code)
                    elif "L" in parts[2]:
                        sym_index = int(''.join(filter(str.isdigit, parts[2])))
                        code = f"{opcode:02d}\t{regcode}\t{self.LITTAB[sym_index - 1].get_address():03d}\n"
                        bw.write(code)


if __name__ == "__main__":
    pass2 = Pass2()
    pass2.generate_code("IC.txt")