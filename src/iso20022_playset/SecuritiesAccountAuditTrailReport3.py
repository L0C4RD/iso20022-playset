import base_types
import DatePeriodSearch1Choice
import AuditTrailOrBusinessError6Choice
import SecuritiesAccount19

class SecuritiesAccountAuditTrailReport3(base_types._BaseFieldType):

	__slots__ = ["_SctiesAcctId", "_DtPrd", "_SctiesAcctAudtTrlOrErr"]
	@property
	def SctiesAcctId(self):
		return self._SctiesAcctId

	@SctiesAcctId.setter
	def SctiesAcctId(self, value):
		self._SctiesAcctId = value if type(value) != auto else self.make_default("SctiesAcctId")

	@SctiesAcctId.deleter
	def SctiesAcctId(self):
		del self._SctiesAcctId
		self._SctiesAcctId = None

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
	def SctiesAcctAudtTrlOrErr(self):
		return self._SctiesAcctAudtTrlOrErr

	@SctiesAcctAudtTrlOrErr.setter
	def SctiesAcctAudtTrlOrErr(self, value):
		self._SctiesAcctAudtTrlOrErr = value if type(value) != auto else self.make_default("SctiesAcctAudtTrlOrErr")

	@SctiesAcctAudtTrlOrErr.deleter
	def SctiesAcctAudtTrlOrErr(self):
		del self._SctiesAcctAudtTrlOrErr
		self._SctiesAcctAudtTrlOrErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesAcctId', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtPrd', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctAudtTrlOrErr', type=AuditTrailOrBusinessError6Choice, min=1, max=1, mutex_group=None, array=False),
	))

