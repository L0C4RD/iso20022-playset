# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Acquirer10
from . import ActiveCurrencyCode
from . import ImpliedCurrencyAndAmount

class PaymentAccount3(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_CurBal", "_PmtAcqrrData"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def CurBal(self):
		return self._CurBal

	@CurBal.setter
	def CurBal(self, value):
		self._CurBal = value if value is not None else base_types.UninitialisedField(self, 'CurBal', ImpliedCurrencyAndAmount, False)

	@CurBal.deleter
	def CurBal(self):
		del self._CurBal
		self._CurBal = base_types.UninitialisedField(self, 'CurBal', ImpliedCurrencyAndAmount, False)

	@property
	def PmtAcqrrData(self):
		return self._PmtAcqrrData

	@PmtAcqrrData.setter
	def PmtAcqrrData(self, value):
		self._PmtAcqrrData = value if value is not None else base_types.UninitialisedField(self, 'PmtAcqrrData', Acquirer10, False)

	@PmtAcqrrData.deleter
	def PmtAcqrrData(self):
		del self._PmtAcqrrData
		self._PmtAcqrrData = base_types.UninitialisedField(self, 'PmtAcqrrData', Acquirer10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurBal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAcqrrData', type=Acquirer10, min=0, max=1, mutex_group=None, array=False),
	))