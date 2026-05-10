from . import base_types
from ._Max20PositiveNumber import Max20PositiveNumber
from ._ActiveOrHistoricCurrencyAnd19DecimalAmount import ActiveOrHistoricCurrencyAnd19DecimalAmount
from ._NotionalAmountLegs6 import NotionalAmountLegs6

class PositionSetTotal2(base_types._BaseFieldType):

	__slots__ = ["_Ntnl", "_NbOfTrds", "_OthrPmtAmt", "_NegVal", "_PostvVal"]
	@property
	def Ntnl(self):
		return self._Ntnl

	@Ntnl.setter
	def Ntnl(self, value):
		self._Ntnl = value if type(value) != base_types.auto else self.make_default("Ntnl")

	@Ntnl.deleter
	def Ntnl(self):
		del self._Ntnl
		self._Ntnl = None

	@property
	def NbOfTrds(self):
		return self._NbOfTrds

	@NbOfTrds.setter
	def NbOfTrds(self, value):
		self._NbOfTrds = value if type(value) != base_types.auto else self.make_default("NbOfTrds")

	@NbOfTrds.deleter
	def NbOfTrds(self):
		del self._NbOfTrds
		self._NbOfTrds = None

	@property
	def OthrPmtAmt(self):
		return self._OthrPmtAmt

	@OthrPmtAmt.setter
	def OthrPmtAmt(self, value):
		self._OthrPmtAmt = value if type(value) != base_types.auto else self.make_default("OthrPmtAmt")

	@OthrPmtAmt.deleter
	def OthrPmtAmt(self):
		del self._OthrPmtAmt
		self._OthrPmtAmt = None

	@property
	def NegVal(self):
		return self._NegVal

	@NegVal.setter
	def NegVal(self, value):
		self._NegVal = value if type(value) != base_types.auto else self.make_default("NegVal")

	@NegVal.deleter
	def NegVal(self):
		del self._NegVal
		self._NegVal = None

	@property
	def PostvVal(self):
		return self._PostvVal

	@PostvVal.setter
	def PostvVal(self, value):
		self._PostvVal = value if type(value) != base_types.auto else self.make_default("PostvVal")

	@PostvVal.deleter
	def PostvVal(self):
		del self._PostvVal
		self._PostvVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ntnl', type=NotionalAmountLegs6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfTrds', type=Max20PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmtAmt', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NegVal', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PostvVal', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=1, mutex_group=None, array=False),
	))

