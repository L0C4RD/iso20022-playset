from . import base_types
from ._SearchAnd1 import SearchAnd1

class SearchOr1(base_types._BaseFieldType):

	__slots__ = ["_SchAnd"]
	@property
	def SchAnd(self):
		return self._SchAnd

	@SchAnd.setter
	def SchAnd(self, value):
		self._SchAnd = value if type(value) != base_types.auto else self.make_default("SchAnd")

	@SchAnd.deleter
	def SchAnd(self):
		del self._SchAnd
		self._SchAnd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SchAnd', type=SearchAnd1, min=1, max=None, mutex_group=None, array=True),
	))

