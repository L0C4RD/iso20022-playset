# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FixingConditions1
from . import OpeningConditions1

class NonDeliverableForwardConditions2(base_types._BaseFieldType):

	__slots__ = ["_FxgConds", "_OpngConds"]
	@property
	def FxgConds(self):
		return self._FxgConds

	@FxgConds.setter
	def FxgConds(self, value):
		self._FxgConds = value if value is not None else base_types.UninitialisedField(self, 'FxgConds', FixingConditions1, False)

	@FxgConds.deleter
	def FxgConds(self):
		del self._FxgConds
		self._FxgConds = base_types.UninitialisedField(self, 'FxgConds', FixingConditions1, False)

	@property
	def OpngConds(self):
		return self._OpngConds

	@OpngConds.setter
	def OpngConds(self, value):
		self._OpngConds = value if value is not None else base_types.UninitialisedField(self, 'OpngConds', OpeningConditions1, False)

	@OpngConds.deleter
	def OpngConds(self):
		del self._OpngConds
		self._OpngConds = base_types.UninitialisedField(self, 'OpngConds', OpeningConditions1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FxgConds', type=FixingConditions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngConds', type=OpeningConditions1, min=1, max=1, mutex_group=None, array=False),
	))