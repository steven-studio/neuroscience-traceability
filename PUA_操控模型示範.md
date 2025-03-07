# PUA 操控模式數學模型示範

> **版本**：1.0  
> **作者**：游哲維  
> **日期**：2025-01-26  

---

## 前言

近來新聞與社交圈廣泛討論的 PUA（Pick-Up Artist）現象，已不僅止於「搭訕、吸引」的早期教學，許多後期「五步陷阱法」演變成**精神控制**，透過打擊自尊、操控心理來讓對方「離不開自己」。以下以**數學模型（抽象動態系統）**示範如何量化「加害者」對「被害者」的心理攻擊流程，以及為何被害者在負面循環中越陷越深。

---

## 1. 主要變數

1. **被害者自尊指數 $Z(t)$**  
   - 表示被PUA對象在時間 $t$ 的自尊/自信程度，範圍 $[0,1]$ 或 $\ge 0$。  
   - $Z(t)$ 高 → 相對具自信；$Z(t)=0$ 表示自我價值感幾乎被摧毀。

2. **加害者需求 / 控制慾 $C(t)$**  
   - 表示加害者(使用PUA手法)對「控制對方」之強度，$\ge 0$。  
   - 值越大 → 他越想透過話術、冷漠、打擊來操控被害者服從。

3. **感情 / 關係依附度 $A(t)$**  
   - 被害者對加害者的「依賴」或「愛」之強度，範圍 $[0,1]$ 或 $\ge 0$；  
   - 若 $A(t)$ 越高 → 被害者越「離不開」加害者，也越順從其要求。

4. **外部支持 / 親友聲音 $S(t)$**  
   - 表示被害者在外部(親友、心理專業、社群)獲得的「真實支持」程度；  
   - 值大 → 容易看清PUA問題並脫離；值小 → 更封閉於加害者操控。

---

## 2. 動態方程（示範）

### 2.1 被害者自尊 $Z(t)$ 的演化

$Z(t+1) = Z(t) - \alpha \bigl[C(t)\bigr] + \beta\,S(t)$.

- **解釋**：  
  - 加害者透過貶低、打擊(「你什麼都做不好」、「除了我沒人要你」)等行為 => $\alpha\,C(t)$ 使被害者自尊下降；  
  - 若外部支持 $S(t)$ 高 → 幫助被害者反思自己不如加害者所說般糟糕 => 增加自尊($\beta\,S(t)$)。

### 2.2 關係依附度 $A(t)$

$A(t+1) = A(t) + \gamma\bigl[\text{情緒綑綁}(Z(t), C(t))\bigr] - \gamma' \bigl[S(t)\bigr]$.

- **情緒綑綁**：加害者常用 「若你不做XX就是不愛我」等話術；當被害者自尊愈低($Z$低)、加害者操控慾 ($C$) 高，就容易**產生更強依附**(想證明自己愛加害者)；  
- 若外部支持 $S(t)$ 大 → 幫助被害者看清不健康關係 => $\gamma'\, S(t)$ 可減少依附度。

### 2.3 加害者控制慾 $C(t)$

$C(t+1) = C(t) + \delta_1 \bigl[\text{操控成功成癮}(A(t),Z(t))\bigr]$.

- 假設加害者透過一次次打擊自尊 => 看到被害者更服從 => 便更增強控制慾；  
- 亦可考慮外界(例如社會譴責)會抑制加害者行為，但此處簡化。

### 2.4 外部支持 $S(t)$

$S(t+1) = S(t) + \eta(\text{親友覺察 or 尋求幫助}) - \eta'(\text{被隔離在封閉環境})$.

- 若被害者多與朋友交流 => $S(t)$上升；  
- 若加害者隔離被害者、減少社交 => $S(t)$下降 => 使被害者更易陷入 PUA 陷阱。

---

## 3. 五步陷阱 vs. 模型

新聞提到 PUA 五步陷阱：吸引、探索、價值觀綁定、摧毀、虐待。可以對應於模型裡的**自尊指數 $Z$** 與 **依附度 $A$** 的逐步演化：

1. **吸引**：起初對方覺得加害者神秘/高價值 => 被害者自尊還在正常水準($Z$不低)，但產生好奇 => 依附度$A$開始升；  
2. **探索**：加害者假裝脆弱，讓被害者覺得自己「特別」，$A$ 升更快；  
3. **價值觀綁定**：開始與被害者要求承諾，若被害者答應 => $A$ 又大幅升；同時 $\alpha\,C$ 開始打壓 $Z$；  
4. **摧毀**：加害者大量指責 => $Z$迅速下降 ($\alpha\,C$拉大)；被害者低自尊下更依附 => $A$ 續升；  
5. **虐待**：在此階段 $Z\approx 0$，$A\approx 1$，被害者被完全操控。

此種「負面循環」體現模型中：**自尊被持續打壓**而 **依附度持續增加**，導致被害者深陷。

---

## 4. 小示例

假設初始： 
- $Z(0)=0.6$（自尊中等）、$A(0)=0.2$（依附低），$C(0)=0.3$（加害者控制慾普通），$S(0)=0.5$（外部支持普通）。  
- 加害者開始運用 PUA 話術 => 逐輪更新後：  
  - $Z(t)$ 受 $\alpha\,C(t)$打擊越來越低；  
  - $A(t)$ 受 $\gamma(\text{低自尊 + 加害者誘導})$↑ => 慢慢逼近 1；  
  - 若$S(t)$無法提升(被隔離)，最後 $Z\approx0, A\approx1$，被害者無法自拔 => 符合「五步陷阱」最終完全被操控。

---

## 5. 預防或脫離：模型視角

1. **增加外部支持 $S(t)$**：找朋友分享、專業協助 => $S$升，進而幫助抑制依附度$A$，改善自尊$Z$。  
2. **減少加害者控制慾 $C$**：社會輿論、法律約束 => 使加害者不敢繼續操控。  
3. **自我評價重建**：若被害者能藉由正面資源提高$\beta\,S$ => 恢復$Z$，終能擺脫 PUA。

---

## 結論

此**PUA操控**數學模型將：
- **被害者自尊 $Z$**、**依附度 $A$**  
- **加害者控制慾 $C$**  
- **外部支持 $S$**  
放入幾條動態方程，展示五步陷阱(打擊自尊、操縱心理)之負面循環，以及「外部幫助與自我評價重建」如何幫助脫離這種**精神控制**。

配合新聞中對 PUA 的描述與案例，可見此模型能解釋為何在不斷被打擊與綁定的關係中，受害者越發低自尊、越聽命於加害者；若外部支持不足，就很難擺脫。
