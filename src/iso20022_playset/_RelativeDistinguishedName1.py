# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AttributeType1Code import AttributeType1Code
from ._Max140Text import Max140Text

class RelativeDistinguishedName1(base_types._BaseFieldType):

	__slots__ = ["_AttrTp", "_AttrVal"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttrTp', type=AttributeType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttrVal', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))