# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._BalanceQuantity13Choice import BalanceQuantity13Choice
from ._BlockChainAddressWallet3 import BlockChainAddressWallet3
from ._ForeignExchangeTerms19 import ForeignExchangeTerms19
from ._GenericIdentification178 import GenericIdentification178
from ._PartyIdentification232 import PartyIdentification232
from ._Rating2 import Rating2
from ._SafeKeepingPlace3 import SafeKeepingPlace3
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SecuritiesSettlementStatus3Code import SecuritiesSettlementStatus3Code
from ._SecurityIdentification19 import SecurityIdentification19
from ._ValuationsDetails1 import ValuationsDetails1
from ._YesNoIndicator import YesNoIndicator

class SecuritiesBalance3(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_BlckChainAdrOrWllt", "_CollInd", "_DnmtnCcy", "_FXDtls", "_FinInstrmId", "_Qty", "_RatgDtls", "_SfkpgAcct", "_SfkpgPlc", "_SttlmSts", "_TxLotNb", "_ValtnDtls"]
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
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != base_types.auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def CollInd(self):
		return self._CollInd

	@CollInd.setter
	def CollInd(self, value):
		self._CollInd = value if type(value) != base_types.auto else self.make_default("CollInd")

	@CollInd.deleter
	def CollInd(self):
		del self._CollInd
		self._CollInd = None

	@property
	def DnmtnCcy(self):
		return self._DnmtnCcy

	@DnmtnCcy.setter
	def DnmtnCcy(self, value):
		self._DnmtnCcy = value if type(value) != base_types.auto else self.make_default("DnmtnCcy")

	@DnmtnCcy.deleter
	def DnmtnCcy(self):
		del self._DnmtnCcy
		self._DnmtnCcy = None

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if type(value) != base_types.auto else self.make_default("FXDtls")

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def RatgDtls(self):
		return self._RatgDtls

	@RatgDtls.setter
	def RatgDtls(self, value):
		self._RatgDtls = value if type(value) != base_types.auto else self.make_default("RatgDtls")

	@RatgDtls.deleter
	def RatgDtls(self):
		del self._RatgDtls
		self._RatgDtls = None

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
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if type(value) != base_types.auto else self.make_default("SttlmSts")

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = None

	@property
	def TxLotNb(self):
		return self._TxLotNb

	@TxLotNb.setter
	def TxLotNb(self, value):
		self._TxLotNb = value if type(value) != base_types.auto else self.make_default("TxLotNb")

	@TxLotNb.deleter
	def TxLotNb(self):
		del self._TxLotNb
		self._TxLotNb = None

	@property
	def ValtnDtls(self):
		return self._ValtnDtls

	@ValtnDtls.setter
	def ValtnDtls(self, value):
		self._ValtnDtls = value if type(value) != base_types.auto else self.make_default("ValtnDtls")

	@ValtnDtls.deleter
	def ValtnDtls(self):
		del self._ValtnDtls
		self._ValtnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification232, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DnmtnCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=BalanceQuantity13Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RatgDtls', type=Rating2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSts', type=SecuritiesSettlementStatus3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxLotNb', type=GenericIdentification178, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValtnDtls', type=ValuationsDetails1, min=0, max=1, mutex_group=None, array=False),
	))