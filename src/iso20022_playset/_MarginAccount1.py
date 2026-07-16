# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification118Choice
from . import PositionAccount1

class MarginAccount1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_PosAcct"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification118Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification118Choice, False)

	@property
	def PosAcct(self):
		return self._PosAcct

	@PosAcct.setter
	def PosAcct(self, value):
		self._PosAcct = value if value is not None else base_types.UninitialisedField(self, 'PosAcct', PositionAccount1, True)

	@PosAcct.deleter
	def PosAcct(self):
		del self._PosAcct
		self._PosAcct = base_types.UninitialisedField(self, 'PosAcct', PositionAccount1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification118Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PosAcct', type=PositionAccount1, min=1, max=None, mutex_group=None, array=True),
	))