import base_types
import DateAndAmount2
import Quantity47
import FundSettlementParameters17
import YesNoIndicator
import Unit11
import TransferType2Choice
import Account28
import ActiveOrHistoricCurrencyAndAmount
import Tax36
import AdditionalReference10
import BusinessFlowType1Code
import ActiveOrHistoricCurrencyCode
import Crystallisation2
import FinancialInstrument63Choice
import Conversion1
import AdditionalInformation15
import Max35Text
import Intermediary43
import ISODate
import PaymentInstrument14

class FinancialInstrument102(base_types._BaseFieldType):

	__slots__ = ["_UnitsDtls", "_ClntRef", "_CrstllstnDtls", "_AddtlInf", "_Trfr", "_LineId", "_SttlmPtiesDtls", "_AddtlAsst", "_AsstsHeldInOwnNm", "_ReqdTrfDt", "_TrfTp", "_PmtDtls", "_TrfeeAcct", "_CtrPtyRef", "_TrfRsltsInChngOfBnfclOwnr", "_ReqdTradDt", "_TrfCcy", "_ReqdSttlmDt", "_Convs", "_AvrgAcqstnPric", "_TaxValtnPt", "_TtlBookVal", "_Qty", "_NotAvlbl", "_IntrmyInf", "_Instrm", "_PrtlInstdQty", "_BizFlowTp"]
	@property
	def UnitsDtls(self):
		return self._UnitsDtls

	@UnitsDtls.setter
	def UnitsDtls(self, value):
		self._UnitsDtls = value if type(value) != auto else self.make_default("UnitsDtls")

	@UnitsDtls.deleter
	def UnitsDtls(self):
		del self._UnitsDtls
		self._UnitsDtls = None

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	@property
	def CrstllstnDtls(self):
		return self._CrstllstnDtls

	@CrstllstnDtls.setter
	def CrstllstnDtls(self, value):
		self._CrstllstnDtls = value if type(value) != auto else self.make_default("CrstllstnDtls")

	@CrstllstnDtls.deleter
	def CrstllstnDtls(self):
		del self._CrstllstnDtls
		self._CrstllstnDtls = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Trfr(self):
		return self._Trfr

	@Trfr.setter
	def Trfr(self, value):
		self._Trfr = value if type(value) != auto else self.make_default("Trfr")

	@Trfr.deleter
	def Trfr(self):
		del self._Trfr
		self._Trfr = None

	@property
	def LineId(self):
		return self._LineId

	@LineId.setter
	def LineId(self, value):
		self._LineId = value if type(value) != auto else self.make_default("LineId")

	@LineId.deleter
	def LineId(self):
		del self._LineId
		self._LineId = None

	@property
	def SttlmPtiesDtls(self):
		return self._SttlmPtiesDtls

	@SttlmPtiesDtls.setter
	def SttlmPtiesDtls(self, value):
		self._SttlmPtiesDtls = value if type(value) != auto else self.make_default("SttlmPtiesDtls")

	@SttlmPtiesDtls.deleter
	def SttlmPtiesDtls(self):
		del self._SttlmPtiesDtls
		self._SttlmPtiesDtls = None

	@property
	def AddtlAsst(self):
		return self._AddtlAsst

	@AddtlAsst.setter
	def AddtlAsst(self, value):
		self._AddtlAsst = value if type(value) != auto else self.make_default("AddtlAsst")

	@AddtlAsst.deleter
	def AddtlAsst(self):
		del self._AddtlAsst
		self._AddtlAsst = None

	@property
	def AsstsHeldInOwnNm(self):
		return self._AsstsHeldInOwnNm

	@AsstsHeldInOwnNm.setter
	def AsstsHeldInOwnNm(self, value):
		self._AsstsHeldInOwnNm = value if type(value) != auto else self.make_default("AsstsHeldInOwnNm")

	@AsstsHeldInOwnNm.deleter
	def AsstsHeldInOwnNm(self):
		del self._AsstsHeldInOwnNm
		self._AsstsHeldInOwnNm = None

	@property
	def ReqdTrfDt(self):
		return self._ReqdTrfDt

	@ReqdTrfDt.setter
	def ReqdTrfDt(self, value):
		self._ReqdTrfDt = value if type(value) != auto else self.make_default("ReqdTrfDt")

	@ReqdTrfDt.deleter
	def ReqdTrfDt(self):
		del self._ReqdTrfDt
		self._ReqdTrfDt = None

	@property
	def TrfTp(self):
		return self._TrfTp

	@TrfTp.setter
	def TrfTp(self, value):
		self._TrfTp = value if type(value) != auto else self.make_default("TrfTp")

	@TrfTp.deleter
	def TrfTp(self):
		del self._TrfTp
		self._TrfTp = None

	@property
	def PmtDtls(self):
		return self._PmtDtls

	@PmtDtls.setter
	def PmtDtls(self, value):
		self._PmtDtls = value if type(value) != auto else self.make_default("PmtDtls")

	@PmtDtls.deleter
	def PmtDtls(self):
		del self._PmtDtls
		self._PmtDtls = None

	@property
	def TrfeeAcct(self):
		return self._TrfeeAcct

	@TrfeeAcct.setter
	def TrfeeAcct(self, value):
		self._TrfeeAcct = value if type(value) != auto else self.make_default("TrfeeAcct")

	@TrfeeAcct.deleter
	def TrfeeAcct(self):
		del self._TrfeeAcct
		self._TrfeeAcct = None

	@property
	def CtrPtyRef(self):
		return self._CtrPtyRef

	@CtrPtyRef.setter
	def CtrPtyRef(self, value):
		self._CtrPtyRef = value if type(value) != auto else self.make_default("CtrPtyRef")

	@CtrPtyRef.deleter
	def CtrPtyRef(self):
		del self._CtrPtyRef
		self._CtrPtyRef = None

	@property
	def TrfRsltsInChngOfBnfclOwnr(self):
		return self._TrfRsltsInChngOfBnfclOwnr

	@TrfRsltsInChngOfBnfclOwnr.setter
	def TrfRsltsInChngOfBnfclOwnr(self, value):
		self._TrfRsltsInChngOfBnfclOwnr = value if type(value) != auto else self.make_default("TrfRsltsInChngOfBnfclOwnr")

	@TrfRsltsInChngOfBnfclOwnr.deleter
	def TrfRsltsInChngOfBnfclOwnr(self):
		del self._TrfRsltsInChngOfBnfclOwnr
		self._TrfRsltsInChngOfBnfclOwnr = None

	@property
	def ReqdTradDt(self):
		return self._ReqdTradDt

	@ReqdTradDt.setter
	def ReqdTradDt(self, value):
		self._ReqdTradDt = value if type(value) != auto else self.make_default("ReqdTradDt")

	@ReqdTradDt.deleter
	def ReqdTradDt(self):
		del self._ReqdTradDt
		self._ReqdTradDt = None

	@property
	def TrfCcy(self):
		return self._TrfCcy

	@TrfCcy.setter
	def TrfCcy(self, value):
		self._TrfCcy = value if type(value) != auto else self.make_default("TrfCcy")

	@TrfCcy.deleter
	def TrfCcy(self):
		del self._TrfCcy
		self._TrfCcy = None

	@property
	def ReqdSttlmDt(self):
		return self._ReqdSttlmDt

	@ReqdSttlmDt.setter
	def ReqdSttlmDt(self, value):
		self._ReqdSttlmDt = value if type(value) != auto else self.make_default("ReqdSttlmDt")

	@ReqdSttlmDt.deleter
	def ReqdSttlmDt(self):
		del self._ReqdSttlmDt
		self._ReqdSttlmDt = None

	@property
	def Convs(self):
		return self._Convs

	@Convs.setter
	def Convs(self, value):
		self._Convs = value if type(value) != auto else self.make_default("Convs")

	@Convs.deleter
	def Convs(self):
		del self._Convs
		self._Convs = None

	@property
	def AvrgAcqstnPric(self):
		return self._AvrgAcqstnPric

	@AvrgAcqstnPric.setter
	def AvrgAcqstnPric(self, value):
		self._AvrgAcqstnPric = value if type(value) != auto else self.make_default("AvrgAcqstnPric")

	@AvrgAcqstnPric.deleter
	def AvrgAcqstnPric(self):
		del self._AvrgAcqstnPric
		self._AvrgAcqstnPric = None

	@property
	def TaxValtnPt(self):
		return self._TaxValtnPt

	@TaxValtnPt.setter
	def TaxValtnPt(self, value):
		self._TaxValtnPt = value if type(value) != auto else self.make_default("TaxValtnPt")

	@TaxValtnPt.deleter
	def TaxValtnPt(self):
		del self._TaxValtnPt
		self._TaxValtnPt = None

	@property
	def TtlBookVal(self):
		return self._TtlBookVal

	@TtlBookVal.setter
	def TtlBookVal(self, value):
		self._TtlBookVal = value if type(value) != auto else self.make_default("TtlBookVal")

	@TtlBookVal.deleter
	def TtlBookVal(self):
		del self._TtlBookVal
		self._TtlBookVal = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def NotAvlbl(self):
		return self._NotAvlbl

	@NotAvlbl.setter
	def NotAvlbl(self, value):
		self._NotAvlbl = value if type(value) != auto else self.make_default("NotAvlbl")

	@NotAvlbl.deleter
	def NotAvlbl(self):
		del self._NotAvlbl
		self._NotAvlbl = None

	@property
	def IntrmyInf(self):
		return self._IntrmyInf

	@IntrmyInf.setter
	def IntrmyInf(self, value):
		self._IntrmyInf = value if type(value) != auto else self.make_default("IntrmyInf")

	@IntrmyInf.deleter
	def IntrmyInf(self):
		del self._IntrmyInf
		self._IntrmyInf = None

	@property
	def Instrm(self):
		return self._Instrm

	@Instrm.setter
	def Instrm(self, value):
		self._Instrm = value if type(value) != auto else self.make_default("Instrm")

	@Instrm.deleter
	def Instrm(self):
		del self._Instrm
		self._Instrm = None

	@property
	def PrtlInstdQty(self):
		return self._PrtlInstdQty

	@PrtlInstdQty.setter
	def PrtlInstdQty(self, value):
		self._PrtlInstdQty = value if type(value) != auto else self.make_default("PrtlInstdQty")

	@PrtlInstdQty.deleter
	def PrtlInstdQty(self):
		del self._PrtlInstdQty
		self._PrtlInstdQty = None

	@property
	def BizFlowTp(self):
		return self._BizFlowTp

	@BizFlowTp.setter
	def BizFlowTp(self, value):
		self._BizFlowTp = value if type(value) != auto else self.make_default("BizFlowTp")

	@BizFlowTp.deleter
	def BizFlowTp(self):
		del self._BizFlowTp
		self._BizFlowTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UnitsDtls', type=Unit11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrstllstnDtls', type=Crystallisation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Trfr', type=Account28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPtiesDtls', type=FundSettlementParameters17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlAsst', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstsHeldInOwnNm', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdTrfDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTp', type=TransferType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDtls', type=PaymentInstrument14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfeeAcct', type=Account28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRsltsInChngOfBnfclOwnr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdTradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Convs', type=Conversion1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgAcqstnPric', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxValtnPt', type=Tax36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlBookVal', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Quantity47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NotAvlbl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyInf', type=Intermediary43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Instrm', type=FinancialInstrument63Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlInstdQty', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizFlowTp', type=BusinessFlowType1Code, min=0, max=1, mutex_group=None, array=False),
	))

