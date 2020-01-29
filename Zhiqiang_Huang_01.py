import math
import unittest


def classify_triangle(a, b, c):
    """
    input: three valid digit number
    return: a list with two elements except the input number can't be a triangle
    """
    num = [a, b, c]
    num.sort()

    if num[0] > 0 and num[1] > 0 and num[2] > 0:
        if num[0] + num[1] > num[2]:
            if num[0] == num[2]:
                return ['equilateral', 'non-right']

            elif num[0] == num[1] or num[1] == num[2]:
                if math.sqrt(math.pow(max(num), 2)) == math.sqrt(2 * math.pow(min(num), 2)):
                    return ['isosceles', 'right']
                else:
                    return ['isosceles', 'non-right']

            else:
                if math.pow(num[2], 2) == math.pow(num[0], 2) + math.pow(num[1], 2):
                    return ['scalene', 'right']
                else:
                    return ['scalene', 'none-right']

        else:
            return None

    else:
        return None


class TestClassifyTriangle(unittest.TestCase):
    def test_classify_triangle(self):
        self.assertTrue(not classify_triangle(0, 11, 2))
        self.assertTrue(not classify_triangle(-1, 2, 3))
        self.assertTrue(not classify_triangle(1, 1, 2))
        self.assertTrue(classify_triangle(3, 3, 3) == ['equilateral', 'non-right'])
        self.assertTrue(classify_triangle(2, 3, 2) == ['isosceles', 'non-right'])
        self.assertTrue(classify_triangle(math.sqrt(2),1,1) == ['isosceles', 'right'])
        self.assertTrue(classify_triangle(3, 5, 4) == ['scalene', 'right'])
        self.assertTrue(classify_triangle(3, 2.5, 1) == ['scalene', 'none-right'])


def main():
    print('please input three parameter to present three triangle length')
    a = input('input the first length of side\n')
    b = input('input the second length of side\n')
    c = input('input the third length of side\n')
    try:
        lis = classify_triangle(float(a), float(b), float(c))
        if lis:
            print('This triangle is a ' + lis[1] + ' ' + lis[0] + ' triangle')
            print(lis)
        else:
            print('Those inputs can not be a triangle')

    except ValueError:
        raise ValueError('the input include none-digit input')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)
