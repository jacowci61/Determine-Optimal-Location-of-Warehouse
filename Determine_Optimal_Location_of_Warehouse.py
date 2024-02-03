import matplotlib.pyplot as plot
import random
import numpy as np

# region GlobalVariables
global AmountOfConsumers
global TransportationCost
global VolumeOfConsumption
global Case
# endregion


def WarehouseWithEqualCosts():
    
    # region CostEqualOrNot
    IsTransportationCostEqual = str(input("Is transportation cost equal for all consumers? Yes/No \n"))

    while (IsTransportationCostEqual.lower() == 'yes' or IsTransportationCostEqual.lower() == 'no') == False:
            IsTransportationCostEqual == ''
            IsTransportationCostEqual = str(input("Incorrect input. Is transportation cost equal for all consumers? Yes/No \n"))
    # endregion


    # region CostEqual
    if IsTransportationCostEqual.lower() == 'yes':
        
        # region AmountOfConsumers
        try:
            AmountOfConsumers = int(input("Enter amount of consumers: "))
        except ValueError:
            AmountOfConsumers = ''
            AmountOfConsumers = input("Incorrect input type. Enter amount of consumers as integer: \n")
        
        while(AmountOfConsumers < 0) == True:
            AmountOfConsumers = ''
            AmountOfConsumers = int(input("Incorrect number of consumers. Enter amount of consumers as positive integer: \n"))
        ListOfConsumers =[None] * AmountOfConsumers  # [x,y,consumption,transportation cost]
        # endregion
        
        # region FillArray
        TransportationCost = int(input("Enter transportation cost: "))  
        
        for i in range(AmountOfConsumers):
            VolumeOfConsumption = int(input("Enter volume of consumption for " + str(i+1) + " consumer: "))      
            ListOfConsumers[i] = [random.randint(0,100), random.randint(0,100), VolumeOfConsumption, TransportationCost]
            VolumeOfConsumption = 0
        # endregion
        
        # region WarehouseCoordinates
        NumeratorX = 0
        NumeratorY = 0
        Denominator = 0
       
        for i1 in range(AmountOfConsumers): 
            NumeratorX += ListOfConsumers[i1][2] * ListOfConsumers[i1][0]
            NumeratorY += ListOfConsumers[i1][2] * ListOfConsumers[i1][1]
            Denominator += ListOfConsumers[i1][2]
            
        WarehouseCoordinates = [NumeratorX / Denominator, NumeratorY / Denominator]
        # endregion
        
    # endregion

    # region CostUnequal    
    elif IsTransportationCostEqual.lower() == 'no':
        try:
            AmountOfConsumers = int(input("Enter amount of consumers: "))
        except ValueError:
            AmountOfConsumers = ''
            AmountOfConsumers = input("Incorrect type. Enter amount of consumers as integer: \n")
                
        while(AmountOfConsumers < 0) == True:
                    AmountOfConsumers = ''
                    AmountOfConsumers = int(input("Incorrect number of consumers. Enter amount of consumers as positive integer: \n"))
            
        ListOfConsumers =[None] * AmountOfConsumers  # [x,y]
        
        for i2 in range(AmountOfConsumers):
            VolumeOfConsumption = int(input("Enter volume of consumption for " + str(i2+1) + " consumer: "))
            TransportationCost = int(input("Enter transportation cost for " + str(i2+1) + " consumer: "))  
            ListOfConsumers[i2] = [random.randint(0,100), random.randint(0,100), VolumeOfConsumption, TransportationCost]
            TransportationCost = 0
            VolumeOfConsumption = 0
            
        NumeratorX = 0
        NumeratorY = 0
        Denominator = 0
        for i3 in range(AmountOfConsumers): 
            NumeratorX += ListOfConsumers[i3][2] * ListOfConsumers[i3][0] * ListOfConsumers[i3][3]
            NumeratorY += ListOfConsumers[i3][2] * ListOfConsumers[i3][1] * ListOfConsumers[i3][3]
            Denominator += ListOfConsumers[i3][2] * ListOfConsumers[i3][3]
            
        WarehouseCoordinates = [NumeratorX / Denominator, NumeratorY / Denominator]
    # endregion
        
    # region DisplayResults
    print(str(ListOfConsumers) + '\n' + str(WarehouseCoordinates))
    
    tempX = [None] * AmountOfConsumers
    tempY = [None] * AmountOfConsumers
    for i4 in range(AmountOfConsumers):
        tempX[i4] = ListOfConsumers[i4][0]
        tempY[i4] = ListOfConsumers[i4][1]
        
    ConsumersX = np.array(tempX)
    ConsumersY = np.array(tempY)
    
    plot.xlim(0,110)
    plot.ylim(0,110)
    plot.scatter(ConsumersX,ConsumersY)
    plot.plot(WarehouseCoordinates[0],WarehouseCoordinates[1],'ro')
    plot.show()
    # endregion
    
WarehouseWithEqualCosts()