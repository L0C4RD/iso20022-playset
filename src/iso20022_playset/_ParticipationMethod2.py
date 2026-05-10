from . import base_types
from ._DateFormat58Choice import DateFormat58Choice
from ._ParticipationMethod3Choice import ParticipationMethod3Choice
from ._YesNoIndicator import YesNoIndicator

class ParticipationMethod2(base_types._BaseFieldType):

	__slots__ = ["_IssrDdlnForVtng", "_PrtcptnMtd", "_RspnDdlnForVtng", "_SpprtdByAcctSvcr"]
	@property
	def IssrDdlnForVtng(self):
		return self._IssrDdlnForVtng

	@IssrDdlnForVtng.setter
	def IssrDdlnForVtng(self, value):
		self._IssrDdlnForVtng = value if type(value) != base_types.auto else self.make_default("IssrDdlnForVtng")

	@IssrDdlnForVtng.deleter
	def IssrDdlnForVtng(self):
		del self._IssrDdlnForVtng
		self._IssrDdlnForVtng = None

	@property
	def PrtcptnMtd(self):
		return self._PrtcptnMtd

	@PrtcptnMtd.setter
	def PrtcptnMtd(self, value):
		self._PrtcptnMtd = value if type(value) != base_types.auto else self.make_default("PrtcptnMtd")

	@PrtcptnMtd.deleter
	def PrtcptnMtd(self):
		del self._PrtcptnMtd
		self._PrtcptnMtd = None

	@property
	def RspnDdlnForVtng(self):
		return self._RspnDdlnForVtng

	@RspnDdlnForVtng.setter
	def RspnDdlnForVtng(self, value):
		self._RspnDdlnForVtng = value if type(value) != base_types.auto else self.make_default("RspnDdlnForVtng")

	@RspnDdlnForVtng.deleter
	def RspnDdlnForVtng(self):
		del self._RspnDdlnForVtng
		self._RspnDdlnForVtng = None

	@property
	def SpprtdByAcctSvcr(self):
		return self._SpprtdByAcctSvcr

	@SpprtdByAcctSvcr.setter
	def SpprtdByAcctSvcr(self, value):
		self._SpprtdByAcctSvcr = value if type(value) != base_types.auto else self.make_default("SpprtdByAcctSvcr")

	@SpprtdByAcctSvcr.deleter
	def SpprtdByAcctSvcr(self):
		del self._SpprtdByAcctSvcr
		self._SpprtdByAcctSvcr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IssrDdlnForVtng', type=DateFormat58Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcptnMtd', type=ParticipationMethod3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnDdlnForVtng', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpprtdByAcctSvcr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

