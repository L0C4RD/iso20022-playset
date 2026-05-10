from . import base_types
from ._ATMMediaType3Code import ATMMediaType3Code
from ._ATMCassetteCounters5 import ATMCassetteCounters5
from ._Number import Number
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount

class ATMCassetteCounters6(base_types._BaseFieldType):

	__slots__ = ["_MdiaCtgy", "_InitlCnt", "_UnitVal", "_Ccy", "_CurAmt", "_CurNb", "_FlowTtls"]
	@property
	def MdiaCtgy(self):
		return self._MdiaCtgy

	@MdiaCtgy.setter
	def MdiaCtgy(self, value):
		self._MdiaCtgy = value if type(value) != base_types.auto else self.make_default("MdiaCtgy")

	@MdiaCtgy.deleter
	def MdiaCtgy(self):
		del self._MdiaCtgy
		self._MdiaCtgy = None

	@property
	def InitlCnt(self):
		return self._InitlCnt

	@InitlCnt.setter
	def InitlCnt(self, value):
		self._InitlCnt = value if type(value) != base_types.auto else self.make_default("InitlCnt")

	@InitlCnt.deleter
	def InitlCnt(self):
		del self._InitlCnt
		self._InitlCnt = None

	@property
	def UnitVal(self):
		return self._UnitVal

	@UnitVal.setter
	def UnitVal(self, value):
		self._UnitVal = value if type(value) != base_types.auto else self.make_default("UnitVal")

	@UnitVal.deleter
	def UnitVal(self):
		del self._UnitVal
		self._UnitVal = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def CurAmt(self):
		return self._CurAmt

	@CurAmt.setter
	def CurAmt(self, value):
		self._CurAmt = value if type(value) != base_types.auto else self.make_default("CurAmt")

	@CurAmt.deleter
	def CurAmt(self):
		del self._CurAmt
		self._CurAmt = None

	@property
	def CurNb(self):
		return self._CurNb

	@CurNb.setter
	def CurNb(self, value):
		self._CurNb = value if type(value) != base_types.auto else self.make_default("CurNb")

	@CurNb.deleter
	def CurNb(self):
		del self._CurNb
		self._CurNb = None

	@property
	def FlowTtls(self):
		return self._FlowTtls

	@FlowTtls.setter
	def FlowTtls(self, value):
		self._FlowTtls = value if type(value) != base_types.auto else self.make_default("FlowTtls")

	@FlowTtls.deleter
	def FlowTtls(self):
		del self._FlowTtls
		self._FlowTtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MdiaCtgy', type=ATMMediaType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlCnt', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitVal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlowTtls', type=ATMCassetteCounters5, min=0, max=None, mutex_group=None, array=True),
	))

