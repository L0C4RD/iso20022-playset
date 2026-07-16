# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max256Text

class AdditionalInformation5(base_types._BaseFieldType):

	__slots__ = ["_Inf"]
	@property
	def Inf(self):
		return self._Inf

	@Inf.setter
	def Inf(self, value):
		self._Inf = value if value is not None else base_types.UninitialisedField(self, 'Inf', Max256Text, True)

	@Inf.deleter
	def Inf(self):
		del self._Inf
		self._Inf = base_types.UninitialisedField(self, 'Inf', Max256Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Inf', type=Max256Text, min=1, max=None, mutex_group=None, array=True),
	))