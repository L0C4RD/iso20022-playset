# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ProprietaryReason4

class Reason4(base_types._BaseFieldType):

	__slots__ = ["_Rsn"]
	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', ProprietaryReason4, True)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', ProprietaryReason4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rsn', type=ProprietaryReason4, min=0, max=None, mutex_group=None, array=True),
	))