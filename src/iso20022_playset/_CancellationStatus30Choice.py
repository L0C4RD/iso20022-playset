from . import base_types
from ._PendingStatus56Choice import PendingStatus56Choice
from ._CancellationStatus29Choice import CancellationStatus29Choice
from ._ProprietaryStatusAndReason6 import ProprietaryStatusAndReason6
from ._RejectionStatus34Choice import RejectionStatus34Choice
from ._ProprietaryReason4 import ProprietaryReason4

class CancellationStatus30Choice(base_types._BaseFieldType):

	__slots__ = ["_Pdg", "_Rjctd", "_Canc", "_Prtry", "_Prcd"]
	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if type(value) != base_types.auto else self.make_default("Canc")

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = None

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
	def Prcd(self):
		return self._Prcd

	@Prcd.setter
	def Prcd(self, value):
		self._Prcd = value if type(value) != base_types.auto else self.make_default("Prcd")

	@Prcd.deleter
	def Prcd(self):
		del self._Prcd
		self._Prcd = None

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

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if type(value) != base_types.auto else self.make_default("Rjctd")

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Canc', type=CancellationStatus29Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus56Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prcd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionStatus34Choice, min=0, max=1, mutex_group=1, array=False),
	))

