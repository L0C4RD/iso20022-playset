from . import base_types
from ._Algorithm26Code import Algorithm26Code

class Parameter18(base_types._BaseFieldType):

	__slots__ = ["_DgstAlgo"]
	@property
	def DgstAlgo(self):
		return self._DgstAlgo

	@DgstAlgo.setter
	def DgstAlgo(self, value):
		self._DgstAlgo = value if type(value) != base_types.auto else self.make_default("DgstAlgo")

	@DgstAlgo.deleter
	def DgstAlgo(self):
		del self._DgstAlgo
		self._DgstAlgo = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgstAlgo', type=Algorithm26Code, min=0, max=1, mutex_group=None, array=False),
	))

