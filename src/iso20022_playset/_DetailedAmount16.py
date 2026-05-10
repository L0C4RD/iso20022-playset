from . import base_types
from ._DetailedAmount13 import DetailedAmount13
from ._Number import Number
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._ActiveCurrencyCode import ActiveCurrencyCode

class DetailedAmount16(base_types._BaseFieldType):

	__slots__ = ["_AmtToDpst", "_Dontn", "_CshBckAmt", "_AcctSeqNb", "_Ccy", "_Fees"]
	@property
	def AmtToDpst(self):
		return self._AmtToDpst

	@AmtToDpst.setter
	def AmtToDpst(self, value):
		self._AmtToDpst = value if type(value) != base_types.auto else self.make_default("AmtToDpst")

	@AmtToDpst.deleter
	def AmtToDpst(self):
		del self._AmtToDpst
		self._AmtToDpst = None

	@property
	def Dontn(self):
		return self._Dontn

	@Dontn.setter
	def Dontn(self, value):
		self._Dontn = value if type(value) != base_types.auto else self.make_default("Dontn")

	@Dontn.deleter
	def Dontn(self):
		del self._Dontn
		self._Dontn = None

	@property
	def CshBckAmt(self):
		return self._CshBckAmt

	@CshBckAmt.setter
	def CshBckAmt(self, value):
		self._CshBckAmt = value if type(value) != base_types.auto else self.make_default("CshBckAmt")

	@CshBckAmt.deleter
	def CshBckAmt(self):
		del self._CshBckAmt
		self._CshBckAmt = None

	@property
	def AcctSeqNb(self):
		return self._AcctSeqNb

	@AcctSeqNb.setter
	def AcctSeqNb(self, value):
		self._AcctSeqNb = value if type(value) != base_types.auto else self.make_default("AcctSeqNb")

	@AcctSeqNb.deleter
	def AcctSeqNb(self):
		del self._AcctSeqNb
		self._AcctSeqNb = None

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

	@property
	def Fees(self):
		return self._Fees

	@Fees.setter
	def Fees(self, value):
		self._Fees = value if type(value) != base_types.auto else self.make_default("Fees")

	@Fees.deleter
	def Fees(self):
		del self._Fees
		self._Fees = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtToDpst', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dontn', type=DetailedAmount13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshBckAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fees', type=DetailedAmount13, min=0, max=None, mutex_group=None, array=True),
	))

