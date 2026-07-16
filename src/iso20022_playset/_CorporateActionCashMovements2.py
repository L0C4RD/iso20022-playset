# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CashAccount19
from . import DateAndDateTimeChoice
from . import Max35Text

class CorporateActionCashMovements2(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_PstngAmt", "_PstngDtTm", "_PstngId"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctDtls', CashAccount19, False)

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = base_types.UninitialisedField(self, 'AcctDtls', CashAccount19, False)

	@property
	def PstngAmt(self):
		return self._PstngAmt

	@PstngAmt.setter
	def PstngAmt(self, value):
		self._PstngAmt = value if value is not None else base_types.UninitialisedField(self, 'PstngAmt', ActiveCurrencyAndAmount, False)

	@PstngAmt.deleter
	def PstngAmt(self):
		del self._PstngAmt
		self._PstngAmt = base_types.UninitialisedField(self, 'PstngAmt', ActiveCurrencyAndAmount, False)

	@property
	def PstngDtTm(self):
		return self._PstngDtTm

	@PstngDtTm.setter
	def PstngDtTm(self, value):
		self._PstngDtTm = value if value is not None else base_types.UninitialisedField(self, 'PstngDtTm', DateAndDateTimeChoice, False)

	@PstngDtTm.deleter
	def PstngDtTm(self):
		del self._PstngDtTm
		self._PstngDtTm = base_types.UninitialisedField(self, 'PstngDtTm', DateAndDateTimeChoice, False)

	@property
	def PstngId(self):
		return self._PstngId

	@PstngId.setter
	def PstngId(self, value):
		self._PstngId = value if value is not None else base_types.UninitialisedField(self, 'PstngId', Max35Text, False)

	@PstngId.deleter
	def PstngId(self):
		del self._PstngId
		self._PstngId = base_types.UninitialisedField(self, 'PstngId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=CashAccount19, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))