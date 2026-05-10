from . import base_types
from ._SearchOr1 import SearchOr1

class SearchCriteria1(base_types._BaseFieldType):

	__slots__ = ["_SchOr"]
	@property
	def SchOr(self):
		return self._SchOr

	@SchOr.setter
	def SchOr(self, value):
		self._SchOr = value if type(value) != base_types.auto else self.make_default("SchOr")

	@SchOr.deleter
	def SchOr(self):
		del self._SchOr
		self._SchOr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SchOr', type=SearchOr1, min=1, max=None, mutex_group=None, array=True),
	))

