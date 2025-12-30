## 每題說明

# 1 (邏輯閘、布林邏輯)
## Not
* **完成方式**: 原創實作
* **使用元件**: `Nand`
* **連結**: [看教材](https://www.nand2tetris.org/course)


[Image of Not gate logic diagram using Nand gate]


## And
* **完成方式**: 原創實作
* **使用元件**: `Nand`, `Not`
* **連結**: [看教材](https://www.nand2tetris.org/course)

## Or
* **完成方式**: 原創實作
* **使用元件**: `Nand`, `Not`
* **連結**: [看教材](https://www.nand2tetris.org/course)

## XOr
* **完成方式**: 原創實作
* **使用元件**: `And`, `Not`, `Or`
* **連結**: [看教材](https://www.nand2tetris.org/course)

## Mux
* **完成方式**: 參考網路上他人的程式
* **使用元件**: `And`, `Not`, `Or`
* **定義**: 根據選擇訊號 (sel) 決定輸出 A 或 B。
* **連結**: [sake92](https://github.com/sake92/nand2tetris/tree/master/projects)


## DMux
* **完成方式**: 參考網路上他人的程式
* **使用元件**: `Not`, `And`
* **原理**: 將單一輸入根據選擇訊號導向特定的輸出路徑。
* **連結**: [sake92](https://github.com/sake92/nand2tetris/tree/master/projects)

## Mux16 / Mux4Way16 / Mux8Way16
* **完成方式**: Gemini 幫寫與修正+參考網路上他人的程式
* **使用元件**: `Mux`, `Mux16`
* **連結**: [sake92](https://github.com/sake92/nand2tetris/tree/master/projects)

---

# 2 (布林運算)
## HalfAdder / FullAdder
* **完成方式**: Gemini 幫寫與修正+參考網路上他人的程式
* **元件**: `XOr`, `And`, `Or`, `HalfAdder`
* **連結**: [sake92](https://github.com/sake92/nand2tetris/tree/master/projects)

## Add16
* **完成方式**: Gemini 幫寫與修正+參考網路上他人的程式
* **核心**: 串聯 16 個全加器處理連波進位 (Ripple Carry)。
* **連結**: [sake92](https://github.com/sake92/nand2tetris/tree/master/projects)

## Inc16
* **完成方式**: 參考網路上他人的程式
* **運作**: 實現 16 位元數值加 1 的運算。
* **連結**: [sake92](https://github.com/sake92/nand2tetris/tree/master/projects)

## ALU (算術邏輯單元)
* **完成方式**: Gemini 幫寫與修正+參考網路上他人的程式
* **功能**: 接收 6 個控制位元，執行指定的算術或邏輯運算，並輸出 zr 與 ng 標誌。
* **連結**: [sake92](https://github.com/sake92/nand2tetris/tree/master/projects)


---

# 3 (時序運算)
## Bit / Register
* **完成方式**: Gemini 幫寫與修正+參考網路上他人的程式
* **原理**: 使用 DFF 配合 Mux 實現數據載入與鎖存。
* **連結**: [sake92](https://github.com/sake92/nand2tetris/tree/master/projects)

## RAM 系列 (RAM8 ~ RAM16K)
* **完成方式**: Gemini 幫寫與修正+參考網路上他人的程式
* **結構**: 透過分層解碼與暫存器堆疊實現隨機存取記憶體。
* **連結**: [sake92](https://github.com/sake92/nand2tetris/tree/master/projects)

## PC (程式計數器)
* **完成方式**: Gemini 幫寫與修正+參考網路上他人的程式
* **邏輯**: 支援 Reset (重置)、Load (載入) 與 Inc (遞增) 優先權控制。

---

# 4 (機器語言)
## fill.asm
* **完成方式**: 參考網路上他人的程式
* **運作**: 監測鍵盤位址 (KBD)，根據狀態填滿或清除螢幕記憶體映射區。
* **連結**: [sake92](https://github.com/sake92/nand2tetris/tree/master/projects)

## Mult.asm
* **完成方式**: 參考網路上他人的程式
* **連結**: 利用重複加法演算法實現 R0 * R1 並存入 R2。

---

# 5 (計算機架構)
## Memory
* **完成方式**: 參考網路上他人的程式
* **運作**: 將 RAM、Screen 與 Keyboard 映射至統一的定址空間。
* **連結**: [sake92](https://github.com/sake92/nand2tetris/tree/master/projects)

## CPU
* **完成方式**: 參考網路上他人的程式
* **邏輯**: 負責指令擷取、解碼與執行，並處理暫存器讀寫與 PC 跳轉。
* **連結**: [sake92](https://github.com/sake92/nand2tetris/tree/master/projects)

## Computer
* **完成方式**: 參考網路上他人的程式
* **整合**: 連結 ROM32K、CPU 與 Memory，形成完整的硬體執行平台。
* **連結**: [sake92](https://github.com/sake92/nand2tetris/tree/master/projects)




