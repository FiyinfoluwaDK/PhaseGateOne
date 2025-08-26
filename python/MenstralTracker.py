# Menstrual Cycle Tracker

def predictNextPeriod(startDay, cycleLength):
    return startDay + cycleLength

def getOvulationDay(startDay, cycleLength):
    return startDay + (cycleLength // 2)

def getSafeDays(startDay, cycleLength):
    ovulation = getOvulationDay(startDay, cycleLength)
    fertileWindow = list(range(ovulation - 4, ovulation + 5))  
    allDays = list(range(startDay, startDay + cycleLength))
    safeDays = [day for day in allDays if day not in fertileWindow]
    return safeDays


flowStartDay = 1          
cycleLength = 28            

nextPeriod = getNextPeriod(flowStartDay, cycleLength)
ovulationDay = getOvulationDay(flowStartDay, cycleLength)
safeDays = getSafeDays(flowStartDay, cycleLength)


print("Menstrual Cycle Summary")
print("Flow Start Day:", flowStartDay)
print("Cycle Length:", cycleLength, "days")
print("Next Expected Period Day:", nextPeriod)
print("Ovulation Day:", ovulationDay)
print("Safe Days:", safeDays)