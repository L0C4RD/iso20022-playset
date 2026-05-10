from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._ClassificationType32Choice import ClassificationType32Choice
from ._FinancialInstrumentQuantity33Choice import FinancialInstrumentQuantity33Choice
from ._ISODate import ISODate
from ._InterestComputationMethodFormat4Choice import InterestComputationMethodFormat4Choice
from ._MarketIdentification3Choice import MarketIdentification3Choice
from ._OptionStyle8Choice import OptionStyle8Choice
from ._PriceFormat81Choice import PriceFormat81Choice
from ._RateFormat12Choice import RateFormat12Choice
from ._RateFormat24Choice import RateFormat24Choice
from ._SecurityIdentification19 import SecurityIdentification19

class FinancialInstrumentAttributes131(base_types._BaseFieldType):

	__slots__ = ["_ClssfctnTp", "_ConvsDt", "_CtrctSz", "_DayCntBsis", "_DnmtnCcy", "_DtdDt", "_FinInstrmId", "_FltgRateFxgDt", "_IntrstRate", "_IsseDt", "_IssePric", "_MinMltplQtyToInst", "_MinNmnlQty", "_MinQtyToInst", "_MtrtyDt", "_NxtCllblDt", "_NxtCpnDt", "_NxtFctr", "_NxtIntrstRate", "_OptnStyle", "_PlcOfListg", "_PrvsFctr", "_PutblDt"]
	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if type(value) != base_types.auto else self.make_default("ClssfctnTp")

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = None

	@property
	def ConvsDt(self):
		return self._ConvsDt

	@ConvsDt.setter
	def ConvsDt(self, value):
		self._ConvsDt = value if type(value) != base_types.auto else self.make_default("ConvsDt")

	@ConvsDt.deleter
	def ConvsDt(self):
		del self._ConvsDt
		self._ConvsDt = None

	@property
	def CtrctSz(self):
		return self._CtrctSz

	@CtrctSz.setter
	def CtrctSz(self, value):
		self._CtrctSz = value if type(value) != base_types.auto else self.make_default("CtrctSz")

	@CtrctSz.deleter
	def CtrctSz(self):
		del self._CtrctSz
		self._CtrctSz = None

	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if type(value) != base_types.auto else self.make_default("DayCntBsis")

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = None

	@property
	def DnmtnCcy(self):
		return self._DnmtnCcy

	@DnmtnCcy.setter
	def DnmtnCcy(self, value):
		self._DnmtnCcy = value if type(value) != base_types.auto else self.make_default("DnmtnCcy")

	@DnmtnCcy.deleter
	def DnmtnCcy(self):
		del self._DnmtnCcy
		self._DnmtnCcy = None

	@property
	def DtdDt(self):
		return self._DtdDt

	@DtdDt.setter
	def DtdDt(self, value):
		self._DtdDt = value if type(value) != base_types.auto else self.make_default("DtdDt")

	@DtdDt.deleter
	def DtdDt(self):
		del self._DtdDt
		self._DtdDt = None

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
	def FltgRateFxgDt(self):
		return self._FltgRateFxgDt

	@FltgRateFxgDt.setter
	def FltgRateFxgDt(self, value):
		self._FltgRateFxgDt = value if type(value) != base_types.auto else self.make_default("FltgRateFxgDt")

	@FltgRateFxgDt.deleter
	def FltgRateFxgDt(self):
		del self._FltgRateFxgDt
		self._FltgRateFxgDt = None

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != base_types.auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != base_types.auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def IssePric(self):
		return self._IssePric

	@IssePric.setter
	def IssePric(self, value):
		self._IssePric = value if type(value) != base_types.auto else self.make_default("IssePric")

	@IssePric.deleter
	def IssePric(self):
		del self._IssePric
		self._IssePric = None

	@property
	def MinMltplQtyToInst(self):
		return self._MinMltplQtyToInst

	@MinMltplQtyToInst.setter
	def MinMltplQtyToInst(self, value):
		self._MinMltplQtyToInst = value if type(value) != base_types.auto else self.make_default("MinMltplQtyToInst")

	@MinMltplQtyToInst.deleter
	def MinMltplQtyToInst(self):
		del self._MinMltplQtyToInst
		self._MinMltplQtyToInst = None

	@property
	def MinNmnlQty(self):
		return self._MinNmnlQty

	@MinNmnlQty.setter
	def MinNmnlQty(self, value):
		self._MinNmnlQty = value if type(value) != base_types.auto else self.make_default("MinNmnlQty")

	@MinNmnlQty.deleter
	def MinNmnlQty(self):
		del self._MinNmnlQty
		self._MinNmnlQty = None

	@property
	def MinQtyToInst(self):
		return self._MinQtyToInst

	@MinQtyToInst.setter
	def MinQtyToInst(self, value):
		self._MinQtyToInst = value if type(value) != base_types.auto else self.make_default("MinQtyToInst")

	@MinQtyToInst.deleter
	def MinQtyToInst(self):
		del self._MinQtyToInst
		self._MinQtyToInst = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != base_types.auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def NxtCllblDt(self):
		return self._NxtCllblDt

	@NxtCllblDt.setter
	def NxtCllblDt(self, value):
		self._NxtCllblDt = value if type(value) != base_types.auto else self.make_default("NxtCllblDt")

	@NxtCllblDt.deleter
	def NxtCllblDt(self):
		del self._NxtCllblDt
		self._NxtCllblDt = None

	@property
	def NxtCpnDt(self):
		return self._NxtCpnDt

	@NxtCpnDt.setter
	def NxtCpnDt(self, value):
		self._NxtCpnDt = value if type(value) != base_types.auto else self.make_default("NxtCpnDt")

	@NxtCpnDt.deleter
	def NxtCpnDt(self):
		del self._NxtCpnDt
		self._NxtCpnDt = None

	@property
	def NxtFctr(self):
		return self._NxtFctr

	@NxtFctr.setter
	def NxtFctr(self, value):
		self._NxtFctr = value if type(value) != base_types.auto else self.make_default("NxtFctr")

	@NxtFctr.deleter
	def NxtFctr(self):
		del self._NxtFctr
		self._NxtFctr = None

	@property
	def NxtIntrstRate(self):
		return self._NxtIntrstRate

	@NxtIntrstRate.setter
	def NxtIntrstRate(self, value):
		self._NxtIntrstRate = value if type(value) != base_types.auto else self.make_default("NxtIntrstRate")

	@NxtIntrstRate.deleter
	def NxtIntrstRate(self):
		del self._NxtIntrstRate
		self._NxtIntrstRate = None

	@property
	def OptnStyle(self):
		return self._OptnStyle

	@OptnStyle.setter
	def OptnStyle(self, value):
		self._OptnStyle = value if type(value) != base_types.auto else self.make_default("OptnStyle")

	@OptnStyle.deleter
	def OptnStyle(self):
		del self._OptnStyle
		self._OptnStyle = None

	@property
	def PlcOfListg(self):
		return self._PlcOfListg

	@PlcOfListg.setter
	def PlcOfListg(self, value):
		self._PlcOfListg = value if type(value) != base_types.auto else self.make_default("PlcOfListg")

	@PlcOfListg.deleter
	def PlcOfListg(self):
		del self._PlcOfListg
		self._PlcOfListg = None

	@property
	def PrvsFctr(self):
		return self._PrvsFctr

	@PrvsFctr.setter
	def PrvsFctr(self, value):
		self._PrvsFctr = value if type(value) != base_types.auto else self.make_default("PrvsFctr")

	@PrvsFctr.deleter
	def PrvsFctr(self):
		del self._PrvsFctr
		self._PrvsFctr = None

	@property
	def PutblDt(self):
		return self._PutblDt

	@PutblDt.setter
	def PutblDt(self, value):
		self._PutblDt = value if type(value) != base_types.auto else self.make_default("PutblDt")

	@PutblDt.deleter
	def PutblDt(self):
		del self._PutblDt
		self._PutblDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctSz', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethodFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DnmtnCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRateFxgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssePric', type=PriceFormat81Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinMltplQtyToInst', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinNmnlQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinQtyToInst', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtCllblDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtCpnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtFctr', type=RateFormat12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtIntrstRate', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnStyle', type=OptionStyle8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfListg', type=MarketIdentification3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsFctr', type=RateFormat12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutblDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

