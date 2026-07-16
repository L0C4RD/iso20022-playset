# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DatePeriod3Choice
from . import PartyAuditTrailOrError4Choice
from . import SystemPartyIdentification8

class PartyAuditTrailReport4(base_types._BaseFieldType):

	__slots__ = ["_DtPrd", "_PtyAudtTrlOrErr", "_PtyId"]
	@property
	def DtPrd(self):
		return self._DtPrd

	@DtPrd.setter
	def DtPrd(self, value):
		self._DtPrd = value if value is not None else base_types.UninitialisedField(self, 'DtPrd', DatePeriod3Choice, False)

	@DtPrd.deleter
	def DtPrd(self):
		del self._DtPrd
		self._DtPrd = base_types.UninitialisedField(self, 'DtPrd', DatePeriod3Choice, False)

	@property
	def PtyAudtTrlOrErr(self):
		return self._PtyAudtTrlOrErr

	@PtyAudtTrlOrErr.setter
	def PtyAudtTrlOrErr(self, value):
		self._PtyAudtTrlOrErr = value if value is not None else base_types.UninitialisedField(self, 'PtyAudtTrlOrErr', PartyAuditTrailOrError4Choice, False)

	@PtyAudtTrlOrErr.deleter
	def PtyAudtTrlOrErr(self):
		del self._PtyAudtTrlOrErr
		self._PtyAudtTrlOrErr = base_types.UninitialisedField(self, 'PtyAudtTrlOrErr', PartyAuditTrailOrError4Choice, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', SystemPartyIdentification8, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', SystemPartyIdentification8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtPrd', type=DatePeriod3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyAudtTrlOrErr', type=PartyAuditTrailOrError4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification8, min=1, max=1, mutex_group=None, array=False),
	))