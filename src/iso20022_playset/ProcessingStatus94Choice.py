import base_types
import AcknowledgedAcceptedStatus25Choice
import RejectionStatus44Choice
import CancellationStatus25Choice
import RepairStatus16Choice
import ProprietaryReason5
import ProprietaryStatusAndReason7
import PendingProcessingStatus19Choice
import PendingStatus46Choice

class ProcessingStatus94Choice(base_types._BaseFieldType):

	__slots__ = ["_PdgPrcg", "_CxlReqd", "_Rjctd", "_Canc", "_Rpr", "_Prtry", "_ModReqd", "_AckdAccptd", "_PdgCxl"]
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

	@property
	def CxlReqd(self):
		return self._CxlReqd

	@CxlReqd.setter
	def CxlReqd(self, value):
		self._CxlReqd = value if type(value) != auto else self.make_default("CxlReqd")

	@CxlReqd.deleter
	def CxlReqd(self):
		del self._CxlReqd
		self._CxlReqd = None

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
	def Rpr(self):
		return self._Rpr

	@Rpr.setter
	def Rpr(self, value):
		self._Rpr = value if type(value) != auto else self.make_default("Rpr")

	@Rpr.deleter
	def Rpr(self):
		del self._Rpr
		self._Rpr = None

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
	def ModReqd(self):
		return self._ModReqd

	@ModReqd.setter
	def ModReqd(self, value):
		self._ModReqd = value if type(value) != auto else self.make_default("ModReqd")

	@ModReqd.deleter
	def ModReqd(self):
		del self._ModReqd
		self._ModReqd = None

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
	def PdgCxl(self):
		return self._PdgCxl

	@PdgCxl.setter
	def PdgCxl(self, value):
		self._PdgCxl = value if type(value) != auto else self.make_default("PdgCxl")

	@PdgCxl.deleter
	def PdgCxl(self):
		del self._PdgCxl
		self._PdgCxl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdgPrcg', type=PendingProcessingStatus19Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlReqd', type=ProprietaryReason5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionStatus44Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancellationStatus25Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rpr', type=RepairStatus16Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ModReqd', type=ProprietaryReason5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus25Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgCxl', type=PendingStatus46Choice, min=0, max=1, mutex_group=1, array=False),
	))

