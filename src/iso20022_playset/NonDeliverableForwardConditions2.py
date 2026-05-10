from . import base_types
from .OpeningConditions1 import OpeningConditions1
from .FixingConditions1 import FixingConditions1

class NonDeliverableForwardConditions2(base_types._BaseFieldType):

	__slots__ = ["_OpngConds", "_FxgConds"]
	@property
	def OpngConds(self):
		return self._OpngConds

	@OpngConds.setter
	def OpngConds(self, value):
		self._OpngConds = value if type(value) != base_types.auto else self.make_default("OpngConds")

	@OpngConds.deleter
	def OpngConds(self):
		del self._OpngConds
		self._OpngConds = None

	@property
	def FxgConds(self):
		return self._FxgConds

	@FxgConds.setter
	def FxgConds(self, value):
		self._FxgConds = value if type(value) != base_types.auto else self.make_default("FxgConds")

	@FxgConds.deleter
	def FxgConds(self):
		del self._FxgConds
		self._FxgConds = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OpngConds', type=OpeningConditions1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxgConds', type=FixingConditions1, min=0, max=1, mutex_group=None, array=False),
	))

