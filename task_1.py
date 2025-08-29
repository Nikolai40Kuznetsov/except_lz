import math

class Octagon():
    '''класс октагона'''
    def __init__(self,len:int, CORNER:int = 135,K:float = 1+math.sqrt(2)):
        self.len = len
        self.CORNER = CORNER
        self.K = K
    
    def print_radius(self)-> None:
        '''выводит информацию об радиусе описаной окружности и его площади'''
        radius = (self.len/2)*self.K
        square = math.pi* radius**2
        print(f"Радиус описаной окружности равен = {radius}\nа его площадь равна ={square}\n")

    def print_radius_min(self)-> None:
        '''выводит информацию об радиусе вписаной окружности и его площади'''
        radius = math.sqrt(self.K/(self.K - 1 )) * self.len
        square_polygon = radius**2
        
        
        print(f"Радиус вписаной окружности равен = {radius}\nа его площадь равна ={square_polygon}\n")

    def print_octagon(self)->None:
        '''Выводит информацию об радиусе и периметре октагона'''
        square_polygon = 2*self.K*self.len**2
        perimetr = 8* self.len 
        print(f"Периметр октагона равен = {perimetr}\nа его площадь равна ={square_polygon}\n")


def main():
    lenth = int(input("Введите длину стороны октагона "))
    print()
    octag= Octagon(lenth)
    octag.print_radius()
    octag.print_radius_min()
    octag.print_octagon()

if __name__ =="__main__":
    main()