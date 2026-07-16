# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OptionParty3Code

class Direction2(base_types._BaseFieldType):

	__slots__ = ["_DrctnOfTheFrstLeg", "_DrctnOfTheScndLeg"]
	@property
	def DrctnOfTheFrstLeg(self):
		return self._DrctnOfTheFrstLeg

	@DrctnOfTheFrstLeg.setter
	def DrctnOfTheFrstLeg(self, value):
		self._DrctnOfTheFrstLeg = value if value is not None else base_types.UninitialisedField(self, 'DrctnOfTheFrstLeg', OptionParty3Code, False)

	@DrctnOfTheFrstLeg.deleter
	def DrctnOfTheFrstLeg(self):
		del self._DrctnOfTheFrstLeg
		self._DrctnOfTheFrstLeg = base_types.UninitialisedField(self, 'DrctnOfTheFrstLeg', OptionParty3Code, False)

	@property
	def DrctnOfTheScndLeg(self):
		return self._DrctnOfTheScndLeg

	@DrctnOfTheScndLeg.setter
	def DrctnOfTheScndLeg(self, value):
		self._DrctnOfTheScndLeg = value if value is not None else base_types.UninitialisedField(self, 'DrctnOfTheScndLeg', OptionParty3Code, False)

	@DrctnOfTheScndLeg.deleter
	def DrctnOfTheScndLeg(self):
		del self._DrctnOfTheScndLeg
		self._DrctnOfTheScndLeg = base_types.UninitialisedField(self, 'DrctnOfTheScndLeg', OptionParty3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DrctnOfTheFrstLeg', type=OptionParty3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctnOfTheScndLeg', type=OptionParty3Code, min=0, max=1, mutex_group=None, array=False),
	))