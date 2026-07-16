# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import ActiveOrHistoricCurrencyAnd13DecimalAmount
from . import ActiveOrHistoricCurrencyCode
from . import AdditionalReference10
from . import BusinessFlowType1Code
from . import ChargePaymentMethod1Choice
from . import DateAndDateTime2Choice
from . import DecimalNumber
from . import FinancialInstrument88
from . import HoldingsPlanType1Code
from . import ISODate
from . import Max350Text
from . import Max35Text
from . import PercentageRate
from . import RoundingDirection2Code
from . import TransferReason1Choice
from . import Unit12
from . import YesNoIndicator

class Transfer37(base_types._BaseFieldType):

	__slots__ = ["_AvrgDt", "_AvrgPric", "_BizFlowTp", "_ClntRef", "_CtrPtyRef", "_FctvSttlmDt", "_FctvTrfDt", "_FinInstrmDtls", "_HldgsPlanTp", "_NewAvrgDt", "_NewAvrgPric", "_NonStdSttlmInf", "_OrgnlCost", "_OwnAcctTrfInd", "_ReqdSttlmDt", "_Rndg", "_TradDt", "_TrfCcy", "_TrfConfRef", "_TrfExpnssPmtTp", "_TrfOrdrDtForm", "_TrfRate", "_TrfRef", "_TrfRsn", "_TtlUnitsNb", "_UnitsDtls"]
	@property
	def AvrgDt(self):
		return self._AvrgDt

	@AvrgDt.setter
	def AvrgDt(self, value):
		self._AvrgDt = value if value is not None else base_types.UninitialisedField(self, 'AvrgDt', ISODate, False)

	@AvrgDt.deleter
	def AvrgDt(self):
		del self._AvrgDt
		self._AvrgDt = base_types.UninitialisedField(self, 'AvrgDt', ISODate, False)

	@property
	def AvrgPric(self):
		return self._AvrgPric

	@AvrgPric.setter
	def AvrgPric(self, value):
		self._AvrgPric = value if value is not None else base_types.UninitialisedField(self, 'AvrgPric', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@AvrgPric.deleter
	def AvrgPric(self):
		del self._AvrgPric
		self._AvrgPric = base_types.UninitialisedField(self, 'AvrgPric', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

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
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument88, False)

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument88, False)

	@property
	def HldgsPlanTp(self):
		return self._HldgsPlanTp

	@HldgsPlanTp.setter
	def HldgsPlanTp(self, value):
		self._HldgsPlanTp = value if value is not None else base_types.UninitialisedField(self, 'HldgsPlanTp', HoldingsPlanType1Code, True)

	@HldgsPlanTp.deleter
	def HldgsPlanTp(self):
		del self._HldgsPlanTp
		self._HldgsPlanTp = base_types.UninitialisedField(self, 'HldgsPlanTp', HoldingsPlanType1Code, True)

	@property
	def NewAvrgDt(self):
		return self._NewAvrgDt

	@NewAvrgDt.setter
	def NewAvrgDt(self, value):
		self._NewAvrgDt = value if value is not None else base_types.UninitialisedField(self, 'NewAvrgDt', ISODate, False)

	@NewAvrgDt.deleter
	def NewAvrgDt(self):
		del self._NewAvrgDt
		self._NewAvrgDt = base_types.UninitialisedField(self, 'NewAvrgDt', ISODate, False)

	@property
	def NewAvrgPric(self):
		return self._NewAvrgPric

	@NewAvrgPric.setter
	def NewAvrgPric(self, value):
		self._NewAvrgPric = value if value is not None else base_types.UninitialisedField(self, 'NewAvrgPric', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@NewAvrgPric.deleter
	def NewAvrgPric(self):
		del self._NewAvrgPric
		self._NewAvrgPric = base_types.UninitialisedField(self, 'NewAvrgPric', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@property
	def NonStdSttlmInf(self):
		return self._NonStdSttlmInf

	@NonStdSttlmInf.setter
	def NonStdSttlmInf(self, value):
		self._NonStdSttlmInf = value if value is not None else base_types.UninitialisedField(self, 'NonStdSttlmInf', Max350Text, False)

	@NonStdSttlmInf.deleter
	def NonStdSttlmInf(self):
		del self._NonStdSttlmInf
		self._NonStdSttlmInf = base_types.UninitialisedField(self, 'NonStdSttlmInf', Max350Text, False)

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
	def OwnAcctTrfInd(self):
		return self._OwnAcctTrfInd

	@OwnAcctTrfInd.setter
	def OwnAcctTrfInd(self, value):
		self._OwnAcctTrfInd = value if value is not None else base_types.UninitialisedField(self, 'OwnAcctTrfInd', YesNoIndicator, False)

	@OwnAcctTrfInd.deleter
	def OwnAcctTrfInd(self):
		del self._OwnAcctTrfInd
		self._OwnAcctTrfInd = base_types.UninitialisedField(self, 'OwnAcctTrfInd', YesNoIndicator, False)

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
	def Rndg(self):
		return self._Rndg

	@Rndg.setter
	def Rndg(self, value):
		self._Rndg = value if value is not None else base_types.UninitialisedField(self, 'Rndg', RoundingDirection2Code, False)

	@Rndg.deleter
	def Rndg(self):
		del self._Rndg
		self._Rndg = base_types.UninitialisedField(self, 'Rndg', RoundingDirection2Code, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', DateAndDateTime2Choice, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', DateAndDateTime2Choice, False)

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
	def TrfConfRef(self):
		return self._TrfConfRef

	@TrfConfRef.setter
	def TrfConfRef(self, value):
		self._TrfConfRef = value if value is not None else base_types.UninitialisedField(self, 'TrfConfRef', Max35Text, False)

	@TrfConfRef.deleter
	def TrfConfRef(self):
		del self._TrfConfRef
		self._TrfConfRef = base_types.UninitialisedField(self, 'TrfConfRef', Max35Text, False)

	@property
	def TrfExpnssPmtTp(self):
		return self._TrfExpnssPmtTp

	@TrfExpnssPmtTp.setter
	def TrfExpnssPmtTp(self, value):
		self._TrfExpnssPmtTp = value if value is not None else base_types.UninitialisedField(self, 'TrfExpnssPmtTp', ChargePaymentMethod1Choice, False)

	@TrfExpnssPmtTp.deleter
	def TrfExpnssPmtTp(self):
		del self._TrfExpnssPmtTp
		self._TrfExpnssPmtTp = base_types.UninitialisedField(self, 'TrfExpnssPmtTp', ChargePaymentMethod1Choice, False)

	@property
	def TrfOrdrDtForm(self):
		return self._TrfOrdrDtForm

	@TrfOrdrDtForm.setter
	def TrfOrdrDtForm(self, value):
		self._TrfOrdrDtForm = value if value is not None else base_types.UninitialisedField(self, 'TrfOrdrDtForm', ISODate, False)

	@TrfOrdrDtForm.deleter
	def TrfOrdrDtForm(self):
		del self._TrfOrdrDtForm
		self._TrfOrdrDtForm = base_types.UninitialisedField(self, 'TrfOrdrDtForm', ISODate, False)

	@property
	def TrfRate(self):
		return self._TrfRate

	@TrfRate.setter
	def TrfRate(self, value):
		self._TrfRate = value if value is not None else base_types.UninitialisedField(self, 'TrfRate', PercentageRate, False)

	@TrfRate.deleter
	def TrfRate(self):
		del self._TrfRate
		self._TrfRate = base_types.UninitialisedField(self, 'TrfRate', PercentageRate, False)

	@property
	def TrfRef(self):
		return self._TrfRef

	@TrfRef.setter
	def TrfRef(self, value):
		self._TrfRef = value if value is not None else base_types.UninitialisedField(self, 'TrfRef', Max35Text, False)

	@TrfRef.deleter
	def TrfRef(self):
		del self._TrfRef
		self._TrfRef = base_types.UninitialisedField(self, 'TrfRef', Max35Text, False)

	@property
	def TrfRsn(self):
		return self._TrfRsn

	@TrfRsn.setter
	def TrfRsn(self, value):
		self._TrfRsn = value if value is not None else base_types.UninitialisedField(self, 'TrfRsn', TransferReason1Choice, False)

	@TrfRsn.deleter
	def TrfRsn(self):
		del self._TrfRsn
		self._TrfRsn = base_types.UninitialisedField(self, 'TrfRsn', TransferReason1Choice, False)

	@property
	def TtlUnitsNb(self):
		return self._TtlUnitsNb

	@TtlUnitsNb.setter
	def TtlUnitsNb(self, value):
		self._TtlUnitsNb = value if value is not None else base_types.UninitialisedField(self, 'TtlUnitsNb', DecimalNumber, False)

	@TtlUnitsNb.deleter
	def TtlUnitsNb(self):
		del self._TtlUnitsNb
		self._TtlUnitsNb = base_types.UninitialisedField(self, 'TtlUnitsNb', DecimalNumber, False)

	@property
	def UnitsDtls(self):
		return self._UnitsDtls

	@UnitsDtls.setter
	def UnitsDtls(self, value):
		self._UnitsDtls = value if value is not None else base_types.UninitialisedField(self, 'UnitsDtls', Unit12, True)

	@UnitsDtls.deleter
	def UnitsDtls(self):
		del self._UnitsDtls
		self._UnitsDtls = base_types.UninitialisedField(self, 'UnitsDtls', Unit12, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvrgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgPric', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizFlowTp', type=BusinessFlowType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvTrfDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument88, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgsPlanTp', type=HoldingsPlanType1Code, min=0, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewAvrgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewAvrgPric', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdSttlmInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCost', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnAcctTrfInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rndg', type=RoundingDirection2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfConfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfExpnssPmtTp', type=ChargePaymentMethod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfOrdrDtForm', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRsn', type=TransferReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlUnitsNb', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsDtls', type=Unit12, min=0, max=None, mutex_group=None, array=True),
	))