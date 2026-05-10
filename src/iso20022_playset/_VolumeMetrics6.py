from . import base_types
from ._ExposureMetrics5 import ExposureMetrics5

class VolumeMetrics6(base_types._BaseFieldType):

	__slots__ = ["_Neg", "_Postv"]
	@property
	def Neg(self):
		return self._Neg

	@Neg.setter
	def Neg(self, value):
		self._Neg = value if type(value) != base_types.auto else self.make_default("Neg")

	@Neg.deleter
	def Neg(self):
		del self._Neg
		self._Neg = None

	@property
	def Postv(self):
		return self._Postv

	@Postv.setter
	def Postv(self, value):
		self._Postv = value if type(value) != base_types.auto else self.make_default("Postv")

	@Postv.deleter
	def Postv(self):
		del self._Postv
		self._Postv = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Neg', type=ExposureMetrics5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Postv', type=ExposureMetrics5, min=0, max=1, mutex_group=None, array=False),
	))

