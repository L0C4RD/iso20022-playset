# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentificationAndAccount197

class OtherParties46(base_types._BaseFieldType):

	__slots__ = ["_Invstr"]
	@property
	def Invstr(self):
		return self._Invstr

	@Invstr.setter
	def Invstr(self, value):
		self._Invstr = value if value is not None else base_types.UninitialisedField(self, 'Invstr', PartyIdentificationAndAccount197, True)

	@Invstr.deleter
	def Invstr(self):
		del self._Invstr
		self._Invstr = base_types.UninitialisedField(self, 'Invstr', PartyIdentificationAndAccount197, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Invstr', type=PartyIdentificationAndAccount197, min=0, max=None, mutex_group=None, array=True),
	))