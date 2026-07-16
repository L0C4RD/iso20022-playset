# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PledgeeType1Code

class PledgeeTypeAndText1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_PldgeeTp"]
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
	def PldgeeTp(self):
		return self._PldgeeTp

	@PldgeeTp.setter
	def PldgeeTp(self, value):
		self._PldgeeTp = value if value is not None else base_types.UninitialisedField(self, 'PldgeeTp', PledgeeType1Code, False)

	@PldgeeTp.deleter
	def PldgeeTp(self):
		del self._PldgeeTp
		self._PldgeeTp = base_types.UninitialisedField(self, 'PldgeeTp', PledgeeType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PldgeeTp', type=PledgeeType1Code, min=1, max=1, mutex_group=None, array=False),
	))