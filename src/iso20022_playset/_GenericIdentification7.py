# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Max8Text

class GenericIdentification7(base_types._BaseFieldType):

	__slots__ = ["_Inf", "_Issr"]
	@property
	def Inf(self):
		return self._Inf

	@Inf.setter
	def Inf(self, value):
		self._Inf = value if value is not None else base_types.UninitialisedField(self, 'Inf', Max35Text, False)

	@Inf.deleter
	def Inf(self):
		del self._Inf
		self._Inf = base_types.UninitialisedField(self, 'Inf', Max35Text, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', Max8Text, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', Max8Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Inf', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=Max8Text, min=1, max=1, mutex_group=None, array=False),
	))