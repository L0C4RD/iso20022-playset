import base_types
import InRepairStatus4Choice
import ReversedStatus2Choice
import CancelledStatus13Choice
import RejectionReason56
import FailedSettlementStatus2Choice
import CancellationPendingStatus7Choice
import TransferUnmatchedStatus4Choice
import TransferInstructionStatus5
import PendingSettlementStatus3Choice

class TransferStatus5Choice(base_types._BaseFieldType):

	__slots__ = ["_PdgSttlm", "_Sts", "_FaildSttlm", "_Rvsd", "_Rjctd", "_InRpr", "_CxlPdg", "_Canc", "_Umtchd"]
	@property
	def PdgSttlm(self):
		return self._PdgSttlm

	@PdgSttlm.setter
	def PdgSttlm(self, value):
		self._PdgSttlm = value if type(value) != auto else self.make_default("PdgSttlm")

	@PdgSttlm.deleter
	def PdgSttlm(self):
		del self._PdgSttlm
		self._PdgSttlm = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def FaildSttlm(self):
		return self._FaildSttlm

	@FaildSttlm.setter
	def FaildSttlm(self, value):
		self._FaildSttlm = value if type(value) != auto else self.make_default("FaildSttlm")

	@FaildSttlm.deleter
	def FaildSttlm(self):
		del self._FaildSttlm
		self._FaildSttlm = None

	@property
	def Rvsd(self):
		return self._Rvsd

	@Rvsd.setter
	def Rvsd(self, value):
		self._Rvsd = value if type(value) != auto else self.make_default("Rvsd")

	@Rvsd.deleter
	def Rvsd(self):
		del self._Rvsd
		self._Rvsd = None

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
	def InRpr(self):
		return self._InRpr

	@InRpr.setter
	def InRpr(self, value):
		self._InRpr = value if type(value) != auto else self.make_default("InRpr")

	@InRpr.deleter
	def InRpr(self):
		del self._InRpr
		self._InRpr = None

	@property
	def CxlPdg(self):
		return self._CxlPdg

	@CxlPdg.setter
	def CxlPdg(self, value):
		self._CxlPdg = value if type(value) != auto else self.make_default("CxlPdg")

	@CxlPdg.deleter
	def CxlPdg(self):
		del self._CxlPdg
		self._CxlPdg = None

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
	def Umtchd(self):
		return self._Umtchd

	@Umtchd.setter
	def Umtchd(self, value):
		self._Umtchd = value if type(value) != auto else self.make_default("Umtchd")

	@Umtchd.deleter
	def Umtchd(self):
		del self._Umtchd
		self._Umtchd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdgSttlm', type=PendingSettlementStatus3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sts', type=TransferInstructionStatus5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FaildSttlm', type=FailedSettlementStatus2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rvsd', type=ReversedStatus2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionReason56, min=1, max=10, mutex_group=1, array=True),
		base_types.FieldEntry(name='InRpr', type=InRepairStatus4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlPdg', type=CancellationPendingStatus7Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancelledStatus13Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Umtchd', type=TransferUnmatchedStatus4Choice, min=0, max=1, mutex_group=1, array=False),
	))

