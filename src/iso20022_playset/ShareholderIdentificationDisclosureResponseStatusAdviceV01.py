from . import base_types
import PartyIdentification215
import DisclosureRequestIdentification1
import SupplementaryData1
import ResponseProcessingStatus1Choice
import Max35Text

class ShareholderIdentificationDisclosureResponseStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_RspndgIntrmy", "_RspnRcptnSts", "_DsclsrRspnId", "_IssrDsclsrReqRef"]
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
	def RspndgIntrmy(self):
		return self._RspndgIntrmy

	@RspndgIntrmy.setter
	def RspndgIntrmy(self, value):
		self._RspndgIntrmy = value if type(value) != auto else self.make_default("RspndgIntrmy")

	@RspndgIntrmy.deleter
	def RspndgIntrmy(self):
		del self._RspndgIntrmy
		self._RspndgIntrmy = None

	@property
	def RspnRcptnSts(self):
		return self._RspnRcptnSts

	@RspnRcptnSts.setter
	def RspnRcptnSts(self, value):
		self._RspnRcptnSts = value if type(value) != auto else self.make_default("RspnRcptnSts")

	@RspnRcptnSts.deleter
	def RspnRcptnSts(self):
		del self._RspnRcptnSts
		self._RspnRcptnSts = None

	@property
	def DsclsrRspnId(self):
		return self._DsclsrRspnId

	@DsclsrRspnId.setter
	def DsclsrRspnId(self, value):
		self._DsclsrRspnId = value if type(value) != auto else self.make_default("DsclsrRspnId")

	@DsclsrRspnId.deleter
	def DsclsrRspnId(self):
		del self._DsclsrRspnId
		self._DsclsrRspnId = None

	@property
	def IssrDsclsrReqRef(self):
		return self._IssrDsclsrReqRef

	@IssrDsclsrReqRef.setter
	def IssrDsclsrReqRef(self, value):
		self._IssrDsclsrReqRef = value if type(value) != auto else self.make_default("IssrDsclsrReqRef")

	@IssrDsclsrReqRef.deleter
	def IssrDsclsrReqRef(self):
		del self._IssrDsclsrReqRef
		self._IssrDsclsrReqRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RspndgIntrmy', type=PartyIdentification215, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnRcptnSts', type=ResponseProcessingStatus1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsclsrRspnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrDsclsrReqRef', type=DisclosureRequestIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

