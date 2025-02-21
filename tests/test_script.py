from mutation.script import calculate_membership_fee

def test_minor_non_student():
    # 18歳未満かつ非学生の場合、正確な料金をチェック
    assert calculate_membership_fee(16, False) == 5.0

def test_minor_student():
    # 18歳未満かつ学生の場合、割引後の料金をチェック
    assert calculate_membership_fee(16, True) == 4.0  # 5.0 * 0.8

def test_adult_non_student():
    # 18歳以上 65歳未満かつ非学生の場合
    assert calculate_membership_fee(30, False) == 20.0

def test_adult_student():
    # 18歳以上 65歳未満かつ学生の場合
    fee = calculate_membership_fee(30, True)
    # ここでは、基本料金より割引後の料金が下がっていることだけを確認しており、具体的な数値はチェックしていない
    assert fee < 20.0

def test_senior_non_student():
    # 65歳以上かつ非学生の場合
    assert calculate_membership_fee(70, False) == 15.0

def test_senior_student():
    # 65歳以上かつ学生の場合
    fee = calculate_membership_fee(70, True)
    # 基本料金が割引適用後に減っているかだけのチェック（具体的な割引率は検証していない）
    assert fee < 15.0