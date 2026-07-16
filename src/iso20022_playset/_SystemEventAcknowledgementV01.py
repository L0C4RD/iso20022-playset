# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Event1
from . import Exact4AlphaNumericText
from . import Max35Text
from . import SupplementaryData1

class SystemEventAcknowledgementV01(base_types._BaseFieldType):

	__slots__ = ["_AckDtls", "_MsgId", "_OrgtrRef", "_SplmtryData", "_SttlmSsnIdr"]
	@property
	def AckDtls(self):
		return self._AckDtls

	@AckDtls.setter
	def AckDtls(self, value):
		self._AckDtls = value if value is not None else base_types.UninitialisedField(self, 'AckDtls', Event1, False)

	@AckDtls.deleter
	def AckDtls(self):
		del self._AckDtls
		self._AckDtls = base_types.UninitialisedField(self, 'AckDtls', Event1, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@property
	def OrgtrRef(self):
		return self._OrgtrRef

	@OrgtrRef.setter
	def OrgtrRef(self, value):
		self._OrgtrRef = value if value is not None else base_types.UninitialisedField(self, 'OrgtrRef', Max35Text, False)

	@OrgtrRef.deleter
	def OrgtrRef(self):
		del self._OrgtrRef
		self._OrgtrRef = base_types.UninitialisedField(self, 'OrgtrRef', Max35Text, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def SttlmSsnIdr(self):
		return self._SttlmSsnIdr

	@SttlmSsnIdr.setter
	def SttlmSsnIdr(self, value):
		self._SttlmSsnIdr = value if value is not None else base_types.UninitialisedField(self, 'SttlmSsnIdr', Exact4AlphaNumericText, False)

	@SttlmSsnIdr.deleter
	def SttlmSsnIdr(self):
		del self._SttlmSsnIdr
		self._SttlmSsnIdr = base_types.UninitialisedField(self, 'SttlmSsnIdr', Exact4AlphaNumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckDtls', type=Event1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSsnIdr', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))