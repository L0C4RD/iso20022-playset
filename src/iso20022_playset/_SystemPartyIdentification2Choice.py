from . import base_types
from ._SystemPartyIdentification8 import SystemPartyIdentification8
from ._PartyIdentification136 import PartyIdentification136

class SystemPartyIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgId", "_CmbndId"]
	@property
	def OrgId(self):
		return self._OrgId

	@OrgId.setter
	def OrgId(self, value):
		self._OrgId = value if type(value) != base_types.auto else self.make_default("OrgId")

	@OrgId.deleter
	def OrgId(self):
		del self._OrgId
		self._OrgId = None

	@property
	def CmbndId(self):
		return self._CmbndId

	@CmbndId.setter
	def CmbndId(self, value):
		self._CmbndId = value if type(value) != base_types.auto else self.make_default("CmbndId")

	@CmbndId.deleter
	def CmbndId(self):
		del self._CmbndId
		self._CmbndId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgId', type=PartyIdentification136, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CmbndId', type=SystemPartyIdentification8, min=0, max=1, mutex_group=1, array=False),
	))

