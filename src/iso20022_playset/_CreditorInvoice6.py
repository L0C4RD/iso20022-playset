# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CustomerTypeRequest2
from . import DocumentFormat2Choice
from . import DocumentType1Choice
from . import Max500Text
from . import RTPPartyIdentification2
from . import TrueFalseIndicator

class CreditorInvoice6(base_types._BaseFieldType):

	__slots__ = ["_ActvtnReqDlvryPty", "_CdtrInstr", "_CstmrIdTp", "_CtrctFrmtTp", "_CtrctRefTp", "_LtdPresntmntInd"]
	@property
	def ActvtnReqDlvryPty(self):
		return self._ActvtnReqDlvryPty

	@ActvtnReqDlvryPty.setter
	def ActvtnReqDlvryPty(self, value):
		self._ActvtnReqDlvryPty = value if value is not None else base_types.UninitialisedField(self, 'ActvtnReqDlvryPty', RTPPartyIdentification2, False)

	@ActvtnReqDlvryPty.deleter
	def ActvtnReqDlvryPty(self):
		del self._ActvtnReqDlvryPty
		self._ActvtnReqDlvryPty = base_types.UninitialisedField(self, 'ActvtnReqDlvryPty', RTPPartyIdentification2, False)

	@property
	def CdtrInstr(self):
		return self._CdtrInstr

	@CdtrInstr.setter
	def CdtrInstr(self, value):
		self._CdtrInstr = value if value is not None else base_types.UninitialisedField(self, 'CdtrInstr', Max500Text, False)

	@CdtrInstr.deleter
	def CdtrInstr(self):
		del self._CdtrInstr
		self._CdtrInstr = base_types.UninitialisedField(self, 'CdtrInstr', Max500Text, False)

	@property
	def CstmrIdTp(self):
		return self._CstmrIdTp

	@CstmrIdTp.setter
	def CstmrIdTp(self, value):
		self._CstmrIdTp = value if value is not None else base_types.UninitialisedField(self, 'CstmrIdTp', CustomerTypeRequest2, False)

	@CstmrIdTp.deleter
	def CstmrIdTp(self):
		del self._CstmrIdTp
		self._CstmrIdTp = base_types.UninitialisedField(self, 'CstmrIdTp', CustomerTypeRequest2, False)

	@property
	def CtrctFrmtTp(self):
		return self._CtrctFrmtTp

	@CtrctFrmtTp.setter
	def CtrctFrmtTp(self, value):
		self._CtrctFrmtTp = value if value is not None else base_types.UninitialisedField(self, 'CtrctFrmtTp', DocumentFormat2Choice, True)

	@CtrctFrmtTp.deleter
	def CtrctFrmtTp(self):
		del self._CtrctFrmtTp
		self._CtrctFrmtTp = base_types.UninitialisedField(self, 'CtrctFrmtTp', DocumentFormat2Choice, True)

	@property
	def CtrctRefTp(self):
		return self._CtrctRefTp

	@CtrctRefTp.setter
	def CtrctRefTp(self, value):
		self._CtrctRefTp = value if value is not None else base_types.UninitialisedField(self, 'CtrctRefTp', DocumentType1Choice, True)

	@CtrctRefTp.deleter
	def CtrctRefTp(self):
		del self._CtrctRefTp
		self._CtrctRefTp = base_types.UninitialisedField(self, 'CtrctRefTp', DocumentType1Choice, True)

	@property
	def LtdPresntmntInd(self):
		return self._LtdPresntmntInd

	@LtdPresntmntInd.setter
	def LtdPresntmntInd(self, value):
		self._LtdPresntmntInd = value if value is not None else base_types.UninitialisedField(self, 'LtdPresntmntInd', TrueFalseIndicator, False)

	@LtdPresntmntInd.deleter
	def LtdPresntmntInd(self):
		del self._LtdPresntmntInd
		self._LtdPresntmntInd = base_types.UninitialisedField(self, 'LtdPresntmntInd', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtnReqDlvryPty', type=RTPPartyIdentification2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrInstr', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrIdTp', type=CustomerTypeRequest2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctFrmtTp', type=DocumentFormat2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrctRefTp', type=DocumentType1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LtdPresntmntInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
	))