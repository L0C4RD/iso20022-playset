# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection21
from . import DateFormat66Choice
from . import FinancialInstrumentQuantity1Choice
from . import ISODate
from . import MarketIdentification20
from . import PartyIdentification255Choice
from . import PartyIdentificationAndAccount227
from . import Price14
from . import ReceiveDelivery1Code
from . import SecuritiesAccount18
from . import SecuritiesAccount19
from . import SecurityIdentification48
from . import TradeLeg13
from . import TradingCapacity5Code

class NetPosition4(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstAmt", "_AvrgDealPric", "_ClrAcct", "_DlvryAcct", "_Dpstry", "_FinInstrmId", "_InitlPosAmt", "_NetPosAmt", "_NetQty", "_NonClrMmb", "_PlcOfTrad", "_SctiesMvmntTp", "_SttlmDt", "_TradDt", "_TradLegDtls", "_TradgCpcty"]
	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection21, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection21, False)

	@property
	def AvrgDealPric(self):
		return self._AvrgDealPric

	@AvrgDealPric.setter
	def AvrgDealPric(self, value):
		self._AvrgDealPric = value if value is not None else base_types.UninitialisedField(self, 'AvrgDealPric', Price14, False)

	@AvrgDealPric.deleter
	def AvrgDealPric(self):
		del self._AvrgDealPric
		self._AvrgDealPric = base_types.UninitialisedField(self, 'AvrgDealPric', Price14, False)

	@property
	def ClrAcct(self):
		return self._ClrAcct

	@ClrAcct.setter
	def ClrAcct(self, value):
		self._ClrAcct = value if value is not None else base_types.UninitialisedField(self, 'ClrAcct', SecuritiesAccount18, False)

	@ClrAcct.deleter
	def ClrAcct(self):
		del self._ClrAcct
		self._ClrAcct = base_types.UninitialisedField(self, 'ClrAcct', SecuritiesAccount18, False)

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
		self._Dpstry = value if value is not None else base_types.UninitialisedField(self, 'Dpstry', PartyIdentification255Choice, False)

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = base_types.UninitialisedField(self, 'Dpstry', PartyIdentification255Choice, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification48, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification48, False)

	@property
	def InitlPosAmt(self):
		return self._InitlPosAmt

	@InitlPosAmt.setter
	def InitlPosAmt(self, value):
		self._InitlPosAmt = value if value is not None else base_types.UninitialisedField(self, 'InitlPosAmt', AmountAndDirection21, False)

	@InitlPosAmt.deleter
	def InitlPosAmt(self):
		del self._InitlPosAmt
		self._InitlPosAmt = base_types.UninitialisedField(self, 'InitlPosAmt', AmountAndDirection21, False)

	@property
	def NetPosAmt(self):
		return self._NetPosAmt

	@NetPosAmt.setter
	def NetPosAmt(self, value):
		self._NetPosAmt = value if value is not None else base_types.UninitialisedField(self, 'NetPosAmt', AmountAndDirection21, False)

	@NetPosAmt.deleter
	def NetPosAmt(self):
		del self._NetPosAmt
		self._NetPosAmt = base_types.UninitialisedField(self, 'NetPosAmt', AmountAndDirection21, False)

	@property
	def NetQty(self):
		return self._NetQty

	@NetQty.setter
	def NetQty(self, value):
		self._NetQty = value if value is not None else base_types.UninitialisedField(self, 'NetQty', FinancialInstrumentQuantity1Choice, False)

	@NetQty.deleter
	def NetQty(self):
		del self._NetQty
		self._NetQty = base_types.UninitialisedField(self, 'NetQty', FinancialInstrumentQuantity1Choice, False)

	@property
	def NonClrMmb(self):
		return self._NonClrMmb

	@NonClrMmb.setter
	def NonClrMmb(self, value):
		self._NonClrMmb = value if value is not None else base_types.UninitialisedField(self, 'NonClrMmb', PartyIdentificationAndAccount227, False)

	@NonClrMmb.deleter
	def NonClrMmb(self):
		del self._NonClrMmb
		self._NonClrMmb = base_types.UninitialisedField(self, 'NonClrMmb', PartyIdentificationAndAccount227, False)

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if value is not None else base_types.UninitialisedField(self, 'PlcOfTrad', MarketIdentification20, False)

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = base_types.UninitialisedField(self, 'PlcOfTrad', MarketIdentification20, False)

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, False)

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', DateFormat66Choice, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', DateFormat66Choice, False)

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

	@property
	def TradLegDtls(self):
		return self._TradLegDtls

	@TradLegDtls.setter
	def TradLegDtls(self, value):
		self._TradLegDtls = value if value is not None else base_types.UninitialisedField(self, 'TradLegDtls', TradeLeg13, True)

	@TradLegDtls.deleter
	def TradLegDtls(self):
		del self._TradLegDtls
		self._TradLegDtls = base_types.UninitialisedField(self, 'TradLegDtls', TradeLeg13, True)

	@property
	def TradgCpcty(self):
		return self._TradgCpcty

	@TradgCpcty.setter
	def TradgCpcty(self, value):
		self._TradgCpcty = value if value is not None else base_types.UninitialisedField(self, 'TradgCpcty', TradingCapacity5Code, False)

	@TradgCpcty.deleter
	def TradgCpcty(self):
		del self._TradgCpcty
		self._TradgCpcty = base_types.UninitialisedField(self, 'TradgCpcty', TradingCapacity5Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgDealPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrAcct', type=SecuritiesAccount18, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification255Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification48, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlPosAmt', type=AmountAndDirection21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetPosAmt', type=AmountAndDirection21, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonClrMmb', type=PartyIdentificationAndAccount227, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=MarketIdentification20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=DateFormat66Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradLegDtls', type=TradeLeg13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradgCpcty', type=TradingCapacity5Code, min=0, max=1, mutex_group=None, array=False),
	))