from . import base_types
from .PlaceOfTradeIdentification1Choice import PlaceOfTradeIdentification1Choice
from .ISODate import ISODate
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .RedemptionOrder15 import RedemptionOrder15
from .FinancialInstrument57 import FinancialInstrument57
from .Max35Text import Max35Text
from .PaymentTransaction72 import PaymentTransaction72
from .ActiveCurrencyCode import ActiveCurrencyCode
from .DateAndDateTimeChoice import DateAndDateTimeChoice
from .CancellationRight1Choice import CancellationRight1Choice
from .ISODateTime import ISODateTime
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode

class RedemptionBulkOrder6(base_types._BaseFieldType):

	__slots__ = ["_OrdrDtTm", "_PlcOfTrad", "_XpryDtTm", "_TtlSttlmAmt", "_IndvOrdrDtls", "_ReqdNAVCcy", "_BlkCshSttlmDtls", "_CxlRght", "_MstrRef", "_FinInstrmDtls", "_ReqdSttlmCcy", "_ReqdFutrTradDt"]
	@property
	def OrdrDtTm(self):
		return self._OrdrDtTm

	@OrdrDtTm.setter
	def OrdrDtTm(self, value):
		self._OrdrDtTm = value if type(value) != base_types.auto else self.make_default("OrdrDtTm")

	@OrdrDtTm.deleter
	def OrdrDtTm(self):
		del self._OrdrDtTm
		self._OrdrDtTm = None

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
	def XpryDtTm(self):
		return self._XpryDtTm

	@XpryDtTm.setter
	def XpryDtTm(self, value):
		self._XpryDtTm = value if type(value) != base_types.auto else self.make_default("XpryDtTm")

	@XpryDtTm.deleter
	def XpryDtTm(self):
		del self._XpryDtTm
		self._XpryDtTm = None

	@property
	def TtlSttlmAmt(self):
		return self._TtlSttlmAmt

	@TtlSttlmAmt.setter
	def TtlSttlmAmt(self, value):
		self._TtlSttlmAmt = value if type(value) != base_types.auto else self.make_default("TtlSttlmAmt")

	@TtlSttlmAmt.deleter
	def TtlSttlmAmt(self):
		del self._TtlSttlmAmt
		self._TtlSttlmAmt = None

	@property
	def IndvOrdrDtls(self):
		return self._IndvOrdrDtls

	@IndvOrdrDtls.setter
	def IndvOrdrDtls(self, value):
		self._IndvOrdrDtls = value if type(value) != base_types.auto else self.make_default("IndvOrdrDtls")

	@IndvOrdrDtls.deleter
	def IndvOrdrDtls(self):
		del self._IndvOrdrDtls
		self._IndvOrdrDtls = None

	@property
	def ReqdNAVCcy(self):
		return self._ReqdNAVCcy

	@ReqdNAVCcy.setter
	def ReqdNAVCcy(self, value):
		self._ReqdNAVCcy = value if type(value) != base_types.auto else self.make_default("ReqdNAVCcy")

	@ReqdNAVCcy.deleter
	def ReqdNAVCcy(self):
		del self._ReqdNAVCcy
		self._ReqdNAVCcy = None

	@property
	def BlkCshSttlmDtls(self):
		return self._BlkCshSttlmDtls

	@BlkCshSttlmDtls.setter
	def BlkCshSttlmDtls(self, value):
		self._BlkCshSttlmDtls = value if type(value) != base_types.auto else self.make_default("BlkCshSttlmDtls")

	@BlkCshSttlmDtls.deleter
	def BlkCshSttlmDtls(self):
		del self._BlkCshSttlmDtls
		self._BlkCshSttlmDtls = None

	@property
	def CxlRght(self):
		return self._CxlRght

	@CxlRght.setter
	def CxlRght(self, value):
		self._CxlRght = value if type(value) != base_types.auto else self.make_default("CxlRght")

	@CxlRght.deleter
	def CxlRght(self):
		del self._CxlRght
		self._CxlRght = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != base_types.auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

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
	def ReqdSttlmCcy(self):
		return self._ReqdSttlmCcy

	@ReqdSttlmCcy.setter
	def ReqdSttlmCcy(self, value):
		self._ReqdSttlmCcy = value if type(value) != base_types.auto else self.make_default("ReqdSttlmCcy")

	@ReqdSttlmCcy.deleter
	def ReqdSttlmCcy(self):
		del self._ReqdSttlmCcy
		self._ReqdSttlmCcy = None

	@property
	def ReqdFutrTradDt(self):
		return self._ReqdFutrTradDt

	@ReqdFutrTradDt.setter
	def ReqdFutrTradDt(self, value):
		self._ReqdFutrTradDt = value if type(value) != base_types.auto else self.make_default("ReqdFutrTradDt")

	@ReqdFutrTradDt.deleter
	def ReqdFutrTradDt(self):
		del self._ReqdFutrTradDt
		self._ReqdFutrTradDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrdrDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlSttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvOrdrDtls', type=RedemptionOrder15, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqdNAVCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlkCshSttlmDtls', type=PaymentTransaction72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRght', type=CancellationRight1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument57, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdFutrTradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

