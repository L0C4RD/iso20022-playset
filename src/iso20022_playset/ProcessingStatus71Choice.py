from . import base_types
from .RejectionOrRepairStatus39Choice import RejectionOrRepairStatus39Choice
from .DeniedStatus16Choice import DeniedStatus16Choice
from .ProprietaryReason4 import ProprietaryReason4
from .PendingStatus38Choice import PendingStatus38Choice
from .AcknowledgedAcceptedStatus21Choice import AcknowledgedAcceptedStatus21Choice
from .ProprietaryStatusAndReason6 import ProprietaryStatusAndReason6
from .RejectionOrRepairStatus40Choice import RejectionOrRepairStatus40Choice

class ProcessingStatus71Choice(base_types._BaseFieldType):

	__slots__ = ["_Rpr", "_Rjctd", "_Prtry", "_Pdg", "_AckdAccptd", "_Dnd", "_Cmpltd"]
	@property
	def Rpr(self):
		return self._Rpr

	@Rpr.setter
	def Rpr(self, value):
		self._Rpr = value if type(value) != base_types.auto else self.make_default("Rpr")

	@Rpr.deleter
	def Rpr(self):
		del self._Rpr
		self._Rpr = None

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
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if type(value) != base_types.auto else self.make_default("AckdAccptd")

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = None

	@property
	def Dnd(self):
		return self._Dnd

	@Dnd.setter
	def Dnd(self, value):
		self._Dnd = value if type(value) != base_types.auto else self.make_default("Dnd")

	@Dnd.deleter
	def Dnd(self):
		del self._Dnd
		self._Dnd = None

	@property
	def Cmpltd(self):
		return self._Cmpltd

	@Cmpltd.setter
	def Cmpltd(self, value):
		self._Cmpltd = value if type(value) != base_types.auto else self.make_default("Cmpltd")

	@Cmpltd.deleter
	def Cmpltd(self):
		del self._Cmpltd
		self._Cmpltd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rpr', type=RejectionOrRepairStatus39Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionOrRepairStatus40Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus38Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus21Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dnd', type=DeniedStatus16Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cmpltd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
	))

