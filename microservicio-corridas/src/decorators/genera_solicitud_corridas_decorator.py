from flask import abort

class CorridasDecorator:

    def valida_inputs(func):
        
        def validacion(body,valor,digito=0):

            if  valor not in body.keys():
                abort(400, "El parámetro " + valor + " no se está enviando en el request")
                
            if  body[valor] == "" or body[valor] is None:
                abort(400, "El parámetro " + valor + " esta vacío")   
            
            if digito == 1:
                if  type(body[valor]) != str or not body[valor].isdigit():
                    abort(400, "El parámetro " + valor + " es incorrecto") 
                    
        def checarBoleto(body,valor):            
             if  type(body[valor]) != str or not body[valor].isdigit():
                    abort(400, "El parámetro " + valor + " es incorrecto")
                       
        def wrapper(*args):
            body = args[1]
            usuario = args[2]
            jwt = ""

            # Valida que usuario venga en el HEADER 
            if not usuario or not usuario.isdigit() :
                abort(400, "El header usuario es incorrecto")   
            
            #Valida la mayor parte del body
            validacion(body,'claveOrigen')
            validacion(body,'claveDestino')
            validacion(body,'dispositivo',1)
            validacion(body,'tipoViaje')
            validacion(body,'fechaCorridaSalida',1)
            validacion(body,'horaCorridaSalida',1)
            validacion(body,'solicitud')
            validacion(body,'password')
            validacion(body,'user')
            
            # Valida tipo de Viaje (Redondo o Sencillo)
            if body['tipoViaje'] == "R" or body['tipoViaje'] == "S":
                if body['tipoViaje'] == "R":
                    validacion(body,'fechaCorridaRegreso',1)
                    validacion(body,'horaCorridaRegreso',1)
            else:
                abort(400, "El parámetro tipoViaje es incorrecto")  
                  
            # Valida que mínimo esté comprando un boleto
            if  (body['numeroAdulto'] == "" or body['numeroAdulto'] is None) and (body['numeroEstudiante'] == "" or body['numeroEstudiante'] is None) and (body['numeroInapam'] == "" or body['numeroInapam'] is None) and (body['numeroMaestro'] == "" or body['numeroMaestro'] is None) and (body['numeroNinio'] == "" or body['numeroNinio'] is None):   
                abort(400, "Mínimo se debe de indicar la compra de un ticket")
            elif  body['numeroEstudiante'] != "" and body['numeroEstudiante'] is not None :
                checarBoleto(body,"numeroEstudiante")
            elif  body['numeroInapam'] != "" and body['numeroInapam'] is not None :
                checarBoleto(body,"numeroInapam")
            elif  body['numeroMaestro'] != "" and body['numeroMaestro'] is not None :
                checarBoleto(body,"numeroMaestro")          
            elif  body['numeroAdulto'] != "" and body['numeroAdulto'] is not None :
                checarBoleto(body,"numeroAdulto")
            elif  body['numeroNinio'] != "" and body['numeroNinio'] is not None :
                checarBoleto(body,"numeroNinio")
            
            result  = func(jwt,body,usuario)
               
            return result

        return wrapper

    
   