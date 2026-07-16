# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection27
from . import FinancialInstrumentQuantity1Choice
from . import ISODate
from . import Max35Text
from . import PartyIdentification34Choice
from . import PartyIdentification35Choice
from . import PartyIdentificationAndAccount31
from . import Price4
from . import SafekeepingPlaceFormat7Choice
from . import SecuritiesAccount19
from . import SecurityIdentification14

class SettlementObligation7(base_types._BaseFieldType):

	__slots__ = ["_CSDTxId", "_ClrSgmt", "_CntrlCtrPtyTxId", "_DealPric", "_DlvryAcct", "_Dpstry", "_FinInstrmId", "_IntnddSttlmDt", "_NonClrMmb", "_PrvsBuyInId", "_Qty", "_RmngAmtToBeSttld", "_RmngQtyToBeSttld", "_SfkpgAcct", "_SfkpgPlc", "_SttlmAmt", "_TradDt"]
	@property
	def CSDTxId(self):
		return self._CSDTxId

	@CSDTxId.setter
	def CSDTxId(self, value):
		self._CSDTxId = value if value is not None else base_types.UninitialisedField(self, 'CSDTxId', Max35Text, False)

	@CSDTxId.deleter
	def CSDTxId(self):
		del self._CSDTxId
		self._CSDTxId = base_types.UninitialisedField(self, 'CSDTxId', Max35Text, False)

	@property
	def ClrSgmt(self):
		return self._ClrSgmt

	@ClrSgmt.setter
	def ClrSgmt(self, value):
		self._ClrSgmt = value if value is not None else base_types.UninitialisedField(self, 'ClrSgmt', PartyIdentification35Choice, False)

	@ClrSgmt.deleter
	def ClrSgmt(self):
		del self._ClrSgmt
		self._ClrSgmt = base_types.UninitialisedField(self, 'ClrSgmt', PartyIdentification35Choice, False)

	@property
	def CntrlCtrPtyTxId(self):
		return self._CntrlCtrPtyTxId

	@CntrlCtrPtyTxId.setter
	def CntrlCtrPtyTxId(self, value):
		self._CntrlCtrPtyTxId = value if value is not None else base_types.UninitialisedField(self, 'CntrlCtrPtyTxId', Max35Text, False)

	@CntrlCtrPtyTxId.deleter
	def CntrlCtrPtyTxId(self):
		del self._CntrlCtrPtyTxId
		self._CntrlCtrPtyTxId = base_types.UninitialisedField(self, 'CntrlCtrPtyTxId', Max35Text, False)

	@property
	def DealPric(self):
		return self._DealPric

	@DealPric.setter
	def DealPric(self, value):
		self._DealPric = value if value is not None else base_types.UninitialisedField(self, 'DealPric', Price4, False)

	@DealPric.deleter
	def DealPric(self):
		del self._DealPric
		self._DealPric = base_types.UninitialisedField(self, 'DealPric', Price4, False)

	@property
	def DlvryAcct(self):
		return self._DlvryAcct

	@DlvryAcct.setter
	def DlvryAcct(self, value):
		self._DlvryAcct = value if value is not None else base_types.UninitialisedField(self, 'DlvryAcct', SecuritiesAccount19, False)

	@DlvryAcct.deleter
	def DlvryAcct(self):
		del self._DlvryAcct
		self._DlvryAcct = base_types.UninitialisedField(self, 'DlvryAcct', SecuritiesAccount19, False)

	@property
	def Dpstry(self):
		return self._Dpstry

	@Dpstry.setter
	def Dpstry(self, value):
		self._Dpstry = value if value is not None else base_types.UninitialisedField(self, 'Dpstry', PartyIdentification34Choice, False)

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = base_types.UninitialisedField(self, 'Dpstry', PartyIdentification34Choice, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification14, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification14, False)

	@property
	def IntnddSttlmDt(self):
		return self._IntnddSttlmDt

	@IntnddSttlmDt.setter
	def IntnddSttlmDt(self, value):
		self._IntnddSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'IntnddSttlmDt', ISODate, False)

	@IntnddSttlmDt.deleter
	def IntnddSttlmDt(self):
		del self._IntnddSttlmDt
		self._IntnddSttlmDt = base_types.UninitialisedField(self, 'IntnddSttlmDt', ISODate, False)

	@property
	def NonClrMmb(self):
		return self._NonClrMmb

	@NonClrMmb.setter
	def NonClrMmb(self, value):
		self._NonClrMmb = value if value is not None else base_types.UninitialisedField(self, 'NonClrMmb', PartyIdentificationAndAccount31, False)

	@NonClrMmb.deleter
	def NonClrMmb(self):
		del self._NonClrMmb
		self._NonClrMmb = base_types.UninitialisedField(self, 'NonClrMmb', PartyIdentificationAndAccount31, False)

	@property
	def PrvsBuyInId(self):
		return self._PrvsBuyInId

	@PrvsBuyInId.setter
	def PrvsBuyInId(self, value):
		self._PrvsBuyInId = value if value is not None else base_types.UninitialisedField(self, 'PrvsBuyInId', Max35Text, False)

	@PrvsBuyInId.deleter
	def PrvsBuyInId(self):
		del self._PrvsBuyInId
		self._PrvsBuyInId = base_types.UninitialisedField(self, 'PrvsBuyInId', Max35Text, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity1Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity1Choice, False)

	@property
	def RmngAmtToBeSttld(self):
		return self._RmngAmtToBeSttld

	@RmngAmtToBeSttld.setter
	def RmngAmtToBeSttld(self, value):
		self._RmngAmtToBeSttld = value if value is not None else base_types.UninitialisedField(self, 'RmngAmtToBeSttld', AmountAndDirection27, False)

	@RmngAmtToBeSttld.deleter
	def RmngAmtToBeSttld(self):
		del self._RmngAmtToBeSttld
		self._RmngAmtToBeSttld = base_types.UninitialisedField(self, 'RmngAmtToBeSttld', AmountAndDirection27, False)

	@property
	def RmngQtyToBeSttld(self):
		return self._RmngQtyToBeSttld

	@RmngQtyToBeSttld.setter
	def RmngQtyToBeSttld(self, value):
		self._RmngQtyToBeSttld = value if value is not None else base_types.UninitialisedField(self, 'RmngQtyToBeSttld', FinancialInstrumentQuantity1Choice, False)

	@RmngQtyToBeSttld.deleter
	def RmngQtyToBeSttld(self):
		del self._RmngQtyToBeSttld
		self._RmngQtyToBeSttld = base_types.UninitialisedField(self, 'RmngQtyToBeSttld', FinancialInstrumentQuantity1Choice, False)

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
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat7Choice, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat7Choice, False)

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection27, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection27, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CSDTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSgmt', type=PartyIdentification35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CntrlCtrPtyTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealPric', type=Price4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification34Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntnddSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonClrMmb', type=PartyIdentificationAndAccount31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsBuyInId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngAmtToBeSttld', type=AmountAndDirection27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngQtyToBeSttld', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection27, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))