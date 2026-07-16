# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact3NumericText
from . import Exact5NumericText

class Number3Choice(base_types._BaseFieldType):

	__slots__ = ["_Lng", "_Shrt"]
	@property
	def Lng(self):
		return self._Lng

	@Lng.setter
	def Lng(self, value):
		self._Lng = value if value is not None else base_types.UninitialisedField(self, 'Lng', Exact5NumericText, False)

	@Lng.deleter
	def Lng(self):
		del self._Lng
		self._Lng = base_types.UninitialisedField(self, 'Lng', Exact5NumericText, False)

	@property
	def Shrt(self):
		return self._Shrt

	@Shrt.setter
	def Shrt(self, value):
		self._Shrt = value if value is not None else base_types.UninitialisedField(self, 'Shrt', Exact3NumericText, False)

	@Shrt.deleter
	def Shrt(self):
		del self._Shrt
		self._Shrt = base_types.UninitialisedField(self, 'Shrt', Exact3NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lng', type=Exact5NumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Shrt', type=Exact3NumericText, min=0, max=1, mutex_group=1, array=False),
	))