## 每題說明

# 1 (邏輯閘、布林邏輯)
## Not
* **完成方式**: 參考網路上他人的程式
* **使用元件**: `Nand`
* **學習記錄**: [使用 GPT 了解 NOT 的定義](https://chatgpt.com/share/691550d7-4680-8006-bf0f-97068832789e)


[Image of Not gate logic diagram using Nand gate]


## And
* **完成方式**: 原創實作
* **使用元件**: `Nand`, `Not`
* **學習記錄**: [使用 GPT 了解 AND 定義並驗證程式](https://chatgpt.com/share/691552e8-5da8-8006-8027-4d807d528f22)

## Or
* **完成方式**: 原創實作
* **使用元件**: `Nand`, `Not`
* **學習記錄**: [使用 GPT 了解 Or 定義](https://chatgpt.com/share/691554d6-520c-8006-9a26-d24297488b23)

## XOr
* **完成方式**: 使用 GPT 改寫
* **使用元件**: `And`, `Not`, `Or`
* **學習記錄**: [使用 GPT 了解 XOr 定義與驗證](https://chatgpt.com/share/69160434-cd10-8006-af8e-43f9dc631272)

## Mux
* **完成方式**: Gemini 幫改寫
* **使用元件**: `And`, `Not`, `Or`
* **定義**: 根據選擇訊號 (sel) 決定輸出 A 或 B。
* **學習記錄**: [使用 Gemini 了解 MUX 定義與驗證](https://gemini.google.com/share/7811ad91dbf4)


## DMux
* **完成方式**: Gemini 幫改寫
* **使用元件**: `Not`, `And`
* **原理**: 將單一輸入根據選擇訊號導向特定的輸出路徑。
* **學習記錄**: [使用 Gemini 了解 DMux 原理與說明](https://gemini.google.com/share/c7a6f528843d)

## Mux16 / Mux4Way16 / Mux8Way16
* **完成方式**: Gemini 幫寫與修正
* **使用元件**: `Mux`, `Mux16`
* **學習記錄**: [使用 Gemini 驗證 Mux 多位元變體程式](https://gemini.google.com/share/b1af285d5095)

---

# 2 (布林運算)
## HalfAdder / FullAdder
* **完成方式**: Gemini 幫寫
* **元件**: `XOr`, `And`, `Or`, `HalfAdder`
* **學習記錄**: [使用 Gemini 了解加法器運作原理](https://gemini.google.com/share/5ebf45b13a4e)

## Add16
* **完成方式**: Gemini 幫寫
* **核心**: 串聯 16 個全加器處理連波進位 (Ripple Carry)。
* **學習記錄**: [使用 Gemini 了解 Add16 與進位機制](https://gemini.google.com/share/81d13cef2e8e)

## Inc16
* **完成方式**: 參考網路上他人的程式
* **運作**: 實現 16 位元數值加 1 的運算。
* **學習記錄**: [使用 Gemini 驗證 Inc16 程式](https://gemini.google.com/share/99415129a7cf)

## ALU (算術邏輯單元)
* **完成方式**: 使用 Gemini 幫寫
* **功能**: 接收 6 個控制位元，執行指定的算術或邏輯運算，並輸出 zr 與 ng 標誌。
* **學習記錄**: [使用 Gemini 撰寫 ALU 程式與說明](https://gemini.google.com/share/41296c3fe2ef)


---

# 3 (時序運算)
## Bit / Register
* **完成方式**: 使用 Gemini 幫寫
* **原理**: 使用 DFF 配合 Mux 實現數據載入與鎖存。
* **學習記錄**: [使用 Gemini 了解時序單元與 DFF](https://gemini.google.com/share/fdd2fc47eab1)

## RAM 系列 (RAM8 ~ RAM16K)
* **完成方式**: 使用 Gemini 幫寫
* **結構**: 透過分層解碼與暫存器堆疊實現隨機存取記憶體。
* **學習記錄**: [使用 Gemini 了解各級 RAM 的定址邏輯](https://gemini.google.com/share/b907c7a684c0)

## PC (程式計數器)
* **完成方式**: 使用 Gemini 幫寫
* **邏輯**: 支援 Reset (重置)、Load (載入) 與 Inc (遞增) 優先權控制。

---

# 4 (機器語言)
## fill.asm
* **完成方式**: Gemini 幫寫
* **運作**: 監測鍵盤位址 (KBD)，根據狀態填滿或清除螢幕記憶體映射區。
* **學習記錄**: [使用 Gemini 撰寫 fill.asm 並驗證](https://gemini.google.com/share/eba87491b874)

## Mult.asm
* **完成方式**: Gemini 幫寫
* **運作**: 利用重複加法演算法實現 R0 * R1 並存入 R2。

---

# 5 (計算機架構)
## Memory
* **完成方式**: 參考網路上他人的程式
* **運作**: 將 RAM、Screen 與 Keyboard 映射至統一的定址空間。
* **學習記錄**: [使用 Gemini 了解 Memory Map 運作](https://gemini.google.com/share/364327f497bb)

## CPU
* **完成方式**: 參考網路上他人的程式
* **邏輯**: 負責指令擷取、解碼與執行，並處理暫存器讀寫與 PC 跳轉。
* **學習記錄**: [使用 Gemini 分析 CPU 指令解碼流程](https://gemini.google.com/share/9c0936b801cf)

## Computer
* **完成方式**: 參考網路上他人的程式
* **整合**: 連結 ROM32K、CPU 與 Memory，形成完整的硬體執行平台。
* **學習記錄**: [使用 Gemini 了解 Computer 整體架構](https://gemini.google.com/share/1da2255dc724)


[Image of Von Neumann architecture diagram]
