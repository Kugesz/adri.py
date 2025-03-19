class Row:
    def __init__(self, row):
        self.csoport = row[3].spit("-")[1]
        self.ora = row[2]
        self.elamrado_tantargy = row[3]
        self.tenyleges_tantargy = row[4]
        self.tanar = row[0]
        self.honnan = row[8]
        self.hova = row[9]

    def get_megnevezes(self):
       if(self.csoport != None):
          match self.csoport:
             case "kezdő":
                return "A kezdő angol csoportnak"
             case "haladó":
                return "A haladó angol csoportnak"
             case "inf":
                return "Az infós csoportnak"
             case "ker":
                return "A kereskedelmes csoportnak"

    def creating_message(self, row):
      if(self.tenyleges_tantargy == "--"):
         return f"{self.get_megnevezes()} a(z) {self.ora}. óráj elmarad."
      return f"{self.get_megnevezes()} a(z) {self.ora}. óráján a(z) {self.elamrado_tantargy} helyett {self.tenyleges_tantargy} lesz."