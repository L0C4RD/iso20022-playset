from . import base_types
import OriginalMessageInformation1
import SupplementaryData1
import OriginalMandate10Choice
import MandateStatus1Choice

class MandateCopy4(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_OrgnlMsgInf", "_MndtSts", "_OrgnlMndt"]
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
	def MndtSts(self):
		return self._MndtSts

	@MndtSts.setter
	def MndtSts(self, value):
		self._MndtSts = value if type(value) != auto else self.make_default("MndtSts")

	@MndtSts.deleter
	def MndtSts(self):
		del self._MndtSts
		self._MndtSts = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlMsgInf', type=OriginalMessageInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtSts', type=MandateStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMndt', type=OriginalMandate10Choice, min=1, max=1, mutex_group=None, array=False),
	))

