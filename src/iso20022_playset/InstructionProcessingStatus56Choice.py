from . import base_types
import PendingCancellationStatus13Choice
import NoSpecifiedReason1
import RejectedStatus58Choice
import CancelledStatus12Choice
import ReturnedStatus2Choice
import PendingStatus71Choice

class InstructionProcessingStatus56Choice(base_types._BaseFieldType):

	__slots__ = ["_Cvrd", "_Canc", "_Ucvrd", "_PdgCxl", "_Accptd", "_AccptdForFrthrPrcg", "_Rtrd", "_Rjctd", "_Pdg"]
	@property
	def Cvrd(self):
		return self._Cvrd

	@Cvrd.setter
	def Cvrd(self, value):
		self._Cvrd = value if type(value) != auto else self.make_default("Cvrd")

	@Cvrd.deleter
	def Cvrd(self):
		del self._Cvrd
		self._Cvrd = None

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
	def Ucvrd(self):
		return self._Ucvrd

	@Ucvrd.setter
	def Ucvrd(self, value):
		self._Ucvrd = value if type(value) != auto else self.make_default("Ucvrd")

	@Ucvrd.deleter
	def Ucvrd(self):
		del self._Ucvrd
		self._Ucvrd = None

	@property
	def PdgCxl(self):
		return self._PdgCxl

	@PdgCxl.setter
	def PdgCxl(self, value):
		self._PdgCxl = value if type(value) != auto else self.make_default("PdgCxl")

	@PdgCxl.deleter
	def PdgCxl(self):
		del self._PdgCxl
		self._PdgCxl = None

	@property
	def Accptd(self):
		return self._Accptd

	@Accptd.setter
	def Accptd(self, value):
		self._Accptd = value if type(value) != auto else self.make_default("Accptd")

	@Accptd.deleter
	def Accptd(self):
		del self._Accptd
		self._Accptd = None

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
	def Rtrd(self):
		return self._Rtrd

	@Rtrd.setter
	def Rtrd(self, value):
		self._Rtrd = value if type(value) != auto else self.make_default("Rtrd")

	@Rtrd.deleter
	def Rtrd(self):
		del self._Rtrd
		self._Rtrd = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cvrd', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancelledStatus12Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ucvrd', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgCxl', type=PendingCancellationStatus13Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Accptd', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AccptdForFrthrPrcg', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rtrd', type=ReturnedStatus2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus58Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus71Choice, min=0, max=1, mutex_group=1, array=False),
	))

