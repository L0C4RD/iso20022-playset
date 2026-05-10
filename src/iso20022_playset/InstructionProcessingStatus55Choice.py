from . import base_types
from .NoSpecifiedReason1 import NoSpecifiedReason1
from .ReturnedStatus2Choice import ReturnedStatus2Choice
from .AcceptedStatus2 import AcceptedStatus2
from .RejectedStatus11 import RejectedStatus11
from .PendingStatus1 import PendingStatus1
from .CancelledStatus5 import CancelledStatus5
from .ProprietaryStatusAndReason6 import ProprietaryStatusAndReason6

class InstructionProcessingStatus55Choice(base_types._BaseFieldType):

	__slots__ = ["_RcvdByIssrOrOfferr", "_StgInstr", "_Pdg", "_DfltActn", "_Canc", "_Fwdd", "_AccptdForFrthrPrcg", "_PrtrySts", "_Rtrd", "_Rjctd"]
	@property
	def RcvdByIssrOrOfferr(self):
		return self._RcvdByIssrOrOfferr

	@RcvdByIssrOrOfferr.setter
	def RcvdByIssrOrOfferr(self, value):
		self._RcvdByIssrOrOfferr = value if type(value) != base_types.auto else self.make_default("RcvdByIssrOrOfferr")

	@RcvdByIssrOrOfferr.deleter
	def RcvdByIssrOrOfferr(self):
		del self._RcvdByIssrOrOfferr
		self._RcvdByIssrOrOfferr = None

	@property
	def StgInstr(self):
		return self._StgInstr

	@StgInstr.setter
	def StgInstr(self, value):
		self._StgInstr = value if type(value) != base_types.auto else self.make_default("StgInstr")

	@StgInstr.deleter
	def StgInstr(self):
		del self._StgInstr
		self._StgInstr = None

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
	def DfltActn(self):
		return self._DfltActn

	@DfltActn.setter
	def DfltActn(self, value):
		self._DfltActn = value if type(value) != base_types.auto else self.make_default("DfltActn")

	@DfltActn.deleter
	def DfltActn(self):
		del self._DfltActn
		self._DfltActn = None

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
	def Fwdd(self):
		return self._Fwdd

	@Fwdd.setter
	def Fwdd(self, value):
		self._Fwdd = value if type(value) != base_types.auto else self.make_default("Fwdd")

	@Fwdd.deleter
	def Fwdd(self):
		del self._Fwdd
		self._Fwdd = None

	@property
	def AccptdForFrthrPrcg(self):
		return self._AccptdForFrthrPrcg

	@AccptdForFrthrPrcg.setter
	def AccptdForFrthrPrcg(self, value):
		self._AccptdForFrthrPrcg = value if type(value) != base_types.auto else self.make_default("AccptdForFrthrPrcg")

	@AccptdForFrthrPrcg.deleter
	def AccptdForFrthrPrcg(self):
		del self._AccptdForFrthrPrcg
		self._AccptdForFrthrPrcg = None

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if type(value) != base_types.auto else self.make_default("PrtrySts")

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = None

	@property
	def Rtrd(self):
		return self._Rtrd

	@Rtrd.setter
	def Rtrd(self, value):
		self._Rtrd = value if type(value) != base_types.auto else self.make_default("Rtrd")

	@Rtrd.deleter
	def Rtrd(self):
		del self._Rtrd
		self._Rtrd = None

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
		base_types.FieldEntry(name='RcvdByIssrOrOfferr', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StgInstr', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DfltActn', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancelledStatus5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Fwdd', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AccptdForFrthrPrcg', type=AcceptedStatus2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rtrd', type=ReturnedStatus2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus11, min=0, max=1, mutex_group=1, array=False),
	))

