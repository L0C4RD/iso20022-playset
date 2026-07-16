# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DeliveringPartiesAndAccount16
from . import ISODate
from . import Max35Text
from . import PartyIdentification113
from . import ReceivingPartiesAndAccount16
from . import SafekeepingPlaceFormat8Choice
from . import SettlementTransactionCondition30Choice
from . import TradeTransactionCondition8Choice

class FundSettlementParameters12(base_types._BaseFieldType):

	__slots__ = ["_DlvrgSdDtls", "_RcvgSdDtls", "_SctiesSttlmSysId", "_SfkpgPlc", "_SttlmDt", "_SttlmPlc", "_SttlmTxCond", "_TradTxCond"]
	@property
	def DlvrgSdDtls(self):
		return self._DlvrgSdDtls

	@DlvrgSdDtls.setter
	def DlvrgSdDtls(self, value):
		self._DlvrgSdDtls = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSdDtls', DeliveringPartiesAndAccount16, False)

	@DlvrgSdDtls.deleter
	def DlvrgSdDtls(self):
		del self._DlvrgSdDtls
		self._DlvrgSdDtls = base_types.UninitialisedField(self, 'DlvrgSdDtls', DeliveringPartiesAndAccount16, False)

	@property
	def RcvgSdDtls(self):
		return self._RcvgSdDtls

	@RcvgSdDtls.setter
	def RcvgSdDtls(self, value):
		self._RcvgSdDtls = value if value is not None else base_types.UninitialisedField(self, 'RcvgSdDtls', ReceivingPartiesAndAccount16, False)

	@RcvgSdDtls.deleter
	def RcvgSdDtls(self):
		del self._RcvgSdDtls
		self._RcvgSdDtls = base_types.UninitialisedField(self, 'RcvgSdDtls', ReceivingPartiesAndAccount16, False)

	@property
	def SctiesSttlmSysId(self):
		return self._SctiesSttlmSysId

	@SctiesSttlmSysId.setter
	def SctiesSttlmSysId(self, value):
		self._SctiesSttlmSysId = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmSysId', Max35Text, False)

	@SctiesSttlmSysId.deleter
	def SctiesSttlmSysId(self):
		del self._SctiesSttlmSysId
		self._SctiesSttlmSysId = base_types.UninitialisedField(self, 'SctiesSttlmSysId', Max35Text, False)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat8Choice, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat8Choice, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', ISODate, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', ISODate, False)

	@property
	def SttlmPlc(self):
		return self._SttlmPlc

	@SttlmPlc.setter
	def SttlmPlc(self, value):
		self._SttlmPlc = value if value is not None else base_types.UninitialisedField(self, 'SttlmPlc', PartyIdentification113, False)

	@SttlmPlc.deleter
	def SttlmPlc(self):
		del self._SttlmPlc
		self._SttlmPlc = base_types.UninitialisedField(self, 'SttlmPlc', PartyIdentification113, False)

	@property
	def SttlmTxCond(self):
		return self._SttlmTxCond

	@SttlmTxCond.setter
	def SttlmTxCond(self, value):
		self._SttlmTxCond = value if value is not None else base_types.UninitialisedField(self, 'SttlmTxCond', SettlementTransactionCondition30Choice, True)

	@SttlmTxCond.deleter
	def SttlmTxCond(self):
		del self._SttlmTxCond
		self._SttlmTxCond = base_types.UninitialisedField(self, 'SttlmTxCond', SettlementTransactionCondition30Choice, True)

	@property
	def TradTxCond(self):
		return self._TradTxCond

	@TradTxCond.setter
	def TradTxCond(self, value):
		self._TradTxCond = value if value is not None else base_types.UninitialisedField(self, 'TradTxCond', TradeTransactionCondition8Choice, True)

	@TradTxCond.deleter
	def TradTxCond(self):
		del self._TradTxCond
		self._TradTxCond = base_types.UninitialisedField(self, 'TradTxCond', TradeTransactionCondition8Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvrgSdDtls', type=DeliveringPartiesAndAccount16, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSdDtls', type=ReceivingPartiesAndAccount16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSttlmSysId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPlc', type=PartyIdentification113, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTxCond', type=SettlementTransactionCondition30Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradTxCond', type=TradeTransactionCondition8Choice, min=0, max=None, mutex_group=None, array=True),
	))