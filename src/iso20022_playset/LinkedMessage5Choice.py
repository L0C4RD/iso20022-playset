from . import base_types
from .AdditionalReference13 import AdditionalReference13

class LinkedMessage5Choice(base_types._BaseFieldType):

	__slots__ = ["_PrvsRef", "_OthrRef"]
	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if type(value) != auto else self.make_default("PrvsRef")

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = None

	@property
	def OthrRef(self):
		return self._OthrRef

	@OthrRef.setter
	def OthrRef(self, value):
		self._OthrRef = value if type(value) != auto else self.make_default("OthrRef")

	@OthrRef.deleter
	def OthrRef(self):
		del self._OthrRef
		self._OthrRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrRef', type=AdditionalReference13, min=0, max=1, mutex_group=1, array=False),
	))

