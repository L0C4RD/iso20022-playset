from . import base_types
import PendingProcessingStatus16Choice
import RejectionStatus42Choice
import ProprietaryStatusAndReason7
import RepairStatus17Choice
import AcknowledgedAcceptedStatus30Choice
import ModificationStatus5Choice
import DeniedStatus19Choice

class ModificationProcessingStatus11Choice(base_types._BaseFieldType):

	__slots__ = ["_Rprd", "_AckdAccptd", "_Rjctd", "_Prtry", "_Modfd", "_Dnd", "_PdgPrcg"]
	@property
	def Rprd(self):
		return self._Rprd

	@Rprd.setter
	def Rprd(self, value):
		self._Rprd = value if type(value) != auto else self.make_default("Rprd")

	@Rprd.deleter
	def Rprd(self):
		del self._Rprd
		self._Rprd = None

	@property
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if type(value) != auto else self.make_default("AckdAccptd")

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = None

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
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def Modfd(self):
		return self._Modfd

	@Modfd.setter
	def Modfd(self, value):
		self._Modfd = value if type(value) != auto else self.make_default("Modfd")

	@Modfd.deleter
	def Modfd(self):
		del self._Modfd
		self._Modfd = None

	@property
	def Dnd(self):
		return self._Dnd

	@Dnd.setter
	def Dnd(self, value):
		self._Dnd = value if type(value) != auto else self.make_default("Dnd")

	@Dnd.deleter
	def Dnd(self):
		del self._Dnd
		self._Dnd = None

	@property
	def PdgPrcg(self):
		return self._PdgPrcg

	@PdgPrcg.setter
	def PdgPrcg(self, value):
		self._PdgPrcg = value if type(value) != auto else self.make_default("PdgPrcg")

	@PdgPrcg.deleter
	def PdgPrcg(self):
		del self._PdgPrcg
		self._PdgPrcg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rprd', type=RepairStatus17Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus30Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionStatus42Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Modfd', type=ModificationStatus5Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dnd', type=DeniedStatus19Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPrcg', type=PendingProcessingStatus16Choice, min=0, max=1, mutex_group=1, array=False),
	))

