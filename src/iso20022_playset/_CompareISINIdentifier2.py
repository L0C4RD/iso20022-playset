# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISINOct2015Identifier

class CompareISINIdentifier2(base_types._BaseFieldType):

	__slots__ = ["_Val1", "_Val2"]
	@property
	def Val1(self):
		return self._Val1

	@Val1.setter
	def Val1(self, value):
		self._Val1 = value if value is not None else base_types.UninitialisedField(self, 'Val1', ISINOct2015Identifier, False)

	@Val1.deleter
	def Val1(self):
		del self._Val1
		self._Val1 = base_types.UninitialisedField(self, 'Val1', ISINOct2015Identifier, False)

	@property
	def Val2(self):
		return self._Val2

	@Val2.setter
	def Val2(self, value):
		self._Val2 = value if value is not None else base_types.UninitialisedField(self, 'Val2', ISINOct2015Identifier, False)

	@Val2.deleter
	def Val2(self):
		del self._Val2
		self._Val2 = base_types.UninitialisedField(self, 'Val2', ISINOct2015Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Val1', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val2', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
	))