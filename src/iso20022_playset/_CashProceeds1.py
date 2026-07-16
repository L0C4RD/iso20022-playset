# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CashAccount19
from . import Max350Text

class CashProceeds1(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_PstngAmt", "_RcncltnDtls"]
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
	def RcncltnDtls(self):
		return self._RcncltnDtls

	@RcncltnDtls.setter
	def RcncltnDtls(self, value):
		self._RcncltnDtls = value if value is not None else base_types.UninitialisedField(self, 'RcncltnDtls', Max350Text, False)

	@RcncltnDtls.deleter
	def RcncltnDtls(self):
		del self._RcncltnDtls
		self._RcncltnDtls = base_types.UninitialisedField(self, 'RcncltnDtls', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=CashAccount19, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))