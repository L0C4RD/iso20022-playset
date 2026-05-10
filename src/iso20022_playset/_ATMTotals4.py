from . import base_types
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._ATMMediaType4Code import ATMMediaType4Code
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._Number import Number

class ATMTotals4(base_types._BaseFieldType):

	__slots__ = ["_ATMBal", "_ATMCur", "_ATMCurNb", "_ATMBalNb", "_MdiaTp", "_Ccy"]
	@property
	def ATMBal(self):
		return self._ATMBal

	@ATMBal.setter
	def ATMBal(self, value):
		self._ATMBal = value if type(value) != base_types.auto else self.make_default("ATMBal")

	@ATMBal.deleter
	def ATMBal(self):
		del self._ATMBal
		self._ATMBal = None

	@property
	def ATMBalNb(self):
		return self._ATMBalNb

	@ATMBalNb.setter
	def ATMBalNb(self, value):
		self._ATMBalNb = value if type(value) != base_types.auto else self.make_default("ATMBalNb")

	@ATMBalNb.deleter
	def ATMBalNb(self):
		del self._ATMBalNb
		self._ATMBalNb = None

	@property
	def ATMCur(self):
		return self._ATMCur

	@ATMCur.setter
	def ATMCur(self, value):
		self._ATMCur = value if type(value) != base_types.auto else self.make_default("ATMCur")

	@ATMCur.deleter
	def ATMCur(self):
		del self._ATMCur
		self._ATMCur = None

	@property
	def ATMCurNb(self):
		return self._ATMCurNb

	@ATMCurNb.setter
	def ATMCurNb(self, value):
		self._ATMCurNb = value if type(value) != base_types.auto else self.make_default("ATMCurNb")

	@ATMCurNb.deleter
	def ATMCurNb(self):
		del self._ATMCurNb
		self._ATMCurNb = None

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
	def MdiaTp(self):
		return self._MdiaTp

	@MdiaTp.setter
	def MdiaTp(self, value):
		self._MdiaTp = value if type(value) != base_types.auto else self.make_default("MdiaTp")

	@MdiaTp.deleter
	def MdiaTp(self):
		del self._MdiaTp
		self._MdiaTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMBal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMBalNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMCur', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMCurNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaTp', type=ATMMediaType4Code, min=0, max=1, mutex_group=None, array=False),
	))

