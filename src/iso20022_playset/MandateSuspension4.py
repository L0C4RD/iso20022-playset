import base_types
import OriginalMandate10Choice
import MandateSuspensionReason3
import Max35Text
import SupplementaryData1
import OriginalMessageInformation1

class MandateSuspension4(base_types._BaseFieldType):

	__slots__ = ["_OrgnlMndt", "_OrgnlMsgInf", "_SplmtryData", "_SspnsnReqId", "_SspnsnRsn"]
	@property
	def OrgnlMndt(self):
		return self._OrgnlMndt

	@OrgnlMndt.setter
	def OrgnlMndt(self, value):
		self._OrgnlMndt = value if type(value) != auto else self.make_default("OrgnlMndt")

	@OrgnlMndt.deleter
	def OrgnlMndt(self):
		del self._OrgnlMndt
		self._OrgnlMndt = None

	@property
	def OrgnlMsgInf(self):
		return self._OrgnlMsgInf

	@OrgnlMsgInf.setter
	def OrgnlMsgInf(self, value):
		self._OrgnlMsgInf = value if type(value) != auto else self.make_default("OrgnlMsgInf")

	@OrgnlMsgInf.deleter
	def OrgnlMsgInf(self):
		del self._OrgnlMsgInf
		self._OrgnlMsgInf = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def SspnsnReqId(self):
		return self._SspnsnReqId

	@SspnsnReqId.setter
	def SspnsnReqId(self, value):
		self._SspnsnReqId = value if type(value) != auto else self.make_default("SspnsnReqId")

	@SspnsnReqId.deleter
	def SspnsnReqId(self):
		del self._SspnsnReqId
		self._SspnsnReqId = None

	@property
	def SspnsnRsn(self):
		return self._SspnsnRsn

	@SspnsnRsn.setter
	def SspnsnRsn(self, value):
		self._SspnsnRsn = value if type(value) != auto else self.make_default("SspnsnRsn")

	@SspnsnRsn.deleter
	def SspnsnRsn(self):
		del self._SspnsnRsn
		self._SspnsnRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlMndt', type=OriginalMandate10Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgInf', type=OriginalMessageInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SspnsnReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SspnsnRsn', type=MandateSuspensionReason3, min=1, max=1, mutex_group=None, array=False),
	))

