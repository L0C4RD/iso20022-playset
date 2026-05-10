from . import base_types
import UniqueProductIdentifier2Choice
import GenericIdentification184
import Max52Text
import ISINOct2015Identifier
import IndexIdentification1
import CustomBasket4
import UnderlyingIdentification1Code

class SecurityIdentification41Choice(base_types._BaseFieldType):

	__slots__ = ["_IdNotAvlbl", "_UnqPdctIdr", "_AltrntvInstrmId", "_Bskt", "_ISIN", "_Indx", "_Othr"]
	@property
	def IdNotAvlbl(self):
		return self._IdNotAvlbl

	@IdNotAvlbl.setter
	def IdNotAvlbl(self, value):
		self._IdNotAvlbl = value if type(value) != auto else self.make_default("IdNotAvlbl")

	@IdNotAvlbl.deleter
	def IdNotAvlbl(self):
		del self._IdNotAvlbl
		self._IdNotAvlbl = None

	@property
	def UnqPdctIdr(self):
		return self._UnqPdctIdr

	@UnqPdctIdr.setter
	def UnqPdctIdr(self, value):
		self._UnqPdctIdr = value if type(value) != auto else self.make_default("UnqPdctIdr")

	@UnqPdctIdr.deleter
	def UnqPdctIdr(self):
		del self._UnqPdctIdr
		self._UnqPdctIdr = None

	@property
	def AltrntvInstrmId(self):
		return self._AltrntvInstrmId

	@AltrntvInstrmId.setter
	def AltrntvInstrmId(self, value):
		self._AltrntvInstrmId = value if type(value) != auto else self.make_default("AltrntvInstrmId")

	@AltrntvInstrmId.deleter
	def AltrntvInstrmId(self):
		del self._AltrntvInstrmId
		self._AltrntvInstrmId = None

	@property
	def Bskt(self):
		return self._Bskt

	@Bskt.setter
	def Bskt(self, value):
		self._Bskt = value if type(value) != auto else self.make_default("Bskt")

	@Bskt.deleter
	def Bskt(self):
		del self._Bskt
		self._Bskt = None

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	@property
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if type(value) != auto else self.make_default("Indx")

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IdNotAvlbl', type=UnderlyingIdentification1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnqPdctIdr', type=UniqueProductIdentifier2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AltrntvInstrmId', type=Max52Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Bskt', type=CustomBasket4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Indx', type=IndexIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=GenericIdentification184, min=0, max=1, mutex_group=1, array=False),
	))

