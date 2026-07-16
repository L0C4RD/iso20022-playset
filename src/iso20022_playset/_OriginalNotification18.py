# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GroupCancellationIndicator
from . import ISODateTime
from . import Max35Text
from . import OriginalNotificationReference16

class OriginalNotification18(base_types._BaseFieldType):

	__slots__ = ["_NtfctnCxl", "_OrgnlCreDtTm", "_OrgnlMsgId", "_OrgnlNtfctnId", "_OrgnlNtfctnRef"]
	@property
	def NtfctnCxl(self):
		return self._NtfctnCxl

	@NtfctnCxl.setter
	def NtfctnCxl(self, value):
		self._NtfctnCxl = value if value is not None else base_types.UninitialisedField(self, 'NtfctnCxl', GroupCancellationIndicator, False)

	@NtfctnCxl.deleter
	def NtfctnCxl(self):
		del self._NtfctnCxl
		self._NtfctnCxl = base_types.UninitialisedField(self, 'NtfctnCxl', GroupCancellationIndicator, False)

	@property
	def OrgnlCreDtTm(self):
		return self._OrgnlCreDtTm

	@OrgnlCreDtTm.setter
	def OrgnlCreDtTm(self, value):
		self._OrgnlCreDtTm = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCreDtTm', ISODateTime, False)

	@OrgnlCreDtTm.deleter
	def OrgnlCreDtTm(self):
		del self._OrgnlCreDtTm
		self._OrgnlCreDtTm = base_types.UninitialisedField(self, 'OrgnlCreDtTm', ISODateTime, False)

	@property
	def OrgnlMsgId(self):
		return self._OrgnlMsgId

	@OrgnlMsgId.setter
	def OrgnlMsgId(self, value):
		self._OrgnlMsgId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMsgId', Max35Text, False)

	@OrgnlMsgId.deleter
	def OrgnlMsgId(self):
		del self._OrgnlMsgId
		self._OrgnlMsgId = base_types.UninitialisedField(self, 'OrgnlMsgId', Max35Text, False)

	@property
	def OrgnlNtfctnId(self):
		return self._OrgnlNtfctnId

	@OrgnlNtfctnId.setter
	def OrgnlNtfctnId(self, value):
		self._OrgnlNtfctnId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlNtfctnId', Max35Text, False)

	@OrgnlNtfctnId.deleter
	def OrgnlNtfctnId(self):
		del self._OrgnlNtfctnId
		self._OrgnlNtfctnId = base_types.UninitialisedField(self, 'OrgnlNtfctnId', Max35Text, False)

	@property
	def OrgnlNtfctnRef(self):
		return self._OrgnlNtfctnRef

	@OrgnlNtfctnRef.setter
	def OrgnlNtfctnRef(self, value):
		self._OrgnlNtfctnRef = value if value is not None else base_types.UninitialisedField(self, 'OrgnlNtfctnRef', OriginalNotificationReference16, True)

	@OrgnlNtfctnRef.deleter
	def OrgnlNtfctnRef(self):
		del self._OrgnlNtfctnRef
		self._OrgnlNtfctnRef = base_types.UninitialisedField(self, 'OrgnlNtfctnRef', OriginalNotificationReference16, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtfctnCxl', type=GroupCancellationIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtfctnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtfctnRef', type=OriginalNotificationReference16, min=0, max=None, mutex_group=None, array=True),
	))