# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import Max10000Binary
from . import TrueFalseIndicator

class CardPaymentTransactionDetails50(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_ICCRltdData", "_KeepAuthstnOpn", "_TtlAmt", "_VldtyDt"]
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
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if value is not None else base_types.UninitialisedField(self, 'ICCRltdData', Max10000Binary, False)

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = base_types.UninitialisedField(self, 'ICCRltdData', Max10000Binary, False)

	@property
	def KeepAuthstnOpn(self):
		return self._KeepAuthstnOpn

	@KeepAuthstnOpn.setter
	def KeepAuthstnOpn(self, value):
		self._KeepAuthstnOpn = value if value is not None else base_types.UninitialisedField(self, 'KeepAuthstnOpn', TrueFalseIndicator, False)

	@KeepAuthstnOpn.deleter
	def KeepAuthstnOpn(self):
		del self._KeepAuthstnOpn
		self._KeepAuthstnOpn = base_types.UninitialisedField(self, 'KeepAuthstnOpn', TrueFalseIndicator, False)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	@property
	def VldtyDt(self):
		return self._VldtyDt

	@VldtyDt.setter
	def VldtyDt(self, value):
		self._VldtyDt = value if value is not None else base_types.UninitialisedField(self, 'VldtyDt', ISODate, False)

	@VldtyDt.deleter
	def VldtyDt(self):
		del self._VldtyDt
		self._VldtyDt = base_types.UninitialisedField(self, 'VldtyDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeepAuthstnOpn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))