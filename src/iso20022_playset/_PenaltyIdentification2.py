# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class PenaltyIdentification2(base_types._BaseFieldType):

	__slots__ = ["_Id", "_MktInfrstrctrId"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def MktInfrstrctrId(self):
		return self._MktInfrstrctrId

	@MktInfrstrctrId.setter
	def MktInfrstrctrId(self, value):
		self._MktInfrstrctrId = value if value is not None else base_types.UninitialisedField(self, 'MktInfrstrctrId', Max35Text, False)

	@MktInfrstrctrId.deleter
	def MktInfrstrctrId(self):
		del self._MktInfrstrctrId
		self._MktInfrstrctrId = base_types.UninitialisedField(self, 'MktInfrstrctrId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktInfrstrctrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))