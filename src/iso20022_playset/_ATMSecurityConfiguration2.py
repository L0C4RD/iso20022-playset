# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Number

class ATMSecurityConfiguration2(base_types._BaseFieldType):

	__slots__ = ["_MaxAsmmtrcKey", "_MaxRSAKeyLngth", "_MaxRootKeyLngth", "_MaxSmmtrcKey"]
	@property
	def MaxAsmmtrcKey(self):
		return self._MaxAsmmtrcKey

	@MaxAsmmtrcKey.setter
	def MaxAsmmtrcKey(self, value):
		self._MaxAsmmtrcKey = value if value is not None else base_types.UninitialisedField(self, 'MaxAsmmtrcKey', Number, False)

	@MaxAsmmtrcKey.deleter
	def MaxAsmmtrcKey(self):
		del self._MaxAsmmtrcKey
		self._MaxAsmmtrcKey = base_types.UninitialisedField(self, 'MaxAsmmtrcKey', Number, False)

	@property
	def MaxRSAKeyLngth(self):
		return self._MaxRSAKeyLngth

	@MaxRSAKeyLngth.setter
	def MaxRSAKeyLngth(self, value):
		self._MaxRSAKeyLngth = value if value is not None else base_types.UninitialisedField(self, 'MaxRSAKeyLngth', Number, False)

	@MaxRSAKeyLngth.deleter
	def MaxRSAKeyLngth(self):
		del self._MaxRSAKeyLngth
		self._MaxRSAKeyLngth = base_types.UninitialisedField(self, 'MaxRSAKeyLngth', Number, False)

	@property
	def MaxRootKeyLngth(self):
		return self._MaxRootKeyLngth

	@MaxRootKeyLngth.setter
	def MaxRootKeyLngth(self, value):
		self._MaxRootKeyLngth = value if value is not None else base_types.UninitialisedField(self, 'MaxRootKeyLngth', Number, False)

	@MaxRootKeyLngth.deleter
	def MaxRootKeyLngth(self):
		del self._MaxRootKeyLngth
		self._MaxRootKeyLngth = base_types.UninitialisedField(self, 'MaxRootKeyLngth', Number, False)

	@property
	def MaxSmmtrcKey(self):
		return self._MaxSmmtrcKey

	@MaxSmmtrcKey.setter
	def MaxSmmtrcKey(self, value):
		self._MaxSmmtrcKey = value if value is not None else base_types.UninitialisedField(self, 'MaxSmmtrcKey', Number, False)

	@MaxSmmtrcKey.deleter
	def MaxSmmtrcKey(self):
		del self._MaxSmmtrcKey
		self._MaxSmmtrcKey = base_types.UninitialisedField(self, 'MaxSmmtrcKey', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxAsmmtrcKey', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxRSAKeyLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxRootKeyLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxSmmtrcKey', type=Number, min=0, max=1, mutex_group=None, array=False),
	))