from . import base_types
from .SecurityIdentification39 import SecurityIdentification39
from .AuditTrailOrBusinessError6Choice import AuditTrailOrBusinessError6Choice
from .DatePeriodSearch1Choice import DatePeriodSearch1Choice

class SecuritiesAuditTrailReport4(base_types._BaseFieldType):

	__slots__ = ["_DtPrd", "_SctiesAudtTrlOrErr", "_FinInstrmId"]
	@property
	def DtPrd(self):
		return self._DtPrd

	@DtPrd.setter
	def DtPrd(self, value):
		self._DtPrd = value if type(value) != auto else self.make_default("DtPrd")

	@DtPrd.deleter
	def DtPrd(self):
		del self._DtPrd
		self._DtPrd = None

	@property
	def SctiesAudtTrlOrErr(self):
		return self._SctiesAudtTrlOrErr

	@SctiesAudtTrlOrErr.setter
	def SctiesAudtTrlOrErr(self, value):
		self._SctiesAudtTrlOrErr = value if type(value) != auto else self.make_default("SctiesAudtTrlOrErr")

	@SctiesAudtTrlOrErr.deleter
	def SctiesAudtTrlOrErr(self):
		del self._SctiesAudtTrlOrErr
		self._SctiesAudtTrlOrErr = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtPrd', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAudtTrlOrErr', type=AuditTrailOrBusinessError6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification39, min=1, max=1, mutex_group=None, array=False),
	))

