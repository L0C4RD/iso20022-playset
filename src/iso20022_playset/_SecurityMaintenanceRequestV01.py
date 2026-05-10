from . import base_types
from ._UpdateType36Choice import UpdateType36Choice
from ._SupplementaryData1 import SupplementaryData1
from ._SecurityIdentification39 import SecurityIdentification39
from ._SecuritiesUpdateReason1Choice import SecuritiesUpdateReason1Choice
from ._MessageHeader1 import MessageHeader1

class SecurityMaintenanceRequestV01(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_UpdTp", "_UpdRsn", "_FinInstrmId", "_SplmtryData"]
	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if type(value) != base_types.auto else self.make_default("MsgHdr")

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = None

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
	def UpdRsn(self):
		return self._UpdRsn

	@UpdRsn.setter
	def UpdRsn(self, value):
		self._UpdRsn = value if type(value) != base_types.auto else self.make_default("UpdRsn")

	@UpdRsn.deleter
	def UpdRsn(self):
		del self._UpdRsn
		self._UpdRsn = None

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if type(value) != base_types.auto else self.make_default("UpdTp")

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification39, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UpdRsn', type=SecuritiesUpdateReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType36Choice, min=1, max=1, mutex_group=None, array=False),
	))

