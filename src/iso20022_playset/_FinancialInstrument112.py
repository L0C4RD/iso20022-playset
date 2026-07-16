# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Account37
from . import ActiveCurrencyAnd13DecimalAmount
from . import ActiveCurrencyAndAmount
from . import ActiveOrHistoricCurrencyCode
from . import AdditionalInformation15
from . import AdditionalReference10
from . import BusinessFlowType1Code
from . import Conversion6
from . import Crystallisation2
from . import DateAndAmount2
from . import DateAndDateTime2Choice
from . import FinancialInstrument103Choice
from . import FundSettlementParameters24
from . import ISODate
from . import Intermediary43
from . import Max35Text
from . import PaymentInstrument21
from . import PercentageRate
from . import Quantity54
from . import Tax36
from . import TransferType2Choice
from . import Unit14
from . import YesNoIndicator

class FinancialInstrument112(base_types._BaseFieldType):

	__slots__ = ["_AddtlAsst", "_AddtlInf", "_AsstsHeldInOwnNm", "_AvrgAcqstnPric", "_BizFlowTp", "_ClntRef", "_Convs", "_CrstllstnDtls", "_CtrPtyRef", "_FctvSttlmDt", "_FctvTrfDt", "_Instrm", "_IntrmyInf", "_LatstValtn", "_LineId", "_NotAvlbl", "_OrgnlCost", "_OrgnlPctgInstd", "_PmtDtls", "_PrtlInstdQty", "_Qty", "_ReqdSttlmDt", "_ReqdTradDt", "_SttlmPtiesDtls", "_TaxValtnPt", "_TrfCcy", "_TrfRsltsInChngOfBnfclOwnr", "_TrfTp", "_TrfeeAcct", "_Trfr", "_TtlBookVal", "_UnitsDtls"]
	@property
	def AddtlAsst(self):
		return self._AddtlAsst

	@AddtlAsst.setter
	def AddtlAsst(self, value):
		self._AddtlAsst = value if value is not None else base_types.UninitialisedField(self, 'AddtlAsst', YesNoIndicator, False)

	@AddtlAsst.deleter
	def AddtlAsst(self):
		del self._AddtlAsst
		self._AddtlAsst = base_types.UninitialisedField(self, 'AddtlAsst', YesNoIndicator, False)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def AsstsHeldInOwnNm(self):
		return self._AsstsHeldInOwnNm

	@AsstsHeldInOwnNm.setter
	def AsstsHeldInOwnNm(self, value):
		self._AsstsHeldInOwnNm = value if value is not None else base_types.UninitialisedField(self, 'AsstsHeldInOwnNm', YesNoIndicator, False)

	@AsstsHeldInOwnNm.deleter
	def AsstsHeldInOwnNm(self):
		del self._AsstsHeldInOwnNm
		self._AsstsHeldInOwnNm = base_types.UninitialisedField(self, 'AsstsHeldInOwnNm', YesNoIndicator, False)

	@property
	def AvrgAcqstnPric(self):
		return self._AvrgAcqstnPric

	@AvrgAcqstnPric.setter
	def AvrgAcqstnPric(self, value):
		self._AvrgAcqstnPric = value if value is not None else base_types.UninitialisedField(self, 'AvrgAcqstnPric', ActiveCurrencyAndAmount, False)

	@AvrgAcqstnPric.deleter
	def AvrgAcqstnPric(self):
		del self._AvrgAcqstnPric
		self._AvrgAcqstnPric = base_types.UninitialisedField(self, 'AvrgAcqstnPric', ActiveCurrencyAndAmount, False)

	@property
	def BizFlowTp(self):
		return self._BizFlowTp

	@BizFlowTp.setter
	def BizFlowTp(self, value):
		self._BizFlowTp = value if value is not None else base_types.UninitialisedField(self, 'BizFlowTp', BusinessFlowType1Code, False)

	@BizFlowTp.deleter
	def BizFlowTp(self):
		del self._BizFlowTp
		self._BizFlowTp = base_types.UninitialisedField(self, 'BizFlowTp', BusinessFlowType1Code, False)

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if value is not None else base_types.UninitialisedField(self, 'ClntRef', AdditionalReference10, False)

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = base_types.UninitialisedField(self, 'ClntRef', AdditionalReference10, False)

	@property
	def Convs(self):
		return self._Convs

	@Convs.setter
	def Convs(self, value):
		self._Convs = value if value is not None else base_types.UninitialisedField(self, 'Convs', Conversion6, False)

	@Convs.deleter
	def Convs(self):
		del self._Convs
		self._Convs = base_types.UninitialisedField(self, 'Convs', Conversion6, False)

	@property
	def CrstllstnDtls(self):
		return self._CrstllstnDtls

	@CrstllstnDtls.setter
	def CrstllstnDtls(self, value):
		self._CrstllstnDtls = value if value is not None else base_types.UninitialisedField(self, 'CrstllstnDtls', Crystallisation2, True)

	@CrstllstnDtls.deleter
	def CrstllstnDtls(self):
		del self._CrstllstnDtls
		self._CrstllstnDtls = base_types.UninitialisedField(self, 'CrstllstnDtls', Crystallisation2, True)

	@property
	def CtrPtyRef(self):
		return self._CtrPtyRef

	@CtrPtyRef.setter
	def CtrPtyRef(self, value):
		self._CtrPtyRef = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyRef', AdditionalReference10, False)

	@CtrPtyRef.deleter
	def CtrPtyRef(self):
		del self._CtrPtyRef
		self._CtrPtyRef = base_types.UninitialisedField(self, 'CtrPtyRef', AdditionalReference10, False)

	@property
	def FctvSttlmDt(self):
		return self._FctvSttlmDt

	@FctvSttlmDt.setter
	def FctvSttlmDt(self, value):
		self._FctvSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'FctvSttlmDt', DateAndDateTime2Choice, False)

	@FctvSttlmDt.deleter
	def FctvSttlmDt(self):
		del self._FctvSttlmDt
		self._FctvSttlmDt = base_types.UninitialisedField(self, 'FctvSttlmDt', DateAndDateTime2Choice, False)

	@property
	def FctvTrfDt(self):
		return self._FctvTrfDt

	@FctvTrfDt.setter
	def FctvTrfDt(self, value):
		self._FctvTrfDt = value if value is not None else base_types.UninitialisedField(self, 'FctvTrfDt', DateAndDateTime2Choice, False)

	@FctvTrfDt.deleter
	def FctvTrfDt(self):
		del self._FctvTrfDt
		self._FctvTrfDt = base_types.UninitialisedField(self, 'FctvTrfDt', DateAndDateTime2Choice, False)

	@property
	def Instrm(self):
		return self._Instrm

	@Instrm.setter
	def Instrm(self, value):
		self._Instrm = value if value is not None else base_types.UninitialisedField(self, 'Instrm', FinancialInstrument103Choice, False)

	@Instrm.deleter
	def Instrm(self):
		del self._Instrm
		self._Instrm = base_types.UninitialisedField(self, 'Instrm', FinancialInstrument103Choice, False)

	@property
	def IntrmyInf(self):
		return self._IntrmyInf

	@IntrmyInf.setter
	def IntrmyInf(self, value):
		self._IntrmyInf = value if value is not None else base_types.UninitialisedField(self, 'IntrmyInf', Intermediary43, True)

	@IntrmyInf.deleter
	def IntrmyInf(self):
		del self._IntrmyInf
		self._IntrmyInf = base_types.UninitialisedField(self, 'IntrmyInf', Intermediary43, True)

	@property
	def LatstValtn(self):
		return self._LatstValtn

	@LatstValtn.setter
	def LatstValtn(self, value):
		self._LatstValtn = value if value is not None else base_types.UninitialisedField(self, 'LatstValtn', DateAndAmount2, False)

	@LatstValtn.deleter
	def LatstValtn(self):
		del self._LatstValtn
		self._LatstValtn = base_types.UninitialisedField(self, 'LatstValtn', DateAndAmount2, False)

	@property
	def LineId(self):
		return self._LineId

	@LineId.setter
	def LineId(self, value):
		self._LineId = value if value is not None else base_types.UninitialisedField(self, 'LineId', Max35Text, False)

	@LineId.deleter
	def LineId(self):
		del self._LineId
		self._LineId = base_types.UninitialisedField(self, 'LineId', Max35Text, False)

	@property
	def NotAvlbl(self):
		return self._NotAvlbl

	@NotAvlbl.setter
	def NotAvlbl(self, value):
		self._NotAvlbl = value if value is not None else base_types.UninitialisedField(self, 'NotAvlbl', YesNoIndicator, False)

	@NotAvlbl.deleter
	def NotAvlbl(self):
		del self._NotAvlbl
		self._NotAvlbl = base_types.UninitialisedField(self, 'NotAvlbl', YesNoIndicator, False)

	@property
	def OrgnlCost(self):
		return self._OrgnlCost

	@OrgnlCost.setter
	def OrgnlCost(self, value):
		self._OrgnlCost = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCost', ActiveCurrencyAnd13DecimalAmount, False)

	@OrgnlCost.deleter
	def OrgnlCost(self):
		del self._OrgnlCost
		self._OrgnlCost = base_types.UninitialisedField(self, 'OrgnlCost', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def OrgnlPctgInstd(self):
		return self._OrgnlPctgInstd

	@OrgnlPctgInstd.setter
	def OrgnlPctgInstd(self, value):
		self._OrgnlPctgInstd = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPctgInstd', PercentageRate, False)

	@OrgnlPctgInstd.deleter
	def OrgnlPctgInstd(self):
		del self._OrgnlPctgInstd
		self._OrgnlPctgInstd = base_types.UninitialisedField(self, 'OrgnlPctgInstd', PercentageRate, False)

	@property
	def PmtDtls(self):
		return self._PmtDtls

	@PmtDtls.setter
	def PmtDtls(self, value):
		self._PmtDtls = value if value is not None else base_types.UninitialisedField(self, 'PmtDtls', PaymentInstrument21, False)

	@PmtDtls.deleter
	def PmtDtls(self):
		del self._PmtDtls
		self._PmtDtls = base_types.UninitialisedField(self, 'PmtDtls', PaymentInstrument21, False)

	@property
	def PrtlInstdQty(self):
		return self._PrtlInstdQty

	@PrtlInstdQty.setter
	def PrtlInstdQty(self, value):
		self._PrtlInstdQty = value if value is not None else base_types.UninitialisedField(self, 'PrtlInstdQty', YesNoIndicator, False)

	@PrtlInstdQty.deleter
	def PrtlInstdQty(self):
		del self._PrtlInstdQty
		self._PrtlInstdQty = base_types.UninitialisedField(self, 'PrtlInstdQty', YesNoIndicator, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', Quantity54, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', Quantity54, False)

	@property
	def ReqdSttlmDt(self):
		return self._ReqdSttlmDt

	@ReqdSttlmDt.setter
	def ReqdSttlmDt(self, value):
		self._ReqdSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdSttlmDt', ISODate, False)

	@ReqdSttlmDt.deleter
	def ReqdSttlmDt(self):
		del self._ReqdSttlmDt
		self._ReqdSttlmDt = base_types.UninitialisedField(self, 'ReqdSttlmDt', ISODate, False)

	@property
	def ReqdTradDt(self):
		return self._ReqdTradDt

	@ReqdTradDt.setter
	def ReqdTradDt(self, value):
		self._ReqdTradDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdTradDt', ISODate, False)

	@ReqdTradDt.deleter
	def ReqdTradDt(self):
		del self._ReqdTradDt
		self._ReqdTradDt = base_types.UninitialisedField(self, 'ReqdTradDt', ISODate, False)

	@property
	def SttlmPtiesDtls(self):
		return self._SttlmPtiesDtls

	@SttlmPtiesDtls.setter
	def SttlmPtiesDtls(self, value):
		self._SttlmPtiesDtls = value if value is not None else base_types.UninitialisedField(self, 'SttlmPtiesDtls', FundSettlementParameters24, False)

	@SttlmPtiesDtls.deleter
	def SttlmPtiesDtls(self):
		del self._SttlmPtiesDtls
		self._SttlmPtiesDtls = base_types.UninitialisedField(self, 'SttlmPtiesDtls', FundSettlementParameters24, False)

	@property
	def TaxValtnPt(self):
		return self._TaxValtnPt

	@TaxValtnPt.setter
	def TaxValtnPt(self, value):
		self._TaxValtnPt = value if value is not None else base_types.UninitialisedField(self, 'TaxValtnPt', Tax36, False)

	@TaxValtnPt.deleter
	def TaxValtnPt(self):
		del self._TaxValtnPt
		self._TaxValtnPt = base_types.UninitialisedField(self, 'TaxValtnPt', Tax36, False)

	@property
	def TrfCcy(self):
		return self._TrfCcy

	@TrfCcy.setter
	def TrfCcy(self, value):
		self._TrfCcy = value if value is not None else base_types.UninitialisedField(self, 'TrfCcy', ActiveOrHistoricCurrencyCode, False)

	@TrfCcy.deleter
	def TrfCcy(self):
		del self._TrfCcy
		self._TrfCcy = base_types.UninitialisedField(self, 'TrfCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def TrfRsltsInChngOfBnfclOwnr(self):
		return self._TrfRsltsInChngOfBnfclOwnr

	@TrfRsltsInChngOfBnfclOwnr.setter
	def TrfRsltsInChngOfBnfclOwnr(self, value):
		self._TrfRsltsInChngOfBnfclOwnr = value if value is not None else base_types.UninitialisedField(self, 'TrfRsltsInChngOfBnfclOwnr', YesNoIndicator, False)

	@TrfRsltsInChngOfBnfclOwnr.deleter
	def TrfRsltsInChngOfBnfclOwnr(self):
		del self._TrfRsltsInChngOfBnfclOwnr
		self._TrfRsltsInChngOfBnfclOwnr = base_types.UninitialisedField(self, 'TrfRsltsInChngOfBnfclOwnr', YesNoIndicator, False)

	@property
	def TrfTp(self):
		return self._TrfTp

	@TrfTp.setter
	def TrfTp(self, value):
		self._TrfTp = value if value is not None else base_types.UninitialisedField(self, 'TrfTp', TransferType2Choice, False)

	@TrfTp.deleter
	def TrfTp(self):
		del self._TrfTp
		self._TrfTp = base_types.UninitialisedField(self, 'TrfTp', TransferType2Choice, False)

	@property
	def TrfeeAcct(self):
		return self._TrfeeAcct

	@TrfeeAcct.setter
	def TrfeeAcct(self, value):
		self._TrfeeAcct = value if value is not None else base_types.UninitialisedField(self, 'TrfeeAcct', Account37, False)

	@TrfeeAcct.deleter
	def TrfeeAcct(self):
		del self._TrfeeAcct
		self._TrfeeAcct = base_types.UninitialisedField(self, 'TrfeeAcct', Account37, False)

	@property
	def Trfr(self):
		return self._Trfr

	@Trfr.setter
	def Trfr(self, value):
		self._Trfr = value if value is not None else base_types.UninitialisedField(self, 'Trfr', Account37, False)

	@Trfr.deleter
	def Trfr(self):
		del self._Trfr
		self._Trfr = base_types.UninitialisedField(self, 'Trfr', Account37, False)

	@property
	def TtlBookVal(self):
		return self._TtlBookVal

	@TtlBookVal.setter
	def TtlBookVal(self, value):
		self._TtlBookVal = value if value is not None else base_types.UninitialisedField(self, 'TtlBookVal', DateAndAmount2, False)

	@TtlBookVal.deleter
	def TtlBookVal(self):
		del self._TtlBookVal
		self._TtlBookVal = base_types.UninitialisedField(self, 'TtlBookVal', DateAndAmount2, False)

	@property
	def UnitsDtls(self):
		return self._UnitsDtls

	@UnitsDtls.setter
	def UnitsDtls(self, value):
		self._UnitsDtls = value if value is not None else base_types.UninitialisedField(self, 'UnitsDtls', Unit14, True)

	@UnitsDtls.deleter
	def UnitsDtls(self):
		del self._UnitsDtls
		self._UnitsDtls = base_types.UninitialisedField(self, 'UnitsDtls', Unit14, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlAsst', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AsstsHeldInOwnNm', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgAcqstnPric', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizFlowTp', type=BusinessFlowType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Convs', type=Conversion6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrstllstnDtls', type=Crystallisation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrPtyRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvTrfDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instrm', type=FinancialInstrument103Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyInf', type=Intermediary43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LatstValtn', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NotAvlbl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCost', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPctgInstd', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDtls', type=PaymentInstrument21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlInstdQty', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Quantity54, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdTradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPtiesDtls', type=FundSettlementParameters24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxValtnPt', type=Tax36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRsltsInChngOfBnfclOwnr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTp', type=TransferType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfeeAcct', type=Account37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trfr', type=Account37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlBookVal', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsDtls', type=Unit14, min=0, max=None, mutex_group=None, array=True),
	))