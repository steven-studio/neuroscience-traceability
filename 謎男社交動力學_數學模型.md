# 謎男社交動力學：示範性數學模型

> **版本**：1.0  
> **作者**：游哲維  
> **日期**：2025-01-26  

---

## 0. 簡介

「謎男方法 (Mystery Method)」中常見的分階段流程 (Attraction, Comfort, Seduction) 與操作要素 (DHV、Neg、IOI、ASD 等)，可用離散狀態與動態變數構建簡化的**社交動力學模型**。以下以馬可夫鏈/動態系統方式呈現，使其在數學層面更易理解。

---

## 1. 主要變量定義

1. **階段 (Phase)**  
   - 可依謎男方法細分 A1、A2、A3、C1、C2、C3、S1、S2、S3，或簡化為：  
     $\text{Phase} \in \{\text{A}, \text{C}, \text{S}, \text{Fail}, \text{Success}\}$
   - A：吸引 (Attraction)  
   - C：舒適 (Comfort)  
   - S：誘惑 (Seduction)  
   - Fail：中途互動破局  
   - Success：最終完成互動目標

2. **對方興趣指標 (IOI)**  
   - 設 $I(t) \in [0,1]$ 表示對方對你的興趣程度；0 代表毫無興趣，1 代表極高興趣。此值會隨互動行為動態改變。

3. **DHV（高價值展示）**  
   - 在謎男理論裡，藉由展現高價值行為、故事、社交證明等方式提高對方的興趣 (IOI)。

4. **Neg**  
   - 「打壓測試」，此方法若執行得當，可在吸引階段刺激對方投入感，若過度則適得其反，IOI 下降。

5. **ASD** (Anti-Slut Defense)  
   - 在 S 階段對方傾向保護自身形象或矜持心態的阻力，會對 IOI 造成負面衝擊。

---

## 2. 相位轉移 (Phase Transition)

把每個階段視作一個「狀態」，可用馬可夫鏈或有限狀態機描述：

$P_{ij} = \Pr(\text{Phase}(t+1)=j \,\bigm|\,
\text{Phase}(t)=i).$

例子：  
- 當 $\text{Phase} = A$ 時，若 $I(t)$ 達到某門檻 $\theta_{A\to C}$，則進入 C；若 IOI 太低則 Fail。  
- C 階段若舒適感累積到門檻 $\theta_{C\to S}$，進入 S；若互動破壞，也可 Fail。  
- S 階段若成功突破 ASD 便達到 Success；否則 Fail。

---

## 3. IOI 的演化

令 $I(t+1)$ 受「行為操作」影響。示範寫法：

$I(t+1) = 
\begin{cases}
I(t) + \Delta I_{\text{DHV}} - \Delta I_{\text{Neg}}, & \text{if Phase} = A,\\
I(t) + \Delta I_{\text{Comfort}}, & \text{if Phase} = C,\\
I(t) - \Delta I_{\text{ASD}}, & \text{if Phase} = S.
\end{cases}$

- 在 A 階段：DHV 可正向增益 IOI，Neg 根據操作而可能正或負（可視為同一項帶正負系數）。  
- 在 C 階段：透過共鳴、深度聊天，提升 IOI。  
- 在 S 階段：ASD 會負面影響；若行為得宜可抵銷或突破 ASD。

---

## 4. 範例數學模型

1. **階段簡化**：A (吸引) → C (舒適) → S (誘惑) → 成功 / 失敗。  
2. **興趣指標 IOI**：  
   $I(t+1) = \max\bigl(0,\,\min\bigl(1,\ I(t) + \alpha_{phase}\bigr)\bigr)$,
   其中 $\alpha_{phase}$ 在不同階段由 DHV、Neg、Comfort、ASD 等行為決定。

3. **轉移規則**：  
   - $\text{A} \to \text{C}$ 若 $I(t+1)\ge\theta_{AC}$；  
   - $\text{C} \to \text{S}$ 若 $I(t+1)\ge\theta_{CS}$；  
   - $\text{S}\to \text{Success}$ 若 $I(t+1)\ge\theta_{S}$；  
   - 任意階段若 $I(t+1)\le\theta_{\text{fail}}$，則 Fail。

---

## 5. 動態迴路示意

1. **初始化**：Phase=A, $I(0)=0.3$（對方起始好感）。  
2. **A階段行為**：使用 DHV=2, Neg=1 之類；更新 $I$。若 $I$ 達 $\theta_{AC}$→進入 C。  
3. **C階段行為**：談共同話題、深度舒適感；若 $\theta_{CS}$ 達標→S。  
4. **S階段行為**：突破 ASD；若成功→ Success。失誤→ Fail。

---

## 6. 實作與應用

- 可在程式中隨機產生對方性格或情境（對 Neg 容忍度、ASD 等），再根據行為策略來演算 IOI 漲跌、階段轉移。  
- 透過模擬可測試某策略組合(多少 DHV vs. Neg vs. Comfort)之「成功率」。

---

## 7. 結論

此模型將謎男理論 (Mystery Method) 常見階段與操作公式化，透過**馬可夫鏈 / 動態方程**檢視「對方興趣 IOI」隨行為增減、並以階段轉移表示互動進程。  
- A（吸引）階段主要靠 DHV、Neg 調整 IOI；  
- C（舒適）階段增強對方安全感；  
- S（誘惑）階段面臨 ASD 的負面衝擊。  
只要 IOI 持續高於各門檻，就能逐步推進並達成成功狀態。  
此數學模型僅為理論化，實際行為仍需根據現場反饋、不斷調整策略。
