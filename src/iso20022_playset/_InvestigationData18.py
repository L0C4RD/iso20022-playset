# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Document12
from . import FileData1
from . import InvestigationDataRecord12Choice
from . import InvestigationReason1Choice
from . import InvestigationReasonSubType1Choice
from . import Max3Number
from . import Party40Choice
from . import RelatedInvestigationData1

class InvestigationData18(base_types._BaseFieldType):

	__slots__ = ["_NclsdFile", "_OrgnlInvstgtnRsn", "_OrgnlInvstgtnRsnSubTp", "_OrgnlInvstgtnSeq", "_RltdFileData", "_RltdInvstgtnData", "_RspnData", "_RspnOrgtr"]
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
	def OrgnlInvstgtnRsn(self):
		return self._OrgnlInvstgtnRsn

	@OrgnlInvstgtnRsn.setter
	def OrgnlInvstgtnRsn(self, value):
		self._OrgnlInvstgtnRsn = value if value is not None else base_types.UninitialisedField(self, 'OrgnlInvstgtnRsn', InvestigationReason1Choice, False)

	@OrgnlInvstgtnRsn.deleter
	def OrgnlInvstgtnRsn(self):
		del self._OrgnlInvstgtnRsn
		self._OrgnlInvstgtnRsn = base_types.UninitialisedField(self, 'OrgnlInvstgtnRsn', InvestigationReason1Choice, False)

	@property
	def OrgnlInvstgtnRsnSubTp(self):
		return self._OrgnlInvstgtnRsnSubTp

	@OrgnlInvstgtnRsnSubTp.setter
	def OrgnlInvstgtnRsnSubTp(self, value):
		self._OrgnlInvstgtnRsnSubTp = value if value is not None else base_types.UninitialisedField(self, 'OrgnlInvstgtnRsnSubTp', InvestigationReasonSubType1Choice, False)

	@OrgnlInvstgtnRsnSubTp.deleter
	def OrgnlInvstgtnRsnSubTp(self):
		del self._OrgnlInvstgtnRsnSubTp
		self._OrgnlInvstgtnRsnSubTp = base_types.UninitialisedField(self, 'OrgnlInvstgtnRsnSubTp', InvestigationReasonSubType1Choice, False)

	@property
	def OrgnlInvstgtnSeq(self):
		return self._OrgnlInvstgtnSeq

	@OrgnlInvstgtnSeq.setter
	def OrgnlInvstgtnSeq(self, value):
		self._OrgnlInvstgtnSeq = value if value is not None else base_types.UninitialisedField(self, 'OrgnlInvstgtnSeq', Max3Number, False)

	@OrgnlInvstgtnSeq.deleter
	def OrgnlInvstgtnSeq(self):
		del self._OrgnlInvstgtnSeq
		self._OrgnlInvstgtnSeq = base_types.UninitialisedField(self, 'OrgnlInvstgtnSeq', Max3Number, False)

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
	def RspnData(self):
		return self._RspnData

	@RspnData.setter
	def RspnData(self, value):
		self._RspnData = value if value is not None else base_types.UninitialisedField(self, 'RspnData', InvestigationDataRecord12Choice, False)

	@RspnData.deleter
	def RspnData(self):
		del self._RspnData
		self._RspnData = base_types.UninitialisedField(self, 'RspnData', InvestigationDataRecord12Choice, False)

	@property
	def RspnOrgtr(self):
		return self._RspnOrgtr

	@RspnOrgtr.setter
	def RspnOrgtr(self, value):
		self._RspnOrgtr = value if value is not None else base_types.UninitialisedField(self, 'RspnOrgtr', Party40Choice, False)

	@RspnOrgtr.deleter
	def RspnOrgtr(self):
		del self._RspnOrgtr
		self._RspnOrgtr = base_types.UninitialisedField(self, 'RspnOrgtr', Party40Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NclsdFile', type=Document12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlInvstgtnRsn', type=InvestigationReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInvstgtnRsnSubTp', type=InvestigationReasonSubType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInvstgtnSeq', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdFileData', type=FileData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdInvstgtnData', type=RelatedInvestigationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnData', type=InvestigationDataRecord12Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnOrgtr', type=Party40Choice, min=0, max=1, mutex_group=None, array=False),
	))