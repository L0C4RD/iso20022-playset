import base_types
import Document12
import InvestigationReasonSubType1Choice
import InvestigationReason1Choice
import FileData1
import AdditionalRequestData1Choice
import RelatedInvestigationData1
import Max3Number

class InvestigationReason2(base_types._BaseFieldType):

	__slots__ = ["_Rsn", "_RsnSubTp", "_RltdInvstgtnData", "_Seq", "_AddtlReqData", "_NclsdFile", "_RltdFileData"]
	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def RsnSubTp(self):
		return self._RsnSubTp

	@RsnSubTp.setter
	def RsnSubTp(self, value):
		self._RsnSubTp = value if type(value) != auto else self.make_default("RsnSubTp")

	@RsnSubTp.deleter
	def RsnSubTp(self):
		del self._RsnSubTp
		self._RsnSubTp = None

	@property
	def RltdInvstgtnData(self):
		return self._RltdInvstgtnData

	@RltdInvstgtnData.setter
	def RltdInvstgtnData(self, value):
		self._RltdInvstgtnData = value if type(value) != auto else self.make_default("RltdInvstgtnData")

	@RltdInvstgtnData.deleter
	def RltdInvstgtnData(self):
		del self._RltdInvstgtnData
		self._RltdInvstgtnData = None

	@property
	def Seq(self):
		return self._Seq

	@Seq.setter
	def Seq(self, value):
		self._Seq = value if type(value) != auto else self.make_default("Seq")

	@Seq.deleter
	def Seq(self):
		del self._Seq
		self._Seq = None

	@property
	def AddtlReqData(self):
		return self._AddtlReqData

	@AddtlReqData.setter
	def AddtlReqData(self, value):
		self._AddtlReqData = value if type(value) != auto else self.make_default("AddtlReqData")

	@AddtlReqData.deleter
	def AddtlReqData(self):
		del self._AddtlReqData
		self._AddtlReqData = None

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if type(value) != auto else self.make_default("NclsdFile")

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = None

	@property
	def RltdFileData(self):
		return self._RltdFileData

	@RltdFileData.setter
	def RltdFileData(self, value):
		self._RltdFileData = value if type(value) != auto else self.make_default("RltdFileData")

	@RltdFileData.deleter
	def RltdFileData(self):
		del self._RltdFileData
		self._RltdFileData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rsn', type=InvestigationReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsnSubTp', type=InvestigationReasonSubType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdInvstgtnData', type=RelatedInvestigationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Seq', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlReqData', type=AdditionalRequestData1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdFileData', type=FileData1, min=0, max=None, mutex_group=None, array=True),
	))

