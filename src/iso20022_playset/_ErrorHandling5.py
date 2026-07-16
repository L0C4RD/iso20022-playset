# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling3Choice
from . import Max140Text

class ErrorHandling5(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_Err"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@property
	def Err(self):
		return self._Err

	@Err.setter
	def Err(self, value):
		self._Err = value if value is not None else base_types.UninitialisedField(self, 'Err', ErrorHandling3Choice, False)

	@Err.deleter
	def Err(self):
		del self._Err
		self._Err = base_types.UninitialisedField(self, 'Err', ErrorHandling3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Err', type=ErrorHandling3Choice, min=1, max=1, mutex_group=None, array=False),
	))