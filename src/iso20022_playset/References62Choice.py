from . import base_types
from .AdditionalReference8 import AdditionalReference8

class References62Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrRef", "_PrvsRef"]
	@property
	def OthrRef(self):
		return self._OthrRef

	@OthrRef.setter
	def OthrRef(self, value):
		self._OthrRef = value if type(value) != base_types.auto else self.make_default("OthrRef")

	@OthrRef.deleter
	def OthrRef(self):
		del self._OthrRef
		self._OthrRef = None

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if type(value) != base_types.auto else self.make_default("PrvsRef")

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrRef', type=AdditionalReference8, min=1, max=2, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference8, min=1, max=2, mutex_group=1, array=False),
	))

