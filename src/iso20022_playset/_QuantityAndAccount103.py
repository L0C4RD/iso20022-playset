# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection19
from . import BlockChainAddressWallet7
from . import CashAccountIdentification6Choice
from . import FinancialInstrumentQuantity36Choice
from . import PartyIdentification156
from . import Quantity54Choice
from . import SafeKeepingPlace4
from . import SecuritiesAccount30

class QuantityAndAccount103(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_BlckChainAdrOrWllt", "_CshAcct", "_PrevslySttldAmt", "_PrevslySttldQty", "_RmngToBeSttldAmt", "_RmngToBeSttldQty", "_SfkpgAcct", "_SfkpgPlc", "_SttldQty"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification156, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification156, False)

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet7, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet7, False)

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if value is not None else base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification6Choice, False)

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification6Choice, False)

	@property
	def PrevslySttldAmt(self):
		return self._PrevslySttldAmt

	@PrevslySttldAmt.setter
	def PrevslySttldAmt(self, value):
		self._PrevslySttldAmt = value if value is not None else base_types.UninitialisedField(self, 'PrevslySttldAmt', AmountAndDirection19, False)

	@PrevslySttldAmt.deleter
	def PrevslySttldAmt(self):
		del self._PrevslySttldAmt
		self._PrevslySttldAmt = base_types.UninitialisedField(self, 'PrevslySttldAmt', AmountAndDirection19, False)

	@property
	def PrevslySttldQty(self):
		return self._PrevslySttldQty

	@PrevslySttldQty.setter
	def PrevslySttldQty(self, value):
		self._PrevslySttldQty = value if value is not None else base_types.UninitialisedField(self, 'PrevslySttldQty', FinancialInstrumentQuantity36Choice, False)

	@PrevslySttldQty.deleter
	def PrevslySttldQty(self):
		del self._PrevslySttldQty
		self._PrevslySttldQty = base_types.UninitialisedField(self, 'PrevslySttldQty', FinancialInstrumentQuantity36Choice, False)

	@property
	def RmngToBeSttldAmt(self):
		return self._RmngToBeSttldAmt

	@RmngToBeSttldAmt.setter
	def RmngToBeSttldAmt(self, value):
		self._RmngToBeSttldAmt = value if value is not None else base_types.UninitialisedField(self, 'RmngToBeSttldAmt', AmountAndDirection19, False)

	@RmngToBeSttldAmt.deleter
	def RmngToBeSttldAmt(self):
		del self._RmngToBeSttldAmt
		self._RmngToBeSttldAmt = base_types.UninitialisedField(self, 'RmngToBeSttldAmt', AmountAndDirection19, False)

	@property
	def RmngToBeSttldQty(self):
		return self._RmngToBeSttldQty

	@RmngToBeSttldQty.setter
	def RmngToBeSttldQty(self, value):
		self._RmngToBeSttldQty = value if value is not None else base_types.UninitialisedField(self, 'RmngToBeSttldQty', FinancialInstrumentQuantity36Choice, False)

	@RmngToBeSttldQty.deleter
	def RmngToBeSttldQty(self):
		del self._RmngToBeSttldQty
		self._RmngToBeSttldQty = base_types.UninitialisedField(self, 'RmngToBeSttldQty', FinancialInstrumentQuantity36Choice, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount30, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount30, False)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafeKeepingPlace4, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafeKeepingPlace4, False)

	@property
	def SttldQty(self):
		return self._SttldQty

	@SttldQty.setter
	def SttldQty(self, value):
		self._SttldQty = value if value is not None else base_types.UninitialisedField(self, 'SttldQty', Quantity54Choice, False)

	@SttldQty.deleter
	def SttldQty(self):
		del self._SttldQty
		self._SttldQty = base_types.UninitialisedField(self, 'SttldQty', Quantity54Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification156, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslySttldAmt', type=AmountAndDirection19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslySttldQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngToBeSttldAmt', type=AmountAndDirection19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngToBeSttldQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttldQty', type=Quantity54Choice, min=1, max=1, mutex_group=None, array=False),
	))