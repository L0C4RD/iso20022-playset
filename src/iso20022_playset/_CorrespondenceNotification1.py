# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Document15
from . import Max2000Text
from . import Max35Text
from . import NotificationSubType1Choice
from . import NotificationType1Choice
from . import RelatedNotificationData1

class CorrespondenceNotification1(base_types._BaseFieldType):

	__slots__ = ["_NclsdFile", "_NtfctnNrrtv", "_NtfctnSubTp", "_NtfctnTp", "_RltdNtfctnData", "_SndrNtfctnId"]
	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if value is not None else base_types.UninitialisedField(self, 'NclsdFile', Document15, True)

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = base_types.UninitialisedField(self, 'NclsdFile', Document15, True)

	@property
	def NtfctnNrrtv(self):
		return self._NtfctnNrrtv

	@NtfctnNrrtv.setter
	def NtfctnNrrtv(self, value):
		self._NtfctnNrrtv = value if value is not None else base_types.UninitialisedField(self, 'NtfctnNrrtv', Max2000Text, True)

	@NtfctnNrrtv.deleter
	def NtfctnNrrtv(self):
		del self._NtfctnNrrtv
		self._NtfctnNrrtv = base_types.UninitialisedField(self, 'NtfctnNrrtv', Max2000Text, True)

	@property
	def NtfctnSubTp(self):
		return self._NtfctnSubTp

	@NtfctnSubTp.setter
	def NtfctnSubTp(self, value):
		self._NtfctnSubTp = value if value is not None else base_types.UninitialisedField(self, 'NtfctnSubTp', NotificationSubType1Choice, False)

	@NtfctnSubTp.deleter
	def NtfctnSubTp(self):
		del self._NtfctnSubTp
		self._NtfctnSubTp = base_types.UninitialisedField(self, 'NtfctnSubTp', NotificationSubType1Choice, False)

	@property
	def NtfctnTp(self):
		return self._NtfctnTp

	@NtfctnTp.setter
	def NtfctnTp(self, value):
		self._NtfctnTp = value if value is not None else base_types.UninitialisedField(self, 'NtfctnTp', NotificationType1Choice, False)

	@NtfctnTp.deleter
	def NtfctnTp(self):
		del self._NtfctnTp
		self._NtfctnTp = base_types.UninitialisedField(self, 'NtfctnTp', NotificationType1Choice, False)

	@property
	def RltdNtfctnData(self):
		return self._RltdNtfctnData

	@RltdNtfctnData.setter
	def RltdNtfctnData(self, value):
		self._RltdNtfctnData = value if value is not None else base_types.UninitialisedField(self, 'RltdNtfctnData', RelatedNotificationData1, True)

	@RltdNtfctnData.deleter
	def RltdNtfctnData(self):
		del self._RltdNtfctnData
		self._RltdNtfctnData = base_types.UninitialisedField(self, 'RltdNtfctnData', RelatedNotificationData1, True)

	@property
	def SndrNtfctnId(self):
		return self._SndrNtfctnId

	@SndrNtfctnId.setter
	def SndrNtfctnId(self, value):
		self._SndrNtfctnId = value if value is not None else base_types.UninitialisedField(self, 'SndrNtfctnId', Max35Text, False)

	@SndrNtfctnId.deleter
	def SndrNtfctnId(self):
		del self._SndrNtfctnId
		self._SndrNtfctnId = base_types.UninitialisedField(self, 'SndrNtfctnId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NclsdFile', type=Document15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtfctnNrrtv', type=Max2000Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtfctnSubTp', type=NotificationSubType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnTp', type=NotificationType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdNtfctnData', type=RelatedNotificationData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SndrNtfctnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))