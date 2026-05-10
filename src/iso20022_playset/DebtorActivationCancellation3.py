import base_types
import SupplementaryData1
import DebtorActivationCancellationReason3
import OriginalActivation3Choice
import OriginalBusinessInstruction1

class DebtorActivationCancellation3(base_types._BaseFieldType):

	__slots__ = ["_CxlRsn", "_OrgnlBizInstr", "_SplmtryData", "_OrgnlActvtn"]
	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

	@property
	def OrgnlBizInstr(self):
		return self._OrgnlBizInstr

	@OrgnlBizInstr.setter
	def OrgnlBizInstr(self, value):
		self._OrgnlBizInstr = value if type(value) != auto else self.make_default("OrgnlBizInstr")

	@OrgnlBizInstr.deleter
	def OrgnlBizInstr(self):
		del self._OrgnlBizInstr
		self._OrgnlBizInstr = None

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
	def OrgnlActvtn(self):
		return self._OrgnlActvtn

	@OrgnlActvtn.setter
	def OrgnlActvtn(self, value):
		self._OrgnlActvtn = value if type(value) != auto else self.make_default("OrgnlActvtn")

	@OrgnlActvtn.deleter
	def OrgnlActvtn(self):
		del self._OrgnlActvtn
		self._OrgnlActvtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlRsn', type=DebtorActivationCancellationReason3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlBizInstr', type=OriginalBusinessInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlActvtn', type=OriginalActivation3Choice, min=1, max=1, mutex_group=None, array=False),
	))

