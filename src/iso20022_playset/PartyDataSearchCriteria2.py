from . import base_types
from .PartyIdentification136 import PartyIdentification136
from .ResidenceType1Code import ResidenceType1Code
from .DatePeriodSearch1Choice import DatePeriodSearch1Choice
from .SystemPartyType1Choice import SystemPartyType1Choice
from .PartyLockStatus1 import PartyLockStatus1
from .DateAndDateTimeSearch4Choice import DateAndDateTimeSearch4Choice
from .Max35Text import Max35Text

class PartyDataSearchCriteria2(base_types._BaseFieldType):

	__slots__ = ["_LckSts", "_PtyId", "_RstrctnId", "_ClsgDt", "_Tp", "_OpngDt", "_RstrctnIsseDt", "_ResTp", "_RspnsblPtyId"]
	@property
	def LckSts(self):
		return self._LckSts

	@LckSts.setter
	def LckSts(self, value):
		self._LckSts = value if type(value) != base_types.auto else self.make_default("LckSts")

	@LckSts.deleter
	def LckSts(self):
		del self._LckSts
		self._LckSts = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != base_types.auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	@property
	def RstrctnId(self):
		return self._RstrctnId

	@RstrctnId.setter
	def RstrctnId(self, value):
		self._RstrctnId = value if type(value) != base_types.auto else self.make_default("RstrctnId")

	@RstrctnId.deleter
	def RstrctnId(self):
		del self._RstrctnId
		self._RstrctnId = None

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if type(value) != base_types.auto else self.make_default("ClsgDt")

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def OpngDt(self):
		return self._OpngDt

	@OpngDt.setter
	def OpngDt(self, value):
		self._OpngDt = value if type(value) != base_types.auto else self.make_default("OpngDt")

	@OpngDt.deleter
	def OpngDt(self):
		del self._OpngDt
		self._OpngDt = None

	@property
	def RstrctnIsseDt(self):
		return self._RstrctnIsseDt

	@RstrctnIsseDt.setter
	def RstrctnIsseDt(self, value):
		self._RstrctnIsseDt = value if type(value) != base_types.auto else self.make_default("RstrctnIsseDt")

	@RstrctnIsseDt.deleter
	def RstrctnIsseDt(self):
		del self._RstrctnIsseDt
		self._RstrctnIsseDt = None

	@property
	def ResTp(self):
		return self._ResTp

	@ResTp.setter
	def ResTp(self, value):
		self._ResTp = value if type(value) != base_types.auto else self.make_default("ResTp")

	@ResTp.deleter
	def ResTp(self):
		del self._ResTp
		self._ResTp = None

	@property
	def RspnsblPtyId(self):
		return self._RspnsblPtyId

	@RspnsblPtyId.setter
	def RspnsblPtyId(self, value):
		self._RspnsblPtyId = value if type(value) != base_types.auto else self.make_default("RspnsblPtyId")

	@RspnsblPtyId.deleter
	def RspnsblPtyId(self):
		del self._RspnsblPtyId
		self._RspnsblPtyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LckSts', type=PartyLockStatus1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=SystemPartyType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngDt', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnIsseDt', type=DateAndDateTimeSearch4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ResTp', type=ResidenceType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPtyId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
	))

