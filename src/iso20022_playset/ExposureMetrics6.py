from . import base_types
from .PostedMarginOrCollateral4 import PostedMarginOrCollateral4

class ExposureMetrics6(base_types._BaseFieldType):

	__slots__ = ["_PstdMrgnOrColl"]
	@property
	def PstdMrgnOrColl(self):
		return self._PstdMrgnOrColl

	@PstdMrgnOrColl.setter
	def PstdMrgnOrColl(self, value):
		self._PstdMrgnOrColl = value if type(value) != base_types.auto else self.make_default("PstdMrgnOrColl")

	@PstdMrgnOrColl.deleter
	def PstdMrgnOrColl(self):
		del self._PstdMrgnOrColl
		self._PstdMrgnOrColl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PstdMrgnOrColl', type=PostedMarginOrCollateral4, min=0, max=1, mutex_group=None, array=False),
	))

