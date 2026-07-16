# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification136
from . import SystemPartyIdentification8

class SystemPartyIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_CmbndId", "_OrgId"]
	@property
	def CmbndId(self):
		return self._CmbndId

	@CmbndId.setter
	def CmbndId(self, value):
		self._CmbndId = value if value is not None else base_types.UninitialisedField(self, 'CmbndId', SystemPartyIdentification8, False)

	@CmbndId.deleter
	def CmbndId(self):
		del self._CmbndId
		self._CmbndId = base_types.UninitialisedField(self, 'CmbndId', SystemPartyIdentification8, False)

	@property
	def OrgId(self):
		return self._OrgId

	@OrgId.setter
	def OrgId(self, value):
		self._OrgId = value if value is not None else base_types.UninitialisedField(self, 'OrgId', PartyIdentification136, False)

	@OrgId.deleter
	def OrgId(self):
		del self._OrgId
		self._OrgId = base_types.UninitialisedField(self, 'OrgId', PartyIdentification136, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmbndId', type=SystemPartyIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgId', type=PartyIdentification136, min=0, max=1, mutex_group=1, array=False),
	))