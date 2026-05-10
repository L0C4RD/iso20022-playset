from . import base_types
import DatePeriodSearch1Choice
import SecuritiesAccount19

class SecuritiesAccountAuditTrailSearchCriteria3(base_types._BaseFieldType):

	__slots__ = ["_SctiesAcctId", "_DtPrd"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesAcctId', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtPrd', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
	))

