'''
Tema: Base de Datos con MongoDB
Fecha: 26 de octubre del 2022
Autor:Leonardo Martínez González
'''
from datetime import datetime

from MongoDb import *

mongoDB = MongoDb(bd="MongoEcommerce")


def InsertarCategorias():
    if mongoDB.conectar_mongoDb():
        for categoria in categorias:
            res = mongoDB.consulta_mongoDb('Categoria', {'idCategoria': categoria[0]})  # si ya existe la categoria
            if len(res) < 1:
                c = {}  # no existe
                c = {atributos_categorias[0]: categoria[0],
                     atributos_categorias[1]: categoria[1],
                     atributos_categorias[2]: categoria[2],
                     atributos_categorias[3]: categoria[3],
                     atributos_categorias[4]: categoria[4],
                     atributos_categorias[5]: categoria[5]
                     }
                # print(c)
                mongoDB.insertar('Categoria', c)
    else:
        print("No se pudo conectar a la base de datos")
    mongoDB.desconectar_mongoDb();


# Crear la tabla categorias e insertar los datos que se anexan
atributos_categorias = ['idCategoria',
                        'nombreCategoria',
                        'descripcionCategoria',
                        'ofertaCategoria',
                        'descuentoCategoria',
                        'imagenCategoria']

categorias = [
    (100, 'Brandy', '...', False, 0, 'categoria-1.jpg'),
    (200, 'Ginebra', '...', True, 10, 'categoria-2.jpg'),
    (300, 'Ron', '...', True, 10, 'categoria-3.jpg'),
    (400, 'Tequila', '...', True, 5, 'categoria-4.jpg'),
    (500, 'Vodka', '...', False, 0, 'categoria-5.jpg'),
    (600, 'Whiskey', '...', False, 0, 'categoria-6.jpg'),
]


def ObtenerCategoria(idCategoria):
    nombreCategoria = "Desconocido";
    for categoria in categorias:
        if idCategoria == categoria[0]:
            nombreCategoria = categoria[1]
            break;

    return nombreCategoria


def ObtenerImagenProducto(idProducto):
    imagenes = []
    for imagen in img_productos:
        if imagen[1] == idProducto:
            imagenes.append(imagen[2])
    if len(imagenes) < 1:
        imagenes = ["Default.jpg"]

    return imagenes;


def InsertarProductos():
    if mongoDB.conectar_mongoDb():
        for producto in productos:
            res = mongoDB.consulta_mongoDb('Producto', {'idProducto': producto[0]})  # si ya existe la categoria
            if len(res) < 1:
                p = {}  # no existe
                p = {atributos_productos[0]: producto[0],  # idProducto
                     atributos_productos[1]: "",  # codigoBarras
                     atributos_productos[2]: {"idCategoria": producto[1],
                                              "nombreCategoriaProducto": ObtenerCategoria(producto[1])},
                     # Categoria # idCategoria # # nombreCategoriaProducto
                     atributos_productos[4]: producto[2],  # productoNombreCorto
                     atributos_productos[5]: producto[3],  # productoNombreLargo
                     atributos_productos[6]: producto[4],  # productoDescripcion
                     atributos_productos[7]: producto[5],  # productoTipo
                     atributos_productos[8]: producto[6],  # productoPresentacion
                     atributos_productos[9]: float(producto[7]),  # productoCosto
                     atributos_productos[10]: producto[8],  # productoGanancia
                     atributos_productos[11]: producto[9],  # productoDescuento
                     atributos_productos[12]: producto[10],  # productoExistencia
                     atributos_productos[13]: [
                         {"idCosto": 1, "Costo": float(producto[7]), "fechaISO": datetime.now().isoformat(),
                          "fecha": datetime.now()}],  # listaproductoCosto
                     atributos_productos[14]: 0,  # productoUtilidad
                     atributos_productos[15]: ObtenerImagenProducto(producto[0]),  # productoImagen
                     "Utilidad": [{"id": 1, "cantidad": 3, "porcentaje": 10},
                                  {"id": 2, "cantidad": 6, "porcentaje": 8},
                                  {"id": 3, "cantidad": 10, "porcentaje": 5}]
                     }
                # (50, 100, 'Bacardi 151', 'Bacardi 151 con nombre largo', 'Descripción ', 1, 'Botella', '120.50', 20, 0, 1000),
                # print(p)
                mongoDB.insertar('Producto', p)
    else:
        print("No se pudo conectar a la base de datos")
    mongoDB.desconectar_mongoDb();


