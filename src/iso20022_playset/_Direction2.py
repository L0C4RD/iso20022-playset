from . import base_types
from ._OptionParty3Code import OptionParty3Code

class Direction2(base_types._BaseFieldType):

	__slots__ = ["_DrctnOfTheFrstLeg", "_DrctnOfTheScndLeg"]
	@property
	def DrctnOfTheFrstLeg(self):
		return self._DrctnOfTheFrstLeg

	@DrctnOfTheFrstLeg.setter
	def DrctnOfTheFrstLeg(self, value):
		self._DrctnOfTheFrstLeg = value if type(value) != base_types.auto else self.make_default("DrctnOfTheFrstLeg")

	@DrctnOfTheFrstLeg.deleter
	def DrctnOfTheFrstLeg(self):
		del self._DrctnOfTheFrstLeg
		self._DrctnOfTheFrstLeg = None

	@property
	def DrctnOfTheScndLeg(self):
		return self._DrctnOfTheScndLeg

	@DrctnOfTheScndLeg.setter
	def DrctnOfTheScndLeg(self, value):
		self._DrctnOfTheScndLeg = value if type(value) != base_types.auto else self.make_default("DrctnOfTheScndLeg")

	@DrctnOfTheScndLeg.deleter
	def DrctnOfTheScndLeg(self):
		del self._DrctnOfTheScndLeg
		self._DrctnOfTheScndLeg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DrctnOfTheFrstLeg', type=OptionParty3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctnOfTheScndLeg', type=OptionParty3Code, min=0, max=1, mutex_group=None, array=False),
	))

