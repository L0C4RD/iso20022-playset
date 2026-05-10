from . import base_types
from .TransferReason1Choice import TransferReason1Choice
from .AdditionalReference10 import AdditionalReference10
from .ChargePaymentMethod1Choice import ChargePaymentMethod1Choice
from .Unit12 import Unit12
from .ActiveCurrencyAnd13DecimalAmount import ActiveCurrencyAnd13DecimalAmount
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .DecimalNumber import DecimalNumber
from .YesNoIndicator import YesNoIndicator
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from .BusinessFlowType1Code import BusinessFlowType1Code
from .ISODate import ISODate
from .Max350Text import Max350Text
from .Max35Text import Max35Text
from .RoundingDirection2Code import RoundingDirection2Code
from .ActiveOrHistoricCurrencyAnd13DecimalAmount import ActiveOrHistoricCurrencyAnd13DecimalAmount
from .PercentageRate import PercentageRate
from .FinancialInstrument88 import FinancialInstrument88
from .HoldingsPlanType1Code import HoldingsPlanType1Code

class Transfer37(base_types._BaseFieldType):

	__slots__ = ["_FctvSttlmDt", "_NonStdSttlmInf", "_FinInstrmDtls", "_NewAvrgDt", "_TrfOrdrDtForm", "_TtlUnitsNb", "_TrfRsn", "_TrfRef", "_CtrPtyRef", "_BizFlowTp", "_AvrgPric", "_Rndg", "_TrfExpnssPmtTp", "_OwnAcctTrfInd", "_AvrgDt", "_FctvTrfDt", "_OrgnlCost", "_TrfCcy", "_NewAvrgPric", "_UnitsDtls", "_ClntRef", "_ReqdSttlmDt", "_TradDt", "_TrfRate", "_TrfConfRef", "_HldgsPlanTp"]
	@property
	def FctvSttlmDt(self):
		return self._FctvSttlmDt

	@FctvSttlmDt.setter
	def FctvSttlmDt(self, value):
		self._FctvSttlmDt = value if type(value) != base_types.auto else self.make_default("FctvSttlmDt")

	@FctvSttlmDt.deleter
	def FctvSttlmDt(self):
		del self._FctvSttlmDt
		self._FctvSttlmDt = None

	@property
	def NonStdSttlmInf(self):
		return self._NonStdSttlmInf

	@NonStdSttlmInf.setter
	def NonStdSttlmInf(self, value):
		self._NonStdSttlmInf = value if type(value) != base_types.auto else self.make_default("NonStdSttlmInf")

	@NonStdSttlmInf.deleter
	def NonStdSttlmInf(self):
		del self._NonStdSttlmInf
		self._NonStdSttlmInf = None

	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if type(value) != base_types.auto else self.make_default("FinInstrmDtls")

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = None

	@property
	def NewAvrgDt(self):
		return self._NewAvrgDt

	@NewAvrgDt.setter
	def NewAvrgDt(self, value):
		self._NewAvrgDt = value if type(value) != base_types.auto else self.make_default("NewAvrgDt")

	@NewAvrgDt.deleter
	def NewAvrgDt(self):
		del self._NewAvrgDt
		self._NewAvrgDt = None

	@property
	def TrfOrdrDtForm(self):
		return self._TrfOrdrDtForm

	@TrfOrdrDtForm.setter
	def TrfOrdrDtForm(self, value):
		self._TrfOrdrDtForm = value if type(value) != base_types.auto else self.make_default("TrfOrdrDtForm")

	@TrfOrdrDtForm.deleter
	def TrfOrdrDtForm(self):
		del self._TrfOrdrDtForm
		self._TrfOrdrDtForm = None

	@property
	def TtlUnitsNb(self):
		return self._TtlUnitsNb

	@TtlUnitsNb.setter
	def TtlUnitsNb(self, value):
		self._TtlUnitsNb = value if type(value) != base_types.auto else self.make_default("TtlUnitsNb")

	@TtlUnitsNb.deleter
	def TtlUnitsNb(self):
		del self._TtlUnitsNb
		self._TtlUnitsNb = None

	@property
	def TrfRsn(self):
		return self._TrfRsn

	@TrfRsn.setter
	def TrfRsn(self, value):
		self._TrfRsn = value if type(value) != base_types.auto else self.make_default("TrfRsn")

	@TrfRsn.deleter
	def TrfRsn(self):
		del self._TrfRsn
		self._TrfRsn = None

	@property
	def TrfRef(self):
		return self._TrfRef

	@TrfRef.setter
	def TrfRef(self, value):
		self._TrfRef = value if type(value) != base_types.auto else self.make_default("TrfRef")

	@TrfRef.deleter
	def TrfRef(self):
		del self._TrfRef
		self._TrfRef = None

	@property
	def CtrPtyRef(self):
		return self._CtrPtyRef

	@CtrPtyRef.setter
	def CtrPtyRef(self, value):
		self._CtrPtyRef = value if type(value) != base_types.auto else self.make_default("CtrPtyRef")

	@CtrPtyRef.deleter
	def CtrPtyRef(self):
		del self._CtrPtyRef
		self._CtrPtyRef = None

	@property
	def BizFlowTp(self):
		return self._BizFlowTp

	@BizFlowTp.setter
	def BizFlowTp(self, value):
		self._BizFlowTp = value if type(value) != base_types.auto else self.make_default("BizFlowTp")

	@BizFlowTp.deleter
	def BizFlowTp(self):
		del self._BizFlowTp
		self._BizFlowTp = None

	@property
	def AvrgPric(self):
		return self._AvrgPric

	@AvrgPric.setter
	def AvrgPric(self, value):
		self._AvrgPric = value if type(value) != base_types.auto else self.make_default("AvrgPric")

	@AvrgPric.deleter
	def AvrgPric(self):
		del self._AvrgPric
		self._AvrgPric = None

	@property
	def Rndg(self):
		return self._Rndg

	@Rndg.setter
	def Rndg(self, value):
		self._Rndg = value if type(value) != base_types.auto else self.make_default("Rndg")

	@Rndg.deleter
	def Rndg(self):
		del self._Rndg
		self._Rndg = None

	@property
	def TrfExpnssPmtTp(self):
		return self._TrfExpnssPmtTp

	@TrfExpnssPmtTp.setter
	def TrfExpnssPmtTp(self, value):
		self._TrfExpnssPmtTp = value if type(value) != base_types.auto else self.make_default("TrfExpnssPmtTp")

	@TrfExpnssPmtTp.deleter
	def TrfExpnssPmtTp(self):
		del self._TrfExpnssPmtTp
		self._TrfExpnssPmtTp = None

	@property
	def OwnAcctTrfInd(self):
		return self._OwnAcctTrfInd

	@OwnAcctTrfInd.setter
	def OwnAcctTrfInd(self, value):
		self._OwnAcctTrfInd = value if type(value) != base_types.auto else self.make_default("OwnAcctTrfInd")

	@OwnAcctTrfInd.deleter
	def OwnAcctTrfInd(self):
		del self._OwnAcctTrfInd
		self._OwnAcctTrfInd = None

	@property
	def AvrgDt(self):
		return self._AvrgDt

	@AvrgDt.setter
	def AvrgDt(self, value):
		self._AvrgDt = value if type(value) != base_types.auto else self.make_default("AvrgDt")

	@AvrgDt.deleter
	def AvrgDt(self):
		del self._AvrgDt
		self._AvrgDt = None

	@property
	def FctvTrfDt(self):
		return self._FctvTrfDt

	@FctvTrfDt.setter
	def FctvTrfDt(self, value):
		self._FctvTrfDt = value if type(value) != base_types.auto else self.make_default("FctvTrfDt")

	@FctvTrfDt.deleter
	def FctvTrfDt(self):
		del self._FctvTrfDt
		self._FctvTrfDt = None

	@property
	def OrgnlCost(self):
		return self._OrgnlCost

	@OrgnlCost.setter
	def OrgnlCost(self, value):
		self._OrgnlCost = value if type(value) != base_types.auto else self.make_default("OrgnlCost")

	@OrgnlCost.deleter
	def OrgnlCost(self):
		del self._OrgnlCost
		self._OrgnlCost = None

	@property
	def TrfCcy(self):
		return self._TrfCcy

	@TrfCcy.setter
	def TrfCcy(self, value):
		self._TrfCcy = value if type(value) != base_types.auto else self.make_default("TrfCcy")

	@TrfCcy.deleter
	def TrfCcy(self):
		del self._TrfCcy
		self._TrfCcy = None

	@property
	def NewAvrgPric(self):
		return self._NewAvrgPric

	@NewAvrgPric.setter
	def NewAvrgPric(self, value):
		self._NewAvrgPric = value if type(value) != base_types.auto else self.make_default("NewAvrgPric")

	@NewAvrgPric.deleter
	def NewAvrgPric(self):
		del self._NewAvrgPric
		self._NewAvrgPric = None

	@property
	def UnitsDtls(self):
		return self._UnitsDtls

	@UnitsDtls.setter
	def UnitsDtls(self, value):
		self._UnitsDtls = value if type(value) != base_types.auto else self.make_default("UnitsDtls")

	@UnitsDtls.deleter
	def UnitsDtls(self):
		del self._UnitsDtls
		self._UnitsDtls = None

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != base_types.auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	@property
	def ReqdSttlmDt(self):
		return self._ReqdSttlmDt

	@ReqdSttlmDt.setter
	def ReqdSttlmDt(self, value):
		self._ReqdSttlmDt = value if type(value) != base_types.auto else self.make_default("ReqdSttlmDt")

	@ReqdSttlmDt.deleter
	def ReqdSttlmDt(self):
		del self._ReqdSttlmDt
		self._ReqdSttlmDt = None

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
	def TrfRate(self):
		return self._TrfRate

	@TrfRate.setter
	def TrfRate(self, value):
		self._TrfRate = value if type(value) != base_types.auto else self.make_default("TrfRate")

	@TrfRate.deleter
	def TrfRate(self):
		del self._TrfRate
		self._TrfRate = None

	@property
	def TrfConfRef(self):
		return self._TrfConfRef

	@TrfConfRef.setter
	def TrfConfRef(self, value):
		self._TrfConfRef = value if type(value) != base_types.auto else self.make_default("TrfConfRef")

	@TrfConfRef.deleter
	def TrfConfRef(self):
		del self._TrfConfRef
		self._TrfConfRef = None

	@property
	def HldgsPlanTp(self):
		return self._HldgsPlanTp

	@HldgsPlanTp.setter
	def HldgsPlanTp(self, value):
		self._HldgsPlanTp = value if type(value) != base_types.auto else self.make_default("HldgsPlanTp")

	@HldgsPlanTp.deleter
	def HldgsPlanTp(self):
		del self._HldgsPlanTp
		self._HldgsPlanTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FctvSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdSttlmInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument88, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewAvrgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfOrdrDtForm', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlUnitsNb', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRsn', type=TransferReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizFlowTp', type=BusinessFlowType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgPric', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rndg', type=RoundingDirection2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfExpnssPmtTp', type=ChargePaymentMethod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnAcctTrfInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvTrfDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCost', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewAvrgPric', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsDtls', type=Unit12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfConfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgsPlanTp', type=HoldingsPlanType1Code, min=0, max=3, mutex_group=None, array=True),
	))

