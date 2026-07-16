# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NotificationCancellationProcessingStatus2
from . import NotificationCancellationRejectionReason2

class NotificationCancellationRequestStatus2Choice(base_types._BaseFieldType):

	__slots__ = ["_PrcdSts", "_RjctdSts"]
	@property
	def PrcdSts(self):
		return self._PrcdSts

	@PrcdSts.setter
	def PrcdSts(self, value):
		self._PrcdSts = value if value is not None else base_types.UninitialisedField(self, 'PrcdSts', NotificationCancellationProcessingStatus2, False)

	@PrcdSts.deleter
	def PrcdSts(self):
		del self._PrcdSts
		self._PrcdSts = base_types.UninitialisedField(self, 'PrcdSts', NotificationCancellationProcessingStatus2, False)

	@property
	def RjctdSts(self):
		return self._RjctdSts

	@RjctdSts.setter
	def RjctdSts(self, value):
		self._RjctdSts = value if value is not None else base_types.UninitialisedField(self, 'RjctdSts', NotificationCancellationRejectionReason2, False)

	@RjctdSts.deleter
	def RjctdSts(self):
		del self._RjctdSts
		self._RjctdSts = base_types.UninitialisedField(self, 'RjctdSts', NotificationCancellationRejectionReason2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrcdSts', type=NotificationCancellationProcessingStatus2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RjctdSts', type=NotificationCancellationRejectionReason2, min=0, max=1, mutex_group=1, array=False),
	))