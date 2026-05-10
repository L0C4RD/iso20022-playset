import base_types
import Max12Text
import UnderlyingProductIdentifier1Code

class ProductIdentifier3Choice(base_types._BaseFieldType):

	__slots__ = ["_UnqPdctIdr", "_UndrlygPdctIdr"]
	@property
	def UnqPdctIdr(self):
		return self._UnqPdctIdr

	@UnqPdctIdr.setter
	def UnqPdctIdr(self, value):
		self._UnqPdctIdr = value if type(value) != auto else self.make_default("UnqPdctIdr")

	@UnqPdctIdr.deleter
	def UnqPdctIdr(self):
		del self._UnqPdctIdr
		self._UnqPdctIdr = None

	@property
	def UndrlygPdctIdr(self):
		return self._UndrlygPdctIdr

	@UndrlygPdctIdr.setter
	def UndrlygPdctIdr(self, value):
		self._UndrlygPdctIdr = value if type(value) != auto else self.make_default("UndrlygPdctIdr")

	@UndrlygPdctIdr.deleter
	def UndrlygPdctIdr(self):
		del self._UndrlygPdctIdr
		self._UndrlygPdctIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UnqPdctIdr', type=Max12Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UndrlygPdctIdr', type=UnderlyingProductIdentifier1Code, min=0, max=1, mutex_group=1, array=False),
	))

