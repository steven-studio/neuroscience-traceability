import random
import math
import matplotlib.pyplot as plt
from collections import Counter

def interaction_success_prob(burden, test_strength):
    """
    根據道德包袱 (burden) 與女性測試強度 (test_strength) 
    來計算成功率 S(m,w)。
    這裡用指數遞減的概念: S = exp(-(alpha1*burden + alpha2*test_strength))
    """
    alpha1 = 0.5  # 道德包袱權重
    alpha2 = 0.3  # 測試強度權重
    exponent = -(alpha1 * burden + alpha2 * test_strength)
    p = math.exp(exponent)  # p in (0,1]
    return p

def simulate_round(burden, test_strength):
    """
    給定當前道德包袱 'burden' 與測試強度 'test_strength'，隨機判斷這一輪成功或失敗。
    回傳 (success_boolean, new_burden)
    - success_boolean: True/False 是否成功
    - new_burden: 若失敗則道德包袱增加
    """
    p = interaction_success_prob(burden, test_strength)
    r = random.random()
    success = (r < p)
    if success:
        # 成功 => 道德包袱可稍微減輕
        new_burden = max(0, burden - 0.2)
    else:
        # 失敗 => 道德包袱進一步加深
        new_burden = burden + 0.5
    return success, new_burden

def main_simulation(num_rounds=10, men_count=3):
    """
    模擬 num_rounds 回合、men_count 名男人同時把妹。
    假設 test_strength 為隨機 0~2, 代表女性測試性話術強度。
    每回合同一 test_strength 會同時施加給多個男人。
    初始道德包袱皆為 1.0
    """
    burdens = [1.0 for _ in range(men_count)]
    success_counts = [0 for _ in range(men_count)]

    for rnd in range(1, num_rounds+1):
        # 每回合隨機產生一個 test_strength
        test_strength = random.uniform(0, 2)

        print(f"\n=== 第 {rnd} 回合，test_strength = {test_strength:.2f} ===")
        
        # 所有男人都經歷同樣的測試
        for i in range(men_count):
            success, new_burden = simulate_round(burdens[i], test_strength)
            burdens[i] = new_burden
            if success:
                success_counts[i] += 1
            
            print(f"  男人#{i+1}: success={success}, new_burden={burdens[i]:.2f}")

    print("\n==== 最終結果 ====")
    for i in range(men_count):
        print(f"男人#{i+1}: 成功次數={success_counts[i]}, 最終道德包袱={burdens[i]:.2f}")

    # ====== 繪製柱狀圖 =======
    # step1: 統計各種成功次數(0, 1, 2, ...)
    count_dict = Counter(success_counts)
    # step2: 準備 x 軸(成功次數) & y 軸(對應男人人數)
    x_vals = sorted(count_dict.keys())
    y_vals = [count_dict[x] for x in x_vals]

    # step3: 繪圖
    plt.bar(x_vals, y_vals, color='skyblue', edgecolor='black')
    plt.xlabel("邀約成功次數")
    plt.ylabel("男人數量")
    plt.title("道德包袱下把妹成功次數分布")
    plt.xticks(x_vals)  # 確保 x 軸顯示整數標籤
    plt.show()

if __name__ == "__main__":
    main_simulation(num_rounds=10, men_count=1000)
