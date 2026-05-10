from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._PercentageRate import PercentageRate
from ._DateAndAmount2 import DateAndAmount2
from ._YesNoIndicator import YesNoIndicator
from ._Quantity50 import Quantity50
from ._Conversion3 import Conversion3
from ._Crystallisation2 import Crystallisation2
from ._ISODate import ISODate
from ._ActiveCurrencyAnd13DecimalAmount import ActiveCurrencyAnd13DecimalAmount
from ._BusinessFlowType1Code import BusinessFlowType1Code
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Unit11 import Unit11
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._TransferType2Choice import TransferType2Choice
from ._FundSettlementParameters17 import FundSettlementParameters17
from ._AdditionalReference10 import AdditionalReference10
from ._Tax36 import Tax36
from ._Max35Text import Max35Text
from ._Intermediary43 import Intermediary43
from ._FinancialInstrument63Choice import FinancialInstrument63Choice
from ._PaymentInstrument20 import PaymentInstrument20
from ._Account28 import Account28
from ._AdditionalInformation15 import AdditionalInformation15

class FinancialInstrument105(base_types._BaseFieldType):

	__slots__ = ["_BizFlowTp", "_ReqdTradDt", "_TrfRsltsInChngOfBnfclOwnr", "_Qty", "_Trfr", "_Convs", "_ClntRef", "_TtlBookVal", "_OrgnlPctgInstd", "_LatstValtn", "_AsstsHeldInOwnNm", "_TaxValtnPt", "_IntrmyInf", "_CrstllstnDtls", "_OrgnlCost", "_UnitsDtls", "_LineId", "_PmtDtls", "_TrfCcy", "_NotAvlbl", "_TrfTp", "_ReqdSttlmDt", "_AvrgAcqstnPric", "_SttlmPtiesDtls", "_TrfeeAcct", "_FctvTrfDt", "_AddtlAsst", "_FctvSttlmDt", "_CtrPtyRef", "_Instrm", "_AddtlInf", "_PrtlInstdQty"]
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
	def ReqdTradDt(self):
		return self._ReqdTradDt

	@ReqdTradDt.setter
	def ReqdTradDt(self, value):
		self._ReqdTradDt = value if type(value) != base_types.auto else self.make_default("ReqdTradDt")

	@ReqdTradDt.deleter
	def ReqdTradDt(self):
		del self._ReqdTradDt
		self._ReqdTradDt = None

	@property
	def TrfRsltsInChngOfBnfclOwnr(self):
		return self._TrfRsltsInChngOfBnfclOwnr

	@TrfRsltsInChngOfBnfclOwnr.setter
	def TrfRsltsInChngOfBnfclOwnr(self, value):
		self._TrfRsltsInChngOfBnfclOwnr = value if type(value) != base_types.auto else self.make_default("TrfRsltsInChngOfBnfclOwnr")

	@TrfRsltsInChngOfBnfclOwnr.deleter
	def TrfRsltsInChngOfBnfclOwnr(self):
		del self._TrfRsltsInChngOfBnfclOwnr
		self._TrfRsltsInChngOfBnfclOwnr = None

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
	def Trfr(self):
		return self._Trfr

	@Trfr.setter
	def Trfr(self, value):
		self._Trfr = value if type(value) != base_types.auto else self.make_default("Trfr")

	@Trfr.deleter
	def Trfr(self):
		del self._Trfr
		self._Trfr = None

	@property
	def Convs(self):
		return self._Convs

	@Convs.setter
	def Convs(self, value):
		self._Convs = value if type(value) != base_types.auto else self.make_default("Convs")

	@Convs.deleter
	def Convs(self):
		del self._Convs
		self._Convs = None

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
	def TtlBookVal(self):
		return self._TtlBookVal

	@TtlBookVal.setter
	def TtlBookVal(self, value):
		self._TtlBookVal = value if type(value) != base_types.auto else self.make_default("TtlBookVal")

	@TtlBookVal.deleter
	def TtlBookVal(self):
		del self._TtlBookVal
		self._TtlBookVal = None

	@property
	def OrgnlPctgInstd(self):
		return self._OrgnlPctgInstd

	@OrgnlPctgInstd.setter
	def OrgnlPctgInstd(self, value):
		self._OrgnlPctgInstd = value if type(value) != base_types.auto else self.make_default("OrgnlPctgInstd")

	@OrgnlPctgInstd.deleter
	def OrgnlPctgInstd(self):
		del self._OrgnlPctgInstd
		self._OrgnlPctgInstd = None

	@property
	def LatstValtn(self):
		return self._LatstValtn

	@LatstValtn.setter
	def LatstValtn(self, value):
		self._LatstValtn = value if type(value) != base_types.auto else self.make_default("LatstValtn")

	@LatstValtn.deleter
	def LatstValtn(self):
		del self._LatstValtn
		self._LatstValtn = None

	@property
	def AsstsHeldInOwnNm(self):
		return self._AsstsHeldInOwnNm

	@AsstsHeldInOwnNm.setter
	def AsstsHeldInOwnNm(self, value):
		self._AsstsHeldInOwnNm = value if type(value) != base_types.auto else self.make_default("AsstsHeldInOwnNm")

	@AsstsHeldInOwnNm.deleter
	def AsstsHeldInOwnNm(self):
		del self._AsstsHeldInOwnNm
		self._AsstsHeldInOwnNm = None

	@property
	def TaxValtnPt(self):
		return self._TaxValtnPt

	@TaxValtnPt.setter
	def TaxValtnPt(self, value):
		self._TaxValtnPt = value if type(value) != base_types.auto else self.make_default("TaxValtnPt")

	@TaxValtnPt.deleter
	def TaxValtnPt(self):
		del self._TaxValtnPt
		self._TaxValtnPt = None

	@property
	def IntrmyInf(self):
		return self._IntrmyInf

	@IntrmyInf.setter
	def IntrmyInf(self, value):
		self._IntrmyInf = value if type(value) != base_types.auto else self.make_default("IntrmyInf")

	@IntrmyInf.deleter
	def IntrmyInf(self):
		del self._IntrmyInf
		self._IntrmyInf = None

	@property
	def CrstllstnDtls(self):
		return self._CrstllstnDtls

	@CrstllstnDtls.setter
	def CrstllstnDtls(self, value):
		self._CrstllstnDtls = value if type(value) != base_types.auto else self.make_default("CrstllstnDtls")

	@CrstllstnDtls.deleter
	def CrstllstnDtls(self):
		del self._CrstllstnDtls
		self._CrstllstnDtls = None

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
	def LineId(self):
		return self._LineId

	@LineId.setter
	def LineId(self, value):
		self._LineId = value if type(value) != base_types.auto else self.make_default("LineId")

	@LineId.deleter
	def LineId(self):
		del self._LineId
		self._LineId = None

	@property
	def PmtDtls(self):
		return self._PmtDtls

	@PmtDtls.setter
	def PmtDtls(self, value):
		self._PmtDtls = value if type(value) != base_types.auto else self.make_default("PmtDtls")

	@PmtDtls.deleter
	def PmtDtls(self):
		del self._PmtDtls
		self._PmtDtls = None

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
	def NotAvlbl(self):
		return self._NotAvlbl

	@NotAvlbl.setter
	def NotAvlbl(self, value):
		self._NotAvlbl = value if type(value) != base_types.auto else self.make_default("NotAvlbl")

	@NotAvlbl.deleter
	def NotAvlbl(self):
		del self._NotAvlbl
		self._NotAvlbl = None

	@property
	def TrfTp(self):
		return self._TrfTp

	@TrfTp.setter
	def TrfTp(self, value):
		self._TrfTp = value if type(value) != base_types.auto else self.make_default("TrfTp")

	@TrfTp.deleter
	def TrfTp(self):
		del self._TrfTp
		self._TrfTp = None

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
	def AvrgAcqstnPric(self):
		return self._AvrgAcqstnPric

	@AvrgAcqstnPric.setter
	def AvrgAcqstnPric(self, value):
		self._AvrgAcqstnPric = value if type(value) != base_types.auto else self.make_default("AvrgAcqstnPric")

	@AvrgAcqstnPric.deleter
	def AvrgAcqstnPric(self):
		del self._AvrgAcqstnPric
		self._AvrgAcqstnPric = None

	@property
	def SttlmPtiesDtls(self):
		return self._SttlmPtiesDtls

	@SttlmPtiesDtls.setter
	def SttlmPtiesDtls(self, value):
		self._SttlmPtiesDtls = value if type(value) != base_types.auto else self.make_default("SttlmPtiesDtls")

	@SttlmPtiesDtls.deleter
	def SttlmPtiesDtls(self):
		del self._SttlmPtiesDtls
		self._SttlmPtiesDtls = None

	@property
	def TrfeeAcct(self):
		return self._TrfeeAcct

	@TrfeeAcct.setter
	def TrfeeAcct(self, value):
		self._TrfeeAcct = value if type(value) != base_types.auto else self.make_default("TrfeeAcct")

	@TrfeeAcct.deleter
	def TrfeeAcct(self):
		del self._TrfeeAcct
		self._TrfeeAcct = None

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
	def AddtlAsst(self):
		return self._AddtlAsst

	@AddtlAsst.setter
	def AddtlAsst(self, value):
		self._AddtlAsst = value if type(value) != base_types.auto else self.make_default("AddtlAsst")

	@AddtlAsst.deleter
	def AddtlAsst(self):
		del self._AddtlAsst
		self._AddtlAsst = None

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
	def Instrm(self):
		return self._Instrm

	@Instrm.setter
	def Instrm(self, value):
		self._Instrm = value if type(value) != base_types.auto else self.make_default("Instrm")

	@Instrm.deleter
	def Instrm(self):
		del self._Instrm
		self._Instrm = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def PrtlInstdQty(self):
		return self._PrtlInstdQty

	@PrtlInstdQty.setter
	def PrtlInstdQty(self, value):
		self._PrtlInstdQty = value if type(value) != base_types.auto else self.make_default("PrtlInstdQty")

	@PrtlInstdQty.deleter
	def PrtlInstdQty(self):
		del self._PrtlInstdQty
		self._PrtlInstdQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizFlowTp', type=BusinessFlowType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdTradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRsltsInChngOfBnfclOwnr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Quantity50, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trfr', type=Account28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Convs', type=Conversion3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlBookVal', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPctgInstd', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LatstValtn', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstsHeldInOwnNm', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxValtnPt', type=Tax36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyInf', type=Intermediary43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CrstllstnDtls', type=Crystallisation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlCost', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsDtls', type=Unit11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LineId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDtls', type=PaymentInstrument20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NotAvlbl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTp', type=TransferType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgAcqstnPric', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPtiesDtls', type=FundSettlementParameters17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfeeAcct', type=Account28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvTrfDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlAsst', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instrm', type=FinancialInstrument63Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtlInstdQty', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

