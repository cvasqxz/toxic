'''
encodes LV64 cipher
Public Function LV64(data As String) As String
Dim i As Integer
If data - 3 > 0 Then
	For i = 0 To 3
		If ((data - i) Mod 4) = 0 Then
		cod1 = i + 80
		cod1 = Chr(cod1)
		cod2 = (data - i) / 4 + 64
		cod2 = Chr(cod2)
		End If
	 Next i
LV64 = cod1 & cod2
Else
LV64 = Chr(data + 72)
End If
End Function
'''


def LV64(data):
	if data <= 3:
		return chr(data + 72)

	for i in range(4):
		if (data - i) % 4 == 0:
			cod1 = chr(i + 80)
			cod2 = chr(round((data - i) / 4) + 64)
			return cod1 + cod2
