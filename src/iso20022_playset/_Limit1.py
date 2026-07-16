# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max3NumericText

class Limit1(base_types._BaseFieldType):

	__slots__ = ["_Cur", "_Lmt"]
	@property
	def Cur(self):
		return self._Cur

	@Cur.setter
	def Cur(self, value):
		self._Cur = value if value is not None else base_types.UninitialisedField(self, 'Cur', Max3NumericText, False)

	@Cur.deleter
	def Cur(self):
		del self._Cur
		self._Cur = base_types.UninitialisedField(self, 'Cur', Max3NumericText, False)

	@property
	def Lmt(self):
		return self._Lmt

	@Lmt.setter
	def Lmt(self, value):
		self._Lmt = value if value is not None else base_types.UninitialisedField(self, 'Lmt', Max3NumericText, False)

	@Lmt.deleter
	def Lmt(self):
		del self._Lmt
		self._Lmt = base_types.UninitialisedField(self, 'Lmt', Max3NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cur', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lmt', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
	))