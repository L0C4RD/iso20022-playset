# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyOrBusinessError4Choice
from . import SystemPartyIdentification8

class PartyReport4(base_types._BaseFieldType):

	__slots__ = ["_PtyId", "_PtyOrErr"]
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

	@property
	def PtyOrErr(self):
		return self._PtyOrErr

	@PtyOrErr.setter
	def PtyOrErr(self, value):
		self._PtyOrErr = value if value is not None else base_types.UninitialisedField(self, 'PtyOrErr', PartyOrBusinessError4Choice, False)

	@PtyOrErr.deleter
	def PtyOrErr(self):
		del self._PtyOrErr
		self._PtyOrErr = base_types.UninitialisedField(self, 'PtyOrErr', PartyOrBusinessError4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyOrErr', type=PartyOrBusinessError4Choice, min=1, max=1, mutex_group=None, array=False),
	))