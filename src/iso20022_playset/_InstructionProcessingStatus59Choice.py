# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NoReasonCode
from . import PendingStatus78Choice
from . import ProprietaryStatusAndReason6
from . import RejectedStatus63Choice

class InstructionProcessingStatus59Choice(base_types._BaseFieldType):

	__slots__ = ["_AccptdAndConfd", "_Pdg", "_PrtrySts", "_Rjctd"]
	@property
	def AccptdAndConfd(self):
		return self._AccptdAndConfd

	@AccptdAndConfd.setter
	def AccptdAndConfd(self, value):
		self._AccptdAndConfd = value if value is not None else base_types.UninitialisedField(self, 'AccptdAndConfd', NoReasonCode, False)

	@AccptdAndConfd.deleter
	def AccptdAndConfd(self):
		del self._AccptdAndConfd
		self._AccptdAndConfd = base_types.UninitialisedField(self, 'AccptdAndConfd', NoReasonCode, False)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', PendingStatus78Choice, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', PendingStatus78Choice, False)

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
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectedStatus63Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectedStatus63Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdAndConfd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus78Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus63Choice, min=0, max=1, mutex_group=1, array=False),
	))