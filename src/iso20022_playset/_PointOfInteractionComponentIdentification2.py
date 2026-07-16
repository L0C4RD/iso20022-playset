# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max256Text
from . import Max35Text

class PointOfInteractionComponentIdentification2(base_types._BaseFieldType):

	__slots__ = ["_Id", "_ItmNb", "_PrvdrId", "_SrlNb"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max256Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max256Text, False)

	@property
	def ItmNb(self):
		return self._ItmNb

	@ItmNb.setter
	def ItmNb(self, value):
		self._ItmNb = value if value is not None else base_types.UninitialisedField(self, 'ItmNb', Max35Text, False)

	@ItmNb.deleter
	def ItmNb(self):
		del self._ItmNb
		self._ItmNb = base_types.UninitialisedField(self, 'ItmNb', Max35Text, False)

	@property
	def PrvdrId(self):
		return self._PrvdrId

	@PrvdrId.setter
	def PrvdrId(self, value):
		self._PrvdrId = value if value is not None else base_types.UninitialisedField(self, 'PrvdrId', Max35Text, False)

	@PrvdrId.deleter
	def PrvdrId(self):
		del self._PrvdrId
		self._PrvdrId = base_types.UninitialisedField(self, 'PrvdrId', Max35Text, False)

	@property
	def SrlNb(self):
		return self._SrlNb

	@SrlNb.setter
	def SrlNb(self, value):
		self._SrlNb = value if value is not None else base_types.UninitialisedField(self, 'SrlNb', Max256Text, False)

	@SrlNb.deleter
	def SrlNb(self):
		del self._SrlNb
		self._SrlNb = base_types.UninitialisedField(self, 'SrlNb', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))