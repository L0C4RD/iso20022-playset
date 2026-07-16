# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AttributeType2Code
from . import Max140Text

class RelativeDistinguishedName2(base_types._BaseFieldType):

	__slots__ = ["_AttrTp", "_AttrVal"]
	@property
	def AttrTp(self):
		return self._AttrTp

	@AttrTp.setter
	def AttrTp(self, value):
		self._AttrTp = value if value is not None else base_types.UninitialisedField(self, 'AttrTp', AttributeType2Code, False)

	@AttrTp.deleter
	def AttrTp(self):
		del self._AttrTp
		self._AttrTp = base_types.UninitialisedField(self, 'AttrTp', AttributeType2Code, False)

	@property
	def AttrVal(self):
		return self._AttrVal

	@AttrVal.setter
	def AttrVal(self, value):
		self._AttrVal = value if value is not None else base_types.UninitialisedField(self, 'AttrVal', Max140Text, False)

	@AttrVal.deleter
	def AttrVal(self):
		del self._AttrVal
		self._AttrVal = base_types.UninitialisedField(self, 'AttrVal', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttrTp', type=AttributeType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttrVal', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))