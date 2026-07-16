# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LEIIdentifier
from . import PledgeeFormat6Choice

class Pledgee4(base_types._BaseFieldType):

	__slots__ = ["_LEI", "_PldgeeTpAndId"]
	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if value is not None else base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@property
	def PldgeeTpAndId(self):
		return self._PldgeeTpAndId

	@PldgeeTpAndId.setter
	def PldgeeTpAndId(self, value):
		self._PldgeeTpAndId = value if value is not None else base_types.UninitialisedField(self, 'PldgeeTpAndId', PledgeeFormat6Choice, False)

	@PldgeeTpAndId.deleter
	def PldgeeTpAndId(self):
		del self._PldgeeTpAndId
		self._PldgeeTpAndId = base_types.UninitialisedField(self, 'PldgeeTpAndId', PledgeeFormat6Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PldgeeTpAndId', type=PledgeeFormat6Choice, min=0, max=1, mutex_group=None, array=False),
	))