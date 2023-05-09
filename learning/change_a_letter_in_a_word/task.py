import test


def one_edit_apart(first: str, other: str):
    if len(first) - 1 > len(other) or len(other) > len(first) + 1:
        print("words are too difference")
        return False
    res = False
    print(other)
    # seq = 0
    # shift = 0
    # prev_l = ""
    # if first in other:
    #     if first == other[-len(first):]:
    #         print("it needs to delete the first letter")
    #         return True
    #     elif first == other[:len(first)]:
    #         print("it needs to delete the last letter")
    #         return True
    # if first[:len(first)-1] == other and len(other) == len(first)-1:
    #     print("it needs to add the last letter")
    #     return True
    # elif first[-len(first)+1:] == other and len(other) == len(first)-1:
    #     print("it needs to add the first letter")
    #     return True
    #######################################################################
    # for i, l in enumerate(other):
    #     print(l, i)
    #     if (l != first[shift - i] and shift == i) or l == prev_l:
    #         shift += 1
    #     elif i - shift <= len(first) - 1:
    #         if l == first[i - shift]:
    #             seq += 1
    #             prev_l = l
    #     else:
    #         seq -= 1
    # if seq < len(first) - 1 or shift > 1:
    #     print("Too short sequence", seq, first, other)
    #     print("or")
    #     print("Too big shift", shift, first, other)
    #     res = False
    # else:
    #     print("word can be changed in 1 movement", first, other, shift, seq)
    #     res = True
    ######################################################################
    # seq_r = 0
    # seq_l = 0
    # shift_r = 0
    # shift_l = 0
    # for i, l in enumerate(other):
    #     print("processing", i, l)
    #     if i - shift_l < len(first):
    #         print("compared letters from LEFT", other[i], first[i - shift_l])
    #         if l == first[i - shift_l]:
    #             seq_l += 1
    #         elif i <= len(first):
    #             if l == first[i]:
    #                 seq_l += 1
    #         else:
    #             shift_l += 1
    #             # seq_l -= 1
    #         print("LEFT sequence is", seq_l)
    #         print("LEFT shift is", shift_l)
    #     if (-i - shift_r - 1)*(-1) < len(first):
    #         print("compared letters from RIGHT", other[-i - 1], first[-i - shift_r - 1])
    #         if other[-i - 1] == first[-i - shift_r - 1]:
    #             seq_r += 1
    #         elif other[-i - 1] == first[-i - 1]:
    #             if other[-i - 1] == first[-i - shift_r - 1]:
    #                 seq_r += 1
    #         else:
    #             shift_r += 1
    #             # seq_r -= 1
    #         print("RIGHT sequence is", seq_r)
    #         print("RIGHT shift is", shift_r)
    # if len(first) - 1 <= seq_l <= len(first) + 1:
    #     res = True
    # if len(first) - 1 <= seq_r <= len(first) + 1:
    #     res = True
    # if len(other) == 3:
    #     if seq_l == 1:
    #         res = True
    #     if seq_r == 1:
    #         res = True
    ################################################################################
    fail = 0
    shift = 0
    # for i, l in enumerate(other):
    #     print("processing", i, l)
    #     if fail >= 2:
    #         return False
    #     if i + 1 <= len(first):
    #         if l != first[i] and fail == 0:
    #             print("comparing", l, "with", first[i + shift])
    #             fail += 1
    #             print("first err")
    #             if other[i + 1] == first[i]:
    #                 shift -= 1
    #                 print("RIGHT SHIFT")
    #             elif other[i] == first[i + 1]:
    #                 shift += 1
    #                 print("LEFT SHIFT")
    #             elif other[i + 1] == first[i + 1]:
    #                 shift = 0
    #                 print("MISSED LETTER")
    #             else:
    #                 return False
    #         elif fail == 1 and i + 1 <= len(first):
    #             fli = i + shift
    #             if fli > len(first):
    #                 fli = -(fli)
    #             print("comparing", l, "with", first[i + shift])
    #             if l != first[fli]:
    #                 fail += 1
    #                 print("Second err")
    #     print("fail is ", fail)
    #########################################################################
    for i, l in enumerate(other):
        print("processing", i, l)
        fli = i + shift
        if fli >= len(first):
            fli = -fli
        print("first letter index is", fli)
        if fail >= 2:
            return False
        if fail == 0 and l != first[fli]:
            print("comparing", l, "with", first[fli])
            fail += 1  # increase counter
            print("first err")
            if other[fli + 1] == first[fli]:  # if it is right shift
                shift -= 1
                print("RIGHT SHIFT")
            elif other[fli] == first[fli + 1]:  # if it is left shift
                shift += 1
                print("LEFT SHIFT")
            elif other[fli + 1] == first[fli + 1]:  # if it is letter missing
                shift = 0
                print("MISSED LETTER")
            else:
                return False
        elif fail == 1:
            print("comparing", l, "with", first[fli])
            if l != first[fli]:  # if next letter with shift will be also incorrect increase fail counter
                fail += 1  # increase counter
                print("Second err")
        print("fail is ", fail)
    if fail < 2:
        res = True
    return res


if __name__ == "__main__":
    # test                function       input       expected result
    test.assert_equals(one_edit_apart("cat", "dog"), False)
    test.assert_equals(one_edit_apart("cat", "caats"), False)
    test.assert_equals(one_edit_apart("cat", "cats"), True)
    test.assert_equals(one_edit_apart("cat", "ccat"), True)
    test.assert_equals(one_edit_apart("cat", "ccccat"), False)
    test.assert_equals(one_edit_apart("cat", "catt"), True)
    test.assert_equals(one_edit_apart("cat", "catttt"), False)
    test.assert_equals(one_edit_apart("cat", "bcat"), True)
    test.assert_equals(one_edit_apart("cat", "at"), True)
    test.assert_equals(one_edit_apart("cat", "ca"), True)
    test.assert_equals(one_edit_apart("cat", "cut"), True)
    test.assert_equals(one_edit_apart("cat", "cast"), True)
    test.assert_equals(one_edit_apart("cat", "acts"), False)
    test.assert_equals(one_edit_apart("cat", "tct"), False)
    test.assert_equals(one_edit_apart("sister", "tsiter"), False)
    test.assert_equals(one_edit_apart("sister", "sister"), True)
    test.assert_equals(one_edit_apart("sister", "ssister"), True)
    test.assert_equals(one_edit_apart("sister", "sssister"), False)
    test.assert_equals(one_edit_apart("sister", "sisterr"), True)
    test.assert_equals(one_edit_apart("sister", "sisterrr"), False)
    test.assert_equals(one_edit_apart("sister", "siter"), True)
    test.assert_equals(one_edit_apart("sister", "sisrter"), True)
    test.assert_equals(one_edit_apart("sister", "sriste"), True)
