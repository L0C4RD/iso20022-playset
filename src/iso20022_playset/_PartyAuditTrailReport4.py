# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DatePeriod3Choice import DatePeriod3Choice
from ._PartyAuditTrailOrError4Choice import PartyAuditTrailOrError4Choice
from ._SystemPartyIdentification8 import SystemPartyIdentification8

class PartyAuditTrailReport4(base_types._BaseFieldType):

	__slots__ = ["_DtPrd", "_PtyAudtTrlOrErr", "_PtyId"]
	@property
	def DtPrd(self):
		return self._DtPrd

	@DtPrd.setter
	def DtPrd(self, value):
		self._DtPrd = value if type(value) != base_types.auto else self.make_default("DtPrd")

	@DtPrd.deleter
	def DtPrd(self):
		del self._DtPrd
		self._DtPrd = None

	@property
	def PtyAudtTrlOrErr(self):
		return self._PtyAudtTrlOrErr

	@PtyAudtTrlOrErr.setter
	def PtyAudtTrlOrErr(self, value):
		self._PtyAudtTrlOrErr = value if type(value) != base_types.auto else self.make_default("PtyAudtTrlOrErr")

	@PtyAudtTrlOrErr.deleter
	def PtyAudtTrlOrErr(self):
		del self._PtyAudtTrlOrErr
		self._PtyAudtTrlOrErr = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != base_types.auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtPrd', type=DatePeriod3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyAudtTrlOrErr', type=PartyAuditTrailOrError4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification8, min=1, max=1, mutex_group=None, array=False),
	))