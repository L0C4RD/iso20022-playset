from . import base_types
from ._GroupCancellationIndicator import GroupCancellationIndicator
from ._ISODateTime import ISODateTime
from ._Max35Text import Max35Text
from ._OriginalNotificationReference14 import OriginalNotificationReference14

class OriginalNotification16(base_types._BaseFieldType):

	__slots__ = ["_NtfctnCxl", "_OrgnlCreDtTm", "_OrgnlMsgId", "_OrgnlNtfctnId", "_OrgnlNtfctnRef"]
	@property
	def NtfctnCxl(self):
		return self._NtfctnCxl

	@NtfctnCxl.setter
	def NtfctnCxl(self, value):
		self._NtfctnCxl = value if type(value) != base_types.auto else self.make_default("NtfctnCxl")

	@NtfctnCxl.deleter
	def NtfctnCxl(self):
		del self._NtfctnCxl
		self._NtfctnCxl = None

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
		base_types.FieldEntry(name='NtfctnCxl', type=GroupCancellationIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtfctnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtfctnRef', type=OriginalNotificationReference14, min=0, max=None, mutex_group=None, array=True),
	))

