from . import base_types
from .ChargeBearerType1Code import ChargeBearerType1Code
from .CurrencyExchange13 import CurrencyExchange13
from .ISODateTime import ISODateTime
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .TrackerPartyIdentification2 import TrackerPartyIdentification2

class TrackerRecord8(base_types._BaseFieldType):

	__slots__ = ["_PrcgDtTm", "_IntrBkSttlmAmt", "_ChrgBr", "_ChrgsAmt", "_XchgRateData", "_PtyOrAgtId"]
	@property
	def PrcgDtTm(self):
		return self._PrcgDtTm

	@PrcgDtTm.setter
	def PrcgDtTm(self, value):
		self._PrcgDtTm = value if type(value) != base_types.auto else self.make_default("PrcgDtTm")

	@PrcgDtTm.deleter
	def PrcgDtTm(self):
		del self._PrcgDtTm
		self._PrcgDtTm = None

	@property
	def IntrBkSttlmAmt(self):
		return self._IntrBkSttlmAmt

	@IntrBkSttlmAmt.setter
	def IntrBkSttlmAmt(self, value):
		self._IntrBkSttlmAmt = value if type(value) != base_types.auto else self.make_default("IntrBkSttlmAmt")

	@IntrBkSttlmAmt.deleter
	def IntrBkSttlmAmt(self):
		del self._IntrBkSttlmAmt
		self._IntrBkSttlmAmt = None

	@property
	def ChrgBr(self):
		return self._ChrgBr

	@ChrgBr.setter
	def ChrgBr(self, value):
		self._ChrgBr = value if type(value) != base_types.auto else self.make_default("ChrgBr")

	@ChrgBr.deleter
	def ChrgBr(self):
		del self._ChrgBr
		self._ChrgBr = None

	@property
	def ChrgsAmt(self):
		return self._ChrgsAmt

	@ChrgsAmt.setter
	def ChrgsAmt(self, value):
		self._ChrgsAmt = value if type(value) != base_types.auto else self.make_default("ChrgsAmt")

	@ChrgsAmt.deleter
	def ChrgsAmt(self):
		del self._ChrgsAmt
		self._ChrgsAmt = None

	@property
	def XchgRateData(self):
		return self._XchgRateData

	@XchgRateData.setter
	def XchgRateData(self, value):
		self._XchgRateData = value if type(value) != base_types.auto else self.make_default("XchgRateData")

	@XchgRateData.deleter
	def XchgRateData(self):
		del self._XchgRateData
		self._XchgRateData = None

	@property
	def PtyOrAgtId(self):
		return self._PtyOrAgtId

	@PtyOrAgtId.setter
	def PtyOrAgtId(self, value):
		self._PtyOrAgtId = value if type(value) != base_types.auto else self.make_default("PtyOrAgtId")

	@PtyOrAgtId.deleter
	def PtyOrAgtId(self):
		del self._PtyOrAgtId
		self._PtyOrAgtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrcgDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateData', type=CurrencyExchange13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyOrAgtId', type=TrackerPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
	))

