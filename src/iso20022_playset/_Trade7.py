# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._AmountAndCurrency2 import AmountAndCurrency2
from ._ClearingMethod1Code import ClearingMethod1Code
from ._ISODate import ISODate
from ._ISODateTime import ISODateTime
from ._InstrumentLeg7 import InstrumentLeg7
from ._Max30Text import Max30Text
from ._Max35Text import Max35Text
from ._Option16 import Option16
from ._OrderStatus8Code import OrderStatus8Code
from ._SecurityIdentification38Choice import SecurityIdentification38Choice
from ._Trade10 import Trade10
from ._TradingMethodType1Code import TradingMethodType1Code
from ._TradingModeType1Code import TradingModeType1Code
from ._UnderlyingProductIdentifier1Code import UnderlyingProductIdentifier1Code

class Trade7(base_types._BaseFieldType):

	__slots__ = ["_BaseCcyOrAmt", "_ClrMtd", "_CmbntnDealTcktId", "_ContraCcy", "_DealTcktId", "_DtAndTm", "_DtConfd", "_ExctnTp", "_FXDtls", "_FXTradPdct", "_Optn", "_PdctId", "_PlcOfConf", "_SttlmCcy", "_SwpLeg", "_Symb", "_TradId", "_TradgCcy", "_TradgMd", "_TradgMtd", "_TrgtCcyOrAmt", "_TxTm"]
	@property
	def BaseCcyOrAmt(self):
		return self._BaseCcyOrAmt

	@BaseCcyOrAmt.setter
	def BaseCcyOrAmt(self, value):
		self._BaseCcyOrAmt = value if type(value) != base_types.auto else self.make_default("BaseCcyOrAmt")

	@BaseCcyOrAmt.deleter
	def BaseCcyOrAmt(self):
		del self._BaseCcyOrAmt
		self._BaseCcyOrAmt = None

	@property
	def ClrMtd(self):
		return self._ClrMtd

	@ClrMtd.setter
	def ClrMtd(self, value):
		self._ClrMtd = value if type(value) != base_types.auto else self.make_default("ClrMtd")

	@ClrMtd.deleter
	def ClrMtd(self):
		del self._ClrMtd
		self._ClrMtd = None

	@property
	def CmbntnDealTcktId(self):
		return self._CmbntnDealTcktId

	@CmbntnDealTcktId.setter
	def CmbntnDealTcktId(self, value):
		self._CmbntnDealTcktId = value if type(value) != base_types.auto else self.make_default("CmbntnDealTcktId")

	@CmbntnDealTcktId.deleter
	def CmbntnDealTcktId(self):
		del self._CmbntnDealTcktId
		self._CmbntnDealTcktId = None

	@property
	def ContraCcy(self):
		return self._ContraCcy

	@ContraCcy.setter
	def ContraCcy(self, value):
		self._ContraCcy = value if type(value) != base_types.auto else self.make_default("ContraCcy")

	@ContraCcy.deleter
	def ContraCcy(self):
		del self._ContraCcy
		self._ContraCcy = None

	@property
	def DealTcktId(self):
		return self._DealTcktId

	@DealTcktId.setter
	def DealTcktId(self, value):
		self._DealTcktId = value if type(value) != base_types.auto else self.make_default("DealTcktId")

	@DealTcktId.deleter
	def DealTcktId(self):
		del self._DealTcktId
		self._DealTcktId = None

	@property
	def DtAndTm(self):
		return self._DtAndTm

	@DtAndTm.setter
	def DtAndTm(self, value):
		self._DtAndTm = value if type(value) != base_types.auto else self.make_default("DtAndTm")

	@DtAndTm.deleter
	def DtAndTm(self):
		del self._DtAndTm
		self._DtAndTm = None

	@property
	def DtConfd(self):
		return self._DtConfd

	@DtConfd.setter
	def DtConfd(self, value):
		self._DtConfd = value if type(value) != base_types.auto else self.make_default("DtConfd")

	@DtConfd.deleter
	def DtConfd(self):
		del self._DtConfd
		self._DtConfd = None

	@property
	def ExctnTp(self):
		return self._ExctnTp

	@ExctnTp.setter
	def ExctnTp(self, value):
		self._ExctnTp = value if type(value) != base_types.auto else self.make_default("ExctnTp")

	@ExctnTp.deleter
	def ExctnTp(self):
		del self._ExctnTp
		self._ExctnTp = None

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
	def FXTradPdct(self):
		return self._FXTradPdct

	@FXTradPdct.setter
	def FXTradPdct(self, value):
		self._FXTradPdct = value if type(value) != base_types.auto else self.make_default("FXTradPdct")

	@FXTradPdct.deleter
	def FXTradPdct(self):
		del self._FXTradPdct
		self._FXTradPdct = None

	@property
	def Optn(self):
		return self._Optn

	@Optn.setter
	def Optn(self, value):
		self._Optn = value if type(value) != base_types.auto else self.make_default("Optn")

	@Optn.deleter
	def Optn(self):
		del self._Optn
		self._Optn = None

	@property
	def PdctId(self):
		return self._PdctId

	@PdctId.setter
	def PdctId(self, value):
		self._PdctId = value if type(value) != base_types.auto else self.make_default("PdctId")

	@PdctId.deleter
	def PdctId(self):
		del self._PdctId
		self._PdctId = None

	@property
	def PlcOfConf(self):
		return self._PlcOfConf

	@PlcOfConf.setter
	def PlcOfConf(self, value):
		self._PlcOfConf = value if type(value) != base_types.auto else self.make_default("PlcOfConf")

	@PlcOfConf.deleter
	def PlcOfConf(self):
		del self._PlcOfConf
		self._PlcOfConf = None

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if type(value) != base_types.auto else self.make_default("SttlmCcy")

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = None

	@property
	def SwpLeg(self):
		return self._SwpLeg

	@SwpLeg.setter
	def SwpLeg(self, value):
		self._SwpLeg = value if type(value) != base_types.auto else self.make_default("SwpLeg")

	@SwpLeg.deleter
	def SwpLeg(self):
		del self._SwpLeg
		self._SwpLeg = None

	@property
	def Symb(self):
		return self._Symb

	@Symb.setter
	def Symb(self, value):
		self._Symb = value if type(value) != base_types.auto else self.make_default("Symb")

	@Symb.deleter
	def Symb(self):
		del self._Symb
		self._Symb = None

	@property
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if type(value) != base_types.auto else self.make_default("TradId")

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = None

	@property
	def TradgCcy(self):
		return self._TradgCcy

	@TradgCcy.setter
	def TradgCcy(self, value):
		self._TradgCcy = value if type(value) != base_types.auto else self.make_default("TradgCcy")

	@TradgCcy.deleter
	def TradgCcy(self):
		del self._TradgCcy
		self._TradgCcy = None

	@property
	def TradgMd(self):
		return self._TradgMd

	@TradgMd.setter
	def TradgMd(self, value):
		self._TradgMd = value if type(value) != base_types.auto else self.make_default("TradgMd")

	@TradgMd.deleter
	def TradgMd(self):
		del self._TradgMd
		self._TradgMd = None

	@property
	def TradgMtd(self):
		return self._TradgMtd

	@TradgMtd.setter
	def TradgMtd(self, value):
		self._TradgMtd = value if type(value) != base_types.auto else self.make_default("TradgMtd")

	@TradgMtd.deleter
	def TradgMtd(self):
		del self._TradgMtd
		self._TradgMtd = None

	@property
	def TrgtCcyOrAmt(self):
		return self._TrgtCcyOrAmt

	@TrgtCcyOrAmt.setter
	def TrgtCcyOrAmt(self, value):
		self._TrgtCcyOrAmt = value if type(value) != base_types.auto else self.make_default("TrgtCcyOrAmt")

	@TrgtCcyOrAmt.deleter
	def TrgtCcyOrAmt(self):
		del self._TrgtCcyOrAmt
		self._TrgtCcyOrAmt = None

	@property
	def TxTm(self):
		return self._TxTm

	@TxTm.setter
	def TxTm(self, value):
		self._TxTm = value if type(value) != base_types.auto else self.make_default("TxTm")

	@TxTm.deleter
	def TxTm(self):
		del self._TxTm
		self._TxTm = None

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