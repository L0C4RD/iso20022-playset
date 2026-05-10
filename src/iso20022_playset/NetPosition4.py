from . import base_types
from .PartyIdentificationAndAccount227 import PartyIdentificationAndAccount227
from .AmountAndDirection21 import AmountAndDirection21
from .TradeLeg13 import TradeLeg13
from .DateFormat66Choice import DateFormat66Choice
from .Price14 import Price14
from .ISODate import ISODate
from .SecuritiesAccount18 import SecuritiesAccount18
from .PartyIdentification255Choice import PartyIdentification255Choice
from .ReceiveDelivery1Code import ReceiveDelivery1Code
from .MarketIdentification20 import MarketIdentification20
from .FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice
from .TradingCapacity5Code import TradingCapacity5Code
from .SecurityIdentification48 import SecurityIdentification48
from .SecuritiesAccount19 import SecuritiesAccount19

class NetPosition4(base_types._BaseFieldType):

	__slots__ = ["_NonClrMmb", "_TradLegDtls", "_SttlmDt", "_DlvryAcct", "_PlcOfTrad", "_SctiesMvmntTp", "_AcrdIntrstAmt", "_FinInstrmId", "_NetQty", "_AvrgDealPric", "_TradgCpcty", "_TradDt", "_NetPosAmt", "_InitlPosAmt", "_ClrAcct", "_Dpstry"]
	@property
	def NonClrMmb(self):
		return self._NonClrMmb

	@NonClrMmb.setter
	def NonClrMmb(self, value):
		self._NonClrMmb = value if type(value) != base_types.auto else self.make_default("NonClrMmb")

	@NonClrMmb.deleter
	def NonClrMmb(self):
		del self._NonClrMmb
		self._NonClrMmb = None

	@property
	def TradLegDtls(self):
		return self._TradLegDtls

	@TradLegDtls.setter
	def TradLegDtls(self, value):
		self._TradLegDtls = value if type(value) != base_types.auto else self.make_default("TradLegDtls")

	@TradLegDtls.deleter
	def TradLegDtls(self):
		del self._TradLegDtls
		self._TradLegDtls = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != base_types.auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	@property
	def DlvryAcct(self):
		return self._DlvryAcct

	@DlvryAcct.setter
	def DlvryAcct(self, value):
		self._DlvryAcct = value if type(value) != base_types.auto else self.make_default("DlvryAcct")

	@DlvryAcct.deleter
	def DlvryAcct(self):
		del self._DlvryAcct
		self._DlvryAcct = None

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if type(value) != base_types.auto else self.make_default("PlcOfTrad")

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = None

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if type(value) != base_types.auto else self.make_default("SctiesMvmntTp")

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = None

	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if type(value) != base_types.auto else self.make_default("AcrdIntrstAmt")

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = None

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
	def NetQty(self):
		return self._NetQty

	@NetQty.setter
	def NetQty(self, value):
		self._NetQty = value if type(value) != base_types.auto else self.make_default("NetQty")

	@NetQty.deleter
	def NetQty(self):
		del self._NetQty
		self._NetQty = None

	@property
	def AvrgDealPric(self):
		return self._AvrgDealPric

	@AvrgDealPric.setter
	def AvrgDealPric(self, value):
		self._AvrgDealPric = value if type(value) != base_types.auto else self.make_default("AvrgDealPric")

	@AvrgDealPric.deleter
	def AvrgDealPric(self):
		del self._AvrgDealPric
		self._AvrgDealPric = None

	@property
	def TradgCpcty(self):
		return self._TradgCpcty

	@TradgCpcty.setter
	def TradgCpcty(self, value):
		self._TradgCpcty = value if type(value) != base_types.auto else self.make_default("TradgCpcty")

	@TradgCpcty.deleter
	def TradgCpcty(self):
		del self._TradgCpcty
		self._TradgCpcty = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != base_types.auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def NetPosAmt(self):
		return self._NetPosAmt

	@NetPosAmt.setter
	def NetPosAmt(self, value):
		self._NetPosAmt = value if type(value) != base_types.auto else self.make_default("NetPosAmt")

	@NetPosAmt.deleter
	def NetPosAmt(self):
		del self._NetPosAmt
		self._NetPosAmt = None

	@property
	def InitlPosAmt(self):
		return self._InitlPosAmt

	@InitlPosAmt.setter
	def InitlPosAmt(self, value):
		self._InitlPosAmt = value if type(value) != base_types.auto else self.make_default("InitlPosAmt")

	@InitlPosAmt.deleter
	def InitlPosAmt(self):
		del self._InitlPosAmt
		self._InitlPosAmt = None

	@property
	def ClrAcct(self):
		return self._ClrAcct

	@ClrAcct.setter
	def ClrAcct(self, value):
		self._ClrAcct = value if type(value) != base_types.auto else self.make_default("ClrAcct")

	@ClrAcct.deleter
	def ClrAcct(self):
		del self._ClrAcct
		self._ClrAcct = None

	@property
	def Dpstry(self):
		return self._Dpstry

	@Dpstry.setter
	def Dpstry(self, value):
		self._Dpstry = value if type(value) != base_types.auto else self.make_default("Dpstry")

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonClrMmb', type=PartyIdentificationAndAccount227, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradLegDtls', type=TradeLeg13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmDt', type=DateFormat66Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=MarketIdentification20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification48, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgDealPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgCpcty', type=TradingCapacity5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetPosAmt', type=AmountAndDirection21, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlPosAmt', type=AmountAndDirection21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrAcct', type=SecuritiesAccount18, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification255Choice, min=1, max=1, mutex_group=None, array=False),
	))

