from . import base_types
from ._InstructionProcessingStatus6 import InstructionProcessingStatus6
from ._PendingStatus84Choice import PendingStatus84Choice
from ._RejectedStatus66Choice import RejectedStatus66Choice

class InstructionStatus14Choice(base_types._BaseFieldType):

	__slots__ = ["_Pdg", "_PrcgSts", "_Rjctd"]
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
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != base_types.auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

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
		base_types.FieldEntry(name='Pdg', type=PendingStatus84Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrcgSts', type=InstructionProcessingStatus6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus66Choice, min=0, max=1, mutex_group=1, array=False),
	))

