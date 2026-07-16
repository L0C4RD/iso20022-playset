# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CashAccount18
from . import Charges1
from . import Max35Text

class CashMovement1(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_Amt", "_Chrgs", "_MvmntId", "_TaxAmt"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctDtls', CashAccount18, False)

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = base_types.UninitialisedField(self, 'AcctDtls', CashAccount18, False)

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if value is not None else base_types.UninitialisedField(self, 'Chrgs', Charges1, True)

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = base_types.UninitialisedField(self, 'Chrgs', Charges1, True)

	@property
	def MvmntId(self):
		return self._MvmntId

	@MvmntId.setter
	def MvmntId(self, value):
		self._MvmntId = value if value is not None else base_types.UninitialisedField(self, 'MvmntId', Max35Text, False)

	@MvmntId.deleter
	def MvmntId(self):
		del self._MvmntId
		self._MvmntId = base_types.UninitialisedField(self, 'MvmntId', Max35Text, False)

	@property
	def TaxAmt(self):
		return self._TaxAmt

	@TaxAmt.setter
	def TaxAmt(self, value):
		self._TaxAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxAmt', ActiveCurrencyAndAmount, False)

	@TaxAmt.deleter
	def TaxAmt(self):
		del self._TaxAmt
		self._TaxAmt = base_types.UninitialisedField(self, 'TaxAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=CashAccount18, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrgs', type=Charges1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))