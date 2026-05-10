from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._Acquirer10 import Acquirer10
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount

class PaymentAccount3(base_types._BaseFieldType):

	__slots__ = ["_PmtAcqrrData", "_CurBal", "_Ccy"]
	@property
	def PmtAcqrrData(self):
		return self._PmtAcqrrData

	@PmtAcqrrData.setter
	def PmtAcqrrData(self, value):
		self._PmtAcqrrData = value if type(value) != base_types.auto else self.make_default("PmtAcqrrData")

	@PmtAcqrrData.deleter
	def PmtAcqrrData(self):
		del self._PmtAcqrrData
		self._PmtAcqrrData = None

	@property
	def CurBal(self):
		return self._CurBal

	@CurBal.setter
	def CurBal(self, value):
		self._CurBal = value if type(value) != base_types.auto else self.make_default("CurBal")

	@CurBal.deleter
	def CurBal(self):
		del self._CurBal
		self._CurBal = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtAcqrrData', type=Acquirer10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurBal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))

