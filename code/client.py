class Client:
	#remove local from client, what if client wants it sent to another local?
    def __init__(self, id):
        self.id = id

    def getId(self, id):
        return self.id

    def makeOffer(self, source, dest, amount, money):
        return [source, dest, amount, money]
