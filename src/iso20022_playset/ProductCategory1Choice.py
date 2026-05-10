import base_types
import GenericIdentification4
import ProductCategory1

class ProductCategory1Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrPdctCtgy", "_StrdPdctCtgy"]
	@property
	def OthrPdctCtgy(self):
		return self._OthrPdctCtgy

	@OthrPdctCtgy.setter
	def OthrPdctCtgy(self, value):
		self._OthrPdctCtgy = value if type(value) != auto else self.make_default("OthrPdctCtgy")

	@OthrPdctCtgy.deleter
	def OthrPdctCtgy(self):
		del self._OthrPdctCtgy
		self._OthrPdctCtgy = None

	@property
	def StrdPdctCtgy(self):
		return self._StrdPdctCtgy

	@StrdPdctCtgy.setter
	def StrdPdctCtgy(self, value):
		self._StrdPdctCtgy = value if type(value) != auto else self.make_default("StrdPdctCtgy")

	@StrdPdctCtgy.deleter
	def StrdPdctCtgy(self):
		del self._StrdPdctCtgy
		self._StrdPdctCtgy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrPdctCtgy', type=GenericIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StrdPdctCtgy', type=ProductCategory1, min=0, max=1, mutex_group=1, array=False),
	))

