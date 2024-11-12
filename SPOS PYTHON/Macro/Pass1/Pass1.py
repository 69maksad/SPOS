def macro_pass1():
    witopen("macro_input.asm", 'r') as br, \
         open("mnt.txt", 'w') as mnt, \
         open("mdt.txt", 'w') as mdt, \
         open("kpdt.txt", 'w') as kpdt, \
         open("pntab.txt", 'w') as pnt, \
         open("intermediate.txt", 'w') as ir:

        pntab = {}
        mdtp = 1
        kpdtp = 0
        paramNo = 1
        pp = 0
        kp = 0
        flag = 0
        Macroname = None

        for line in br:
            parts = line.split()
            if len(parts) == 0:
                continue
            
            if parts[0].upper() == "MACRO":
                flag = 1
                line = next(br)
                parts = line.split()
                Macroname = parts[0]
                
                if len(parts) <= 1:
                    mnt.write(f"{parts[0]}\t{pp}\t{kp}\t{mdtp}\t{kp if kp == 0 else (kpdtp + 1)}\n")
                    continue
                
                for i in range(1, len(parts)):  # processing of parameters
                    parts[i] = parts[i].replace(",", "").replace("&", "")
                    if "=" in parts[i]:
                        kp += 1
                        keywordParam = parts[i].split("=")
                        pntab[keywordParam[0]] = paramNo
                        paramNo += 1
                        if len(keywordParam) == 2:
                            kpdt.write(f"{keywordParam[0]}\t{keywordParam[1]}\n")
                        else:
                            kpdt.write(f"{keywordParam[0]}\t-\n")
                    else:
                        pntab[parts[i]] = paramNo
                        paramNo += 1
                        pp += 1
                
                mnt.write(f"{parts[0]}\t{pp}\t{kp}\t{mdtp}\t{kp if kp == 0 else (kpdtp + 1)}\n")
                kpdtp += kp
                # Reset parameter counts
                paramNo = 1
                kp = pp = 0

            elif parts[0].upper() == "MEND":
                mdt.write(line)
                flag = 0
                mdtp += 1
                pnt.write(f"{Macroname}:\t")
                for key in pntab:
                    pnt.write(f"{key}\t")
                pnt.write("\n")
                pntab.clear()

            elif flag == 1:  # inside macro definition
                for part in parts:
                    # Remove the extra commas or ampersands from parameters
                    clean_part = part.replace(",", "").replace("&", "")
                    if "&" in part:  # replace with the parameter number
                        mdt.write(f"(P,{pntab[clean_part]})\t")
                    else:
                        mdt.write(f"{part}\t")
                mdt.write("\n")
                mdtp += 1

            else:  # For lines outside macros
                ir.write(line)
        
    print("Macro Pass1 Processing done. :)")

# Run the macro pass1 function
macro_pass1()
