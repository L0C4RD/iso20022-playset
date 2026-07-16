# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InstructionProcessingStatus6
from . import PendingStatus70Choice
from . import RejectedStatus55Choice

class InstructionStatus13Choice(base_types._BaseFieldType):

	__slots__ = ["_Pdg", "_PrcgSts", "_Rjctd"]
	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', PendingStatus70Choice, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', PendingStatus70Choice, False)

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if value is not None else base_types.UninitialisedField(self, 'PrcgSts', InstructionProcessingStatus6, False)

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = base_types.UninitialisedField(self, 'PrcgSts', InstructionProcessingStatus6, False)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectedStatus55Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectedStatus55Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pdg', type=PendingStatus70Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrcgSts', type=InstructionProcessingStatus6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus55Choice, min=0, max=1, mutex_group=1, array=False),
	))