from . import base_types
from .AcceptedStatusReason7 import AcceptedStatusReason7
from .RejectedStatusReason12 import RejectedStatusReason12
from .ProprietaryStatusAndReason5 import ProprietaryStatusAndReason5
from .PendingProcessingStatusReason1 import PendingProcessingStatusReason1
from .ReceivedStatusReason1 import ReceivedStatusReason1

class ProcessingStatus43Choice(base_types._BaseFieldType):

	__slots__ = ["_Rcvd", "_PdgPrcg", "_PrtrySts", "_Accptd", "_Rjctd"]
	@property
	def Rcvd(self):
		return self._Rcvd

	@Rcvd.setter
	def Rcvd(self, value):
		self._Rcvd = value if type(value) != base_types.auto else self.make_default("Rcvd")

	@Rcvd.deleter
	def Rcvd(self):
		del self._Rcvd
		self._Rcvd = None

	@property
	def PdgPrcg(self):
		return self._PdgPrcg

	@PdgPrcg.setter
	def PdgPrcg(self, value):
		self._PdgPrcg = value if type(value) != base_types.auto else self.make_default("PdgPrcg")

	@PdgPrcg.deleter
	def PdgPrcg(self):
		del self._PdgPrcg
		self._PdgPrcg = None

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
	def Accptd(self):
		return self._Accptd

	@Accptd.setter
	def Accptd(self, value):
		self._Accptd = value if type(value) != base_types.auto else self.make_default("Accptd")

	@Accptd.deleter
	def Accptd(self):
		del self._Accptd
		self._Accptd = None

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
		base_types.FieldEntry(name='Rcvd', type=ReceivedStatusReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPrcg', type=PendingProcessingStatusReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Accptd', type=AcceptedStatusReason7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatusReason12, min=0, max=1, mutex_group=1, array=False),
	))

