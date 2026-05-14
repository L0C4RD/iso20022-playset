# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ProprietaryReason4 import ProprietaryReason4
from ._ProprietaryStatusAndReason6 import ProprietaryStatusAndReason6

class CollateralStatus3Choice(base_types._BaseFieldType):

	__slots__ = ["_Pdg", "_Prtry"]
	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if type(value) != base_types.auto else self.make_default("Pdg")

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pdg', type=ProprietaryReason4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=1, max=None, mutex_group=1, array=True),
	))