def macro_pass2():
    # Read input files
    with open('intermediate.txt', 'r') as irb:
        ir_lines = irb.readlines()

    with open('mdt.txt', 'r') as mdtb:
        mdt_lines = mdtb.readlines()

    with open('kpdt.txt', 'r') as kpdtb:
        kpdt_lines = kpdtb.readlines()

    with open('mnt.txt', 'r') as mntb:
        mnt_lines = mntb.readlines()

    # Prepare output file
    with open('pass2.txt', 'w') as fr:
        mnt = {}
        aptab = {}
        aptab_inverse = {}

        # Load MDT and KPDT into lists
        mdt = [line.strip() for line in mdt_lines]
        kpdt = [line.strip() for line in kpdt_lines]

        # Parse MNT entries
        for line in mnt_lines:
            parts = line.split()
            if len(parts) > 4:
                mnt[parts[0]] = {
                    'pp': int(parts[1]),
                    'kp': int(parts[2]),
                    'mdtp': int(parts[3]),
                    'kpdtp': int(parts[4])
                }

        # Process the intermediate file line by line
        for line in ir_lines:
            parts = line.split()
            if parts[0] in mnt:
                macro_name = parts[0]
                pp = mnt[macro_name]['pp']
                kp = mnt[macro_name]['kp']
                mdtp = mnt[macro_name]['mdtp']
                kpdtp = mnt[macro_name]['kpdtp']

                param_no = 1

                # Store positional parameters in aptab
                for i in range(pp):
                    parts[param_no] = parts[param_no].replace(",", "")
                    aptab[param_no] = parts[param_no]
                    aptab_inverse[parts[param_no]] = param_no
                    param_no += 1

                # Store keyword parameters in aptab from kpdt
                j = kpdtp - 1
                for i in range(kp):
                    if j < len(kpdt):
                        temp = kpdt[j].split("\t")
                        if len(temp) > 1:
                            aptab[param_no] = temp[1]
                            aptab_inverse[temp[0]] = param_no
                        else:
                            print(f"Warning: Invalid line in KPDT at line {j+1}: {kpdt[j]}")
                    else:
                        print(f"Warning: Index out of range in KPDT at line {j+1}")
                    j += 1
                    param_no += 1

                # Handle keyword parameters with default values (if any)
                for i in range(pp + 1, len(parts)):
                    parts[i] = parts[i].replace(",", "")
                    splits = parts[i].split("=")
                    name = splits[0].replace("&", "")
                    if name in aptab_inverse:
                        aptab[aptab_inverse[name]] = splits[1]
                    else:
                        print(f"Warning: Keyword parameter {name} not found in aptab_inverse")

                # Process MDT and replace parameter references
                i = mdtp - 1
                while mdt[i] != "MEND":
                    splits = mdt[i].split()
                    fr.write("+")
                    for k in range(len(splits)):
                        if "(P," in splits[k]:
                            param_index = int(splits[k].replace("(P,", "").replace(")", ""))
                            value = aptab.get(param_index, "UNKNOWN")
                            fr.write(f"{value}\t")
                        else:
                            fr.write(f"{splits[k]}\t")
                    fr.write("\n")
                    i += 1

                # Clear aptab and aptab_inverse for the next macro
                aptab.clear()
                aptab_inverse.clear()

            else:
                # If it's not a macro invocation, just write the line as is
                fr.write(line)


if __name__ == "__main__":
    macro_pass2()
    print("Macro Pass2 Processing completed.")
