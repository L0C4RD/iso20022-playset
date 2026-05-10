from . import base_types
from .ProductIdentifier2 import ProductIdentifier2
from .GenericIdentification4 import GenericIdentification4

class ProductIdentifier2Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrPdctIdr", "_StrdPdctIdr"]
	@property
	def OthrPdctIdr(self):
		return self._OthrPdctIdr

	@OthrPdctIdr.setter
	def OthrPdctIdr(self, value):
		self._OthrPdctIdr = value if type(value) != auto else self.make_default("OthrPdctIdr")

	@OthrPdctIdr.deleter
	def OthrPdctIdr(self):
		del self._OthrPdctIdr
		self._OthrPdctIdr = None

	@property
	def StrdPdctIdr(self):
		return self._StrdPdctIdr

	@StrdPdctIdr.setter
	def StrdPdctIdr(self, value):
		self._StrdPdctIdr = value if type(value) != auto else self.make_default("StrdPdctIdr")

	@StrdPdctIdr.deleter
	def StrdPdctIdr(self):
		del self._StrdPdctIdr
		self._StrdPdctIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrPdctIdr', type=GenericIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StrdPdctIdr', type=ProductIdentifier2, min=0, max=1, mutex_group=1, array=False),
	))

