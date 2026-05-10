import base_types
import InvestigationReasonSubType1Choice
import InvestigationReason1Choice
import RelatedInvestigationData1
import InvestigationDataRecord7Choice
import Document12
import FileData1
import Party40Choice
import Max3Number

class InvestigationData6(base_types._BaseFieldType):

	__slots__ = ["_RspnData", "_NclsdFile", "_RspnOrgtr", "_OrgnlInvstgtnRsnSubTp", "_OrgnlInvstgtnRsn", "_RltdInvstgtnData", "_RltdFileData", "_OrgnlInvstgtnSeq"]
	@property
	def RspnData(self):
		return self._RspnData

	@RspnData.setter
	def RspnData(self, value):
		self._RspnData = value if type(value) != auto else self.make_default("RspnData")

	@RspnData.deleter
	def RspnData(self):
		del self._RspnData
		self._RspnData = None

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
	def RspnOrgtr(self):
		return self._RspnOrgtr

	@RspnOrgtr.setter
	def RspnOrgtr(self, value):
		self._RspnOrgtr = value if type(value) != auto else self.make_default("RspnOrgtr")

	@RspnOrgtr.deleter
	def RspnOrgtr(self):
		del self._RspnOrgtr
		self._RspnOrgtr = None

	@property
	def OrgnlInvstgtnRsnSubTp(self):
		return self._OrgnlInvstgtnRsnSubTp

	@OrgnlInvstgtnRsnSubTp.setter
	def OrgnlInvstgtnRsnSubTp(self, value):
		self._OrgnlInvstgtnRsnSubTp = value if type(value) != auto else self.make_default("OrgnlInvstgtnRsnSubTp")

	@OrgnlInvstgtnRsnSubTp.deleter
	def OrgnlInvstgtnRsnSubTp(self):
		del self._OrgnlInvstgtnRsnSubTp
		self._OrgnlInvstgtnRsnSubTp = None

	@property
	def OrgnlInvstgtnRsn(self):
		return self._OrgnlInvstgtnRsn

	@OrgnlInvstgtnRsn.setter
	def OrgnlInvstgtnRsn(self, value):
		self._OrgnlInvstgtnRsn = value if type(value) != auto else self.make_default("OrgnlInvstgtnRsn")

	@OrgnlInvstgtnRsn.deleter
	def OrgnlInvstgtnRsn(self):
		del self._OrgnlInvstgtnRsn
		self._OrgnlInvstgtnRsn = None

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
	def RltdFileData(self):
		return self._RltdFileData

	@RltdFileData.setter
	def RltdFileData(self, value):
		self._RltdFileData = value if type(value) != auto else self.make_default("RltdFileData")

	@RltdFileData.deleter
	def RltdFileData(self):
		del self._RltdFileData
		self._RltdFileData = None

	@property
	def OrgnlInvstgtnSeq(self):
		return self._OrgnlInvstgtnSeq

	@OrgnlInvstgtnSeq.setter
	def OrgnlInvstgtnSeq(self, value):
		self._OrgnlInvstgtnSeq = value if type(value) != auto else self.make_default("OrgnlInvstgtnSeq")

	@OrgnlInvstgtnSeq.deleter
	def OrgnlInvstgtnSeq(self):
		del self._OrgnlInvstgtnSeq
		self._OrgnlInvstgtnSeq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RspnData', type=InvestigationDataRecord7Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RspnOrgtr', type=Party40Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInvstgtnRsnSubTp', type=InvestigationReasonSubType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInvstgtnRsn', type=InvestigationReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdInvstgtnData', type=RelatedInvestigationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdFileData', type=FileData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlInvstgtnSeq', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
	))

