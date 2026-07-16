# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import BalanceQuantity13Choice
from . import BlockChainAddressWallet3
from . import ForeignExchangeTerms19
from . import GenericIdentification178
from . import PartyIdentification232
from . import Rating2
from . import SafeKeepingPlace3
from . import SecuritiesAccount19
from . import SecuritiesSettlementStatus3Code
from . import SecurityIdentification19
from . import ValuationsDetails1
from . import YesNoIndicator

class SecuritiesBalance3(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_BlckChainAdrOrWllt", "_CollInd", "_DnmtnCcy", "_FXDtls", "_FinInstrmId", "_Qty", "_RatgDtls", "_SfkpgAcct", "_SfkpgPlc", "_SttlmSts", "_TxLotNb", "_ValtnDtls"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification232, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification232, False)

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet3, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet3, False)

	@property
	def CollInd(self):
		return self._CollInd

	@CollInd.setter
	def CollInd(self, value):
		self._CollInd = value if value is not None else base_types.UninitialisedField(self, 'CollInd', YesNoIndicator, False)

	@CollInd.deleter
	def CollInd(self):
		del self._CollInd
		self._CollInd = base_types.UninitialisedField(self, 'CollInd', YesNoIndicator, False)

	@property
	def DnmtnCcy(self):
		return self._DnmtnCcy

	@DnmtnCcy.setter
	def DnmtnCcy(self, value):
		self._DnmtnCcy = value if value is not None else base_types.UninitialisedField(self, 'DnmtnCcy', ActiveOrHistoricCurrencyCode, False)

	@DnmtnCcy.deleter
	def DnmtnCcy(self):
		del self._DnmtnCcy
		self._DnmtnCcy = base_types.UninitialisedField(self, 'DnmtnCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if value is not None else base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms19, False)

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms19, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', BalanceQuantity13Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', BalanceQuantity13Choice, False)

	@property
	def RatgDtls(self):
		return self._RatgDtls

	@RatgDtls.setter
	def RatgDtls(self, value):
		self._RatgDtls = value if value is not None else base_types.UninitialisedField(self, 'RatgDtls', Rating2, True)

	@RatgDtls.deleter
	def RatgDtls(self):
		del self._RatgDtls
		self._RatgDtls = base_types.UninitialisedField(self, 'RatgDtls', Rating2, True)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafeKeepingPlace3, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafeKeepingPlace3, False)

	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if value is not None else base_types.UninitialisedField(self, 'SttlmSts', SecuritiesSettlementStatus3Code, False)

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = base_types.UninitialisedField(self, 'SttlmSts', SecuritiesSettlementStatus3Code, False)

	@property
	def TxLotNb(self):
		return self._TxLotNb

	@TxLotNb.setter
	def TxLotNb(self, value):
		self._TxLotNb = value if value is not None else base_types.UninitialisedField(self, 'TxLotNb', GenericIdentification178, True)

	@TxLotNb.deleter
	def TxLotNb(self):
		del self._TxLotNb
		self._TxLotNb = base_types.UninitialisedField(self, 'TxLotNb', GenericIdentification178, True)

	@property
	def ValtnDtls(self):
		return self._ValtnDtls

	@ValtnDtls.setter
	def ValtnDtls(self, value):
		self._ValtnDtls = value if value is not None else base_types.UninitialisedField(self, 'ValtnDtls', ValuationsDetails1, False)

	@ValtnDtls.deleter
	def ValtnDtls(self):
		del self._ValtnDtls
		self._ValtnDtls = base_types.UninitialisedField(self, 'ValtnDtls', ValuationsDetails1, False)

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