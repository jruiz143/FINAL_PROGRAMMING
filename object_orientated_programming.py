#FINAL EXAM QUESTION 1


#DEFINE RECTANGLE CLASS
class Rectangle:
    def __init__(self, width, height):
        #INITIALIZE ATTRIBUTES
        self.__width = width
        self.__height = height

    #SET ATTRITBUTES (ACCESSOR METHOD)
    def set_width(self, width):
        self.__width = width
    
    def set__height(self, height):
        self.__height

    #GET ATTRIBUTES (MUTATORS)
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    #CALCULATE RECTANGLE PERIMETER AND AREA
    def calculate_perimeter(self):
        width = self.__width
        height = self.__height
        perimeter = 2 * (width + height)
        return perimeter
    def calculate_area(self):
        width = self.__width
        height = self.__height
        area = width * height
        return area
    
    #DISPLAY OUTPUTS
    def display(self):
        print("WIDTH:", self.__width)
        print("HEIGHT:", self.__height)
        print("AREA:", self.calculate_area())
        print("PERIMETER:", self.calculate_perimeter())
#CALL MAIN
if __name__ == "__main__":

    rect = Rectangle(5, 10)
    rect.display()



    
