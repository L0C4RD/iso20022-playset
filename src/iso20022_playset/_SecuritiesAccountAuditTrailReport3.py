# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuditTrailOrBusinessError6Choice
from . import DatePeriodSearch1Choice
from . import SecuritiesAccount19

class SecuritiesAccountAuditTrailReport3(base_types._BaseFieldType):

	__slots__ = ["_DtPrd", "_SctiesAcctAudtTrlOrErr", "_SctiesAcctId"]
	@property
	def DtPrd(self):
		return self._DtPrd

	@DtPrd.setter
	def DtPrd(self, value):
		self._DtPrd = value if value is not None else base_types.UninitialisedField(self, 'DtPrd', DatePeriodSearch1Choice, False)

	@DtPrd.deleter
	def DtPrd(self):
		del self._DtPrd
		self._DtPrd = base_types.UninitialisedField(self, 'DtPrd', DatePeriodSearch1Choice, False)

	@property
	def SctiesAcctAudtTrlOrErr(self):
		return self._SctiesAcctAudtTrlOrErr

	@SctiesAcctAudtTrlOrErr.setter
	def SctiesAcctAudtTrlOrErr(self, value):
		self._SctiesAcctAudtTrlOrErr = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctAudtTrlOrErr', AuditTrailOrBusinessError6Choice, False)

	@SctiesAcctAudtTrlOrErr.deleter
	def SctiesAcctAudtTrlOrErr(self):
		del self._SctiesAcctAudtTrlOrErr
		self._SctiesAcctAudtTrlOrErr = base_types.UninitialisedField(self, 'SctiesAcctAudtTrlOrErr', AuditTrailOrBusinessError6Choice, False)

	@property
	def SctiesAcctId(self):
		return self._SctiesAcctId

	@SctiesAcctId.setter
	def SctiesAcctId(self, value):
		self._SctiesAcctId = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctId', SecuritiesAccount19, False)

	@SctiesAcctId.deleter
	def SctiesAcctId(self):
		del self._SctiesAcctId
		self._SctiesAcctId = base_types.UninitialisedField(self, 'SctiesAcctId', SecuritiesAccount19, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtPrd', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctAudtTrlOrErr', type=AuditTrailOrBusinessError6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctId', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
	))