from . import base_types
import AcceptedStatus8Choice
import RejectedStatus37Choice
import ProprietaryStatusAndReason6
import MatchingStatus34Choice
import CancelledStatus12Choice
import PendingStatus63Choice

class MarketClaimProcessingStatus1Choice(base_types._BaseFieldType):

	__slots__ = ["_Canc", "_PrtrySts", "_MtchgSts", "_Pdg", "_AccptdForFrthrPrcg", "_Rjctd"]
	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if type(value) != auto else self.make_default("Canc")

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = None

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if type(value) != auto else self.make_default("PrtrySts")

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = None

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if type(value) != auto else self.make_default("MtchgSts")

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = None

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if type(value) != auto else self.make_default("Pdg")

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = None

	@property
	def AccptdForFrthrPrcg(self):
		return self._AccptdForFrthrPrcg

	@AccptdForFrthrPrcg.setter
	def AccptdForFrthrPrcg(self, value):
		self._AccptdForFrthrPrcg = value if type(value) != auto else self.make_default("AccptdForFrthrPrcg")

	@AccptdForFrthrPrcg.deleter
	def AccptdForFrthrPrcg(self):
		del self._AccptdForFrthrPrcg
		self._AccptdForFrthrPrcg = None

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if type(value) != auto else self.make_default("Rjctd")

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Canc', type=CancelledStatus12Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus34Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus63Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AccptdForFrthrPrcg', type=AcceptedStatus8Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus37Choice, min=0, max=1, mutex_group=1, array=False),
	))

