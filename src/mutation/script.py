def calculate_membership_fee(age: int, is_student: bool) -> float:
    """
    会員料金を年齢と学生判定に基づいて計算する関数です。

    - 18歳未満: 基本料金は 5.0
    - 18歳以上 65歳未満: 基本料金は 20.0
    - 65歳以上: 基本料金は 15.0
    - 学生の場合は基本料金に 20% の割引を適用
    """
    if age < 18:
        fee = 5.0
    elif age < 65:
        fee = 20.0
    else:
        fee = 15.0

    if is_student:
        fee *= 0.8  # 学生割引の係数（0.8）の部分が、ミューテーションに弱い
    return fee