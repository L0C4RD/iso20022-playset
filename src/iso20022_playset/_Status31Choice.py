from . import base_types
from ._TransferCancellationPendingStatus1 import TransferCancellationPendingStatus1
from ._CancelledCompleteReason1 import CancelledCompleteReason1
from ._RejectionReason33 import RejectionReason33
from ._TransferCancellationStatus3 import TransferCancellationStatus3

class Status31Choice(base_types._BaseFieldType):

	__slots__ = ["_Rjctd", "_Cmplt", "_Sts", "_Pdg"]
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

	@property
	def Cmplt(self):
		return self._Cmplt

	@Cmplt.setter
	def Cmplt(self, value):
		self._Cmplt = value if type(value) != base_types.auto else self.make_default("Cmplt")

	@Cmplt.deleter
	def Cmplt(self):
		del self._Cmplt
		self._Cmplt = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rjctd', type=RejectionReason33, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cmplt', type=CancelledCompleteReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sts', type=TransferCancellationStatus3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=TransferCancellationPendingStatus1, min=0, max=1, mutex_group=1, array=False),
	))

