# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FailingStatus10Choice
from . import PendingStatus40Choice
from . import ProprietaryStatusAndReason6

class SettlementStatus18Choice(base_types._BaseFieldType):

	__slots__ = ["_Flng", "_Pdg", "_Prtry"]
	@property
	def Flng(self):
		return self._Flng

	@Flng.setter
	def Flng(self, value):
		self._Flng = value if value is not None else base_types.UninitialisedField(self, 'Flng', FailingStatus10Choice, False)

	@Flng.deleter
	def Flng(self):
		del self._Flng
		self._Flng = base_types.UninitialisedField(self, 'Flng', FailingStatus10Choice, False)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', PendingStatus40Choice, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', PendingStatus40Choice, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', ProprietaryStatusAndReason6, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', ProprietaryStatusAndReason6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Flng', type=FailingStatus10Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus40Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
	))