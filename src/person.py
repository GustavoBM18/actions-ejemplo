class Person:
    """
    Clase Person que representa una persona con nombre y apellido.
    
    Esta clase implementa el método especial _str_ para mostrar
    el nombre completo de la persona en formato capitalizado.
    """
    
    def _init_(self, first_name, last_name):
        """
        Inicializa una persona con nombre y apellido.
        
        Args:
            first_name (str): El nombre de la persona
            last_name (str): El apellido de la persona
        """
        self.first_name = first_name
        self.last_name = last_name
    
    def _str_(self):
        """
        Retorna una representación en string de la persona.
        
        El formato es "Nombre Apellido" con la primera letra de cada
        palabra en mayúscula (capitalizado).
        
        Returns:
            str: Nombre completo capitalizado.
        """
        return f"{self.first_name} {self.last_name}".title()   


# Ejemplo de uso (opcional, para pruebas locales)
if _name_ == "_main_":
    # Crear personas de ejemplo
    p1 = Person("juan", "perez")
    p2 = Person("MARIA", "LOPEZ")
    p3 = Person("cArLoS", "gOnZaLeZ")
    
    # Imprimir usando _str_ automáticamente
    print(p1)  # Juan Perez
    print(p2)  # Maria Lopez
    print(p3)  # Carlos Gonzalez