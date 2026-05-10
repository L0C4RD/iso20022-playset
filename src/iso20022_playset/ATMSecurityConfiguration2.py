from . import base_types
from .Number import Number

class ATMSecurityConfiguration2(base_types._BaseFieldType):

	__slots__ = ["_MaxAsmmtrcKey", "_MaxRootKeyLngth", "_MaxRSAKeyLngth", "_MaxSmmtrcKey"]
	@property
	def MaxAsmmtrcKey(self):
		return self._MaxAsmmtrcKey

	@MaxAsmmtrcKey.setter
	def MaxAsmmtrcKey(self, value):
		self._MaxAsmmtrcKey = value if type(value) != auto else self.make_default("MaxAsmmtrcKey")

	@MaxAsmmtrcKey.deleter
	def MaxAsmmtrcKey(self):
		del self._MaxAsmmtrcKey
		self._MaxAsmmtrcKey = None

	@property
	def MaxRootKeyLngth(self):
		return self._MaxRootKeyLngth

	@MaxRootKeyLngth.setter
	def MaxRootKeyLngth(self, value):
		self._MaxRootKeyLngth = value if type(value) != auto else self.make_default("MaxRootKeyLngth")

	@MaxRootKeyLngth.deleter
	def MaxRootKeyLngth(self):
		del self._MaxRootKeyLngth
		self._MaxRootKeyLngth = None

	@property
	def MaxRSAKeyLngth(self):
		return self._MaxRSAKeyLngth

	@MaxRSAKeyLngth.setter
	def MaxRSAKeyLngth(self, value):
		self._MaxRSAKeyLngth = value if type(value) != auto else self.make_default("MaxRSAKeyLngth")

	@MaxRSAKeyLngth.deleter
	def MaxRSAKeyLngth(self):
		del self._MaxRSAKeyLngth
		self._MaxRSAKeyLngth = None

	@property
	def MaxSmmtrcKey(self):
		return self._MaxSmmtrcKey

	@MaxSmmtrcKey.setter
	def MaxSmmtrcKey(self, value):
		self._MaxSmmtrcKey = value if type(value) != auto else self.make_default("MaxSmmtrcKey")

	@MaxSmmtrcKey.deleter
	def MaxSmmtrcKey(self):
		del self._MaxSmmtrcKey
		self._MaxSmmtrcKey = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxAsmmtrcKey', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxRootKeyLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxRSAKeyLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxSmmtrcKey', type=Number, min=0, max=1, mutex_group=None, array=False),
	))

