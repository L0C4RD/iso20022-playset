import base_types
import OrganisationIdentification15Choice
import Max140Text

class TradeTransactionIdentification17(base_types._BaseFieldType):

	__slots__ = ["_RptSubmitgNtty", "_RptgCtrPty", "_TechRcrdId", "_NttyRspnsblForRpt"]
	@property
	def RptSubmitgNtty(self):
		return self._RptSubmitgNtty

	@RptSubmitgNtty.setter
	def RptSubmitgNtty(self, value):
		self._RptSubmitgNtty = value if type(value) != auto else self.make_default("RptSubmitgNtty")

	@RptSubmitgNtty.deleter
	def RptSubmitgNtty(self):
		del self._RptSubmitgNtty
		self._RptSubmitgNtty = None

	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if type(value) != auto else self.make_default("RptgCtrPty")

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	@property
	def NttyRspnsblForRpt(self):
		return self._NttyRspnsblForRpt

	@NttyRspnsblForRpt.setter
	def NttyRspnsblForRpt(self, value):
		self._NttyRspnsblForRpt = value if type(value) != auto else self.make_default("NttyRspnsblForRpt")

	@NttyRspnsblForRpt.deleter
	def NttyRspnsblForRpt(self):
		del self._NttyRspnsblForRpt
		self._NttyRspnsblForRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptSubmitgNtty', type=OrganisationIdentification15Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=OrganisationIdentification15Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyRspnsblForRpt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
	))

