# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AffirmationReason2Choice
from . import ProprietaryReason4
from . import ProprietaryStatusAndReason6

class AffirmationStatus11Choice(base_types._BaseFieldType):

	__slots__ = ["_Affrmd", "_PrtrySts", "_Uaffrmd"]
	@property
	def Affrmd(self):
		return self._Affrmd

	@Affrmd.setter
	def Affrmd(self, value):
		self._Affrmd = value if value is not None else base_types.UninitialisedField(self, 'Affrmd', ProprietaryReason4, False)

	@Affrmd.deleter
	def Affrmd(self):
		del self._Affrmd
		self._Affrmd = base_types.UninitialisedField(self, 'Affrmd', ProprietaryReason4, False)

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if value is not None else base_types.UninitialisedField(self, 'PrtrySts', ProprietaryStatusAndReason6, False)

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = base_types.UninitialisedField(self, 'PrtrySts', ProprietaryStatusAndReason6, False)

	@property
	def Uaffrmd(self):
		return self._Uaffrmd

	@Uaffrmd.setter
	def Uaffrmd(self, value):
		self._Uaffrmd = value if value is not None else base_types.UninitialisedField(self, 'Uaffrmd', AffirmationReason2Choice, False)

	@Uaffrmd.deleter
	def Uaffrmd(self):
		del self._Uaffrmd
		self._Uaffrmd = base_types.UninitialisedField(self, 'Uaffrmd', AffirmationReason2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Affrmd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Uaffrmd', type=AffirmationReason2Choice, min=0, max=1, mutex_group=1, array=False),
	))