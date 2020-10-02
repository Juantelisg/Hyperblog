import time



class CajaRegistradora:

    _IMAGENES = ['''

            _____________________________________
           |                       |            |   
           |                       |            |   
           |                       |            |   
           |  CAJA REGISTRADORA    |            |  
           |                       |            |   
           |                       |            |  
           |_______________________|            |
          / __|_C_|___|___|___|____|           /|
         /____|_7_|_8_|_9_|_/_|____|          / |
        /_____|_4_|_5_|_6_|_x_|____|         /  |
       /______|_1_|_2_|_3_|_-_|____|        /   |
      /_______|_0_|_00|_._|_+_|_=__|_______/____|

    ''',   
    '''
            _____________________________________
           |                       |            |   
           |                       |            |   
           |    AÑADIR ARTICULOS   |            |   
           |          o            |            |  
           |    BORRAR ARTICULOS   |            |   
           |                       |            |  
           |_______________________|            |
          / __|_C_|___|___|___|____|           /|
         /____|_7_|_8_|_9_|_/_|____|          / |
        /_____|_4_|_5_|_6_|_x_|____|         /  |
       /______|_1_|_2_|_3_|_-_|____|        /   |
      /_______|_0_|_00|_._|_+_|_=__|_______/____|
    
    ''',
    '''
            _____________________________________
           |                       |            |   
           |                       |            |   
           |                       |            |   
           |    BORRAR ARTICULOS   |            |  
           |                       |            |   
           |                       |            |  
           |_______________________|            |
          / __|_C_|___|___|___|____|           /|
         /____|_7_|_8_|_9_|_/_|____|          / |
        /_____|_4_|_5_|_6_|_x_|____|         /  |
       /______|_1_|_2_|_3_|_-_|____|        /   |
      /_______|_0_|_00|_._|_+_|_=__|_______/____|
      
    

    ''',
    '''

           _____________________________________
           |                       |            |   
           |                       |            |   
           |                       |            |   
           |     VER PRECIOS       |            |  
           |                       |            |   
           |                       |            |  
           |_______________________|            |
          / __|_C_|___|___|___|____|           /|
         /____|_7_|_8_|_9_|_/_|____|          / |
        /_____|_4_|_5_|_6_|_x_|____|         /  |
       /______|_1_|_2_|_3_|_-_|____|        /   |
      /_______|_0_|_00|_._|_+_|_=__|_______/____|



    ''',
    '''
            _____________________________________
           |                       |            |   
           |                       |            |   
           |                       |            |   
           |     PAGAR TOTAL       |            |  
           |                       |            |   
           |                       |            |  
           |_______________________|            |
          / __|_C_|___|___|___|____|           /|
         /____|_7_|_8_|_9_|_/_|____|          / |
        /_____|_4_|_5_|_6_|_x_|____|         /  |
       /______|_1_|_2_|_3_|_-_|____|        /   |
      /_______|_0_|_00|_._|_+_|_=__|_______/____|

    ''']


    #Genero las funciones iniciales
    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on

    #Funcion que nos lleva al MENU :)
    def main_menu(self):
        self._is_turned_on = True        
        self._IMAGENES[0]
        self._display_image_main_menu()

    def añadir_o_borrar_articulos(self, cuenta, pollo, carne, arroz, leche):
        
        self._is_turned_on = True
        print(self._IMAGENES[1])
        time.sleep(1)
        
        while True:
            command2 = str(input('''
            
                    [a]ñadir objetos
                    [b]orrar objetos
                    [p]agar TOTAL
                    [v]olver a MENU

            : '''))

            if command2 == 'a':

                while True:
                    add = str(input('''
                            ¿Que deseas agregar?

                            [p]ollo
                            [c]arne 
                            [a]rroz
                            [l]eche
                            [s]alir

                            : ''')).lower()


                    if add == 'p':
                        cuenta += pollo
                        print('TOTAL: {}'.format(cuenta))
            

                    elif  add == 'c':
                        cuenta += carne
                        print('TOTAL: {}'.format(cuenta))
            

                    elif add == 'a':
                        cuenta += arroz
                        print('TOTAL: {}'.format(cuenta))
            
            
                    elif add == 'l':
                        cuenta += leche
                        print('TOTAL: {}'.format(cuenta))
            
                    elif add == 's':
                        print(self._IMAGENES[1])
                        break
                    
                    else:
                        print('Has ingresado un comando incorrecto: {}'.format(add))

            elif command2 == 'b':
                while True:
                    delete = str(input('''
            
                    ¿Que deseas borrar?

                    [p]ollo
                    [c]arne
                    [a]rroz
                    [l]eche
                    [s]alir

                    : '''))

                    if delete == 'p':
                        cuenta -= pollo
                        print('TOTAL: {}'.format(cuenta))
            
                    elif delete == 'c':
                        cuenta -= carne
                        print('TOTAL: {}'.format(cuenta))
                    elif delete == 'a':
                        cuenta -= arroz
                        print('TOTAL: {}'.format(cuenta))
            
                    elif delete == 'l':
                        cuenta -= leche
                        print('TOTAL: {}'.format(cuenta))
            
                    elif delete == 's':
                        print(self._IMAGENES[1])
                        break

                    else:
                        print('Has ingresado un comando incorrecto: {}'.format(delete))

            elif command2 == 'p':
                self.total(cuenta)

            elif command2 == 'v':
                run()

            else:
                print('Has ingresado un comando incorrecto: {}'.format(command2))


    
    def ver_precios(self, pollo, carne, arroz, leche):
        self._is_turned_on = True
        print(self._IMAGENES[3])
        time.sleep(1)
        
        while True:
            check = str(input('''1
            
                    ¿Que precio deseas chequear?

                    [p]ollo
                    [c]arne
                    [a]rroz
                    [l]eche
                    [s]alir

                    : ''')).lower()

            if check == 'p':
                print('PRECIO POLLO: {}'.format(pollo))
            
            elif check == 'c':
                
                print('PRECIO CARNE: {}'.format(carne))
            elif check == 'a':
                
                print('PRECIO ARROZ: {}'.format(arroz))
            
            elif check == 'l':
                
                print('PRECIO LECHE: {}'.format(leche))
            
            elif check == 's':
                time.sleep(1)
                run() 



    def total(self, cuenta):
        
        print(self._IMAGENES[4])

        if cuenta > 0 :
            print('El total de la cuenta es ---> {}'.format(cuenta))

            metodo = str(input('''
            
                    ¿Que metodo de pago deseas usar?
                        [e]fectivo
                        [v]isa credito/debito
                    
                    : '''))
        
            while metodo == 'e':
                print('EFECTIVO')
                print('El total es ---> {}'.format(cuenta))
                pago = int(input('Ingresa el monto que abonas en efectivo: '))

                if pago < cuenta:
                    print('¡FALTA DINERO! Has ingresado un monto menor: {}, te faltan --> {}'.format(pago, cuenta - pago))
                    time.sleep(0.5)
                    print('')
                    metodo = 'e'

                elif pago > cuenta:
                    print('¡PAGASTE DINERO DEMAS! ---> {}, aca tienes la diferencia ----> {}'.format(pago, pago - cuenta))
                    time.sleep(0.5)
                    print('')
                    print('HASTA LUEGO')
                    run()
                   

                elif pago == cuenta:
                    print('¡PAGO REALIZADO!')
                    time.sleep(0.5)
                    print('')
                    print('HASTA LUEGO')
                    run()

            while metodo == 'v':
                print('VISA CREDITO/DEBITO')
                print('El total es ---> {}'.format(cuenta))
                pago = int(input('Ingresa el monto que abonas con VISA CREDITO/DEBITO: '))

                if pago < cuenta:
                    print('¡FALTA DINERO! Has ingresado un monto menor: {}, te faltan --> {}'.format(pago, cuenta - pago))
                    time.sleep(0.5)
                    print('')
                    metodo = 'v'

                elif pago > cuenta:
                    print('¡PAGASTE DINERO DEMAS! ---> {}, aca tienes la diferencia ----> {}'.format(pago, pago - cuenta))
                    time.sleep(0.5)
                    print('')
                    print('HASTA LUEGO')
                    run()

                elif pago == cuenta:
                    print('¡PAGO REALIZADO!')
                    time.sleep(0.5)
                    print('')
                    print('HASTA LUEGO')
                    run()



        
        else:       
            print('Primero debes añadir objetos a la cuenta')
            run()


    #Funciones para desplegar imagenes :)

    def _display_image_main_menu(self):

        if self._is_turned_on == True:
                print(self._IMAGENES[0])

        
def run():

    #PRECIOS 
    pollo = 100
    carne = 120
    arroz = 50
    leche = 30

    cuenta = 0
    
    
    caja = CajaRegistradora(is_turned_on = True)
   
   

    while True:
        caja.main_menu()      
        
        command = str(input('''
                ¿Que deseas hacer?

                [a]ñadir/borrar articulos 
                [v]er precios
                [t]otal

                :   ''')).lower()
        
        if command == 'a':
            caja.añadir_o_borrar_articulos(cuenta, pollo, carne, leche, arroz)
        
        elif command == 'v':
            caja.ver_precios(pollo, carne, arroz, leche)
        
        elif command == 't':
            caja.total(cuenta)    


          

if __name__ == "__main__":
    run()