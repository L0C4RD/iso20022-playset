# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageIdentification1
from . import Pagination
from . import PartyIdentification100
from . import SafekeepingAccount7
from . import Statement59
from . import SupplementaryData1

class SecuritiesBalanceTransparencyReportV02(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_Pgntn", "_RcvrId", "_SfkpgAcctAndHldgs", "_SndrId", "_SplmtryData", "_StmtGnlDtls"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination, False)

	@property
	def RcvrId(self):
		return self._RcvrId

	@RcvrId.setter
	def RcvrId(self, value):
		self._RcvrId = value if value is not None else base_types.UninitialisedField(self, 'RcvrId', PartyIdentification100, False)

	@RcvrId.deleter
	def RcvrId(self):
		del self._RcvrId
		self._RcvrId = base_types.UninitialisedField(self, 'RcvrId', PartyIdentification100, False)

	@property
	def SfkpgAcctAndHldgs(self):
		return self._SfkpgAcctAndHldgs

	@SfkpgAcctAndHldgs.setter
	def SfkpgAcctAndHldgs(self, value):
		self._SfkpgAcctAndHldgs = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcctAndHldgs', SafekeepingAccount7, True)

	@SfkpgAcctAndHldgs.deleter
	def SfkpgAcctAndHldgs(self):
		del self._SfkpgAcctAndHldgs
		self._SfkpgAcctAndHldgs = base_types.UninitialisedField(self, 'SfkpgAcctAndHldgs', SafekeepingAccount7, True)

	@property
	def SndrId(self):
		return self._SndrId

	@SndrId.setter
	def SndrId(self, value):
		self._SndrId = value if value is not None else base_types.UninitialisedField(self, 'SndrId', PartyIdentification100, False)

	@SndrId.deleter
	def SndrId(self):
		del self._SndrId
		self._SndrId = base_types.UninitialisedField(self, 'SndrId', PartyIdentification100, False)

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

	@property
	def StmtGnlDtls(self):
		return self._StmtGnlDtls

	@StmtGnlDtls.setter
	def StmtGnlDtls(self, value):
		self._StmtGnlDtls = value if value is not None else base_types.UninitialisedField(self, 'StmtGnlDtls', Statement59, False)

	@StmtGnlDtls.deleter
	def StmtGnlDtls(self):
		del self._StmtGnlDtls
		self._StmtGnlDtls = base_types.UninitialisedField(self, 'StmtGnlDtls', Statement59, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrId', type=PartyIdentification100, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcctAndHldgs', type=SafekeepingAccount7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SndrId', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement59, min=1, max=1, mutex_group=None, array=False),
	))