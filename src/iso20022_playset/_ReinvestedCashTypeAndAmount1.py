from . import base_types
from ._ReinvestmentType1Code import ReinvestmentType1Code
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class ReinvestedCashTypeAndAmount1(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_RinvstdCshAmt"]
	@property
	def RinvstdCshAmt(self):
		return self._RinvstdCshAmt

	@RinvstdCshAmt.setter
	def RinvstdCshAmt(self, value):
		self._RinvstdCshAmt = value if type(value) != base_types.auto else self.make_default("RinvstdCshAmt")

	@RinvstdCshAmt.deleter
	def RinvstdCshAmt(self):
		del self._RinvstdCshAmt
		self._RinvstdCshAmt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RinvstdCshAmt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ReinvestmentType1Code, min=1, max=1, mutex_group=None, array=False),
	))

