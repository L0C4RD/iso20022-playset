from . import base_types
from ._Statement59 import Statement59
from ._MessageIdentification1 import MessageIdentification1
from ._PartyIdentification100 import PartyIdentification100
from ._Pagination import Pagination
from ._SupplementaryData1 import SupplementaryData1
from ._SafekeepingAccount7 import SafekeepingAccount7

class SecuritiesBalanceTransparencyReportV02(base_types._BaseFieldType):

	__slots__ = ["_SndrId", "_StmtGnlDtls", "_Pgntn", "_MsgId", "_SplmtryData", "_SfkpgAcctAndHldgs", "_RcvrId"]
	@property
	def SndrId(self):
		return self._SndrId

	@SndrId.setter
	def SndrId(self, value):
		self._SndrId = value if type(value) != base_types.auto else self.make_default("SndrId")

	@SndrId.deleter
	def SndrId(self):
		del self._SndrId
		self._SndrId = None

	@property
	def StmtGnlDtls(self):
		return self._StmtGnlDtls

	@StmtGnlDtls.setter
	def StmtGnlDtls(self, value):
		self._StmtGnlDtls = value if type(value) != base_types.auto else self.make_default("StmtGnlDtls")

	@StmtGnlDtls.deleter
	def StmtGnlDtls(self):
		del self._StmtGnlDtls
		self._StmtGnlDtls = None

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
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

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
	def SfkpgAcctAndHldgs(self):
		return self._SfkpgAcctAndHldgs

	@SfkpgAcctAndHldgs.setter
	def SfkpgAcctAndHldgs(self, value):
		self._SfkpgAcctAndHldgs = value if type(value) != base_types.auto else self.make_default("SfkpgAcctAndHldgs")

	@SfkpgAcctAndHldgs.deleter
	def SfkpgAcctAndHldgs(self):
		del self._SfkpgAcctAndHldgs
		self._SfkpgAcctAndHldgs = None

	@property
	def RcvrId(self):
		return self._RcvrId

	@RcvrId.setter
	def RcvrId(self, value):
		self._RcvrId = value if type(value) != base_types.auto else self.make_default("RcvrId")

	@RcvrId.deleter
	def RcvrId(self):
		del self._RcvrId
		self._RcvrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SndrId', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement59, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcctAndHldgs', type=SafekeepingAccount7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcvrId', type=PartyIdentification100, min=0, max=1, mutex_group=None, array=False),
	))

