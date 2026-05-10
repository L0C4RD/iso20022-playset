from . import base_types
from ._MultimodalTransport3 import MultimodalTransport3
from ._SingleTransport8 import SingleTransport8

class TransportMeans6(base_types._BaseFieldType):

	__slots__ = ["_MltmdlTrnsprt", "_IndvTrnsprt"]
	@property
	def MltmdlTrnsprt(self):
		return self._MltmdlTrnsprt

	@MltmdlTrnsprt.setter
	def MltmdlTrnsprt(self, value):
		self._MltmdlTrnsprt = value if type(value) != base_types.auto else self.make_default("MltmdlTrnsprt")

	@MltmdlTrnsprt.deleter
	def MltmdlTrnsprt(self):
		del self._MltmdlTrnsprt
		self._MltmdlTrnsprt = None

	@property
	def IndvTrnsprt(self):
		return self._IndvTrnsprt

	@IndvTrnsprt.setter
	def IndvTrnsprt(self, value):
		self._IndvTrnsprt = value if type(value) != base_types.auto else self.make_default("IndvTrnsprt")

	@IndvTrnsprt.deleter
	def IndvTrnsprt(self):
		del self._IndvTrnsprt
		self._IndvTrnsprt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MltmdlTrnsprt', type=MultimodalTransport3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvTrnsprt', type=SingleTransport8, min=1, max=1, mutex_group=None, array=False),
	))

