# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptedStatus8Choice
from . import CancelledStatus12Choice
from . import MatchingStatus34Choice
from . import PendingStatus86Choice
from . import ProprietaryStatusAndReason6
from . import RejectedStatus37Choice

class MarketClaimProcessingStatus2Choice(base_types._BaseFieldType):

	__slots__ = ["_AccptdForFrthrPrcg", "_Canc", "_MtchgSts", "_Pdg", "_PrtrySts", "_Rjctd"]
	@property
	def AccptdForFrthrPrcg(self):
		return self._AccptdForFrthrPrcg

	@AccptdForFrthrPrcg.setter
	def AccptdForFrthrPrcg(self, value):
		self._AccptdForFrthrPrcg = value if value is not None else base_types.UninitialisedField(self, 'AccptdForFrthrPrcg', AcceptedStatus8Choice, False)

	@AccptdForFrthrPrcg.deleter
	def AccptdForFrthrPrcg(self):
		del self._AccptdForFrthrPrcg
		self._AccptdForFrthrPrcg = base_types.UninitialisedField(self, 'AccptdForFrthrPrcg', AcceptedStatus8Choice, False)

	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if value is not None else base_types.UninitialisedField(self, 'Canc', CancelledStatus12Choice, False)

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = base_types.UninitialisedField(self, 'Canc', CancelledStatus12Choice, False)

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if value is not None else base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus34Choice, False)

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus34Choice, False)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', PendingStatus86Choice, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', PendingStatus86Choice, False)

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
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectedStatus37Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectedStatus37Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdForFrthrPrcg', type=AcceptedStatus8Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancelledStatus12Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus34Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus86Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus37Choice, min=0, max=1, mutex_group=1, array=False),
	))