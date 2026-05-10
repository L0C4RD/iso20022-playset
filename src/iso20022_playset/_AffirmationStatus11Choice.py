from . import base_types
from ._AffirmationReason2Choice import AffirmationReason2Choice
from ._ProprietaryReason4 import ProprietaryReason4
from ._ProprietaryStatusAndReason6 import ProprietaryStatusAndReason6

class AffirmationStatus11Choice(base_types._BaseFieldType):

	__slots__ = ["_Affrmd", "_PrtrySts", "_Uaffrmd"]
	@property
	def Affrmd(self):
		return self._Affrmd

	@Affrmd.setter
	def Affrmd(self, value):
		self._Affrmd = value if type(value) != base_types.auto else self.make_default("Affrmd")

	@Affrmd.deleter
	def Affrmd(self):
		del self._Affrmd
		self._Affrmd = None

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if type(value) != base_types.auto else self.make_default("PrtrySts")

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = None

	@property
	def Uaffrmd(self):
		return self._Uaffrmd

	@Uaffrmd.setter
	def Uaffrmd(self, value):
		self._Uaffrmd = value if type(value) != base_types.auto else self.make_default("Uaffrmd")

	@Uaffrmd.deleter
	def Uaffrmd(self):
		del self._Uaffrmd
		self._Uaffrmd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Affrmd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Uaffrmd', type=AffirmationReason2Choice, min=0, max=1, mutex_group=1, array=False),
	))

