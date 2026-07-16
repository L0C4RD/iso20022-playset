# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcknowledgementReason16Choice
from . import AcknowledgementReason18Choice
from . import CancellationReason30Choice
from . import DeniedReason23Choice
from . import FailingReason15Choice
from . import GeneratedReasons6Choice
from . import PendingCancellationReasons5Choice
from . import PendingProcessingReason13Choice
from . import PendingReason37Choice
from . import PendingReason47Choice
from . import RejectionReason51Choice
from . import RepairReason18Choice
from . import UnmatchedReason29Choice

class Reason20Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptdRsn", "_CxlRsn", "_DndRsn", "_FlngRsn", "_GnrtdRsn", "_PdgCxlRsn", "_PdgModRsn", "_PdgPrcgRsn", "_PdgRsn", "_RepoCallAckRsn", "_RjctnRsn", "_RprRsn", "_UmtchdRsn"]
	@property
	def AckdAccptdRsn(self):
		return self._AckdAccptdRsn

	@AckdAccptdRsn.setter
	def AckdAccptdRsn(self, value):
		self._AckdAccptdRsn = value if value is not None else base_types.UninitialisedField(self, 'AckdAccptdRsn', AcknowledgementReason16Choice, False)

	@AckdAccptdRsn.deleter
	def AckdAccptdRsn(self):
		del self._AckdAccptdRsn
		self._AckdAccptdRsn = base_types.UninitialisedField(self, 'AckdAccptdRsn', AcknowledgementReason16Choice, False)

	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if value is not None else base_types.UninitialisedField(self, 'CxlRsn', CancellationReason30Choice, False)

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = base_types.UninitialisedField(self, 'CxlRsn', CancellationReason30Choice, False)

	@property
	def DndRsn(self):
		return self._DndRsn

	@DndRsn.setter
	def DndRsn(self, value):
		self._DndRsn = value if value is not None else base_types.UninitialisedField(self, 'DndRsn', DeniedReason23Choice, False)

	@DndRsn.deleter
	def DndRsn(self):
		del self._DndRsn
		self._DndRsn = base_types.UninitialisedField(self, 'DndRsn', DeniedReason23Choice, False)

	@property
	def FlngRsn(self):
		return self._FlngRsn

	@FlngRsn.setter
	def FlngRsn(self, value):
		self._FlngRsn = value if value is not None else base_types.UninitialisedField(self, 'FlngRsn', FailingReason15Choice, False)

	@FlngRsn.deleter
	def FlngRsn(self):
		del self._FlngRsn
		self._FlngRsn = base_types.UninitialisedField(self, 'FlngRsn', FailingReason15Choice, False)

	@property
	def GnrtdRsn(self):
		return self._GnrtdRsn

	@GnrtdRsn.setter
	def GnrtdRsn(self, value):
		self._GnrtdRsn = value if value is not None else base_types.UninitialisedField(self, 'GnrtdRsn', GeneratedReasons6Choice, False)

	@GnrtdRsn.deleter
	def GnrtdRsn(self):
		del self._GnrtdRsn
		self._GnrtdRsn = base_types.UninitialisedField(self, 'GnrtdRsn', GeneratedReasons6Choice, False)

	@property
	def PdgCxlRsn(self):
		return self._PdgCxlRsn

	@PdgCxlRsn.setter
	def PdgCxlRsn(self, value):
		self._PdgCxlRsn = value if value is not None else base_types.UninitialisedField(self, 'PdgCxlRsn', PendingCancellationReasons5Choice, False)

	@PdgCxlRsn.deleter
	def PdgCxlRsn(self):
		del self._PdgCxlRsn
		self._PdgCxlRsn = base_types.UninitialisedField(self, 'PdgCxlRsn', PendingCancellationReasons5Choice, False)

	@property
	def PdgModRsn(self):
		return self._PdgModRsn

	@PdgModRsn.setter
	def PdgModRsn(self, value):
		self._PdgModRsn = value if value is not None else base_types.UninitialisedField(self, 'PdgModRsn', PendingReason37Choice, False)

	@PdgModRsn.deleter
	def PdgModRsn(self):
		del self._PdgModRsn
		self._PdgModRsn = base_types.UninitialisedField(self, 'PdgModRsn', PendingReason37Choice, False)

	@property
	def PdgPrcgRsn(self):
		return self._PdgPrcgRsn

	@PdgPrcgRsn.setter
	def PdgPrcgRsn(self, value):
		self._PdgPrcgRsn = value if value is not None else base_types.UninitialisedField(self, 'PdgPrcgRsn', PendingProcessingReason13Choice, False)

	@PdgPrcgRsn.deleter
	def PdgPrcgRsn(self):
		del self._PdgPrcgRsn
		self._PdgPrcgRsn = base_types.UninitialisedField(self, 'PdgPrcgRsn', PendingProcessingReason13Choice, False)

	@property
	def PdgRsn(self):
		return self._PdgRsn

	@PdgRsn.setter
	def PdgRsn(self, value):
		self._PdgRsn = value if value is not None else base_types.UninitialisedField(self, 'PdgRsn', PendingReason47Choice, False)

	@PdgRsn.deleter
	def PdgRsn(self):
		del self._PdgRsn
		self._PdgRsn = base_types.UninitialisedField(self, 'PdgRsn', PendingReason47Choice, False)

	@property
	def RepoCallAckRsn(self):
		return self._RepoCallAckRsn

	@RepoCallAckRsn.setter
	def RepoCallAckRsn(self, value):
		self._RepoCallAckRsn = value if value is not None else base_types.UninitialisedField(self, 'RepoCallAckRsn', AcknowledgementReason18Choice, False)

	@RepoCallAckRsn.deleter
	def RepoCallAckRsn(self):
		del self._RepoCallAckRsn
		self._RepoCallAckRsn = base_types.UninitialisedField(self, 'RepoCallAckRsn', AcknowledgementReason18Choice, False)

	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctnRsn', RejectionReason51Choice, False)

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = base_types.UninitialisedField(self, 'RjctnRsn', RejectionReason51Choice, False)

	@property
	def RprRsn(self):
		return self._RprRsn

	@RprRsn.setter
	def RprRsn(self, value):
		self._RprRsn = value if value is not None else base_types.UninitialisedField(self, 'RprRsn', RepairReason18Choice, False)

	@RprRsn.deleter
	def RprRsn(self):
		del self._RprRsn
		self._RprRsn = base_types.UninitialisedField(self, 'RprRsn', RepairReason18Choice, False)

	@property
	def UmtchdRsn(self):
		return self._UmtchdRsn

	@UmtchdRsn.setter
	def UmtchdRsn(self, value):
		self._UmtchdRsn = value if value is not None else base_types.UninitialisedField(self, 'UmtchdRsn', UnmatchedReason29Choice, False)

	@UmtchdRsn.deleter
	def UmtchdRsn(self):
		del self._UmtchdRsn
		self._UmtchdRsn = base_types.UninitialisedField(self, 'UmtchdRsn', UnmatchedReason29Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdAccptdRsn', type=AcknowledgementReason16Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlRsn', type=CancellationReason30Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DndRsn', type=DeniedReason23Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FlngRsn', type=FailingReason15Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='GnrtdRsn', type=GeneratedReasons6Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgCxlRsn', type=PendingCancellationReasons5Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgModRsn', type=PendingReason37Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPrcgRsn', type=PendingProcessingReason13Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgRsn', type=PendingReason47Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RepoCallAckRsn', type=AcknowledgementReason18Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=RejectionReason51Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RprRsn', type=RepairReason18Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UmtchdRsn', type=UnmatchedReason29Choice, min=0, max=1, mutex_group=1, array=False),
	))