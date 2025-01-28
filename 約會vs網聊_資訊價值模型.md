# 約會與網聊資訊價值的數學模型

> **版本**：1.0  
> **作者**：游哲維  
> **日期**：2025-01-26  

---

## 前言

在現代社交情境中，「面對面約會 (In-Person Date)」與「網路聊天 (Online Chat)」都扮演了解對象的管道。但兩種形式帶來的 **資訊量** 及 **互動成本** 各不相同。本模型嘗試以 **貝氏更新 (Bayesian Update)** 與 **訊息論 (Information Theory)** 的概念，來評估網聊與約會在「辨別雙方相容度 (compatibility)」上所帶來的資訊價值。

---

## 1. 模型核心概念

1. **相容度 $\mathbf{C}$**  
   - 令 $\mathbf{C} \in [0,1]$ 表示「雙方長期和諧度」或「成功交往機率」的真實但未知量。  
   - 我們對 $\mathbf{C}$ 有一個先驗分佈（如 Beta 分佈），並在互動中不斷收集證據更新。

2. **觀測 (observation)**  
   - 「網聊」或「面對面約會」各帶來一組觀測結果，例如：  
     - $\text{Chat} \in \{\text{成功}, \text{失敗}\}$  
     - $\text{Date} \in \{\text{大好}, \text{普通}, \text{糟糕}\}$  
   - 數值越「正面」表示與高相容度更匹配；「負面」則可能暗示失敗風險。

3. **資訊增益 (Information Gain)**  
   - 透過 Shannon 熵 (Shannon Entropy) 變化，衡量每次互動後，我們對 $\mathbf{C}$ 的不確定度減少多少。  
   - 也可考慮成本 (時間、金錢) 與單位資訊效率。

---

## 2. 先驗分佈

- 假設先驗 $\mathbf{C} \sim \text{Beta}(\alpha_0, \beta_0)$。  
- 若一開始對對方沒任何了解，可用 $\alpha_0=1, \beta_0=1$（均勻分佈）。  
- 如果已有朋友介紹或社群口碑，則可選較集中形狀的 Beta 分佈。

---

## 3. 網聊與約會的「成功機率函數」

### 3.1 網聊 (Online Chat)

- 網聊成功機率記為 $p_{\text{chat}}(\mathbf{C})$。  
- 例如，用線性近似： $p_{\text{chat}}(C) = a + b\cdot C$，其中 $a$ 表示最低可能成功率（對方很友善），$b$ 表示與真實相容度掛鉤的敏感度。  
- 網聊得到的觀測 $o_{\text{chat}} \in \{\text{成功}, \text{失敗}\}$ 之條件機率：
  $P(o_{\text{chat}}=\text{成功} \mid C) = p_{\text{chat}}(C)$,
  
  $P(o_{\text{chat}}=\text{失敗} \mid C) = 1 - p_{\text{chat}}(C).$

### 3.2 約會 (Face-to-Face)

- 約會成功機率 $p_{\text{date}}(C)$ 相對更靈敏，可設 $p_{\text{date}}(C) = a' + b' \cdot C$，且 \(b' > b\)。  
- 實際可能多分類（如大好/普通/糟糕），可用多項式形式來表示與 $\mathbf{C}$ 的對應關係。  
- 因約會包含更多非語言訊號、臨場氛圍，故對相容度有較高辨別力。

---

## 4. 貝氏更新與資訊增益

### 4.1 貝氏更新

1. 假設先驗分佈為 $P(C)$。  
2. 一次觀測 $o$ 後，後驗分佈：
   $P(C \mid o) \propto P(o \mid C)\, P(C).$
3. 不同互動方式帶來不同 $P(o \mid C)$，故更新後的分佈會有不同程度的「聚焦」。

### 4.2 期望資訊增益

- 用 Shannon 熵 $H(p)$ 量度分佈不確定度： $H(\text{prior}) - H(\text{posterior})$。  
- 一次互動的 **資訊增益 (Information Gain, IG)**：
  $\text{EIG} = \sum_{o} P(o)\, \bigl[H(\text{prior}) - H(\text{posterior}\mid o)\bigr].$
- 面對面約會若帶來更明確正/負觀測，更新幅度更大，EIG 通常也更高。

---

## 5. 成本函數與策略

1. **互動成本**  
   - 網聊成本相對低，但資訊增益也較小；  
   - 約會成本高（時間、金錢、心理壓力），但資訊增益較大。  
2. **單位成本資訊效率**  

   $\eta_{\text{chat}}$ = $\frac{\text{EIG}_{\text{chat}}}{\text{Cost}_{\text{chat}}}$,

   $\eta_{\text{date}}$ = $\frac{\text{EIG}_{\text{date}}}{\text{Cost}_{\text{date}}}.$
   
   - 依此指標判斷何時適合「跳過網聊」直接約會，或何時先透過網聊篩選。

---

## 6. 數值示例

1. **先驗：** $\mathbf{C} \sim \text{Beta}(1,1)$ (均勻)。  
2. **網聊：** $p_{\text{chat}}(C) = 0.3 + 0.5C$。  
3. **約會：** $p_{\text{date}}(C) = 0.1 + 0.8C$。  
4. **單回合模擬**：  
   - 用數值計算熵的改變，可發現約會帶來更高資訊增益；若其成本也高很多，就看你對時間/費用的預算。

---

## 7. 小結

透過此模型，能「理性化」衡量網聊與約會在「確認雙方適合度」上貢獻的資訊量。  
- **若資訊需求高且經費時間允許** → 面對面約會更快知道對方合不合。  
- **若成本顧慮多** → 先多次網聊，等有一定成功機率再進一步見面。  

此只是**示範**：真實世界多維度（如對話內容深度、非語言線索），尚需實驗數據或問卷來優化參數；本模型提供一條量化思路。

---

### 參考文獻

1. **Jaynes, E. T. (2003).** *Probability Theory: The Logic of Science.* Cambridge University Press.  
2. **Shannon, C. E. (1948).** A mathematical theory of communication. *The Bell System Technical Journal*, 27, 379–423.  
3. **Bishop, C. M. (2006).** *Pattern Recognition and Machine Learning.* Springer.  
4. **Gigerenzer, G., & Todd, P. M. (1999).** *Simple Heuristics That Make Us Smart.* Oxford University Press. (另闡述人類在交往決策的簡化策略)  
