# ������� �� ����� ���� � ������� ������� ASCII, ������� � ������� ��� ������� 32 � ���������� 
# 127-� ������������. ����� ��������� � ��������� �����: �� ������ ��� "���-������" � ������ ������.


print("ASCII character table 32 through 127 inclusive")

i = 32
j = 0
string = ""

while i <= 127:
    
    string = string + str(i) + " " + str(chr(i)) + "    "
    i = i + 1
    j = j + 1
    if ((j % 10) == 0) or (i == 128):
        print(string)
        string = ""
    