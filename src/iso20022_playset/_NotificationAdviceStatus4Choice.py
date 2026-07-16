# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NotificationAcceptedWithWarningStatus1
from . import NotificationPendingStatus1
from . import NotificationProcessingStatus2
from . import NotificationRejectionReason3

class NotificationAdviceStatus4Choice(base_types._BaseFieldType):

	__slots__ = ["_AccptdWthWrngSts", "_PdgSts", "_PrcdSts", "_RjctdSts"]
	@property
	def AccptdWthWrngSts(self):
		return self._AccptdWthWrngSts

	@AccptdWthWrngSts.setter
	def AccptdWthWrngSts(self, value):
		self._AccptdWthWrngSts = value if value is not None else base_types.UninitialisedField(self, 'AccptdWthWrngSts', NotificationAcceptedWithWarningStatus1, False)

	@AccptdWthWrngSts.deleter
	def AccptdWthWrngSts(self):
		del self._AccptdWthWrngSts
		self._AccptdWthWrngSts = base_types.UninitialisedField(self, 'AccptdWthWrngSts', NotificationAcceptedWithWarningStatus1, False)

	@property
	def PdgSts(self):
		return self._PdgSts

	@PdgSts.setter
	def PdgSts(self, value):
		self._PdgSts = value if value is not None else base_types.UninitialisedField(self, 'PdgSts', NotificationPendingStatus1, False)

	@PdgSts.deleter
	def PdgSts(self):
		del self._PdgSts
		self._PdgSts = base_types.UninitialisedField(self, 'PdgSts', NotificationPendingStatus1, False)

	@property
	def PrcdSts(self):
		return self._PrcdSts

	@PrcdSts.setter
	def PrcdSts(self, value):
		self._PrcdSts = value if value is not None else base_types.UninitialisedField(self, 'PrcdSts', NotificationProcessingStatus2, False)

	@PrcdSts.deleter
	def PrcdSts(self):
		del self._PrcdSts
		self._PrcdSts = base_types.UninitialisedField(self, 'PrcdSts', NotificationProcessingStatus2, False)

	@property
	def RjctdSts(self):
		return self._RjctdSts

	@RjctdSts.setter
	def RjctdSts(self, value):
		self._RjctdSts = value if value is not None else base_types.UninitialisedField(self, 'RjctdSts', NotificationRejectionReason3, False)

	@RjctdSts.deleter
	def RjctdSts(self):
		del self._RjctdSts
		self._RjctdSts = base_types.UninitialisedField(self, 'RjctdSts', NotificationRejectionReason3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdWthWrngSts', type=NotificationAcceptedWithWarningStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgSts', type=NotificationPendingStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrcdSts', type=NotificationProcessingStatus2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RjctdSts', type=NotificationRejectionReason3, min=0, max=1, mutex_group=1, array=False),
	))