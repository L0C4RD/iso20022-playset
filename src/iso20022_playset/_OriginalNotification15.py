from . import base_types
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text
from ._OriginalNotificationReference13 import OriginalNotificationReference13
from ._ISODateTime import ISODateTime
from ._NotificationStatus3Code import NotificationStatus3Code

class OriginalNotification15(base_types._BaseFieldType):

	__slots__ = ["_OrgnlMsgId", "_OrgnlNtfctnRef", "_NtfctnSts", "_OrgnlNtfctnId", "_AddtlStsInf", "_OrgnlCreDtTm"]
	@property
	def AddtlStsInf(self):
		return self._AddtlStsInf

	@AddtlStsInf.setter
	def AddtlStsInf(self, value):
		self._AddtlStsInf = value if type(value) != base_types.auto else self.make_default("AddtlStsInf")

	@AddtlStsInf.deleter
	def AddtlStsInf(self):
		del self._AddtlStsInf
		self._AddtlStsInf = None

	@property
	def NtfctnSts(self):
		return self._NtfctnSts

	@NtfctnSts.setter
	def NtfctnSts(self, value):
		self._NtfctnSts = value if type(value) != base_types.auto else self.make_default("NtfctnSts")

	@NtfctnSts.deleter
	def NtfctnSts(self):
		del self._NtfctnSts
		self._NtfctnSts = None

	@property
	def OrgnlCreDtTm(self):
		return self._OrgnlCreDtTm

	@OrgnlCreDtTm.setter
	def OrgnlCreDtTm(self, value):
		self._OrgnlCreDtTm = value if type(value) != base_types.auto else self.make_default("OrgnlCreDtTm")

	@OrgnlCreDtTm.deleter
	def OrgnlCreDtTm(self):
		del self._OrgnlCreDtTm
		self._OrgnlCreDtTm = None

	@property
	def OrgnlMsgId(self):
		return self._OrgnlMsgId

	@OrgnlMsgId.setter
	def OrgnlMsgId(self, value):
		self._OrgnlMsgId = value if type(value) != base_types.auto else self.make_default("OrgnlMsgId")

	@OrgnlMsgId.deleter
	def OrgnlMsgId(self):
		del self._OrgnlMsgId
		self._OrgnlMsgId = None

	@property
	def OrgnlNtfctnId(self):
		return self._OrgnlNtfctnId

	@OrgnlNtfctnId.setter
	def OrgnlNtfctnId(self, value):
		self._OrgnlNtfctnId = value if type(value) != base_types.auto else self.make_default("OrgnlNtfctnId")

	@OrgnlNtfctnId.deleter
	def OrgnlNtfctnId(self):
		del self._OrgnlNtfctnId
		self._OrgnlNtfctnId = None

	@property
	def OrgnlNtfctnRef(self):
		return self._OrgnlNtfctnRef

	@OrgnlNtfctnRef.setter
	def OrgnlNtfctnRef(self, value):
		self._OrgnlNtfctnRef = value if type(value) != base_types.auto else self.make_default("OrgnlNtfctnRef")

	@OrgnlNtfctnRef.deleter
	def OrgnlNtfctnRef(self):
		del self._OrgnlNtfctnRef
		self._OrgnlNtfctnRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlStsInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnSts', type=NotificationStatus3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtfctnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtfctnRef', type=OriginalNotificationReference13, min=0, max=None, mutex_group=None, array=True),
	))

