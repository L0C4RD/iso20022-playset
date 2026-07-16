# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMTransactionAmounts10
from . import ATMTransactionAmounts7
from . import ActiveCurrencyCode
from . import ImpliedCurrencyAndAmount

class ATMTransactionAmounts11(base_types._BaseFieldType):

	__slots__ = ["_AddtlAmt", "_Ccy", "_DpstLmts", "_MaxPssblAmt", "_MinPssblAmt"]
	@property
	def AddtlAmt(self):
		return self._AddtlAmt

	@AddtlAmt.setter
	def AddtlAmt(self, value):
		self._AddtlAmt = value if value is not None else base_types.UninitialisedField(self, 'AddtlAmt', ATMTransactionAmounts7, True)

	@AddtlAmt.deleter
	def AddtlAmt(self):
		del self._AddtlAmt
		self._AddtlAmt = base_types.UninitialisedField(self, 'AddtlAmt', ATMTransactionAmounts7, True)

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
	def DpstLmts(self):
		return self._DpstLmts

	@DpstLmts.setter
	def DpstLmts(self, value):
		self._DpstLmts = value if value is not None else base_types.UninitialisedField(self, 'DpstLmts', ATMTransactionAmounts10, True)

	@DpstLmts.deleter
	def DpstLmts(self):
		del self._DpstLmts
		self._DpstLmts = base_types.UninitialisedField(self, 'DpstLmts', ATMTransactionAmounts10, True)

	@property
	def MaxPssblAmt(self):
		return self._MaxPssblAmt

	@MaxPssblAmt.setter
	def MaxPssblAmt(self, value):
		self._MaxPssblAmt = value if value is not None else base_types.UninitialisedField(self, 'MaxPssblAmt', ImpliedCurrencyAndAmount, False)

	@MaxPssblAmt.deleter
	def MaxPssblAmt(self):
		del self._MaxPssblAmt
		self._MaxPssblAmt = base_types.UninitialisedField(self, 'MaxPssblAmt', ImpliedCurrencyAndAmount, False)

	@property
	def MinPssblAmt(self):
		return self._MinPssblAmt

	@MinPssblAmt.setter
	def MinPssblAmt(self, value):
		self._MinPssblAmt = value if value is not None else base_types.UninitialisedField(self, 'MinPssblAmt', ImpliedCurrencyAndAmount, False)

	@MinPssblAmt.deleter
	def MinPssblAmt(self):
		del self._MinPssblAmt
		self._MinPssblAmt = base_types.UninitialisedField(self, 'MinPssblAmt', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlAmt', type=ATMTransactionAmounts7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstLmts', type=ATMTransactionAmounts10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MaxPssblAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinPssblAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))