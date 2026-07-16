# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ProprietaryReason4
from . import ProprietaryStatusAndReason6

class CollateralStatus3Choice(base_types._BaseFieldType):

	__slots__ = ["_Pdg", "_Prtry"]
	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', ProprietaryReason4, True)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', ProprietaryReason4, True)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', ProprietaryStatusAndReason6, True)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', ProprietaryStatusAndReason6, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pdg', type=ProprietaryReason4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=1, max=None, mutex_group=1, array=True),
	))