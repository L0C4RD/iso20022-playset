# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DateAndDateTimeSearch5Choice import DateAndDateTimeSearch5Choice
from ._InstructionQueryType1Code import InstructionQueryType1Code
from ._Max35Text import Max35Text
from ._ModificationProcessingStatus9Choice import ModificationProcessingStatus9Choice
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SystemPartyIdentification8 import SystemPartyIdentification8

class SecuritiesModificationQueryCriteria1(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_CreDtTm", "_InstrQryTp", "_ModReqId", "_MsgOrgtr", "_PrcgSts", "_SfkpgAcct"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def InstrQryTp(self):
		return self._InstrQryTp

	@InstrQryTp.setter
	def InstrQryTp(self, value):
		self._InstrQryTp = value if type(value) != base_types.auto else self.make_default("InstrQryTp")

	@InstrQryTp.deleter
	def InstrQryTp(self):
		del self._InstrQryTp
		self._InstrQryTp = None

	@property
	def ModReqId(self):
		return self._ModReqId

	@ModReqId.setter
	def ModReqId(self, value):
		self._ModReqId = value if type(value) != base_types.auto else self.make_default("ModReqId")

	@ModReqId.deleter
	def ModReqId(self):
		del self._ModReqId
		self._ModReqId = None

	@property
	def MsgOrgtr(self):
		return self._MsgOrgtr

	@MsgOrgtr.setter
	def MsgOrgtr(self, value):
		self._MsgOrgtr = value if type(value) != base_types.auto else self.make_default("MsgOrgtr")

	@MsgOrgtr.deleter
	def MsgOrgtr(self):
		del self._MsgOrgtr
		self._MsgOrgtr = None

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != base_types.auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=SystemPartyIdentification8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CreDtTm', type=DateAndDateTimeSearch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrQryTp', type=InstructionQueryType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModReqId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgOrgtr', type=SystemPartyIdentification8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgSts', type=ModificationProcessingStatus9Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=None, mutex_group=None, array=True),
	))