from . import base_types
from ._RepairStatus16Choice import RepairStatus16Choice
from ._CancellationStatus25Choice import CancellationStatus25Choice
from ._PendingProcessingStatus19Choice import PendingProcessingStatus19Choice
from ._GeneratedStatus8Choice import GeneratedStatus8Choice
from ._PendingStatus46Choice import PendingStatus46Choice
from ._ProprietaryReason5 import ProprietaryReason5
from ._AcknowledgedAcceptedStatus25Choice import AcknowledgedAcceptedStatus25Choice

class InstructionProcessingStatus45Choice(base_types._BaseFieldType):

	__slots__ = ["_PdgCxl", "_AckdAccptd", "_Gnrtd", "_CxlReqd", "_ModReqd", "_Canc", "_Rpr", "_PdgPrcg"]
	@property
	def PdgCxl(self):
		return self._PdgCxl

	@PdgCxl.setter
	def PdgCxl(self, value):
		self._PdgCxl = value if type(value) != base_types.auto else self.make_default("PdgCxl")

	@PdgCxl.deleter
	def PdgCxl(self):
		del self._PdgCxl
		self._PdgCxl = None

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
	def Gnrtd(self):
		return self._Gnrtd

	@Gnrtd.setter
	def Gnrtd(self, value):
		self._Gnrtd = value if type(value) != base_types.auto else self.make_default("Gnrtd")

	@Gnrtd.deleter
	def Gnrtd(self):
		del self._Gnrtd
		self._Gnrtd = None

	@property
	def CxlReqd(self):
		return self._CxlReqd

	@CxlReqd.setter
	def CxlReqd(self, value):
		self._CxlReqd = value if type(value) != base_types.auto else self.make_default("CxlReqd")

	@CxlReqd.deleter
	def CxlReqd(self):
		del self._CxlReqd
		self._CxlReqd = None

	@property
	def ModReqd(self):
		return self._ModReqd

	@ModReqd.setter
	def ModReqd(self, value):
		self._ModReqd = value if type(value) != base_types.auto else self.make_default("ModReqd")

	@ModReqd.deleter
	def ModReqd(self):
		del self._ModReqd
		self._ModReqd = None

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
	def PdgPrcg(self):
		return self._PdgPrcg

	@PdgPrcg.setter
	def PdgPrcg(self, value):
		self._PdgPrcg = value if type(value) != base_types.auto else self.make_default("PdgPrcg")

	@PdgPrcg.deleter
	def PdgPrcg(self):
		del self._PdgPrcg
		self._PdgPrcg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdgCxl', type=PendingStatus46Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus25Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Gnrtd', type=GeneratedStatus8Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlReqd', type=ProprietaryReason5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ModReqd', type=ProprietaryReason5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancellationStatus25Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rpr', type=RepairStatus16Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPrcg', type=PendingProcessingStatus19Choice, min=0, max=1, mutex_group=1, array=False),
	))

