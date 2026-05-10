import base_types
import Max500Text
import CustomerTypeRequest2
import RTPPartyIdentification2
import DocumentType1Choice
import DocumentFormat2Choice
import TrueFalseIndicator

class CreditorInvoice6(base_types._BaseFieldType):

	__slots__ = ["_LtdPresntmntInd", "_CtrctRefTp", "_ActvtnReqDlvryPty", "_CdtrInstr", "_CstmrIdTp", "_CtrctFrmtTp"]
	@property
	def LtdPresntmntInd(self):
		return self._LtdPresntmntInd

	@LtdPresntmntInd.setter
	def LtdPresntmntInd(self, value):
		self._LtdPresntmntInd = value if type(value) != auto else self.make_default("LtdPresntmntInd")

	@LtdPresntmntInd.deleter
	def LtdPresntmntInd(self):
		del self._LtdPresntmntInd
		self._LtdPresntmntInd = None

	@property
	def CtrctRefTp(self):
		return self._CtrctRefTp

	@CtrctRefTp.setter
	def CtrctRefTp(self, value):
		self._CtrctRefTp = value if type(value) != auto else self.make_default("CtrctRefTp")

	@CtrctRefTp.deleter
	def CtrctRefTp(self):
		del self._CtrctRefTp
		self._CtrctRefTp = None

	@property
	def ActvtnReqDlvryPty(self):
		return self._ActvtnReqDlvryPty

	@ActvtnReqDlvryPty.setter
	def ActvtnReqDlvryPty(self, value):
		self._ActvtnReqDlvryPty = value if type(value) != auto else self.make_default("ActvtnReqDlvryPty")

	@ActvtnReqDlvryPty.deleter
	def ActvtnReqDlvryPty(self):
		del self._ActvtnReqDlvryPty
		self._ActvtnReqDlvryPty = None

	@property
	def CdtrInstr(self):
		return self._CdtrInstr

	@CdtrInstr.setter
	def CdtrInstr(self, value):
		self._CdtrInstr = value if type(value) != auto else self.make_default("CdtrInstr")

	@CdtrInstr.deleter
	def CdtrInstr(self):
		del self._CdtrInstr
		self._CdtrInstr = None

	@property
	def CstmrIdTp(self):
		return self._CstmrIdTp

	@CstmrIdTp.setter
	def CstmrIdTp(self, value):
		self._CstmrIdTp = value if type(value) != auto else self.make_default("CstmrIdTp")

	@CstmrIdTp.deleter
	def CstmrIdTp(self):
		del self._CstmrIdTp
		self._CstmrIdTp = None

	@property
	def CtrctFrmtTp(self):
		return self._CtrctFrmtTp

	@CtrctFrmtTp.setter
	def CtrctFrmtTp(self, value):
		self._CtrctFrmtTp = value if type(value) != auto else self.make_default("CtrctFrmtTp")

	@CtrctFrmtTp.deleter
	def CtrctFrmtTp(self):
		del self._CtrctFrmtTp
		self._CtrctFrmtTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LtdPresntmntInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctRefTp', type=DocumentType1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ActvtnReqDlvryPty', type=RTPPartyIdentification2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrInstr', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrIdTp', type=CustomerTypeRequest2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctFrmtTp', type=DocumentFormat2Choice, min=0, max=None, mutex_group=None, array=True),
	))

