import base_types
import Max35Text
import NotificationLocationData1

class RelatedNotificationData1(base_types._BaseFieldType):

	__slots__ = ["_Lctn", "_NtfctnId"]
	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if type(value) != auto else self.make_default("Lctn")

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = None

	@property
	def NtfctnId(self):
		return self._NtfctnId

	@NtfctnId.setter
	def NtfctnId(self, value):
		self._NtfctnId = value if type(value) != auto else self.make_default("NtfctnId")

	@NtfctnId.deleter
	def NtfctnId(self):
		del self._NtfctnId
		self._NtfctnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lctn', type=NotificationLocationData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtfctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

