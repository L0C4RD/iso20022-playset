from . import base_types
from .DatePeriodSearch1Choice import DatePeriodSearch1Choice
from .SystemPartyIdentification8 import SystemPartyIdentification8

class PartyAuditTrailSearchCriteria2(base_types._BaseFieldType):

	__slots__ = ["_DtPrd", "_PtyId"]
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
		base_types.FieldEntry(name='DtPrd', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
	))

