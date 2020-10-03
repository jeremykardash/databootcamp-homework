Sub VBAofWallStreet():

    Dim ticker As String
    Dim volume As Double
    Dim YrChange As Double
    Dim PctChange As Double
   
    Dim YrOpen As Double
    Dim start As Long

    Dim YrClose As Double
    Dim lastrow As Long
    Dim SumRow As Double
        
        
For Each ws In Worksheets
lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
SumRow = 2
start = 2
PctChange = 0
YrChange = 0
volume = 0
    ws.Cells(1, 9).Value = "Ticker"
    ws.Cells(1, 10).Value = "Yearly Change"
    ws.Cells(1, 11).Value = "Percent Change"
    ws.Cells(1, 12).Value = "Volume"

For i = 2 To lastrow

    If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
        ticker = ws.Cells(i, 1).Value
        volume = volume + ws.Cells(i, 7).Value

            ws.Range("I" & SumRow).Value = ticker
            ws.Range("L" & SumRow).Value = volume
        
        YrClose = ws.Cells(i, 6).Value

        If Cells(start, 3).Value = 0 Then
            For Value = start To i
                If Cells(Value, 3).Value <> 0 Then
                    start = Value
                    Exit For
                End If
            Next Value
        End If
    
        YrChange = Cells(i, 6) - Cells(start, 3)
        PctChange = Round((YrChange / Cells(start, 3)) * 100, 2)
        
        start = i + 1

        ws.Range("J" & SumRow).Value = YrChange
        ws.Range("K" & SumRow).Value = "%" & PctChange
        
        volume = 0
        YrChange = 0
        PctChange = 0
        SumRow = SumRow + 1
    Else
        volume = volume + ws.Cells(i, 7).Value

    End If

    
Next i

For c = 2 To lastrow
     If ws.Cells(c, 11).Value >= 0 Then
            ws.Cells(c, 11).Interior.Color = vbGreen
         Else
            ws.Cells(c, 11).Interior.Color = vbRed
     End If

Next c

ws.Range("O2").Value = "Greatest Percent Increase"
ws.Range("O3").Value = "Greatest Percent Decrease"
ws.Range("O4").Value = "Greatest Volume"
ws.Range("P1").Value = "Ticker"
ws.Range("Q1").Value = "Value"

ws.Range("Q2").Value = WorksheetFunction.Max(ws.Range("K2:K" & lastrow))
ws.Range("Q2").Style = "Percent"
ws.Range("Q3").Value = WorksheetFunction.Min(ws.Range("K2:K" & lastrow)) 
ws.Range("Q3").Style = "Percent"
ws.Range("Q4").Value = WorksheetFunction.Max(ws.Range("L2:L" & lastrow)) 

increase_ticker = WorksheetFunction.Match(WorksheetFunction.Max(ws.Range("K2:K" & lastrow)), ws.Range("K2:K" & lastrow), 0)
decrease_ticker = WorksheetFunction.Match(WorksheetFunction.Min(ws.Range("K2:K" & lastrow)), ws.Range("K2:K" & lastrow), 0)
volume_ticker = WorksheetFunction.Match(WorksheetFunction.Max(ws.Range("L2:L" & lastrow)), ws.Range("L2:L" & lastrow), 0)

ws.Range("P2").Value = ws.Cells(increase_ticker + 1, 9)
ws.Range("P3").Value = ws.Cells(decrease_ticker + 1, 9)
ws.Range("P4").Value = ws.Cells(volume_ticker + 1, 9)


Next ws
End Sub
