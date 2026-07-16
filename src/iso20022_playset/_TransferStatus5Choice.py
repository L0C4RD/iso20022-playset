# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationPendingStatus7Choice
from . import CancelledStatus13Choice
from . import FailedSettlementStatus2Choice
from . import InRepairStatus4Choice
from . import PendingSettlementStatus3Choice
from . import RejectionReason56
from . import ReversedStatus2Choice
from . import TransferInstructionStatus5
from . import TransferUnmatchedStatus4Choice

class TransferStatus5Choice(base_types._BaseFieldType):

	__slots__ = ["_Canc", "_CxlPdg", "_FaildSttlm", "_InRpr", "_PdgSttlm", "_Rjctd", "_Rvsd", "_Sts", "_Umtchd"]
	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if value is not None else base_types.UninitialisedField(self, 'Canc', CancelledStatus13Choice, False)

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = base_types.UninitialisedField(self, 'Canc', CancelledStatus13Choice, False)

	@property
	def CxlPdg(self):
		return self._CxlPdg

	@CxlPdg.setter
	def CxlPdg(self, value):
		self._CxlPdg = value if value is not None else base_types.UninitialisedField(self, 'CxlPdg', CancellationPendingStatus7Choice, False)

	@CxlPdg.deleter
	def CxlPdg(self):
		del self._CxlPdg
		self._CxlPdg = base_types.UninitialisedField(self, 'CxlPdg', CancellationPendingStatus7Choice, False)

	@property
	def FaildSttlm(self):
		return self._FaildSttlm

	@FaildSttlm.setter
	def FaildSttlm(self, value):
		self._FaildSttlm = value if value is not None else base_types.UninitialisedField(self, 'FaildSttlm', FailedSettlementStatus2Choice, False)

	@FaildSttlm.deleter
	def FaildSttlm(self):
		del self._FaildSttlm
		self._FaildSttlm = base_types.UninitialisedField(self, 'FaildSttlm', FailedSettlementStatus2Choice, False)

	@property
	def InRpr(self):
		return self._InRpr

	@InRpr.setter
	def InRpr(self, value):
		self._InRpr = value if value is not None else base_types.UninitialisedField(self, 'InRpr', InRepairStatus4Choice, False)

	@InRpr.deleter
	def InRpr(self):
		del self._InRpr
		self._InRpr = base_types.UninitialisedField(self, 'InRpr', InRepairStatus4Choice, False)

	@property
	def PdgSttlm(self):
		return self._PdgSttlm

	@PdgSttlm.setter
	def PdgSttlm(self, value):
		self._PdgSttlm = value if value is not None else base_types.UninitialisedField(self, 'PdgSttlm', PendingSettlementStatus3Choice, False)

	@PdgSttlm.deleter
	def PdgSttlm(self):
		del self._PdgSttlm
		self._PdgSttlm = base_types.UninitialisedField(self, 'PdgSttlm', PendingSettlementStatus3Choice, False)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectionReason56, True)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectionReason56, True)

	@property
	def Rvsd(self):
		return self._Rvsd

	@Rvsd.setter
	def Rvsd(self, value):
		self._Rvsd = value if value is not None else base_types.UninitialisedField(self, 'Rvsd', ReversedStatus2Choice, False)

	@Rvsd.deleter
	def Rvsd(self):
		del self._Rvsd
		self._Rvsd = base_types.UninitialisedField(self, 'Rvsd', ReversedStatus2Choice, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', TransferInstructionStatus5, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', TransferInstructionStatus5, False)

	@property
	def Umtchd(self):
		return self._Umtchd

	@Umtchd.setter
	def Umtchd(self, value):
		self._Umtchd = value if value is not None else base_types.UninitialisedField(self, 'Umtchd', TransferUnmatchedStatus4Choice, False)

	@Umtchd.deleter
	def Umtchd(self):
		del self._Umtchd
		self._Umtchd = base_types.UninitialisedField(self, 'Umtchd', TransferUnmatchedStatus4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Canc', type=CancelledStatus13Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlPdg', type=CancellationPendingStatus7Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FaildSttlm', type=FailedSettlementStatus2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InRpr', type=InRepairStatus4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgSttlm', type=PendingSettlementStatus3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionReason56, min=1, max=10, mutex_group=1, array=True),
		base_types.FieldEntry(name='Rvsd', type=ReversedStatus2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sts', type=TransferInstructionStatus5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Umtchd', type=TransferUnmatchedStatus4Choice, min=0, max=1, mutex_group=1, array=False),
	))