from . import base_types
from ._TradeData43 import TradeData43

class TradeReport33Choice(base_types._BaseFieldType):

	__slots__ = ["_Cmprssn", "_Crrctn", "_Err", "_Mod", "_New", "_Othr", "_PortOut", "_PosCmpnt", "_Rvv", "_Termntn", "_ValtnUpd"]
	@property
	def Cmprssn(self):
		return self._Cmprssn

	@Cmprssn.setter
	def Cmprssn(self, value):
		self._Cmprssn = value if type(value) != base_types.auto else self.make_default("Cmprssn")

	@Cmprssn.deleter
	def Cmprssn(self):
		del self._Cmprssn
		self._Cmprssn = None

	@property
	def Crrctn(self):
		return self._Crrctn

	@Crrctn.setter
	def Crrctn(self, value):
		self._Crrctn = value if type(value) != base_types.auto else self.make_default("Crrctn")

	@Crrctn.deleter
	def Crrctn(self):
		del self._Crrctn
		self._Crrctn = None

	@property
	def Err(self):
		return self._Err

	@Err.setter
	def Err(self, value):
		self._Err = value if type(value) != base_types.auto else self.make_default("Err")

	@Err.deleter
	def Err(self):
		del self._Err
		self._Err = None

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if type(value) != base_types.auto else self.make_default("Mod")

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = None

	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if type(value) != base_types.auto else self.make_default("New")

	@New.deleter
	def New(self):
		del self._New
		self._New = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def PortOut(self):
		return self._PortOut

	@PortOut.setter
	def PortOut(self, value):
		self._PortOut = value if type(value) != base_types.auto else self.make_default("PortOut")

	@PortOut.deleter
	def PortOut(self):
		del self._PortOut
		self._PortOut = None

	@property
	def PosCmpnt(self):
		return self._PosCmpnt

	@PosCmpnt.setter
	def PosCmpnt(self, value):
		self._PosCmpnt = value if type(value) != base_types.auto else self.make_default("PosCmpnt")

	@PosCmpnt.deleter
	def PosCmpnt(self):
		del self._PosCmpnt
		self._PosCmpnt = None

	@property
	def Rvv(self):
		return self._Rvv

	@Rvv.setter
	def Rvv(self, value):
		self._Rvv = value if type(value) != base_types.auto else self.make_default("Rvv")

	@Rvv.deleter
	def Rvv(self):
		del self._Rvv
		self._Rvv = None

	@property
	def Termntn(self):
		return self._Termntn

	@Termntn.setter
	def Termntn(self, value):
		self._Termntn = value if type(value) != base_types.auto else self.make_default("Termntn")

	@Termntn.deleter
	def Termntn(self):
		del self._Termntn
		self._Termntn = None

	@property
	def ValtnUpd(self):
		return self._ValtnUpd

	@ValtnUpd.setter
	def ValtnUpd(self, value):
		self._ValtnUpd = value if type(value) != base_types.auto else self.make_default("ValtnUpd")

	@ValtnUpd.deleter
	def ValtnUpd(self):
		del self._ValtnUpd
		self._ValtnUpd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmprssn', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Crrctn', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Err', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mod', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='New', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PortOut', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PosCmpnt', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rvv', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Termntn', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ValtnUpd', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
	))

