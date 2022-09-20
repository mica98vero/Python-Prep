def test_ListaDeListas_01(self):
    lista_test = ch.ListaDeListas((100,101))
    lista_esperada = None
    self.assertEqual(lista_test, lista_esperada)

def test_ListaDeListas_02(self):
    lista_test = ch.ListaDeListas([0,1,[2,3],[[4,5],6],[[7]],8,[8,9,10]])
    lista_esperada = [0,1,2,3,4,5,6,7,8,8,9,10]
    self.assertEqual(lista_test, lista_esperada)

    def test_ListaDeListas_03(self):
      lista_test = ch.ListaDeListas(['a','b',1,2,['a1','b3'],[['a'],2]])
      lista_esperada = ['a','b',1,2,'a1','b3','a',2]
      self.assertEqual(lista_test, lista_esperada)

    def test_Factorial_01(self):
      valor_test = ch.Factorial(6)
      valor_esperado = 720
      self.assertEqual(valor_test, valor_esperado)

    def test_Factorial_02(self):
      valor_test = ch.Factorial(9)
      valor_esperado = 362880
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseVehiculo_01(self):
      a = ch.ClaseVehiculo('auto','gris')
      valor_test = a.Acelerar(50)
      valor_test = a.Acelerar(100)
      valor_test = a.Acelerar(-30)
      valor_esperado = 70
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseVehiculo_02(self):
      a = ch.ClaseVehiculo('camion','blanco')
      valor_test = a.Acelerar(20)
      valor_test = a.Acelerar(-30)
      valor_esperado = 0
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseVehiculo_03(self):
      a = ch.ClaseVehiculo('moto','negra')
      valor_test = a.Acelerar(10)
      valor_esperado = 10
      self.assertEqual(valor_test, valor_esperado)

    def test_NumeroCapicua_01(self):
      valor_test = ch.NumeroCapicua(1234)
      valor_esperado = False
      self.assertEqual(valor_test, valor_esperado)

    def test_NumeroCapicua_02(self):
      valor_test = ch.NumeroCapicua(358853)
      valor_esperado = True
      self.assertEqual(valor_test, valor_esperado)

    def test_NumeroCapicua_03(self):
      valor_test = ch.NumeroCapicua('hola')
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)
      
    def test_ProximoPrimo_01(self):
      valor_test = ch.ProximoPrimo(61)
      valor_esperado = 67
      self.assertEqual(valor_test, valor_esperado)

    def test_ProximoPrimo_02(self):
      valor_test = ch.ProximoPrimo(139)
      valor_esperado = 149
      self.assertEqual(valor_test, valor_esperado)

    def test_ProximoPrimo_03(self):
      valor_test = ch.ProximoPrimo(200)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_FactorizarNumero_01(self):
      valor_test = ch.FactorizarNumero(5)
      valor_esperado = [[5],[1]]
      self.assertEqual(valor_test, valor_esperado)

    def test_FactorizarNumero_02(self):
      valor_test = ch.FactorizarNumero(1428)
      valor_esperado = [[2,3,7,17], [2,1,1,1]]
      self.assertEqual(valor_test, valor_esperado)

    def test_FactorizarNumero_03(self):
      valor_test = ch.FactorizarNumero('cinco')
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_OrdenarDiccionario_01(self):
      dicc = {'clave1':['c','a','b'], 'clave2':['casa','auto','barco'], 'clave3':[3,1,2]}
      valor_test = ch.OrdenarDiccionario(dicc, 'clave1')
      valor_esperado = {'clave1':['c','b','a'], 'clave2':['casa','barco','auto'], 'clave3':[3,2,1]}
      self.assertEqual(valor_test, valor_esperado)

    def test_OrdenarDiccionario_02(self):
      dicc = ['c','a','b']
      valor_test = ch.OrdenarDiccionario(dicc, 'clave1', True)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_OrdenarDiccionario_03(self):
      dicc = {'clave1':['c','a','b'], 'clave2':['casa','auto','barco'], 'clave3':[3,1,2]}
      valor_test = ch.OrdenarDiccionario(dicc, 'clave1', False)
      valor_esperado = {'clave1':['a','b','c'], 'clave2':['auto','barco','casa'], 'clave3':[1,2,3]}
      self.assertEqual(valor_test, valor_esperado)