# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat58Choice
from . import InvestorTypeIdentification1
from . import ParticipationMethod3Choice
from . import YesNoIndicator

class ParticipationMethod3(base_types._BaseFieldType):

	__slots__ = ["_AttndeeEmailReqrdInd", "_InvstrTpId", "_IssrDdlnForVtng", "_PrtcptnMtd", "_RspnDdlnForVtng", "_SpprtdByAcctSvcr"]
	@property
	def AttndeeEmailReqrdInd(self):
		return self._AttndeeEmailReqrdInd

	@AttndeeEmailReqrdInd.setter
	def AttndeeEmailReqrdInd(self, value):
		self._AttndeeEmailReqrdInd = value if value is not None else base_types.UninitialisedField(self, 'AttndeeEmailReqrdInd', YesNoIndicator, False)

	@AttndeeEmailReqrdInd.deleter
	def AttndeeEmailReqrdInd(self):
		del self._AttndeeEmailReqrdInd
		self._AttndeeEmailReqrdInd = base_types.UninitialisedField(self, 'AttndeeEmailReqrdInd', YesNoIndicator, False)

	@property
	def InvstrTpId(self):
		return self._InvstrTpId

	@InvstrTpId.setter
	def InvstrTpId(self, value):
		self._InvstrTpId = value if value is not None else base_types.UninitialisedField(self, 'InvstrTpId', InvestorTypeIdentification1, True)

	@InvstrTpId.deleter
	def InvstrTpId(self):
		del self._InvstrTpId
		self._InvstrTpId = base_types.UninitialisedField(self, 'InvstrTpId', InvestorTypeIdentification1, True)

	@property
	def IssrDdlnForVtng(self):
		return self._IssrDdlnForVtng

	@IssrDdlnForVtng.setter
	def IssrDdlnForVtng(self, value):
		self._IssrDdlnForVtng = value if value is not None else base_types.UninitialisedField(self, 'IssrDdlnForVtng', DateFormat58Choice, False)

	@IssrDdlnForVtng.deleter
	def IssrDdlnForVtng(self):
		del self._IssrDdlnForVtng
		self._IssrDdlnForVtng = base_types.UninitialisedField(self, 'IssrDdlnForVtng', DateFormat58Choice, False)

	@property
	def PrtcptnMtd(self):
		return self._PrtcptnMtd

	@PrtcptnMtd.setter
	def PrtcptnMtd(self, value):
		self._PrtcptnMtd = value if value is not None else base_types.UninitialisedField(self, 'PrtcptnMtd', ParticipationMethod3Choice, False)

	@PrtcptnMtd.deleter
	def PrtcptnMtd(self):
		del self._PrtcptnMtd
		self._PrtcptnMtd = base_types.UninitialisedField(self, 'PrtcptnMtd', ParticipationMethod3Choice, False)

	@property
	def RspnDdlnForVtng(self):
		return self._RspnDdlnForVtng

	@RspnDdlnForVtng.setter
	def RspnDdlnForVtng(self, value):
		self._RspnDdlnForVtng = value if value is not None else base_types.UninitialisedField(self, 'RspnDdlnForVtng', DateFormat58Choice, False)

	@RspnDdlnForVtng.deleter
	def RspnDdlnForVtng(self):
		del self._RspnDdlnForVtng
		self._RspnDdlnForVtng = base_types.UninitialisedField(self, 'RspnDdlnForVtng', DateFormat58Choice, False)

	@property
	def SpprtdByAcctSvcr(self):
		return self._SpprtdByAcctSvcr

	@SpprtdByAcctSvcr.setter
	def SpprtdByAcctSvcr(self, value):
		self._SpprtdByAcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'SpprtdByAcctSvcr', YesNoIndicator, False)

	@SpprtdByAcctSvcr.deleter
	def SpprtdByAcctSvcr(self):
		del self._SpprtdByAcctSvcr
		self._SpprtdByAcctSvcr = base_types.UninitialisedField(self, 'SpprtdByAcctSvcr', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttndeeEmailReqrdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrTpId', type=InvestorTypeIdentification1, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='IssrDdlnForVtng', type=DateFormat58Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcptnMtd', type=ParticipationMethod3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnDdlnForVtng', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpprtdByAcctSvcr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))