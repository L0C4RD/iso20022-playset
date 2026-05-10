from . import base_types
from .Max140Text import Max140Text
from .AttributeType2Code import AttributeType2Code

class RelativeDistinguishedName2(base_types._BaseFieldType):

	__slots__ = ["_AttrVal", "_AttrTp"]
	@property
	def AttrVal(self):
		return self._AttrVal

	@AttrVal.setter
	def AttrVal(self, value):
		self._AttrVal = value if type(value) != base_types.auto else self.make_default("AttrVal")

	@AttrVal.deleter
	def AttrVal(self):
		del self._AttrVal
		self._AttrVal = None

	@property
	def AttrTp(self):
		return self._AttrTp

	@AttrTp.setter
	def AttrTp(self, value):
		self._AttrTp = value if type(value) != base_types.auto else self.make_default("AttrTp")

	@AttrTp.deleter
	def AttrTp(self):
		del self._AttrTp
		self._AttrTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttrVal', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttrTp', type=AttributeType2Code, min=1, max=1, mutex_group=None, array=False),
	))

