# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalRequestData1Choice
from . import Document12
from . import FileData1
from . import InvestigationReason1Choice
from . import InvestigationReasonSubType1Choice
from . import Max3Number
from . import RelatedInvestigationData1

class InvestigationReason2(base_types._BaseFieldType):

	__slots__ = ["_AddtlReqData", "_NclsdFile", "_RltdFileData", "_RltdInvstgtnData", "_Rsn", "_RsnSubTp", "_Seq"]
	@property
	def AddtlReqData(self):
		return self._AddtlReqData

	@AddtlReqData.setter
	def AddtlReqData(self, value):
		self._AddtlReqData = value if value is not None else base_types.UninitialisedField(self, 'AddtlReqData', AdditionalRequestData1Choice, False)

	@AddtlReqData.deleter
	def AddtlReqData(self):
		del self._AddtlReqData
		self._AddtlReqData = base_types.UninitialisedField(self, 'AddtlReqData', AdditionalRequestData1Choice, False)

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if value is not None else base_types.UninitialisedField(self, 'NclsdFile', Document12, True)

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = base_types.UninitialisedField(self, 'NclsdFile', Document12, True)

	@property
	def RltdFileData(self):
		return self._RltdFileData

	@RltdFileData.setter
	def RltdFileData(self, value):
		self._RltdFileData = value if value is not None else base_types.UninitialisedField(self, 'RltdFileData', FileData1, True)

	@RltdFileData.deleter
	def RltdFileData(self):
		del self._RltdFileData
		self._RltdFileData = base_types.UninitialisedField(self, 'RltdFileData', FileData1, True)

	@property
	def RltdInvstgtnData(self):
		return self._RltdInvstgtnData

	@RltdInvstgtnData.setter
	def RltdInvstgtnData(self, value):
		self._RltdInvstgtnData = value if value is not None else base_types.UninitialisedField(self, 'RltdInvstgtnData', RelatedInvestigationData1, False)

	@RltdInvstgtnData.deleter
	def RltdInvstgtnData(self):
		del self._RltdInvstgtnData
		self._RltdInvstgtnData = base_types.UninitialisedField(self, 'RltdInvstgtnData', RelatedInvestigationData1, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', InvestigationReason1Choice, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', InvestigationReason1Choice, False)

	@property
	def RsnSubTp(self):
		return self._RsnSubTp

	@RsnSubTp.setter
	def RsnSubTp(self, value):
		self._RsnSubTp = value if value is not None else base_types.UninitialisedField(self, 'RsnSubTp', InvestigationReasonSubType1Choice, False)

	@RsnSubTp.deleter
	def RsnSubTp(self):
		del self._RsnSubTp
		self._RsnSubTp = base_types.UninitialisedField(self, 'RsnSubTp', InvestigationReasonSubType1Choice, False)

	@property
	def Seq(self):
		return self._Seq

	@Seq.setter
	def Seq(self, value):
		self._Seq = value if value is not None else base_types.UninitialisedField(self, 'Seq', Max3Number, False)

	@Seq.deleter
	def Seq(self):
		del self._Seq
		self._Seq = base_types.UninitialisedField(self, 'Seq', Max3Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlReqData', type=AdditionalRequestData1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdFileData', type=FileData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdInvstgtnData', type=RelatedInvestigationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=InvestigationReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsnSubTp', type=InvestigationReasonSubType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Seq', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
	))