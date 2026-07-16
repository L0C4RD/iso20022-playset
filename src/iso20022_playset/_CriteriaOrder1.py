# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max500Text

class CriteriaOrder1(base_types._BaseFieldType):

	__slots__ = ["_Trgt"]
	@property
	def Trgt(self):
		return self._Trgt

	@Trgt.setter
	def Trgt(self, value):
		self._Trgt = value if value is not None else base_types.UninitialisedField(self, 'Trgt', Max500Text, False)

	@Trgt.deleter
	def Trgt(self):
		del self._Trgt
		self._Trgt = base_types.UninitialisedField(self, 'Trgt', Max500Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Trgt', type=Max500Text, min=1, max=1, mutex_group=None, array=False),
	))