# Nand2Tetris Ch 6-12)

這是我在電腦架構課程中的期末專作報告，內容涵蓋了從組譯器、虛擬機、編譯器到作業系統的完整構建過程。

---

## 📜 著作狀態與 AI 輔助說明

本作業結合了自主學習與 AI 工具輔助，旨在透過 AI 生成的程式碼進行逆向理解與邏輯推導。

* **實作來源：** * 第 6-12 章：主要由 AI 生成 (Gemini) 並進行邏輯驗證。
    * 第 9 章：由 AI 協助修改範例完成。
* **AI 對話紀錄連結：**
    * [Gemini](https://gemini.google.com/share/018c0a17a110)


---

## 📂 各章節實作心得與理解

### 🛠 Project 6: The Assembler (組譯器)
* **來源：** AI 生成 (AI Generated)
* **理解程度：** 理解 Assembler 如何將 `.asm` 符號翻譯成二進制 `.hack`。我知道 **Symbol Table** 用來處理變數和跳轉標籤 (Labels)，也理解 **A-instruction** 與 **C-instruction** 的格式區別。

### 📦 Project 7 & 8: Virtual Machine Translator (虛擬機翻譯器)
* **來源：** AI 生成 (AI Generated)
* **理解程度：** 理解 VM 翻譯的邏輯。我知道 **Stack arithmetic** (push/pop, add, sub) 是如何運作的，以及 **Memory Segments** (local, argument, this, that) 是如何映射到 Hack RAM 的。

### 🎮 Project 9: High-Level Language Application (Catch Fruit)
* **來源：** AI 協助修改範例 (AI Assisted / Modified)
* **理解程度：** 這是用 Jack 語言寫的小遊戲。我理解 Jack 的語法結構以及如何呼叫標準庫 (如 `Output`, `Screen`) 來實現視覺與互動功能。

### 🔍 Project 10: Compiler I (Syntax Analysis)
* **來源：** AI 生成 (AI Generated)
* **理解程度：** 理解 Compiler 前端的工作流程：先透過 **Tokenizer** 將原始碼切分成 Tokens，再透過 **Parser** 根據語法規則建立 XML 結構 (**Parse Tree**)。

### ⚙️ Project 11: Compiler II (Code Generation)
* **來源：** AI 生成 (AI Generated)
* **理解程度：** 理解 Backend 的目標是輸出 VM Code。我知道 **Symbol Table** 需要區分 Class scope 和 Subroutine scope，雖然具體的遞迴生成邏輯由 AI 完成，但我能追蹤變數分配的流程。

### 🖥️ Project 12: The Operating System (作業系統)
* **來源：** AI 生成 (AI Generated)
* **理解程度：** 雖然老師指示可以閱讀解答，但我嘗試使用 AI 協助完成了 OS 的實作。我理解這些 Class 是為了**彌補硬體功能的不足** (例如用軟體實作乘法、除法、以及記憶體管理)。

---

## 🚀 如何運行
1.  **Assembler:** `python assembler.py XXX.asm`
2.  **VM Translator:** `python vm_translator.py XXX.vm`
3.  **Compiler:** `python JackCompiler.py [Directory]`
4.  **OS:** 將 `.vm` 檔案放入專案資料夾後，使用 **VM Emulator** 執行。

---

## 🎓 學習總結
透過這學期的專案，我從軟體的角度重新審視了硬體的運作。儘管大部分程式碼由 AI 輔助生成，但透過偵錯與對話過程，我掌握了計算機系統中各層級（Abstraction Layers）之間的溝通協定，這對理解底層開發有巨大的幫助。

