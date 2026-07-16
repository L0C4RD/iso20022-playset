# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MandateSuspensionReason3
from . import Max35Text
from . import OriginalMandate10Choice
from . import OriginalMessageInformation1
from . import SupplementaryData1

class MandateSuspension4(base_types._BaseFieldType):

	__slots__ = ["_OrgnlMndt", "_OrgnlMsgInf", "_SplmtryData", "_SspnsnReqId", "_SspnsnRsn"]
	@property
	def OrgnlMndt(self):
		return self._OrgnlMndt

	@OrgnlMndt.setter
	def OrgnlMndt(self, value):
		self._OrgnlMndt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMndt', OriginalMandate10Choice, False)

	@OrgnlMndt.deleter
	def OrgnlMndt(self):
		del self._OrgnlMndt
		self._OrgnlMndt = base_types.UninitialisedField(self, 'OrgnlMndt', OriginalMandate10Choice, False)

	@property
	def OrgnlMsgInf(self):
		return self._OrgnlMsgInf

	@OrgnlMsgInf.setter
	def OrgnlMsgInf(self, value):
		self._OrgnlMsgInf = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMsgInf', OriginalMessageInformation1, False)

	@OrgnlMsgInf.deleter
	def OrgnlMsgInf(self):
		del self._OrgnlMsgInf
		self._OrgnlMsgInf = base_types.UninitialisedField(self, 'OrgnlMsgInf', OriginalMessageInformation1, False)

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
	def SspnsnReqId(self):
		return self._SspnsnReqId

	@SspnsnReqId.setter
	def SspnsnReqId(self, value):
		self._SspnsnReqId = value if value is not None else base_types.UninitialisedField(self, 'SspnsnReqId', Max35Text, False)

	@SspnsnReqId.deleter
	def SspnsnReqId(self):
		del self._SspnsnReqId
		self._SspnsnReqId = base_types.UninitialisedField(self, 'SspnsnReqId', Max35Text, False)

	@property
	def SspnsnRsn(self):
		return self._SspnsnRsn

	@SspnsnRsn.setter
	def SspnsnRsn(self, value):
		self._SspnsnRsn = value if value is not None else base_types.UninitialisedField(self, 'SspnsnRsn', MandateSuspensionReason3, False)

	@SspnsnRsn.deleter
	def SspnsnRsn(self):
		del self._SspnsnRsn
		self._SspnsnRsn = base_types.UninitialisedField(self, 'SspnsnRsn', MandateSuspensionReason3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlMndt', type=OriginalMandate10Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgInf', type=OriginalMessageInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SspnsnReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SspnsnRsn', type=MandateSuspensionReason3, min=1, max=1, mutex_group=None, array=False),
	))