# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import FundOrderType5Choice
from . import FundPaymentType1Choice

class PaymentInstrument16(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_InstrmTp", "_OrdrTp"]
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
	def InstrmTp(self):
		return self._InstrmTp

	@InstrmTp.setter
	def InstrmTp(self, value):
		self._InstrmTp = value if value is not None else base_types.UninitialisedField(self, 'InstrmTp', FundPaymentType1Choice, False)

	@InstrmTp.deleter
	def InstrmTp(self):
		del self._InstrmTp
		self._InstrmTp = base_types.UninitialisedField(self, 'InstrmTp', FundPaymentType1Choice, False)

	@property
	def OrdrTp(self):
		return self._OrdrTp

	@OrdrTp.setter
	def OrdrTp(self, value):
		self._OrdrTp = value if value is not None else base_types.UninitialisedField(self, 'OrdrTp', FundOrderType5Choice, False)

	@OrdrTp.deleter
	def OrdrTp(self):
		del self._OrdrTp
		self._OrdrTp = base_types.UninitialisedField(self, 'OrdrTp', FundOrderType5Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrmTp', type=FundPaymentType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrTp', type=FundOrderType5Choice, min=1, max=1, mutex_group=None, array=False),
	))