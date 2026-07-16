# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DisclosureRequestIdentification1
from . import Max35Text
from . import PartyIdentification215
from . import SupplementaryData1

class ShareholderIdentificationDisclosureResponseCancellationAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_DsclsrRspnId", "_IssrDsclsrReqRef", "_RspndgIntrmy", "_SplmtryData"]
	@property
	def DsclsrRspnId(self):
		return self._DsclsrRspnId

	@DsclsrRspnId.setter
	def DsclsrRspnId(self, value):
		self._DsclsrRspnId = value if value is not None else base_types.UninitialisedField(self, 'DsclsrRspnId', Max35Text, False)

	@DsclsrRspnId.deleter
	def DsclsrRspnId(self):
		del self._DsclsrRspnId
		self._DsclsrRspnId = base_types.UninitialisedField(self, 'DsclsrRspnId', Max35Text, False)

	@property
	def IssrDsclsrReqRef(self):
		return self._IssrDsclsrReqRef

	@IssrDsclsrReqRef.setter
	def IssrDsclsrReqRef(self, value):
		self._IssrDsclsrReqRef = value if value is not None else base_types.UninitialisedField(self, 'IssrDsclsrReqRef', DisclosureRequestIdentification1, False)

	@IssrDsclsrReqRef.deleter
	def IssrDsclsrReqRef(self):
		del self._IssrDsclsrReqRef
		self._IssrDsclsrReqRef = base_types.UninitialisedField(self, 'IssrDsclsrReqRef', DisclosureRequestIdentification1, False)

	@property
	def RspndgIntrmy(self):
		return self._RspndgIntrmy

	@RspndgIntrmy.setter
	def RspndgIntrmy(self, value):
		self._RspndgIntrmy = value if value is not None else base_types.UninitialisedField(self, 'RspndgIntrmy', PartyIdentification215, False)

	@RspndgIntrmy.deleter
	def RspndgIntrmy(self):
		del self._RspndgIntrmy
		self._RspndgIntrmy = base_types.UninitialisedField(self, 'RspndgIntrmy', PartyIdentification215, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DsclsrRspnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrDsclsrReqRef', type=DisclosureRequestIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspndgIntrmy', type=PartyIdentification215, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))