class HashException(Exception):
    def __init__(self,code, msg:str):
        '''
        code Error:
        1: chave já cadastrada
        '''
        super().__init__(f'Hash Table Exception {code}: {msg}')

class HashTable:
    def __init__(self, tamanho_inicial=10):
        self.tamanho_inicial = tamanho_inicial
        self.tamanho = tamanho_inicial
        self.buckets = [[] for _ in range(tamanho_inicial)]
        self.ocupados = 0

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def _rehash(self, nova_tamanho):
        elementos = []
        for bucket in self.buckets:
            elementos.extend(bucket)

        self.tamanho = nova_tamanho
        self.buckets = [[] for _ in range(nova_tamanho)]
        self.ocupados = 0

        for elemento in elementos:
            self.inserir(elemento[0], elemento[1])

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        bucket = self.buckets[indice]

        for i, (chave_existente, _) in enumerate(bucket):
            if chave == chave_existente:
                raise HashException(1,f"A chave '{chave}' já está cadastrada na tabela.")

        bucket.append((chave, valor))
        self.ocupados += 1

        fator_carga = self.ocupados / self.tamanho

        if fator_carga > 0.7:
            nova_tamanho = self.tamanho * 2
            self._rehash(nova_tamanho)

    def remover(self, chave):
        indice = self._hash(chave)
        bucket = self.buckets[indice]

        for i, (chave_existente, _) in enumerate(bucket):
            if chave == chave_existente:
                del bucket[i]
                self.ocupados -= 1
                return

    def buscar(self, chave):
        indice = self._hash(chave)
        bucket = self.buckets[indice]

        for chave_existente, valor in bucket:
            if chave == chave_existente:
                return valor

        return None

    def imprimir(self):
        for i, bucket in enumerate(self.buckets):
            print(f'Bucket {i}: {bucket}')
