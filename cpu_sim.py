class CPU:
  def __init__(self, komutlar, pc=1, memory={}):
    self.komutlar = komutlar
    self.pc = pc
    self.mar = None
    self.mbr = None
    self.ir = None
    self.acc = None
    self.al = None
    self.bl = None
    self.memory = memory

  def yazdir(self):
    print(f'PC: {self.pc} '\
          f'MAR: {self.mar} '\
          f'MBR: {self.mbr} '\
          f'IR: {self.ir} '\
          f'ACC: {self.acc} '\
          f'AL: {self.al} '\
          f'BL: {self.bl}')
  
  def akis1(self):
      self.mar = self.pc
      self.mbr = f'I{self.pc}'
      self.ir = f'I{self.pc}'
      self.pc += 1
      self.yazdir()
    
  def calistir(self):
    self.yazdir()
    for komut in self.komutlar:
      komut_islem, komut_veri = komut.split(" ")

      if komut_islem == "LOAD":
        self.akis1()
        self.acc = memory.get(komut_veri)
        self.mar = komut_veri
        self.yazdir()
      elif komut_islem == "MOV":
        self.akis1()
        hedef, kaynak = komut_veri.split(",")
        if hedef == "AL":
          if kaynak == "BL":
            self.al = self.bl
          else:
            if kaynak[0] == "#":
              self.al = int(kaynak[1:])
            elif kaynak[0] == "@":
              kaynak = kaynak[1:]
              self.mar = kaynak
              self.mbr = self.memory.get(kaynak)
              self.yazdir()
              self.mar = self.mbr
              self.mbr = self.memory.get(self.mbr)
              self.al = self.mbr
            else:
              self.mar = kaynak
              self.mbr = self.memory.get(kaynak)
              self.al = self.memory.get(kaynak)
        if hedef == "BL":
          if kaynak == "AL":
            self.bl = self.al
          else:
            if kaynak[0] == "#":
              self.bl = int(kaynak[1:])
            elif kaynak[0] == "@":
              kaynak = kaynak[1:]
              self.mar = kaynak
              self.mbr = self.memory.get(kaynak)
              self.yazdir()
              self.mar = self.mbr
              self.mbr = self.memory.get(self.mbr)
              self.al = self.mbr
            else:
              self.mar = kaynak
              self.mbr = self.memory.get(kaynak)
              self.bl = self.memory.get(kaynak)
        self.yazdir()
      elif komut_islem == "ADD":
        self.akis1()
        hedef, kaynak = komut_veri.split(",")
        if (hedef == "AL" or hedef == "BL") and (kaynak == "AL" or kaynak == "BL"):
          self.acc = int(self.al) + int(self.bl)
        else:
          access_memory_hedef, access_memory_kaynak = False, False
          if hedef.isdigit():
            access_memory_hedef = True
          if kaynak.isdigit():
            access_memory_kaynak = True
          if hedef == "AL":
            hedef = self.al
          if hedef == "BL":
            hedef = self.bl
          if kaynak == "AL":
            kaynak = self.al
          if kaynak == "BL":
            kaynak = self.bl
          hedef = str(hedef)
          kaynak = str(kaynak)
          if hedef[0] == "#":
            hedef = hedef[1:]
          if kaynak[0] == "#":
            kaynak = kaynak[1:]
          if access_memory_hedef:
            self.mar = hedef
            self.mbr = self.memory.get(self.mar)
            hedef = self.mbr
          # aynı anda ikisi de olunca düzgün çalışmayabilir
          if access_memory_kaynak:
            self.mar = kaynak
            self.mbr = self.memory.get(self.mar)
            kaynak = self.mbr
          self.acc = int(kaynak) + int(hedef)
        self.yazdir()
      elif komut_islem == "STO":
        self.akis1()
        if komut_veri[0] == "@":
          komut_veri = komut_veri[1:]
          self.mar = komut_veri
          self.mbr = self.memory.get(komut_veri)
          self.yazdir()
          self.mar = self.mbr
          self.memory[self.mar] = self.acc
        else:
          self.mar = komut_veri
          self.memory[komut_veri] = self.acc
        self.yazdir()
    self.akis1()