import base_types
import OriginalMandate11Choice
import OriginalMessageInformation1
import SupplementaryData1
import AcceptanceResult6

class MandateAcceptance8(base_types._BaseFieldType):

	__slots__ = ["_OrgnlMsgInf", "_SplmtryData", "_OrgnlMndt", "_AccptncRslt"]
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
	def AccptncRslt(self):
		return self._AccptncRslt

	@AccptncRslt.setter
	def AccptncRslt(self, value):
		self._AccptncRslt = value if type(value) != auto else self.make_default("AccptncRslt")

	@AccptncRslt.deleter
	def AccptncRslt(self):
		del self._AccptncRslt
		self._AccptncRslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlMsgInf', type=OriginalMessageInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlMndt', type=OriginalMandate11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptncRslt', type=AcceptanceResult6, min=1, max=1, mutex_group=None, array=False),
	))

