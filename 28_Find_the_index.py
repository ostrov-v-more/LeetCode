'''
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''

class Solution:
    @staticmethod
    def strStr_1(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    @staticmethod
    def strStr_2(haystack: str, needle: str) -> int:  # Алгоритм Бойера — Мура — Хорспула

        # Этап 1: формирование таблицы смещений
        needle_set = set()  # уникальные символы в образе
        needle_len = len(needle)  # число символов в образе
        needle_dict = {}  # словарь смещений
        for i in range(needle_len - 2, -1, -1):  # итерации с предпоследнего символа
            if needle[i] not in needle_set:  # если символ еще не добавлен в таблицу
                needle_dict[needle[i]] = needle_len - i - 1
                needle_set.add(needle[i])
        if needle[needle_len - 1] not in needle_set:  # отдельно формируем последний символ
            needle_dict[needle[needle_len - 1]] = needle_len
        needle_dict['*'] = needle_len  # смещения для прочих символов
        print(needle_dict)

        # Этап 2: поиск образа в строке
        haystack_len = len(haystack)
        if haystack_len >= needle_len:
            i = needle_len - 1  # счетчик проверяемого символа в строке
            while (i < haystack_len):
                k = 0
                j = 0
                flBreak = False
                for j in range(needle_len - 1, -1, -1):
                    if haystack[i - k] != needle[j]:
                        if j == needle_len - 1:
                            off = needle_dict[haystack[i]] if needle_dict.get(haystack[i], False) else needle_dict[
                                '*']  # смещение, если не равен последний символ образа
                        else:
                            off = needle_dict[needle[j]]  # смещение, если не равен не последний символ образа
                        i += off  # смещение счетчика строки
                        flBreak = True  # если несовпадение символа, то flBreak = True
                        break
                    k += 1  # смещение для сравниваемого символа в строке
                if not flBreak:  # если дошли до начала образа, значит, все его символы совпали
                    print(f"образ найден по индексу {i - k + 1}")
                    return i - k + 1
                    break
            else:
                print("образ не найден")
                return -1
        else:
            print("образ не найден")
            return -1



