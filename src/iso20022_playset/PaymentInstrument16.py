from . import base_types
import FundOrderType5Choice
import AdditionalInformation15
import FundPaymentType1Choice

class PaymentInstrument16(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_OrdrTp", "_InstrmTp"]
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
	def OrdrTp(self):
		return self._OrdrTp

	@OrdrTp.setter
	def OrdrTp(self, value):
		self._OrdrTp = value if type(value) != auto else self.make_default("OrdrTp")

	@OrdrTp.deleter
	def OrdrTp(self):
		del self._OrdrTp
		self._OrdrTp = None

	@property
	def InstrmTp(self):
		return self._InstrmTp

	@InstrmTp.setter
	def InstrmTp(self, value):
		self._InstrmTp = value if type(value) != auto else self.make_default("InstrmTp")

	@InstrmTp.deleter
	def InstrmTp(self):
		del self._InstrmTp
		self._InstrmTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrdrTp', type=FundOrderType5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmTp', type=FundPaymentType1Choice, min=1, max=1, mutex_group=None, array=False),
	))

