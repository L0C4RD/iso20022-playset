from . import base_types
from .PartyIdentification144 import PartyIdentification144
from .Quantity51Choice import Quantity51Choice
from .SafeKeepingPlace5 import SafeKeepingPlace5
from .AmountAndDirection5 import AmountAndDirection5
from .CashAccountIdentification9Choice import CashAccountIdentification9Choice
from .FinancialInstrumentQuantity33Choice import FinancialInstrumentQuantity33Choice
from .SecuritiesAccount19 import SecuritiesAccount19
from .BlockChainAddressWallet3 import BlockChainAddressWallet3

class QuantityAndAccount120(base_types._BaseFieldType):

	__slots__ = ["_CshAcct", "_PrevslySttldQty", "_PrevslySttldAmt", "_RmngToBeSttldQty", "_AcctOwnr", "_RmngToBeSttldAmt", "_SfkpgAcct", "_SttldQty", "_SfkpgPlc", "_BlckChainAdrOrWllt"]
	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def PrevslySttldQty(self):
		return self._PrevslySttldQty

	@PrevslySttldQty.setter
	def PrevslySttldQty(self, value):
		self._PrevslySttldQty = value if type(value) != base_types.auto else self.make_default("PrevslySttldQty")

	@PrevslySttldQty.deleter
	def PrevslySttldQty(self):
		del self._PrevslySttldQty
		self._PrevslySttldQty = None

	@property
	def PrevslySttldAmt(self):
		return self._PrevslySttldAmt

	@PrevslySttldAmt.setter
	def PrevslySttldAmt(self, value):
		self._PrevslySttldAmt = value if type(value) != base_types.auto else self.make_default("PrevslySttldAmt")

	@PrevslySttldAmt.deleter
	def PrevslySttldAmt(self):
		del self._PrevslySttldAmt
		self._PrevslySttldAmt = None

	@property
	def RmngToBeSttldQty(self):
		return self._RmngToBeSttldQty

	@RmngToBeSttldQty.setter
	def RmngToBeSttldQty(self, value):
		self._RmngToBeSttldQty = value if type(value) != base_types.auto else self.make_default("RmngToBeSttldQty")

	@RmngToBeSttldQty.deleter
	def RmngToBeSttldQty(self):
		del self._RmngToBeSttldQty
		self._RmngToBeSttldQty = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def RmngToBeSttldAmt(self):
		return self._RmngToBeSttldAmt

	@RmngToBeSttldAmt.setter
	def RmngToBeSttldAmt(self, value):
		self._RmngToBeSttldAmt = value if type(value) != base_types.auto else self.make_default("RmngToBeSttldAmt")

	@RmngToBeSttldAmt.deleter
	def RmngToBeSttldAmt(self):
		del self._RmngToBeSttldAmt
		self._RmngToBeSttldAmt = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def SttldQty(self):
		return self._SttldQty

	@SttldQty.setter
	def SttldQty(self, value):
		self._SttldQty = value if type(value) != base_types.auto else self.make_default("SttldQty")

	@SttldQty.deleter
	def SttldQty(self):
		del self._SttldQty
		self._SttldQty = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != base_types.auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslySttldQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslySttldAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngToBeSttldQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification144, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngToBeSttldAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttldQty', type=Quantity51Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
	))

