# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ActiveCurrencyCode
from . import ActiveOrHistoricCurrencyCode
from . import CancellationRight1Choice
from . import DateAndDateTimeChoice
from . import FinancialInstrument57
from . import ISODate
from . import ISODateTime
from . import Max35Text
from . import PaymentTransaction70
from . import PlaceOfTradeIdentification1Choice
from . import SubscriptionOrder15

class SubscriptionBulkOrder5(base_types._BaseFieldType):

	__slots__ = ["_BlkCshSttlmDtls", "_CxlRght", "_FinInstrmDtls", "_IndvOrdrDtls", "_MstrRef", "_OrdrDtTm", "_PlcOfTrad", "_ReqdFutrTradDt", "_ReqdNAVCcy", "_ReqdSttlmCcy", "_TtlSttlmAmt", "_XpryDtTm"]
	@property
	def BlkCshSttlmDtls(self):
		return self._BlkCshSttlmDtls

	@BlkCshSttlmDtls.setter
	def BlkCshSttlmDtls(self, value):
		self._BlkCshSttlmDtls = value if value is not None else base_types.UninitialisedField(self, 'BlkCshSttlmDtls', PaymentTransaction70, False)

	@BlkCshSttlmDtls.deleter
	def BlkCshSttlmDtls(self):
		del self._BlkCshSttlmDtls
		self._BlkCshSttlmDtls = base_types.UninitialisedField(self, 'BlkCshSttlmDtls', PaymentTransaction70, False)

	@property
	def CxlRght(self):
		return self._CxlRght

	@CxlRght.setter
	def CxlRght(self, value):
		self._CxlRght = value if value is not None else base_types.UninitialisedField(self, 'CxlRght', CancellationRight1Choice, False)

	@CxlRght.deleter
	def CxlRght(self):
		del self._CxlRght
		self._CxlRght = base_types.UninitialisedField(self, 'CxlRght', CancellationRight1Choice, False)

	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument57, False)

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument57, False)

	@property
	def IndvOrdrDtls(self):
		return self._IndvOrdrDtls

	@IndvOrdrDtls.setter
	def IndvOrdrDtls(self, value):
		self._IndvOrdrDtls = value if value is not None else base_types.UninitialisedField(self, 'IndvOrdrDtls', SubscriptionOrder15, True)

	@IndvOrdrDtls.deleter
	def IndvOrdrDtls(self):
		del self._IndvOrdrDtls
		self._IndvOrdrDtls = base_types.UninitialisedField(self, 'IndvOrdrDtls', SubscriptionOrder15, True)

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if value is not None else base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@property
	def OrdrDtTm(self):
		return self._OrdrDtTm

	@OrdrDtTm.setter
	def OrdrDtTm(self, value):
		self._OrdrDtTm = value if value is not None else base_types.UninitialisedField(self, 'OrdrDtTm', ISODateTime, False)

	@OrdrDtTm.deleter
	def OrdrDtTm(self):
		del self._OrdrDtTm
		self._OrdrDtTm = base_types.UninitialisedField(self, 'OrdrDtTm', ISODateTime, False)

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if value is not None else base_types.UninitialisedField(self, 'PlcOfTrad', PlaceOfTradeIdentification1Choice, False)

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = base_types.UninitialisedField(self, 'PlcOfTrad', PlaceOfTradeIdentification1Choice, False)

	@property
	def ReqdFutrTradDt(self):
		return self._ReqdFutrTradDt

	@ReqdFutrTradDt.setter
	def ReqdFutrTradDt(self, value):
		self._ReqdFutrTradDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdFutrTradDt', ISODate, False)

	@ReqdFutrTradDt.deleter
	def ReqdFutrTradDt(self):
		del self._ReqdFutrTradDt
		self._ReqdFutrTradDt = base_types.UninitialisedField(self, 'ReqdFutrTradDt', ISODate, False)

	@property
	def ReqdNAVCcy(self):
		return self._ReqdNAVCcy

	@ReqdNAVCcy.setter
	def ReqdNAVCcy(self, value):
		self._ReqdNAVCcy = value if value is not None else base_types.UninitialisedField(self, 'ReqdNAVCcy', ActiveOrHistoricCurrencyCode, False)

	@ReqdNAVCcy.deleter
	def ReqdNAVCcy(self):
		del self._ReqdNAVCcy
		self._ReqdNAVCcy = base_types.UninitialisedField(self, 'ReqdNAVCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def ReqdSttlmCcy(self):
		return self._ReqdSttlmCcy

	@ReqdSttlmCcy.setter
	def ReqdSttlmCcy(self, value):
		self._ReqdSttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'ReqdSttlmCcy', ActiveCurrencyCode, False)

	@ReqdSttlmCcy.deleter
	def ReqdSttlmCcy(self):
		del self._ReqdSttlmCcy
		self._ReqdSttlmCcy = base_types.UninitialisedField(self, 'ReqdSttlmCcy', ActiveCurrencyCode, False)

	@property
	def TtlSttlmAmt(self):
		return self._TtlSttlmAmt

	@TtlSttlmAmt.setter
	def TtlSttlmAmt(self, value):
		self._TtlSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlSttlmAmt', ActiveCurrencyAndAmount, False)

	@TtlSttlmAmt.deleter
	def TtlSttlmAmt(self):
		del self._TtlSttlmAmt
		self._TtlSttlmAmt = base_types.UninitialisedField(self, 'TtlSttlmAmt', ActiveCurrencyAndAmount, False)

	@property
	def XpryDtTm(self):
		return self._XpryDtTm

	@XpryDtTm.setter
	def XpryDtTm(self, value):
		self._XpryDtTm = value if value is not None else base_types.UninitialisedField(self, 'XpryDtTm', DateAndDateTimeChoice, False)

	@XpryDtTm.deleter
	def XpryDtTm(self):
		del self._XpryDtTm
		self._XpryDtTm = base_types.UninitialisedField(self, 'XpryDtTm', DateAndDateTimeChoice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlkCshSttlmDtls', type=PaymentTransaction70, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRght', type=CancellationRight1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument57, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvOrdrDtls', type=SubscriptionOrder15, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdFutrTradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdNAVCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlSttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
	))