# Crear la tabla productos, de acuerdo a los datos que se anexan
atributos_productos = ['idProducto',
                       'codigoBarras',
                       'idCategoria',
                       'nombreCategoriaProducto',
                       'productoNombreCorto',
                       'productoNombreLargo',
                       'productoDescripcion',
                       'productoTipo',
                       'productoPresentacion',
                       'productoCosto',
                       'productoGanancia',
                       'productoDescuento',
                       'productoExistencia',
                       'listaproductoCosto',
                       'productoUtilidad',
                       'productoImagen'
                       ]

productos = {
    (50, 100, 'Bacardi 151', 'Bacardi 151 con nombre largo', 'Descripción del Bacardi 151 con tanto grados de alcohol',
     1, 'Botella', '120.50', 20, 0, 1000),
    (100, 100, 'Brandi Torres 20', 'Brandy Torres 20 150 Aniversario 700 ml',
     'Edición especial creada para conmemorar el 150 aniversario del nacimiento de Joan Torres Casals, tiene notas de frutas maduras como ciruelas y pasas.',
     1, 'Botella', '940.50', 20, 0, 1000),
    (150, 100, 'Brandi Torres 10 DB', 'Brandy Torres 10 Double Barrel 700 ml',
     'Es un brandy doblemente añejado en barricas de roble americano, tiene un aroma amplio a notas de vainilla y tabaco. En boca es rico y equilibrado con un tostado redondo.',
     1, 'Botella', '440.50', 20, 0, 1000),
    (200, 100, 'Brandy Alma De Magno', 'Brandy Alma De Magno C/Vaso 700 ml',
     'Edición especial con un vaso de regalo. Es un brandy obtenido a partir de holandas y aguardiente de vino de baja graduación, tiene aromas a finas notas de frutos secos con toques de roble.',
     1, 'Botella', '500.50', 15, 0, 1000),
    (250, 100, 'Brandy Presidente', 'Brandy Presidente Edicion 50A 1.75L',
     'Envejecido en barricas de roble blanco, tiene un sabor a frutos secos y vainilla.', 1, 'Botella', '220.50', 15, 0,
     1000),
    (300, 100, 'Brandy Gran Duque', 'Brandy Gran Duque D Alba 700ml',
     'Envejecido en botas de roble americano envinadas con oloroso, tiene un aroma complejo con notas balsámicas derivadas de la larga crianza en madera.',
     1, 'Botella', '1000.00', 10, 0, 1000),
    (350, 200, 'Ginebra Tanqueray Ten', 'Ginebra Tanqueray Ten Estuche Con Llave 700ml',
     'Edición especial en estuche con llave. Es una ginebra con aroma a flores de manzanilla, frutos secos y limón verde, en boca se perciben notas toronja y miel.',
     1, 'Botella', '800.90', 10, 0, 1000),
    (400, 200, 'Ginebra Beefeater', 'Ginebra Beefeater 24 C/Copa 750ml',
     'Edición especial con una copa de regalo. Es un ginebra con distintos tipos de botánicos como té sencha japonés y el té verde chino, posee aromas a notas cítricas y un sabor herbal y cremoso.',
     1, 'Botella', '700.90', 10, 0, 1000),
    (450, 200, 'Ginebra Greenalls', 'Ginebra Greenalls The Original+Wild Berry C/4 Vasos 750ml', '', 1, 'Paquete',
     '750.90', 10, 0, 1000),
    (500, 200, 'Ginebra Boodles', 'Ginebra Boodles Mulberry 750 ml',
     'Es la primera ginebra con sabor a moras que combina delicadas moras con notas de frambuesa y grosella para crear un dulce y sutil sabor.',
     1, 'Paquete', '509.90', 10, 0, 1000),
    (550, 200, 'Ginebra Mom ', 'Ginebra Mom 700 ml',
     'Considerada la Reyna de las Ginebras, tiene un intenso aroma a frutos rojos, en boca se percibe un carácter aterciopelado y agradable a frutos rojos.',
     1, 'Paquete', '509.90', 10, 0, 1000),
    (600, 200, 'Ginebra Tanqueray', 'Ginebra Tanqueray 750 ML ',
     'Destilado en 4 ocasiones de manera artesanal, posee un sabor botánico seco a manzanilla, limón verde y toronja, así como aromas florales.',
     1, 'Botella', '400.90', 30, 0, 1000),
    (650, 300, 'Ron Bacardi Blanco', 'Ron Bacardi Blanco Edic Halloween 750ml',
     'Perfecto para las celebraciones de Hallowen, es un ron en la botella clásica de la marca con una etiqueta disfrazada de Jack-o-lantern que brilla en la oscuridad.',
     1, 'Botella', '200.5', 15, 5, 1000),
    (700, 300, 'Ron Havana', 'RON HAVANA SELECCION 700 ML',
     'Elaborado por los mejores maestros roneros de Cuba, posee un aroma a nuez pascana tostada y aroma de especias y tabaco. Tiene una entrada redonda.',
     1, 'Botella', '900.5', 15, 10, 1000),
    (750, 300, 'Ron Bacardi Blanco', 'Ron Bacardi Blanco 980ml+Raspberry+Limon C/Hielera/Vasos', '', 1, 'Botella',
     '600.5', 15, 10, 1000),
    (800, 300, 'Ron Bacardi Gran Reserva', 'Ron Bacardi Gran Reserva Limitada 750ml',
     'Es una mezcla de rones maduros añejados en barriles bajo el sol del Caribe durante 12 años. Es un ron generoso y complejo que muestra suaves notas de caramelo y frutas secas.',
     1, 'Botella', '2500.5', 15, 10, 1000),
    (850, 300, 'Ron Antillano Blanco', 'Ron Antillano Blanco C/Vaso/Macerador 1L', '', 1, 'Botella', '150.5', 15, 10,
     1000),
    (900, 300, 'Ron Flor De Caña', 'Ron Flor De Caña Gran Rva 7A Party Kit 750ml', '', 1, 'Botella', '400.5', 15, 10,
     1000),
    (950, 300, 'Ron Flor De Caña Centenario', 'Ron Flor De Caña Centenario 12A 750 ml C/4 Vasos',
     'País de Origen: Nicaragua', 1, 'Botella', '700.5', 15, 10, 1000),
    (1000, 400, 'Don Julio 70 Añejo 700ml', 'Tequila Don Julio 70 Añejo 700ml',
     'Caracterizado por poseer un color cristalino, tiene aromas a notas iniciales de cítricos y frutas como la guayaba y la tradicional esencia del agave.',
     1, 'Botella', '800.5', 15, 10, 1000),
    (1050, 400, 'Herradura Rep 950ml', 'Tequila Herradura Rep 950ml',
     'Considerado el primer tequila reposado en el mundo, tiene un sabor a madera, vainilla, caramelo, ligero agave cocido, frutas, nuez y especias.',
     1, 'Botella', '500.5', 15, 10, 1000),
    (1100, 400, 'Cazadores Añejo Cristalino', 'Tequila Cazadores Añejo Cristalino 750 ml',
     'Es un tequila sumamente transparente, tiene notas a madera tostada, nuez, almendra y manzana.', 1, 'Botella',
     '400.5', 15, 10, 1000),
    (1150, 400, 'Herradura Ultra Añejo', 'Tequila Herradura Ultra Añejo 750 ml',
     'Ideal para degustarse solo, posee un sabor suave y un aroma a madera, vainilla, caramelo y cítricos, que se entrelazan el ahumado del agave cocido.',
     1, 'Botella', '600.5', 15, 10, 1000),
    (1200, 400, 'Gran Centenario', 'Tequila Gran Centenario Añejo 695ml',
     'Considerado el mejor tequila añejo, es elaborado 100% de agave, se madura en barricas de roble blanco y se caracteriza por ser muy suave al paladar y en aromas.',
     1, 'Botella', '500.5', 15, 0, 1000),
    (1250, 400, 'Jimador Reposado', 'Tequila El Jimador Reposado Cristalino 700 ml',
     'Considerado el tequila más suave de la familia, tiene un color limpio y brillante, con notas a cítricos, frutas, flores, hierbas, vainilla y caramelo.',
     1, 'Botella', '300.5', 15, 0, 1000),
    (
        1300, 500, 'Absolut Extrakt', 'Vodka Absolut Extrakt C/2 Vasos Shot 700ml', '', 1, 'Botella', '300.5', 15, 0,
        1000),
    (1350, 500, 'Absolut Azul', 'Vodka Absolut Azul 750 ml con Absolut Lime de 50 ml y copa',
     'Elaborado con elementos naturales, tiene un aroma a notas de cereal puro y fresco. Esta presentación incluye un Absolut Lime de 50 ml y una copa de regalo.',
     1, 'Botella', '280.5', 15, 0, 1000),
    (1400, 500, 'Zaverich Vanilla', 'Vodka Zaverich Vanilla 1L+Zaverich Premium 1L',
     'Es un vodka ruso destilado a través de la fermentación de granos y otras plantas ricas en almidón, tiene aromas y sabores intensos a vainilla. Incluye una botella de Zaverich Premium de 1 L.',
     1, 'Botella', '200.5', 15, 0, 1000),
    (1450, 500, 'Outer Space', 'Vodka Outer Space 750 ml',
     'Es un vodka hecho con maíz 100% americano, sin gluten, el diseño de su botella es único y llamativo. Tiene aromas y sabores a frutos secos.',
     1, 'Botella', '700.5', 15, 0, 1000),
    (1500, 500, 'Grey Goose', 'Vodka Grey Goose Est Alpine 750ml',
     'Edición especial. Es un vodka elaborado con agua pura de manantial y exclusivos ingredientes franceses, es considerado el mejor vodka del mundo.',
     1, 'Botella', '700.5', 15, 0, 1000),
    (1550, 500, 'Karat', 'Vodka Karat 1 L',
     'Elaborado con grano importado de Estados Unidos, es un vodka de cuerpo ligero y un sabor ideal para preparar todo tipo de cocteles.',
     1, 'Botella', '150.5', 15, 0, 1000),
    (1600, 600, 'Johnnie Walker Song Of Fire', 'Whisky Johnnie Walker Game Thrones A Song Of Fire 700ml',
     'Elaborado con grano importado de Estados Unidos, es un vodka de cuerpo ligero y un sabor ideal para preparar todo tipo de cocteles.',
     1, 'Botella', '500.5', 15, 0, 1000),
    (1650, 600, 'Johnnie Walker Red Label', 'Whisky Johnnie Walker Red Label 700 ml',
     'Es un whisky ligero con sabor a especias aromáticas con ligeras notas a frutas dulces, y un aroma ahumado.', 1,
     'Botella', '300.5', 15, 0, 1000),
    (1700, 600, 'Buchanans Select 15 Años', 'Whisky Buchanans Select 15 Años 750 ml',
     'Es una mezcla de los más finos single malts. Ha sido madurado durante 15 años, ofreciendo un perfil de sabor más audaz y complejo con notas de roble tostado.',
     1, 'Botella', '1500.5', 15, 0, 1000),
    (1750, 600, 'Johnnie Walker 18 Años', 'Whisky Johnnie Walker 18 Años 750 ml',
     'Es una mezcla de los mejores whiskies de Escocia de 18 años, tiene un carácter dulce, rico, afrutado y equilibrado con sutil ahumado.',
     1, 'Botella', '2000.5', 15, 0, 1000),
    (1800, 600, 'Buchanans 12 Años', 'Whisky Buchanans 12 Años 1L',
     'Ideal para maridar con platillos frescos, tiene aromas a notas de naranja y chocolate; así como un sabor suave a cítricos, chocolate y miel.',
     1, 'Botella', '1020.5', 15, 0, 1000),
    (1850, 600, 'William Lawsons Std', 'Whisky William Lawsons Std 750 ml',
     'Es un whisky afrutado de cuerpo ligero, se caracteriza por su aroma a pastel de manzana y su sabor a cereal tostado y al tofee, con un final suave.',
     1, 'Botella', '170.5', 15, 0, 1000),

}

