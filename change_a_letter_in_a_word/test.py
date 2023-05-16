def assert_equals(result, case, err="test failed"):
    print("correct answer "+str(case)+" giver result "+str(result))
    assert case == result, err
    return print("test is passed")
