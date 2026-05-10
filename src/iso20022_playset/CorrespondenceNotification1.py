import base_types
import Max35Text
import RelatedNotificationData1
import Document15
import NotificationSubType1Choice
import NotificationType1Choice
import Max2000Text

class CorrespondenceNotification1(base_types._BaseFieldType):

	__slots__ = ["_NtfctnSubTp", "_SndrNtfctnId", "_NtfctnTp", "_RltdNtfctnData", "_NclsdFile", "_NtfctnNrrtv"]
	@property
	def NtfctnSubTp(self):
		return self._NtfctnSubTp

	@NtfctnSubTp.setter
	def NtfctnSubTp(self, value):
		self._NtfctnSubTp = value if type(value) != auto else self.make_default("NtfctnSubTp")

	@NtfctnSubTp.deleter
	def NtfctnSubTp(self):
		del self._NtfctnSubTp
		self._NtfctnSubTp = None

	@property
	def SndrNtfctnId(self):
		return self._SndrNtfctnId

	@SndrNtfctnId.setter
	def SndrNtfctnId(self, value):
		self._SndrNtfctnId = value if type(value) != auto else self.make_default("SndrNtfctnId")

	@SndrNtfctnId.deleter
	def SndrNtfctnId(self):
		del self._SndrNtfctnId
		self._SndrNtfctnId = None

	@property
	def NtfctnTp(self):
		return self._NtfctnTp

	@NtfctnTp.setter
	def NtfctnTp(self, value):
		self._NtfctnTp = value if type(value) != auto else self.make_default("NtfctnTp")

	@NtfctnTp.deleter
	def NtfctnTp(self):
		del self._NtfctnTp
		self._NtfctnTp = None

	@property
	def RltdNtfctnData(self):
		return self._RltdNtfctnData

	@RltdNtfctnData.setter
	def RltdNtfctnData(self, value):
		self._RltdNtfctnData = value if type(value) != auto else self.make_default("RltdNtfctnData")

	@RltdNtfctnData.deleter
	def RltdNtfctnData(self):
		del self._RltdNtfctnData
		self._RltdNtfctnData = None

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if type(value) != auto else self.make_default("NclsdFile")

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = None

	@property
	def NtfctnNrrtv(self):
		return self._NtfctnNrrtv

	@NtfctnNrrtv.setter
	def NtfctnNrrtv(self, value):
		self._NtfctnNrrtv = value if type(value) != auto else self.make_default("NtfctnNrrtv")

	@NtfctnNrrtv.deleter
	def NtfctnNrrtv(self):
		del self._NtfctnNrrtv
		self._NtfctnNrrtv = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtfctnSubTp', type=NotificationSubType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrNtfctnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnTp', type=NotificationType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdNtfctnData', type=RelatedNotificationData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NclsdFile', type=Document15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtfctnNrrtv', type=Max2000Text, min=0, max=None, mutex_group=None, array=True),
	))

