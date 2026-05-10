from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .DisclosureRequestIdentification1 import DisclosureRequestIdentification1
from .PartyIdentification129Choice import PartyIdentification129Choice
from .DisclosureRequestCancellationReason1Code import DisclosureRequestCancellationReason1Code

class ShareholdersIdentificationDisclosureRequestCancellationAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_CxlRsn", "_Issr", "_IssrDsclsrReqRef"]
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

	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != base_types.auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CxlRsn', type=DisclosureRequestCancellationReason1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification129Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrDsclsrReqRef', type=DisclosureRequestIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

