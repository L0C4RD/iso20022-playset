# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import DetailedAmount13
from . import ImpliedCurrencyAndAmount
from . import Number

class DetailedAmount16(base_types._BaseFieldType):

	__slots__ = ["_AcctSeqNb", "_AmtToDpst", "_Ccy", "_CshBckAmt", "_Dontn", "_Fees"]
	@property
	def AcctSeqNb(self):
		return self._AcctSeqNb

	@AcctSeqNb.setter
	def AcctSeqNb(self, value):
		self._AcctSeqNb = value if value is not None else base_types.UninitialisedField(self, 'AcctSeqNb', Number, False)

	@AcctSeqNb.deleter
	def AcctSeqNb(self):
		del self._AcctSeqNb
		self._AcctSeqNb = base_types.UninitialisedField(self, 'AcctSeqNb', Number, False)

	@property
	def AmtToDpst(self):
		return self._AmtToDpst

	@AmtToDpst.setter
	def AmtToDpst(self, value):
		self._AmtToDpst = value if value is not None else base_types.UninitialisedField(self, 'AmtToDpst', ImpliedCurrencyAndAmount, False)

	@AmtToDpst.deleter
	def AmtToDpst(self):
		del self._AmtToDpst
		self._AmtToDpst = base_types.UninitialisedField(self, 'AmtToDpst', ImpliedCurrencyAndAmount, False)

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
	def CshBckAmt(self):
		return self._CshBckAmt

	@CshBckAmt.setter
	def CshBckAmt(self, value):
		self._CshBckAmt = value if value is not None else base_types.UninitialisedField(self, 'CshBckAmt', ImpliedCurrencyAndAmount, False)

	@CshBckAmt.deleter
	def CshBckAmt(self):
		del self._CshBckAmt
		self._CshBckAmt = base_types.UninitialisedField(self, 'CshBckAmt', ImpliedCurrencyAndAmount, False)

	@property
	def Dontn(self):
		return self._Dontn

	@Dontn.setter
	def Dontn(self, value):
		self._Dontn = value if value is not None else base_types.UninitialisedField(self, 'Dontn', DetailedAmount13, True)

	@Dontn.deleter
	def Dontn(self):
		del self._Dontn
		self._Dontn = base_types.UninitialisedField(self, 'Dontn', DetailedAmount13, True)

	@property
	def Fees(self):
		return self._Fees

	@Fees.setter
	def Fees(self, value):
		self._Fees = value if value is not None else base_types.UninitialisedField(self, 'Fees', DetailedAmount13, True)

	@Fees.deleter
	def Fees(self):
		del self._Fees
		self._Fees = base_types.UninitialisedField(self, 'Fees', DetailedAmount13, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtToDpst', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshBckAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dontn', type=DetailedAmount13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Fees', type=DetailedAmount13, min=0, max=None, mutex_group=None, array=True),
	))