# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max500Text import Max500Text

class CriteriaOrder1(base_types._BaseFieldType):

	__slots__ = ["_Trgt"]
	@property
	def Trgt(self):
		return self._Trgt

	@Trgt.setter
	def Trgt(self, value):
		self._Trgt = value if type(value) != base_types.auto else self.make_default("Trgt")

	@Trgt.deleter
	def Trgt(self):
		del self._Trgt
		self._Trgt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Trgt', type=Max500Text, min=1, max=1, mutex_group=None, array=False),
	))