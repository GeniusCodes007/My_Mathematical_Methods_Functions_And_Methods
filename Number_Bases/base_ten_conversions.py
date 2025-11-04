def count(word:str, character:str)->int:
    take_note =0
    for letter in word:
        if letter == character:
            take_note = take_note + 1
    return take_note


hexa_extras = ["A", "B", "C", "D", "E", "F"]

#This Function Converts Base 10 Decimals To Decimals Of The Specified Base
def from_decimal_conversions(base_num:int, decimal_num:str="0") -> str | None:
    try:
        if decimal_num == "":
            return None
        if decimal_num == "0":
            return "0"

        #Converts The Decimal Number To A Floating Point Number, For Evaluation
        working_num= float(f"0.{decimal_num}")
        answer = "0."
        multiplied = working_num

        #While Loop Keeps Running As Long As The 'multiplied' variable Is Not Equal To Zero Yet
        while multiplied != 0:
            #multiplied is evaluated
            multiplied = multiplied * base_num
            #answer is built up
            answer = answer + str(int(multiplied))
            #multiplied is re-assigned a new value
            multiplied = abs(multiplied - int(multiplied))

            #In The Case Of Recurring Decimals, The Loop Breaks As Soon As The Length of 'answer' variable equals '14'
            if len(answer) == 14:
                break
        return answer
    except ValueError:
        return None

#For Example In The Commented Code Below, Converts 0.375 in Base 10 To A Base Two Equivalent Decimal
#print(from_decimal_conversions(2, "375"))# -> 0.011 In Base Two


#This Function Converts Decimals in The Base Specified To Equivalent Base 10 Decimal
def to_decimal_conversion(base_num:int, decimal_num:str)-> int|None:
    try:
        if decimal_num == "":
            return None
        if decimal_num == "0":
            return 0
        answer = 0
        for digit in range(len(decimal_num)):
            if int(decimal_num[digit]) >= base_num:
                return None
            answer = answer + (int(decimal_num[digit]) * (base_num ** -(digit+1)))
        return answer
    except ValueError:
        return None


#For Example In The Commented Code Below, Converts 0.12 in Base 4 To A Base 10 Equivalent Decimal
#print(to_decimal_conversion(4, "12"))

class Base_Ten_Conversions:

    @staticmethod
    def base10_to_binary(number:str) -> str | None:
        try:
            div = int(number[0:number.index('.')])
            answer = ""
            while div != 0:
                rem = div % 2
                div = div // 2
                answer = str(rem) + answer
            answer = int(answer) + float(from_decimal_conversions(2, number[number.index('.')+1:]))
            return str(answer)
        except ValueError:
           return None

    def base10_to_other_base(self,number:str, base_num:int) -> str | None :
        try:
            if base_num == 16:
                return self.base10_to_hexa(number)
            if 1 <= base_num <= 10:
                if '.' in number and count(number, '.') == 1:
                    dec_num=float(from_decimal_conversions(base_num, number[number.index('.') + 1:]))
                    div = int(number[0:number.index('.')])

                elif count(number, '.') > 1:
                    return None

                else:
                    dec_num= 0
                    div = int(number)

                answer = ""
                while div != 0:
                    rem = div % base_num
                    div = div // base_num
                    answer = str(rem) + answer
                answer = int(answer) + dec_num
                return str(answer)

        except ValueError:
            return None
    #This Needs Work
    @staticmethod
    def base10_to_hexa(number: str) -> str | None :
        try:
            div = abs(int(number))
            answer = ""
            while div != 0:
                rem = div % 16
                div = div // 16

                if rem == 10:
                    rem = 'A'
                elif rem == 11:
                    rem = 'B'
                elif rem == 12:
                    rem = 'C'
                elif rem == 13:
                    rem = 'D'
                elif rem == 14:
                    rem = 'E'
                elif rem == 15:
                    rem = 'F'

                answer = str(rem) + answer

            return answer
        except ValueError:
            return None

ten = Base_Ten_Conversions().base10_to_other_base("16.1",16)
