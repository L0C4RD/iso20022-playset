from . import base_types
from ._NotificationAcceptedWithWarningStatus1 import NotificationAcceptedWithWarningStatus1
from ._NotificationPendingStatus1 import NotificationPendingStatus1
from ._NotificationProcessingStatus2 import NotificationProcessingStatus2
from ._NotificationRejectionReason3 import NotificationRejectionReason3

class NotificationAdviceStatus4Choice(base_types._BaseFieldType):

	__slots__ = ["_AccptdWthWrngSts", "_PdgSts", "_PrcdSts", "_RjctdSts"]
	@property
	def AccptdWthWrngSts(self):
		return self._AccptdWthWrngSts

	@AccptdWthWrngSts.setter
	def AccptdWthWrngSts(self, value):
		self._AccptdWthWrngSts = value if type(value) != base_types.auto else self.make_default("AccptdWthWrngSts")

	@AccptdWthWrngSts.deleter
	def AccptdWthWrngSts(self):
		del self._AccptdWthWrngSts
		self._AccptdWthWrngSts = None

	@property
	def PdgSts(self):
		return self._PdgSts

	@PdgSts.setter
	def PdgSts(self, value):
		self._PdgSts = value if type(value) != base_types.auto else self.make_default("PdgSts")

	@PdgSts.deleter
	def PdgSts(self):
		del self._PdgSts
		self._PdgSts = None

	@property
	def PrcdSts(self):
		return self._PrcdSts

	@PrcdSts.setter
	def PrcdSts(self, value):
		self._PrcdSts = value if type(value) != base_types.auto else self.make_default("PrcdSts")

	@PrcdSts.deleter
	def PrcdSts(self):
		del self._PrcdSts
		self._PrcdSts = None

	@property
	def RjctdSts(self):
		return self._RjctdSts

	@RjctdSts.setter
	def RjctdSts(self, value):
		self._RjctdSts = value if type(value) != base_types.auto else self.make_default("RjctdSts")

	@RjctdSts.deleter
	def RjctdSts(self):
		del self._RjctdSts
		self._RjctdSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdWthWrngSts', type=NotificationAcceptedWithWarningStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgSts', type=NotificationPendingStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrcdSts', type=NotificationProcessingStatus2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RjctdSts', type=NotificationRejectionReason3, min=0, max=1, mutex_group=1, array=False),
	))

