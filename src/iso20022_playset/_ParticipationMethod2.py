# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat58Choice
from . import ParticipationMethod3Choice
from . import YesNoIndicator

class ParticipationMethod2(base_types._BaseFieldType):

	__slots__ = ["_IssrDdlnForVtng", "_PrtcptnMtd", "_RspnDdlnForVtng", "_SpprtdByAcctSvcr"]
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
		base_types.FieldEntry(name='IssrDdlnForVtng', type=DateFormat58Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcptnMtd', type=ParticipationMethod3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnDdlnForVtng', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpprtdByAcctSvcr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))