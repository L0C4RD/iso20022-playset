# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import Max35Text

class UserDefinedInformation1(base_types._BaseFieldType):

	__slots__ = ["_Inf", "_Labl"]
	@property
	def Inf(self):
		return self._Inf

	@Inf.setter
	def Inf(self, value):
		self._Inf = value if value is not None else base_types.UninitialisedField(self, 'Inf', Max140Text, False)

	@Inf.deleter
	def Inf(self):
		del self._Inf
		self._Inf = base_types.UninitialisedField(self, 'Inf', Max140Text, False)

	@property
	def Labl(self):
		return self._Labl

	@Labl.setter
	def Labl(self, value):
		self._Labl = value if value is not None else base_types.UninitialisedField(self, 'Labl', Max35Text, False)

	@Labl.deleter
	def Labl(self):
		del self._Labl
		self._Labl = base_types.UninitialisedField(self, 'Labl', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Inf', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Labl', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))