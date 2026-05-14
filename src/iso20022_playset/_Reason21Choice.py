# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcknowledgementReason12Choice import AcknowledgementReason12Choice
from ._AcknowledgementReason13Choice import AcknowledgementReason13Choice
from ._CancellationReason20Choice import CancellationReason20Choice
from ._DeniedReason14Choice import DeniedReason14Choice
from ._FailingReason9Choice import FailingReason9Choice
from ._GeneratedReasons5Choice import GeneratedReasons5Choice
from ._PendingCancellationReasons6Choice import PendingCancellationReasons6Choice
from ._PendingProcessingReason20Choice import PendingProcessingReason20Choice
from ._PendingReason28Choice import PendingReason28Choice
from ._PendingReason78Choice import PendingReason78Choice
from ._RejectionReason45Choice import RejectionReason45Choice
from ._RepairReason11Choice import RepairReason11Choice
from ._UnmatchedReason22Choice import UnmatchedReason22Choice

class Reason21Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptdRsn", "_CxlRsn", "_DndRsn", "_FlngRsn", "_GnrtdRsn", "_PdgCxlRsn", "_PdgModRsn", "_PdgPrcgRsn", "_PdgRsn", "_RepoCallAckRsn", "_RjctnRsn", "_RprRsn", "_UmtchdRsn"]
	@property
	def AckdAccptdRsn(self):
		return self._AckdAccptdRsn

	@AckdAccptdRsn.setter
	def AckdAccptdRsn(self, value):
		self._AckdAccptdRsn = value if type(value) != base_types.auto else self.make_default("AckdAccptdRsn")

	@AckdAccptdRsn.deleter
	def AckdAccptdRsn(self):
		del self._AckdAccptdRsn
		self._AckdAccptdRsn = None

	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != base_types.auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

	@property
	def DndRsn(self):
		return self._DndRsn

	@DndRsn.setter
	def DndRsn(self, value):
		self._DndRsn = value if type(value) != base_types.auto else self.make_default("DndRsn")

	@DndRsn.deleter
	def DndRsn(self):
		del self._DndRsn
		self._DndRsn = None

	@property
	def FlngRsn(self):
		return self._FlngRsn

	@FlngRsn.setter
	def FlngRsn(self, value):
		self._FlngRsn = value if type(value) != base_types.auto else self.make_default("FlngRsn")

	@FlngRsn.deleter
	def FlngRsn(self):
		del self._FlngRsn
		self._FlngRsn = None

	@property
	def GnrtdRsn(self):
		return self._GnrtdRsn

	@GnrtdRsn.setter
	def GnrtdRsn(self, value):
		self._GnrtdRsn = value if type(value) != base_types.auto else self.make_default("GnrtdRsn")

	@GnrtdRsn.deleter
	def GnrtdRsn(self):
		del self._GnrtdRsn
		self._GnrtdRsn = None

	@property
	def PdgCxlRsn(self):
		return self._PdgCxlRsn

	@PdgCxlRsn.setter
	def PdgCxlRsn(self, value):
		self._PdgCxlRsn = value if type(value) != base_types.auto else self.make_default("PdgCxlRsn")

	@PdgCxlRsn.deleter
	def PdgCxlRsn(self):
		del self._PdgCxlRsn
		self._PdgCxlRsn = None

	@property
	def PdgModRsn(self):
		return self._PdgModRsn

	@PdgModRsn.setter
	def PdgModRsn(self, value):
		self._PdgModRsn = value if type(value) != base_types.auto else self.make_default("PdgModRsn")

	@PdgModRsn.deleter
	def PdgModRsn(self):
		del self._PdgModRsn
		self._PdgModRsn = None

	@property
	def PdgPrcgRsn(self):
		return self._PdgPrcgRsn

	@PdgPrcgRsn.setter
	def PdgPrcgRsn(self, value):
		self._PdgPrcgRsn = value if type(value) != base_types.auto else self.make_default("PdgPrcgRsn")

	@PdgPrcgRsn.deleter
	def PdgPrcgRsn(self):
		del self._PdgPrcgRsn
		self._PdgPrcgRsn = None

	@property
	def PdgRsn(self):
		return self._PdgRsn

	@PdgRsn.setter
	def PdgRsn(self, value):
		self._PdgRsn = value if type(value) != base_types.auto else self.make_default("PdgRsn")

	@PdgRsn.deleter
	def PdgRsn(self):
		del self._PdgRsn
		self._PdgRsn = None

	@property
	def RepoCallAckRsn(self):
		return self._RepoCallAckRsn

	@RepoCallAckRsn.setter
	def RepoCallAckRsn(self, value):
		self._RepoCallAckRsn = value if type(value) != base_types.auto else self.make_default("RepoCallAckRsn")

	@RepoCallAckRsn.deleter
	def RepoCallAckRsn(self):
		del self._RepoCallAckRsn
		self._RepoCallAckRsn = None

	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if type(value) != base_types.auto else self.make_default("RjctnRsn")

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = None

	@property
	def RprRsn(self):
		return self._RprRsn

	@RprRsn.setter
	def RprRsn(self, value):
		self._RprRsn = value if type(value) != base_types.auto else self.make_default("RprRsn")

	@RprRsn.deleter
	def RprRsn(self):
		del self._RprRsn
		self._RprRsn = None

	@property
	def UmtchdRsn(self):
		return self._UmtchdRsn

	@UmtchdRsn.setter
	def UmtchdRsn(self, value):
		self._UmtchdRsn = value if type(value) != base_types.auto else self.make_default("UmtchdRsn")

	@UmtchdRsn.deleter
	def UmtchdRsn(self):
		del self._UmtchdRsn
		self._UmtchdRsn = None

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