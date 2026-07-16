# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateTimePeriod1Choice
from . import Max4AlphaNumericText
from . import PaymentStatusCodeSearch2Choice

class InstructionStatusSearch5(base_types._BaseFieldType):

	__slots__ = ["_PmtInstrSts", "_PmtInstrStsDtTm", "_PrtryStsRsn"]
	@property
	def PmtInstrSts(self):
		return self._PmtInstrSts

	@PmtInstrSts.setter
	def PmtInstrSts(self, value):
		self._PmtInstrSts = value if value is not None else base_types.UninitialisedField(self, 'PmtInstrSts', PaymentStatusCodeSearch2Choice, False)

	@PmtInstrSts.deleter
	def PmtInstrSts(self):
		del self._PmtInstrSts
		self._PmtInstrSts = base_types.UninitialisedField(self, 'PmtInstrSts', PaymentStatusCodeSearch2Choice, False)

	@property
	def PmtInstrStsDtTm(self):
		return self._PmtInstrStsDtTm

	@PmtInstrStsDtTm.setter
	def PmtInstrStsDtTm(self, value):
		self._PmtInstrStsDtTm = value if value is not None else base_types.UninitialisedField(self, 'PmtInstrStsDtTm', DateTimePeriod1Choice, False)

	@PmtInstrStsDtTm.deleter
	def PmtInstrStsDtTm(self):
		del self._PmtInstrStsDtTm
		self._PmtInstrStsDtTm = base_types.UninitialisedField(self, 'PmtInstrStsDtTm', DateTimePeriod1Choice, False)

	@property
	def PrtryStsRsn(self):
		return self._PrtryStsRsn

	@PrtryStsRsn.setter
	def PrtryStsRsn(self, value):
		self._PrtryStsRsn = value if value is not None else base_types.UninitialisedField(self, 'PrtryStsRsn', Max4AlphaNumericText, False)

	@PrtryStsRsn.deleter
	def PrtryStsRsn(self):
		del self._PrtryStsRsn
		self._PrtryStsRsn = base_types.UninitialisedField(self, 'PrtryStsRsn', Max4AlphaNumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtInstrSts', type=PaymentStatusCodeSearch2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrStsDtTm', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryStsRsn', type=Max4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))