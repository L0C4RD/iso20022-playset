# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max140Text
from . import Max35Text
from . import NotificationStatus3Code
from . import OriginalNotificationReference15

class OriginalNotification17(base_types._BaseFieldType):

	__slots__ = ["_AddtlStsInf", "_NtfctnSts", "_OrgnlCreDtTm", "_OrgnlMsgId", "_OrgnlNtfctnId", "_OrgnlNtfctnRef"]
	@property
	def AddtlStsInf(self):
		return self._AddtlStsInf

	@AddtlStsInf.setter
	def AddtlStsInf(self, value):
		self._AddtlStsInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlStsInf', Max140Text, False)

	@AddtlStsInf.deleter
	def AddtlStsInf(self):
		del self._AddtlStsInf
		self._AddtlStsInf = base_types.UninitialisedField(self, 'AddtlStsInf', Max140Text, False)

	@property
	def NtfctnSts(self):
		return self._NtfctnSts

	@NtfctnSts.setter
	def NtfctnSts(self, value):
		self._NtfctnSts = value if value is not None else base_types.UninitialisedField(self, 'NtfctnSts', NotificationStatus3Code, False)

	@NtfctnSts.deleter
	def NtfctnSts(self):
		del self._NtfctnSts
		self._NtfctnSts = base_types.UninitialisedField(self, 'NtfctnSts', NotificationStatus3Code, False)

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
		self._OrgnlNtfctnRef = value if value is not None else base_types.UninitialisedField(self, 'OrgnlNtfctnRef', OriginalNotificationReference15, True)

	@OrgnlNtfctnRef.deleter
	def OrgnlNtfctnRef(self):
		del self._OrgnlNtfctnRef
		self._OrgnlNtfctnRef = base_types.UninitialisedField(self, 'OrgnlNtfctnRef', OriginalNotificationReference15, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlStsInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnSts', type=NotificationStatus3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtfctnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtfctnRef', type=OriginalNotificationReference15, min=0, max=None, mutex_group=None, array=True),
	))