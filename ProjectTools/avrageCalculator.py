def avrageCalc(marks):
    if marks.size <= 0:
        print("Es sind keine Noten vorhanden")
    sum = 0
    for x in marks:
        sum = sum + marks.get(x)
    sumMark = sum / marks.size
    return sumMark