# idCategoria, idProducto, Imagen
img_productos = [
    (100, 50, 'brandy-50.webp'),
    (200, 100, 'brandy-100.webp'),
    (300, 150, 'brandy-150.webp'),
    (400, 200, 'brandy-200.webp'),
    (500, 250, 'brandy-250.webp'),
    (600, 300, 'brandy-300.webp'),

    (700, 350, 'Ginebra-350.webp'),
    (800, 400, 'Ginebra-400.webp'),
    (900, 450, 'Ginebra-450.webp'),
    (1000, 500, 'Ginebra-500.webp'),
    (1100, 550, 'Ginebra-550.webp'),
    (1200, 600, 'Ginebra-600.webp'),

    (1300, 650, 'Ron-650.webp'),
    (1400, 700, 'Ron-700.webp'),
    (1500, 750, 'Ron-750.webp'),
    (1600, 800, 'Ron-800.webp'),
    (1700, 850, 'Ron-850.webp'),
    (1800, 900, 'Ron-900.webp'),
    (1900, 950, 'Ron-950.webp'),

    (2000, 1000, 'Tequila-1000.webp'),
    (2100, 1050, 'Tequila-1050.webp'),
    (2200, 1100, 'Tequila-1100.webp'),
    (2300, 1150, 'Tequila-1150.webp'),
    (2400, 1200, 'Tequila-1200.webp'),
    (2500, 1250, 'Tequila-1250.webp'),

    (2600, 1300, 'Vodka-1300.webp'),
    (2700, 1350, 'Vodka-1350.webp'),
    (2800, 1400, 'Vodka-1400.webp'),
    (2900, 1450, 'Vodka-1450.webp'),
    (3000, 1500, 'Vodka-1500.webp'),
    (3100, 1550, 'Vodka-1550.webp'),

    (3200, 1600, 'Whisky-1600.webp'),
    (3300, 1650, 'Whisky-1650.webp'),
    (3400, 1700, 'Whisky-1700.webp'),
    (3500, 1750, 'Whisky-1750.webp'),
    (3600, 1800, 'Whisky-1800.webp'),
    (3700, 1850, 'Whisky-1850.webp')

]


