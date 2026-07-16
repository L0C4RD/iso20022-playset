# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import ClassificationType33Choice
from . import FinancialInstrumentQuantity36Choice
from . import ISODate
from . import InterestComputationMethodFormat5Choice
from . import MarketIdentification4Choice
from . import OptionStyle9Choice
from . import PriceFormat92Choice
from . import RateFormat12Choice
from . import RateFormat24Choice
from . import SecurityIdentification20

class FinancialInstrumentAttributes137(base_types._BaseFieldType):

	__slots__ = ["_ClssfctnTp", "_ConvsDt", "_CtrctSz", "_DayCntBsis", "_DnmtnCcy", "_DtdDt", "_FinInstrmId", "_FltgRateFxgDt", "_IntrstRate", "_IsseDt", "_IssePric", "_MinMltplQtyToInst", "_MinNmnlQty", "_MinQtyToInst", "_MtrtyDt", "_NxtCllblDt", "_NxtCpnDt", "_NxtFctr", "_NxtIntrstRate", "_OptnStyle", "_PlcOfListg", "_PrvsFctr", "_PutblDt"]
	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnTp', ClassificationType33Choice, False)

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = base_types.UninitialisedField(self, 'ClssfctnTp', ClassificationType33Choice, False)

	@property
	def ConvsDt(self):
		return self._ConvsDt

	@ConvsDt.setter
	def ConvsDt(self, value):
		self._ConvsDt = value if value is not None else base_types.UninitialisedField(self, 'ConvsDt', ISODate, False)

	@ConvsDt.deleter
	def ConvsDt(self):
		del self._ConvsDt
		self._ConvsDt = base_types.UninitialisedField(self, 'ConvsDt', ISODate, False)

	@property
	def CtrctSz(self):
		return self._CtrctSz

	@CtrctSz.setter
	def CtrctSz(self, value):
		self._CtrctSz = value if value is not None else base_types.UninitialisedField(self, 'CtrctSz', FinancialInstrumentQuantity36Choice, False)

	@CtrctSz.deleter
	def CtrctSz(self):
		del self._CtrctSz
		self._CtrctSz = base_types.UninitialisedField(self, 'CtrctSz', FinancialInstrumentQuantity36Choice, False)

	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if value is not None else base_types.UninitialisedField(self, 'DayCntBsis', InterestComputationMethodFormat5Choice, False)

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = base_types.UninitialisedField(self, 'DayCntBsis', InterestComputationMethodFormat5Choice, False)

	@property
	def DnmtnCcy(self):
		return self._DnmtnCcy

	@DnmtnCcy.setter
	def DnmtnCcy(self, value):
		self._DnmtnCcy = value if value is not None else base_types.UninitialisedField(self, 'DnmtnCcy', ActiveOrHistoricCurrencyCode, False)

	@DnmtnCcy.deleter
	def DnmtnCcy(self):
		del self._DnmtnCcy
		self._DnmtnCcy = base_types.UninitialisedField(self, 'DnmtnCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def DtdDt(self):
		return self._DtdDt

	@DtdDt.setter
	def DtdDt(self, value):
		self._DtdDt = value if value is not None else base_types.UninitialisedField(self, 'DtdDt', ISODate, False)

	@DtdDt.deleter
	def DtdDt(self):
		del self._DtdDt
		self._DtdDt = base_types.UninitialisedField(self, 'DtdDt', ISODate, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification20, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification20, False)

	@property
	def FltgRateFxgDt(self):
		return self._FltgRateFxgDt

	@FltgRateFxgDt.setter
	def FltgRateFxgDt(self, value):
		self._FltgRateFxgDt = value if value is not None else base_types.UninitialisedField(self, 'FltgRateFxgDt', ISODate, False)

	@FltgRateFxgDt.deleter
	def FltgRateFxgDt(self):
		del self._FltgRateFxgDt
		self._FltgRateFxgDt = base_types.UninitialisedField(self, 'FltgRateFxgDt', ISODate, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', RateFormat24Choice, False)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', RateFormat24Choice, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@property
	def IssePric(self):
		return self._IssePric

	@IssePric.setter
	def IssePric(self, value):
		self._IssePric = value if value is not None else base_types.UninitialisedField(self, 'IssePric', PriceFormat92Choice, False)

	@IssePric.deleter
	def IssePric(self):
		del self._IssePric
		self._IssePric = base_types.UninitialisedField(self, 'IssePric', PriceFormat92Choice, False)

	@property
	def MinMltplQtyToInst(self):
		return self._MinMltplQtyToInst

	@MinMltplQtyToInst.setter
	def MinMltplQtyToInst(self, value):
		self._MinMltplQtyToInst = value if value is not None else base_types.UninitialisedField(self, 'MinMltplQtyToInst', FinancialInstrumentQuantity36Choice, False)

	@MinMltplQtyToInst.deleter
	def MinMltplQtyToInst(self):
		del self._MinMltplQtyToInst
		self._MinMltplQtyToInst = base_types.UninitialisedField(self, 'MinMltplQtyToInst', FinancialInstrumentQuantity36Choice, False)

	@property
	def MinNmnlQty(self):
		return self._MinNmnlQty

	@MinNmnlQty.setter
	def MinNmnlQty(self, value):
		self._MinNmnlQty = value if value is not None else base_types.UninitialisedField(self, 'MinNmnlQty', FinancialInstrumentQuantity36Choice, False)

	@MinNmnlQty.deleter
	def MinNmnlQty(self):
		del self._MinNmnlQty
		self._MinNmnlQty = base_types.UninitialisedField(self, 'MinNmnlQty', FinancialInstrumentQuantity36Choice, False)

	@property
	def MinQtyToInst(self):
		return self._MinQtyToInst

	@MinQtyToInst.setter
	def MinQtyToInst(self, value):
		self._MinQtyToInst = value if value is not None else base_types.UninitialisedField(self, 'MinQtyToInst', FinancialInstrumentQuantity36Choice, False)

	@MinQtyToInst.deleter
	def MinQtyToInst(self):
		del self._MinQtyToInst
		self._MinQtyToInst = base_types.UninitialisedField(self, 'MinQtyToInst', FinancialInstrumentQuantity36Choice, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@property
	def NxtCllblDt(self):
		return self._NxtCllblDt

	@NxtCllblDt.setter
	def NxtCllblDt(self, value):
		self._NxtCllblDt = value if value is not None else base_types.UninitialisedField(self, 'NxtCllblDt', ISODate, False)

	@NxtCllblDt.deleter
	def NxtCllblDt(self):
		del self._NxtCllblDt
		self._NxtCllblDt = base_types.UninitialisedField(self, 'NxtCllblDt', ISODate, False)

	@property
	def NxtCpnDt(self):
		return self._NxtCpnDt

	@NxtCpnDt.setter
	def NxtCpnDt(self, value):
		self._NxtCpnDt = value if value is not None else base_types.UninitialisedField(self, 'NxtCpnDt', ISODate, False)

	@NxtCpnDt.deleter
	def NxtCpnDt(self):
		del self._NxtCpnDt
		self._NxtCpnDt = base_types.UninitialisedField(self, 'NxtCpnDt', ISODate, False)

	@property
	def NxtFctr(self):
		return self._NxtFctr

	@NxtFctr.setter
	def NxtFctr(self, value):
		self._NxtFctr = value if value is not None else base_types.UninitialisedField(self, 'NxtFctr', RateFormat12Choice, False)

	@NxtFctr.deleter
	def NxtFctr(self):
		del self._NxtFctr
		self._NxtFctr = base_types.UninitialisedField(self, 'NxtFctr', RateFormat12Choice, False)

	@property
	def NxtIntrstRate(self):
		return self._NxtIntrstRate

	@NxtIntrstRate.setter
	def NxtIntrstRate(self, value):
		self._NxtIntrstRate = value if value is not None else base_types.UninitialisedField(self, 'NxtIntrstRate', RateFormat24Choice, False)

	@NxtIntrstRate.deleter
	def NxtIntrstRate(self):
		del self._NxtIntrstRate
		self._NxtIntrstRate = base_types.UninitialisedField(self, 'NxtIntrstRate', RateFormat24Choice, False)

	@property
	def OptnStyle(self):
		return self._OptnStyle

	@OptnStyle.setter
	def OptnStyle(self, value):
		self._OptnStyle = value if value is not None else base_types.UninitialisedField(self, 'OptnStyle', OptionStyle9Choice, False)

	@OptnStyle.deleter
	def OptnStyle(self):
		del self._OptnStyle
		self._OptnStyle = base_types.UninitialisedField(self, 'OptnStyle', OptionStyle9Choice, False)

	@property
	def PlcOfListg(self):
		return self._PlcOfListg

	@PlcOfListg.setter
	def PlcOfListg(self, value):
		self._PlcOfListg = value if value is not None else base_types.UninitialisedField(self, 'PlcOfListg', MarketIdentification4Choice, False)

	@PlcOfListg.deleter
	def PlcOfListg(self):
		del self._PlcOfListg
		self._PlcOfListg = base_types.UninitialisedField(self, 'PlcOfListg', MarketIdentification4Choice, False)

	@property
	def PrvsFctr(self):
		return self._PrvsFctr

	@PrvsFctr.setter
	def PrvsFctr(self, value):
		self._PrvsFctr = value if value is not None else base_types.UninitialisedField(self, 'PrvsFctr', RateFormat12Choice, False)

	@PrvsFctr.deleter
	def PrvsFctr(self):
		del self._PrvsFctr
		self._PrvsFctr = base_types.UninitialisedField(self, 'PrvsFctr', RateFormat12Choice, False)

	@property
	def PutblDt(self):
		return self._PutblDt

	@PutblDt.setter
	def PutblDt(self, value):
		self._PutblDt = value if value is not None else base_types.UninitialisedField(self, 'PutblDt', ISODate, False)

	@PutblDt.deleter
	def PutblDt(self):
		del self._PutblDt
		self._PutblDt = base_types.UninitialisedField(self, 'PutblDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctSz', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethodFormat5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DnmtnCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRateFxgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssePric', type=PriceFormat92Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinMltplQtyToInst', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinNmnlQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinQtyToInst', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtCllblDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtCpnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtFctr', type=RateFormat12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtIntrstRate', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnStyle', type=OptionStyle9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfListg', type=MarketIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsFctr', type=RateFormat12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutblDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))