# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcknowledgementReason12Choice
from . import AcknowledgementReason13Choice
from . import CancellationReason20Choice
from . import DeniedReason14Choice
from . import FailingReason9Choice
from . import GeneratedReasons5Choice
from . import PendingCancellationReasons6Choice
from . import PendingProcessingReason20Choice
from . import PendingReason28Choice
from . import PendingReason78Choice
from . import RejectionReason45Choice
from . import RepairReason11Choice
from . import UnmatchedReason22Choice

class Reason21Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptdRsn", "_CxlRsn", "_DndRsn", "_FlngRsn", "_GnrtdRsn", "_PdgCxlRsn", "_PdgModRsn", "_PdgPrcgRsn", "_PdgRsn", "_RepoCallAckRsn", "_RjctnRsn", "_RprRsn", "_UmtchdRsn"]
	@property
	def AckdAccptdRsn(self):
		return self._AckdAccptdRsn

	@AckdAccptdRsn.setter
	def AckdAccptdRsn(self, value):
		self._AckdAccptdRsn = value if value is not None else base_types.UninitialisedField(self, 'AckdAccptdRsn', AcknowledgementReason12Choice, False)

	@AckdAccptdRsn.deleter
	def AckdAccptdRsn(self):
		del self._AckdAccptdRsn
		self._AckdAccptdRsn = base_types.UninitialisedField(self, 'AckdAccptdRsn', AcknowledgementReason12Choice, False)

	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if value is not None else base_types.UninitialisedField(self, 'CxlRsn', CancellationReason20Choice, False)

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = base_types.UninitialisedField(self, 'CxlRsn', CancellationReason20Choice, False)

	@property
	def DndRsn(self):
		return self._DndRsn

	@DndRsn.setter
	def DndRsn(self, value):
		self._DndRsn = value if value is not None else base_types.UninitialisedField(self, 'DndRsn', DeniedReason14Choice, False)

	@DndRsn.deleter
	def DndRsn(self):
		del self._DndRsn
		self._DndRsn = base_types.UninitialisedField(self, 'DndRsn', DeniedReason14Choice, False)

	@property
	def FlngRsn(self):
		return self._FlngRsn

	@FlngRsn.setter
	def FlngRsn(self, value):
		self._FlngRsn = value if value is not None else base_types.UninitialisedField(self, 'FlngRsn', FailingReason9Choice, False)

	@FlngRsn.deleter
	def FlngRsn(self):
		del self._FlngRsn
		self._FlngRsn = base_types.UninitialisedField(self, 'FlngRsn', FailingReason9Choice, False)

	@property
	def GnrtdRsn(self):
		return self._GnrtdRsn

	@GnrtdRsn.setter
	def GnrtdRsn(self, value):
		self._GnrtdRsn = value if value is not None else base_types.UninitialisedField(self, 'GnrtdRsn', GeneratedReasons5Choice, False)

	@GnrtdRsn.deleter
	def GnrtdRsn(self):
		del self._GnrtdRsn
		self._GnrtdRsn = base_types.UninitialisedField(self, 'GnrtdRsn', GeneratedReasons5Choice, False)

	@property
	def PdgCxlRsn(self):
		return self._PdgCxlRsn

	@PdgCxlRsn.setter
	def PdgCxlRsn(self, value):
		self._PdgCxlRsn = value if value is not None else base_types.UninitialisedField(self, 'PdgCxlRsn', PendingCancellationReasons6Choice, False)

	@PdgCxlRsn.deleter
	def PdgCxlRsn(self):
		del self._PdgCxlRsn
		self._PdgCxlRsn = base_types.UninitialisedField(self, 'PdgCxlRsn', PendingCancellationReasons6Choice, False)

	@property
	def PdgModRsn(self):
		return self._PdgModRsn

	@PdgModRsn.setter
	def PdgModRsn(self, value):
		self._PdgModRsn = value if value is not None else base_types.UninitialisedField(self, 'PdgModRsn', PendingReason28Choice, False)

	@PdgModRsn.deleter
	def PdgModRsn(self):
		del self._PdgModRsn
		self._PdgModRsn = base_types.UninitialisedField(self, 'PdgModRsn', PendingReason28Choice, False)

	@property
	def PdgPrcgRsn(self):
		return self._PdgPrcgRsn

	@PdgPrcgRsn.setter
	def PdgPrcgRsn(self, value):
		self._PdgPrcgRsn = value if value is not None else base_types.UninitialisedField(self, 'PdgPrcgRsn', PendingProcessingReason20Choice, False)

	@PdgPrcgRsn.deleter
	def PdgPrcgRsn(self):
		del self._PdgPrcgRsn
		self._PdgPrcgRsn = base_types.UninitialisedField(self, 'PdgPrcgRsn', PendingProcessingReason20Choice, False)

	@property
	def PdgRsn(self):
		return self._PdgRsn

	@PdgRsn.setter
	def PdgRsn(self, value):
		self._PdgRsn = value if value is not None else base_types.UninitialisedField(self, 'PdgRsn', PendingReason78Choice, False)

	@PdgRsn.deleter
	def PdgRsn(self):
		del self._PdgRsn
		self._PdgRsn = base_types.UninitialisedField(self, 'PdgRsn', PendingReason78Choice, False)

	@property
	def RepoCallAckRsn(self):
		return self._RepoCallAckRsn

	@RepoCallAckRsn.setter
	def RepoCallAckRsn(self, value):
		self._RepoCallAckRsn = value if value is not None else base_types.UninitialisedField(self, 'RepoCallAckRsn', AcknowledgementReason13Choice, False)

	@RepoCallAckRsn.deleter
	def RepoCallAckRsn(self):
		del self._RepoCallAckRsn
		self._RepoCallAckRsn = base_types.UninitialisedField(self, 'RepoCallAckRsn', AcknowledgementReason13Choice, False)

	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctnRsn', RejectionReason45Choice, False)

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = base_types.UninitialisedField(self, 'RjctnRsn', RejectionReason45Choice, False)

	@property
	def RprRsn(self):
		return self._RprRsn

	@RprRsn.setter
	def RprRsn(self, value):
		self._RprRsn = value if value is not None else base_types.UninitialisedField(self, 'RprRsn', RepairReason11Choice, False)

	@RprRsn.deleter
	def RprRsn(self):
		del self._RprRsn
		self._RprRsn = base_types.UninitialisedField(self, 'RprRsn', RepairReason11Choice, False)

	@property
	def UmtchdRsn(self):
		return self._UmtchdRsn

	@UmtchdRsn.setter
	def UmtchdRsn(self, value):
		self._UmtchdRsn = value if value is not None else base_types.UninitialisedField(self, 'UmtchdRsn', UnmatchedReason22Choice, False)

	@UmtchdRsn.deleter
	def UmtchdRsn(self):
		del self._UmtchdRsn
		self._UmtchdRsn = base_types.UninitialisedField(self, 'UmtchdRsn', UnmatchedReason22Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdAccptdRsn', type=AcknowledgementReason12Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlRsn', type=CancellationReason20Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DndRsn', type=DeniedReason14Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FlngRsn', type=FailingReason9Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='GnrtdRsn', type=GeneratedReasons5Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgCxlRsn', type=PendingCancellationReasons6Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgModRsn', type=PendingReason28Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPrcgRsn', type=PendingProcessingReason20Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgRsn', type=PendingReason78Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RepoCallAckRsn', type=AcknowledgementReason13Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=RejectionReason45Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RprRsn', type=RepairReason11Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UmtchdRsn', type=UnmatchedReason22Choice, min=0, max=1, mutex_group=1, array=False),
	))