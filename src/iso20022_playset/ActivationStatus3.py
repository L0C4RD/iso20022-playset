import base_types
import OriginalBusinessInstruction1
import DateAndDateTime2Choice
import DebtorActivationStatusReason3
import SupplementaryData1
import ServiceStatus1Choice
import OriginalActivation3Choice

class ActivationStatus3(base_types._BaseFieldType):

	__slots__ = ["_StsRsn", "_SplmtryData", "_OrgnlBizInstr", "_Sts", "_OrgnlActvtnRef", "_FctvActvtnDt"]
	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

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
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def OrgnlActvtnRef(self):
		return self._OrgnlActvtnRef

	@OrgnlActvtnRef.setter
	def OrgnlActvtnRef(self, value):
		self._OrgnlActvtnRef = value if type(value) != auto else self.make_default("OrgnlActvtnRef")

	@OrgnlActvtnRef.deleter
	def OrgnlActvtnRef(self):
		del self._OrgnlActvtnRef
		self._OrgnlActvtnRef = None

	@property
	def FctvActvtnDt(self):
		return self._FctvActvtnDt

	@FctvActvtnDt.setter
	def FctvActvtnDt(self, value):
		self._FctvActvtnDt = value if type(value) != auto else self.make_default("FctvActvtnDt")

	@FctvActvtnDt.deleter
	def FctvActvtnDt(self):
		del self._FctvActvtnDt
		self._FctvActvtnDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsRsn', type=DebtorActivationStatusReason3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlBizInstr', type=OriginalBusinessInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=ServiceStatus1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlActvtnRef', type=OriginalActivation3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvActvtnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