def InsertarPedidos():
    if mongoDB.conectar_mongoDb():
        for pedido in pedidos:
            res = mongoDB.consulta_mongoDb('Pedido', {'idPedido': pedido["idPedido"]})  # si ya existe el pedido
            if len(res) < 1:
                mongoDB.insertar('Pedido', pedido)
    else:
        print("No se pudo conectar a la base de datos")
    mongoDB.desconectar_mongoDb();


pedidos = [{
    "idPedido": 1,
    "idCliente":1,
    "fecha": datetime.now(),
    "subtotal": 0,
    "descuento": 0,
    "total": 0,
    "pagado": False,
    "estado": -1,  # 0surtido,1empaquetado,2
    "productoPedido": [{"idProducto": 1350, "cantidad": 1, "utilidad": [{"id": 1, "cantidad": 3, "porcentaje": 10}]}]},
{
    "idPedido": 2,
    "idCliente":2,
    "fecha": datetime.now(),
    "subtotal": 0,
    "descuento": 0,
    "total": 0,
    "pagado": False,
    "estado": -1,  # 0surtido,1empaquetado,2
    "productoPedido": [{"idProducto": 1350, "cantidad": 1, "utilidad": [{"id": 1, "cantidad": 3, "porcentaje": 10}]}]}
]
def InsertarCliente():
    if mongoDB.conectar_mongoDb():
        for cliente in clientes:
            res = mongoDB.consulta_mongoDb('Cliente', {'idCliente': cliente["idCliente"]})  # si ya existe el cliente
            if len(res) < 1:
                mongoDB.insertar('Cliente', cliente)
    else:
        print("No se pudo conectar a la base de datos")
    mongoDB.desconectar_mongoDb();

clientes = [{
    "idCliente": 1,
    "Nombre": "Santiago",
    "Apellidos": "Torres Ochoa",
    "Direcciones": [{"idDireccion": 1,"CP": "2235","Pais": "Mexico","Estado": "Michoacan","Ciudad":  "Jiquilpan","Calle": "Colina alta","Numero ext": "4","Numero int": ""}]
},
    {
    "idCliente": 2,
    "Nombre": "Juan",
    "Apellidos": "Perez Ochoa",
    "Direcciones": [{"idDireccion": 1,"CP": "1234","Pais": "Mexico","Estado": "Michoacan","Ciudad":  "Jiquilpan","Calle": "Alameda","Numero ext": "234","Numero int": "2"}]
}]


InsertarCategorias()
InsertarProductos()
InsertarPedidos()
InsertarCliente()