import base_types
import ISODateTime
import ExternalAuthorityExchangeReason1Code

class RecordTechnicalData5(base_types._BaseFieldType):

	__slots__ = ["_XchgRsn", "_RctDtTm"]
	@property
	def XchgRsn(self):
		return self._XchgRsn

	@XchgRsn.setter
	def XchgRsn(self, value):
		self._XchgRsn = value if type(value) != auto else self.make_default("XchgRsn")

	@XchgRsn.deleter
	def XchgRsn(self):
		del self._XchgRsn
		self._XchgRsn = None

	@property
	def RctDtTm(self):
		return self._RctDtTm

	@RctDtTm.setter
	def RctDtTm(self, value):
		self._RctDtTm = value if type(value) != auto else self.make_default("RctDtTm")

	@RctDtTm.deleter
	def RctDtTm(self):
		del self._RctDtTm
		self._RctDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XchgRsn', type=ExternalAuthorityExchangeReason1Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RctDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

