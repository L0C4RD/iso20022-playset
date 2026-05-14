# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LEIIdentifier import LEIIdentifier
from ._PledgeeFormat6Choice import PledgeeFormat6Choice

class Pledgee4(base_types._BaseFieldType):

	__slots__ = ["_LEI", "_PldgeeTpAndId"]
	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	@property
	def PldgeeTpAndId(self):
		return self._PldgeeTpAndId

	@PldgeeTpAndId.setter
	def PldgeeTpAndId(self, value):
		self._PldgeeTpAndId = value if type(value) != base_types.auto else self.make_default("PldgeeTpAndId")

	@PldgeeTpAndId.deleter
	def PldgeeTpAndId(self):
		del self._PldgeeTpAndId
		self._PldgeeTpAndId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PldgeeTpAndId', type=PledgeeFormat6Choice, min=0, max=1, mutex_group=None, array=False),
	))