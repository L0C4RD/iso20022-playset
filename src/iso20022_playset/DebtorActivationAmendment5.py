import base_types
import OriginalBusinessInstruction1
import DebtorActivationAmendmentReason3
import DebtorActivationAmendment6
import SupplementaryData1
import OriginalActivation3Choice

class DebtorActivationAmendment5(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_OrgnlBizInstr", "_Amdmnt", "_AmdmntRsn", "_OrgnlActvtn"]
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
	def Amdmnt(self):
		return self._Amdmnt

	@Amdmnt.setter
	def Amdmnt(self, value):
		self._Amdmnt = value if type(value) != auto else self.make_default("Amdmnt")

	@Amdmnt.deleter
	def Amdmnt(self):
		del self._Amdmnt
		self._Amdmnt = None

	@property
	def AmdmntRsn(self):
		return self._AmdmntRsn

	@AmdmntRsn.setter
	def AmdmntRsn(self, value):
		self._AmdmntRsn = value if type(value) != auto else self.make_default("AmdmntRsn")

	@AmdmntRsn.deleter
	def AmdmntRsn(self):
		del self._AmdmntRsn
		self._AmdmntRsn = None

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
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlBizInstr', type=OriginalBusinessInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amdmnt', type=DebtorActivationAmendment6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmdmntRsn', type=DebtorActivationAmendmentReason3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlActvtn', type=OriginalActivation3Choice, min=1, max=1, mutex_group=None, array=False),
	))

