# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Modification1Code
from . import PartyIdentification274

class PartyModification3(base_types._BaseFieldType):

	__slots__ = ["_ModCd", "_PtyId"]
	@property
	def ModCd(self):
		return self._ModCd

	@ModCd.setter
	def ModCd(self, value):
		self._ModCd = value if value is not None else base_types.UninitialisedField(self, 'ModCd', Modification1Code, False)

	@ModCd.deleter
	def ModCd(self):
		del self._ModCd
		self._ModCd = base_types.UninitialisedField(self, 'ModCd', Modification1Code, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PartyIdentification274, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PartyIdentification274, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification274, min=1, max=1, mutex_group=None, array=False),
	))