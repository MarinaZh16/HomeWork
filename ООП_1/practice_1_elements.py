class Element():
    def __init__(self, melt_temp, vapor_temp):
        self.melt_temp=melt_temp
        self.vapor_temp=vapor_temp
    def convert_to_c(self, temp, scale):
        if scale=="K":
            temp=temp-273
        if scale=="F":
            temp=temp*9/5+32
        return temp
        
    def agg_state(self, temp, scale="C"):
        temp=self.convert_to_c(temp, scale)            
        if temp < self.melt_temp:
            return "SOLID", temp
        if temp >= self.vapor_temp:
            return "GAS", temp
        return "LIQUID", temp
    

oxygen=Element(melt_temp=-218, vapor_temp=-182)
iron=Element(melt_temp=1538, vapor_temp=2862)
print(oxygen.agg_state(-190, "F"))
print(iron.agg_state(2000, "K"))
