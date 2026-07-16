# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import AmountAndCurrency2
from . import ClearingMethod1Code
from . import ISODate
from . import ISODateTime
from . import InstrumentLeg7
from . import Max30Text
from . import Max35Text
from . import Option16
from . import OrderStatus8Code
from . import SecurityIdentification38Choice
from . import Trade10
from . import TradingMethodType1Code
from . import TradingModeType1Code
from . import UnderlyingProductIdentifier1Code

class Trade7(base_types._BaseFieldType):

	__slots__ = ["_BaseCcyOrAmt", "_ClrMtd", "_CmbntnDealTcktId", "_ContraCcy", "_DealTcktId", "_DtAndTm", "_DtConfd", "_ExctnTp", "_FXDtls", "_FXTradPdct", "_Optn", "_PdctId", "_PlcOfConf", "_SttlmCcy", "_SwpLeg", "_Symb", "_TradId", "_TradgCcy", "_TradgMd", "_TradgMtd", "_TrgtCcyOrAmt", "_TxTm"]
	@property
	def BaseCcyOrAmt(self):
		return self._BaseCcyOrAmt

	@BaseCcyOrAmt.setter
	def BaseCcyOrAmt(self, value):
		self._BaseCcyOrAmt = value if value is not None else base_types.UninitialisedField(self, 'BaseCcyOrAmt', AmountAndCurrency2, False)

	@BaseCcyOrAmt.deleter
	def BaseCcyOrAmt(self):
		del self._BaseCcyOrAmt
		self._BaseCcyOrAmt = base_types.UninitialisedField(self, 'BaseCcyOrAmt', AmountAndCurrency2, False)

	@property
	def ClrMtd(self):
		return self._ClrMtd

	@ClrMtd.setter
	def ClrMtd(self, value):
		self._ClrMtd = value if value is not None else base_types.UninitialisedField(self, 'ClrMtd', ClearingMethod1Code, False)

	@ClrMtd.deleter
	def ClrMtd(self):
		del self._ClrMtd
		self._ClrMtd = base_types.UninitialisedField(self, 'ClrMtd', ClearingMethod1Code, False)

	@property
	def CmbntnDealTcktId(self):
		return self._CmbntnDealTcktId

	@CmbntnDealTcktId.setter
	def CmbntnDealTcktId(self, value):
		self._CmbntnDealTcktId = value if value is not None else base_types.UninitialisedField(self, 'CmbntnDealTcktId', Max35Text, False)

	@CmbntnDealTcktId.deleter
	def CmbntnDealTcktId(self):
		del self._CmbntnDealTcktId
		self._CmbntnDealTcktId = base_types.UninitialisedField(self, 'CmbntnDealTcktId', Max35Text, False)

	@property
	def ContraCcy(self):
		return self._ContraCcy

	@ContraCcy.setter
	def ContraCcy(self, value):
		self._ContraCcy = value if value is not None else base_types.UninitialisedField(self, 'ContraCcy', ActiveCurrencyCode, False)

	@ContraCcy.deleter
	def ContraCcy(self):
		del self._ContraCcy
		self._ContraCcy = base_types.UninitialisedField(self, 'ContraCcy', ActiveCurrencyCode, False)

	@property
	def DealTcktId(self):
		return self._DealTcktId

	@DealTcktId.setter
	def DealTcktId(self, value):
		self._DealTcktId = value if value is not None else base_types.UninitialisedField(self, 'DealTcktId', Max30Text, False)

	@DealTcktId.deleter
	def DealTcktId(self):
		del self._DealTcktId
		self._DealTcktId = base_types.UninitialisedField(self, 'DealTcktId', Max30Text, False)

	@property
	def DtAndTm(self):
		return self._DtAndTm

	@DtAndTm.setter
	def DtAndTm(self, value):
		self._DtAndTm = value if value is not None else base_types.UninitialisedField(self, 'DtAndTm', ISODateTime, False)

	@DtAndTm.deleter
	def DtAndTm(self):
		del self._DtAndTm
		self._DtAndTm = base_types.UninitialisedField(self, 'DtAndTm', ISODateTime, False)

	@property
	def DtConfd(self):
		return self._DtConfd

	@DtConfd.setter
	def DtConfd(self, value):
		self._DtConfd = value if value is not None else base_types.UninitialisedField(self, 'DtConfd', ISODate, False)

	@DtConfd.deleter
	def DtConfd(self):
		del self._DtConfd
		self._DtConfd = base_types.UninitialisedField(self, 'DtConfd', ISODate, False)

	@property
	def ExctnTp(self):
		return self._ExctnTp

	@ExctnTp.setter
	def ExctnTp(self, value):
		self._ExctnTp = value if value is not None else base_types.UninitialisedField(self, 'ExctnTp', OrderStatus8Code, False)

	@ExctnTp.deleter
	def ExctnTp(self):
		del self._ExctnTp
		self._ExctnTp = base_types.UninitialisedField(self, 'ExctnTp', OrderStatus8Code, False)

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if value is not None else base_types.UninitialisedField(self, 'FXDtls', Trade10, False)

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = base_types.UninitialisedField(self, 'FXDtls', Trade10, False)

	@property
	def FXTradPdct(self):
		return self._FXTradPdct

	@FXTradPdct.setter
	def FXTradPdct(self, value):
		self._FXTradPdct = value if value is not None else base_types.UninitialisedField(self, 'FXTradPdct', UnderlyingProductIdentifier1Code, False)

	@FXTradPdct.deleter
	def FXTradPdct(self):
		del self._FXTradPdct
		self._FXTradPdct = base_types.UninitialisedField(self, 'FXTradPdct', UnderlyingProductIdentifier1Code, False)

	@property
	def Optn(self):
		return self._Optn

	@Optn.setter
	def Optn(self, value):
		self._Optn = value if value is not None else base_types.UninitialisedField(self, 'Optn', Option16, False)

	@Optn.deleter
	def Optn(self):
		del self._Optn
		self._Optn = base_types.UninitialisedField(self, 'Optn', Option16, False)

	@property
	def PdctId(self):
		return self._PdctId

	@PdctId.setter
	def PdctId(self, value):
		self._PdctId = value if value is not None else base_types.UninitialisedField(self, 'PdctId', SecurityIdentification38Choice, False)

	@PdctId.deleter
	def PdctId(self):
		del self._PdctId
		self._PdctId = base_types.UninitialisedField(self, 'PdctId', SecurityIdentification38Choice, False)

	@property
	def PlcOfConf(self):
		return self._PlcOfConf

	@PlcOfConf.setter
	def PlcOfConf(self, value):
		self._PlcOfConf = value if value is not None else base_types.UninitialisedField(self, 'PlcOfConf', Max35Text, False)

	@PlcOfConf.deleter
	def PlcOfConf(self):
		del self._PlcOfConf
		self._PlcOfConf = base_types.UninitialisedField(self, 'PlcOfConf', Max35Text, False)

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@property
	def SwpLeg(self):
		return self._SwpLeg

	@SwpLeg.setter
	def SwpLeg(self, value):
		self._SwpLeg = value if value is not None else base_types.UninitialisedField(self, 'SwpLeg', InstrumentLeg7, True)

	@SwpLeg.deleter
	def SwpLeg(self):
		del self._SwpLeg
		self._SwpLeg = base_types.UninitialisedField(self, 'SwpLeg', InstrumentLeg7, True)

	@property
	def Symb(self):
		return self._Symb

	@Symb.setter
	def Symb(self, value):
		self._Symb = value if value is not None else base_types.UninitialisedField(self, 'Symb', Max35Text, False)

	@Symb.deleter
	def Symb(self):
		del self._Symb
		self._Symb = base_types.UninitialisedField(self, 'Symb', Max35Text, False)

	@property
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if value is not None else base_types.UninitialisedField(self, 'TradId', Max35Text, False)

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = base_types.UninitialisedField(self, 'TradId', Max35Text, False)

	@property
	def TradgCcy(self):
		return self._TradgCcy

	@TradgCcy.setter
	def TradgCcy(self, value):
		self._TradgCcy = value if value is not None else base_types.UninitialisedField(self, 'TradgCcy', ActiveCurrencyCode, False)

	@TradgCcy.deleter
	def TradgCcy(self):
		del self._TradgCcy
		self._TradgCcy = base_types.UninitialisedField(self, 'TradgCcy', ActiveCurrencyCode, False)

	@property
	def TradgMd(self):
		return self._TradgMd

	@TradgMd.setter
	def TradgMd(self, value):
		self._TradgMd = value if value is not None else base_types.UninitialisedField(self, 'TradgMd', TradingModeType1Code, False)

	@TradgMd.deleter
	def TradgMd(self):
		del self._TradgMd
		self._TradgMd = base_types.UninitialisedField(self, 'TradgMd', TradingModeType1Code, False)

	@property
	def TradgMtd(self):
		return self._TradgMtd

	@TradgMtd.setter
	def TradgMtd(self, value):
		self._TradgMtd = value if value is not None else base_types.UninitialisedField(self, 'TradgMtd', TradingMethodType1Code, False)

	@TradgMtd.deleter
	def TradgMtd(self):
		del self._TradgMtd
		self._TradgMtd = base_types.UninitialisedField(self, 'TradgMtd', TradingMethodType1Code, False)

	@property
	def TrgtCcyOrAmt(self):
		return self._TrgtCcyOrAmt

	@TrgtCcyOrAmt.setter
	def TrgtCcyOrAmt(self, value):
		self._TrgtCcyOrAmt = value if value is not None else base_types.UninitialisedField(self, 'TrgtCcyOrAmt', AmountAndCurrency2, False)

	@TrgtCcyOrAmt.deleter
	def TrgtCcyOrAmt(self):
		del self._TrgtCcyOrAmt
		self._TrgtCcyOrAmt = base_types.UninitialisedField(self, 'TrgtCcyOrAmt', AmountAndCurrency2, False)

	@property
	def TxTm(self):
		return self._TxTm

	@TxTm.setter
	def TxTm(self, value):
		self._TxTm = value if value is not None else base_types.UninitialisedField(self, 'TxTm', ISODateTime, False)

	@TxTm.deleter
	def TxTm(self):
		del self._TxTm
		self._TxTm = base_types.UninitialisedField(self, 'TxTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BaseCcyOrAmt', type=AmountAndCurrency2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMtd', type=ClearingMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmbntnDealTcktId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ContraCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealTcktId', type=Max30Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAndTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtConfd', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnTp', type=OrderStatus8Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=Trade10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXTradPdct', type=UnderlyingProductIdentifier1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Optn', type=Option16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctId', type=SecurityIdentification38Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfConf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwpLeg', type=InstrumentLeg7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Symb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgMd', type=TradingModeType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgMtd', type=TradingMethodType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtCcyOrAmt', type=AmountAndCurrency2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))