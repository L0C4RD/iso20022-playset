from . import base_types
from ._PaymentStatusCodeSearch2Choice import PaymentStatusCodeSearch2Choice
from ._Max4AlphaNumericText import Max4AlphaNumericText
from ._DateTimePeriod1Choice import DateTimePeriod1Choice

class InstructionStatusSearch5(base_types._BaseFieldType):

	__slots__ = ["_PmtInstrStsDtTm", "_PmtInstrSts", "_PrtryStsRsn"]
	@property
	def PmtInstrStsDtTm(self):
		return self._PmtInstrStsDtTm

	@PmtInstrStsDtTm.setter
	def PmtInstrStsDtTm(self, value):
		self._PmtInstrStsDtTm = value if type(value) != base_types.auto else self.make_default("PmtInstrStsDtTm")

	@PmtInstrStsDtTm.deleter
	def PmtInstrStsDtTm(self):
		del self._PmtInstrStsDtTm
		self._PmtInstrStsDtTm = None

	@property
	def PmtInstrSts(self):
		return self._PmtInstrSts

	@PmtInstrSts.setter
	def PmtInstrSts(self, value):
		self._PmtInstrSts = value if type(value) != base_types.auto else self.make_default("PmtInstrSts")

	@PmtInstrSts.deleter
	def PmtInstrSts(self):
		del self._PmtInstrSts
		self._PmtInstrSts = None

	@property
	def PrtryStsRsn(self):
		return self._PrtryStsRsn

	@PrtryStsRsn.setter
	def PrtryStsRsn(self, value):
		self._PrtryStsRsn = value if type(value) != base_types.auto else self.make_default("PrtryStsRsn")

	@PrtryStsRsn.deleter
	def PrtryStsRsn(self):
		del self._PrtryStsRsn
		self._PrtryStsRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtInstrStsDtTm', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrSts', type=PaymentStatusCodeSearch2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryStsRsn', type=Max4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))

