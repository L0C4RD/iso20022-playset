from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._Max35Text import Max35Text
from ._Pagination1 import Pagination1
from ._DisclosureRequestIdentification1 import DisclosureRequestIdentification1
from ._PartyIdentification219 import PartyIdentification219
from ._Disclosure3Choice import Disclosure3Choice

class ShareholdersIdentificationDisclosureResponseV03(base_types._BaseFieldType):

	__slots__ = ["_DsclsrRspnId", "_IssrDsclsrReqRef", "_RspndgIntrmy", "_DsclsrInf", "_SplmtryData", "_Pgntn"]
	@property
	def DsclsrInf(self):
		return self._DsclsrInf

	@DsclsrInf.setter
	def DsclsrInf(self, value):
		self._DsclsrInf = value if type(value) != base_types.auto else self.make_default("DsclsrInf")

	@DsclsrInf.deleter
	def DsclsrInf(self):
		del self._DsclsrInf
		self._DsclsrInf = None

	@property
	def DsclsrRspnId(self):
		return self._DsclsrRspnId

	@DsclsrRspnId.setter
	def DsclsrRspnId(self, value):
		self._DsclsrRspnId = value if type(value) != base_types.auto else self.make_default("DsclsrRspnId")

	@DsclsrRspnId.deleter
	def DsclsrRspnId(self):
		del self._DsclsrRspnId
		self._DsclsrRspnId = None

	@property
	def IssrDsclsrReqRef(self):
		return self._IssrDsclsrReqRef

	@IssrDsclsrReqRef.setter
	def IssrDsclsrReqRef(self, value):
		self._IssrDsclsrReqRef = value if type(value) != base_types.auto else self.make_default("IssrDsclsrReqRef")

	@IssrDsclsrReqRef.deleter
	def IssrDsclsrReqRef(self):
		del self._IssrDsclsrReqRef
		self._IssrDsclsrReqRef = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def RspndgIntrmy(self):
		return self._RspndgIntrmy

	@RspndgIntrmy.setter
	def RspndgIntrmy(self, value):
		self._RspndgIntrmy = value if type(value) != base_types.auto else self.make_default("RspndgIntrmy")

	@RspndgIntrmy.deleter
	def RspndgIntrmy(self):
		del self._RspndgIntrmy
		self._RspndgIntrmy = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DsclsrInf', type=Disclosure3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsclsrRspnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrDsclsrReqRef', type=DisclosureRequestIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspndgIntrmy', type=PartyIdentification219, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

