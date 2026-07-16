# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Account37
from . import ActiveCurrencyAnd13DecimalAmount
from . import ActiveOrHistoricCurrencyAndAmount
from . import ActiveOrHistoricCurrencyCode
from . import AdditionalInformation15
from . import AdditionalReference10
from . import BusinessFlowType1Code
from . import Crystallisation2
from . import DateAndAmount2
from . import FinancialInstrument102Choice
from . import FundSettlementParameters24
from . import Intermediary43
from . import Max35Text
from . import Quantity53
from . import Tax36
from . import Unit14
from . import YesNoIndicator

class FinancialInstrument110(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AsstsHeldInOwnNm", "_AvrgAcqstnPric", "_BizFlowTp", "_ClntRef", "_CrstllstnDtls", "_CtrPtyRef", "_Instrm", "_IntrmyInf", "_LatstValtn", "_LineId", "_OrgnlCost", "_Qty", "_SttlmPtiesDtls", "_TaxValtnPt", "_TrfCcy", "_TrfRsltsInChngOfBnfclOwnr", "_TrfeeAcct", "_Trfr", "_TtlBookVal", "_UnitsDtls"]
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
		self._AvrgAcqstnPric = value if value is not None else base_types.UninitialisedField(self, 'AvrgAcqstnPric', ActiveOrHistoricCurrencyAndAmount, False)

	@AvrgAcqstnPric.deleter
	def AvrgAcqstnPric(self):
		del self._AvrgAcqstnPric
		self._AvrgAcqstnPric = base_types.UninitialisedField(self, 'AvrgAcqstnPric', ActiveOrHistoricCurrencyAndAmount, False)

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
	def Instrm(self):
		return self._Instrm

	@Instrm.setter
	def Instrm(self, value):
		self._Instrm = value if value is not None else base_types.UninitialisedField(self, 'Instrm', FinancialInstrument102Choice, False)

	@Instrm.deleter
	def Instrm(self):
		del self._Instrm
		self._Instrm = base_types.UninitialisedField(self, 'Instrm', FinancialInstrument102Choice, False)

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
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', Quantity53, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', Quantity53, False)

	@property
	def SttlmPtiesDtls(self):
		return self._SttlmPtiesDtls

	@SttlmPtiesDtls.setter
	def SttlmPtiesDtls(self, value):
		self._SttlmPtiesDtls = value if value is not None else base_types.UninitialisedField(self, 'SttlmPtiesDtls', FundSettlementParameters24, True)

	@SttlmPtiesDtls.deleter
	def SttlmPtiesDtls(self):
		del self._SttlmPtiesDtls
		self._SttlmPtiesDtls = base_types.UninitialisedField(self, 'SttlmPtiesDtls', FundSettlementParameters24, True)

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
		self._Trfr = value if value is not None else base_types.UninitialisedField(self, 'Trfr', Account37, True)

	@Trfr.deleter
	def Trfr(self):
		del self._Trfr
		self._Trfr = base_types.UninitialisedField(self, 'Trfr', Account37, True)

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
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AsstsHeldInOwnNm', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgAcqstnPric', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizFlowTp', type=BusinessFlowType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrstllstnDtls', type=Crystallisation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrPtyRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instrm', type=FinancialInstrument102Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyInf', type=Intermediary43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LatstValtn', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCost', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Quantity53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPtiesDtls', type=FundSettlementParameters24, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxValtnPt', type=Tax36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRsltsInChngOfBnfclOwnr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfeeAcct', type=Account37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trfr', type=Account37, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlBookVal', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsDtls', type=Unit14, min=0, max=None, mutex_group=None, array=True),
	))