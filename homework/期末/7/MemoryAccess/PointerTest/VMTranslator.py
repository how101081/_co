import sys

def translate(vm_file):
    asm_file = vm_file.replace(".vm", ".asm")
    segments = {"local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT"}

    with open(vm_file, 'r') as f, open(asm_file, 'w') as out:
        for line in f:
            line = line.split("//")[0].strip()
            if not line: continue
            
            out.write(f"// {line}\n")
            p = line.split()
            cmd, seg = p[0], p[1] if len(p) > 1 else ""
            idx = p[2] if len(p) > 2 else ""

            if cmd == "push":
                if seg == "constant": out.write(f"@{idx}\nD=A\n")
                elif seg in segments: out.write(f"@{idx}\nD=A\n@{segments[seg]}\nA=M+D\nD=M\n")
                elif seg == "temp": out.write(f"@{int(idx)+5}\nD=M\n")
                # --- 新增 Pointer 處理 ---
                elif seg == "pointer": out.write(f"@{'THIS' if idx=='0' else 'THAT'}\nD=M\n")
                out.write("@SP\nA=M\nM=D\n@SP\nM=M+1\n")

            elif cmd == "pop":
                if seg in segments:
                    out.write(f"@{idx}\nD=A\n@{segments[seg]}\nD=M+D\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
                elif seg == "temp":
                    out.write(f"@SP\nAM=M-1\nD=M\n@{int(idx)+5}\nM=D\n")
                # --- 新增 Pointer 處理 ---
                elif seg == "pointer":
                    out.write(f"@SP\nAM=M-1\nD=M\n@{'THIS' if idx=='0' else 'THAT'}\nM=D\n")

            elif cmd in ["add", "sub"]:
                out.write("@SP\nAM=M-1\nD=M\n@SP\nAM=M-1\n")
                out.write(f"M={'D+M' if cmd=='add' else 'M-D'}\n@SP\nM=M+1\n")

    print(f"成功生成: {asm_file}")

# 修改這裡來產出 PointerTest.asm
translate("PointerTest.vm")