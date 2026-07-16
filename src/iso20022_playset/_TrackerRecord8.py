# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ChargeBearerType1Code
from . import CurrencyExchange13
from . import ISODateTime
from . import TrackerPartyIdentification2

class TrackerRecord8(base_types._BaseFieldType):

	__slots__ = ["_ChrgBr", "_ChrgsAmt", "_IntrBkSttlmAmt", "_PrcgDtTm", "_PtyOrAgtId", "_XchgRateData"]
	@property
	def ChrgBr(self):
		return self._ChrgBr

	@ChrgBr.setter
	def ChrgBr(self, value):
		self._ChrgBr = value if value is not None else base_types.UninitialisedField(self, 'ChrgBr', ChargeBearerType1Code, False)

	@ChrgBr.deleter
	def ChrgBr(self):
		del self._ChrgBr
		self._ChrgBr = base_types.UninitialisedField(self, 'ChrgBr', ChargeBearerType1Code, False)

	@property
	def ChrgsAmt(self):
		return self._ChrgsAmt

	@ChrgsAmt.setter
	def ChrgsAmt(self, value):
		self._ChrgsAmt = value if value is not None else base_types.UninitialisedField(self, 'ChrgsAmt', ActiveCurrencyAndAmount, False)

	@ChrgsAmt.deleter
	def ChrgsAmt(self):
		del self._ChrgsAmt
		self._ChrgsAmt = base_types.UninitialisedField(self, 'ChrgsAmt', ActiveCurrencyAndAmount, False)

	@property
	def IntrBkSttlmAmt(self):
		return self._IntrBkSttlmAmt

	@IntrBkSttlmAmt.setter
	def IntrBkSttlmAmt(self, value):
		self._IntrBkSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmAmt', ActiveCurrencyAndAmount, False)

	@IntrBkSttlmAmt.deleter
	def IntrBkSttlmAmt(self):
		del self._IntrBkSttlmAmt
		self._IntrBkSttlmAmt = base_types.UninitialisedField(self, 'IntrBkSttlmAmt', ActiveCurrencyAndAmount, False)

	@property
	def PrcgDtTm(self):
		return self._PrcgDtTm

	@PrcgDtTm.setter
	def PrcgDtTm(self, value):
		self._PrcgDtTm = value if value is not None else base_types.UninitialisedField(self, 'PrcgDtTm', ISODateTime, False)

	@PrcgDtTm.deleter
	def PrcgDtTm(self):
		del self._PrcgDtTm
		self._PrcgDtTm = base_types.UninitialisedField(self, 'PrcgDtTm', ISODateTime, False)

	@property
	def PtyOrAgtId(self):
		return self._PtyOrAgtId

	@PtyOrAgtId.setter
	def PtyOrAgtId(self, value):
		self._PtyOrAgtId = value if value is not None else base_types.UninitialisedField(self, 'PtyOrAgtId', TrackerPartyIdentification2, False)

	@PtyOrAgtId.deleter
	def PtyOrAgtId(self):
		del self._PtyOrAgtId
		self._PtyOrAgtId = base_types.UninitialisedField(self, 'PtyOrAgtId', TrackerPartyIdentification2, False)

	@property
	def XchgRateData(self):
		return self._XchgRateData

	@XchgRateData.setter
	def XchgRateData(self, value):
		self._XchgRateData = value if value is not None else base_types.UninitialisedField(self, 'XchgRateData', CurrencyExchange13, False)

	@XchgRateData.deleter
	def XchgRateData(self):
		del self._XchgRateData
		self._XchgRateData = base_types.UninitialisedField(self, 'XchgRateData', CurrencyExchange13, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyOrAgtId', type=TrackerPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateData', type=CurrencyExchange13, min=0, max=1, mutex_group=None, array=False),
	))