from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ISODateTime import ISODateTime
from ._Number import Number
from ._PreferenceToIncome5Choice import PreferenceToIncome5Choice

class Equity3(base_types._BaseFieldType):

	__slots__ = ["_MtrtyDt", "_PrefToIncm", "_ParVal", "_NonPdAmt", "_VtngRghtsPerShr"]
	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != base_types.auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def NonPdAmt(self):
		return self._NonPdAmt

	@NonPdAmt.setter
	def NonPdAmt(self, value):
		self._NonPdAmt = value if type(value) != base_types.auto else self.make_default("NonPdAmt")

	@NonPdAmt.deleter
	def NonPdAmt(self):
		del self._NonPdAmt
		self._NonPdAmt = None

	@property
	def ParVal(self):
		return self._ParVal

	@ParVal.setter
	def ParVal(self, value):
		self._ParVal = value if type(value) != base_types.auto else self.make_default("ParVal")

	@ParVal.deleter
	def ParVal(self):
		del self._ParVal
		self._ParVal = None

	@property
	def PrefToIncm(self):
		return self._PrefToIncm

	@PrefToIncm.setter
	def PrefToIncm(self, value):
		self._PrefToIncm = value if type(value) != base_types.auto else self.make_default("PrefToIncm")

	@PrefToIncm.deleter
	def PrefToIncm(self):
		del self._PrefToIncm
		self._PrefToIncm = None

	@property
	def VtngRghtsPerShr(self):
		return self._VtngRghtsPerShr

	@VtngRghtsPerShr.setter
	def VtngRghtsPerShr(self, value):
		self._VtngRghtsPerShr = value if type(value) != base_types.auto else self.make_default("VtngRghtsPerShr")

	@VtngRghtsPerShr.deleter
	def VtngRghtsPerShr(self):
		del self._VtngRghtsPerShr
		self._VtngRghtsPerShr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtrtyDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonPdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ParVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrefToIncm', type=PreferenceToIncome5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VtngRghtsPerShr', type=Number, min=0, max=1, mutex_group=None, array=False),
	))

