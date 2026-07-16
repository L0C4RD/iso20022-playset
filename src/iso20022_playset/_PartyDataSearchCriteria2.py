# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTimeSearch4Choice
from . import DatePeriodSearch1Choice
from . import Max35Text
from . import PartyIdentification136
from . import PartyLockStatus1
from . import ResidenceType1Code
from . import SystemPartyType1Choice

class PartyDataSearchCriteria2(base_types._BaseFieldType):

	__slots__ = ["_ClsgDt", "_LckSts", "_OpngDt", "_PtyId", "_ResTp", "_RspnsblPtyId", "_RstrctnId", "_RstrctnIsseDt", "_Tp"]
	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if value is not None else base_types.UninitialisedField(self, 'ClsgDt', DatePeriodSearch1Choice, False)

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = base_types.UninitialisedField(self, 'ClsgDt', DatePeriodSearch1Choice, False)

	@property
	def LckSts(self):
		return self._LckSts

	@LckSts.setter
	def LckSts(self, value):
		self._LckSts = value if value is not None else base_types.UninitialisedField(self, 'LckSts', PartyLockStatus1, False)

	@LckSts.deleter
	def LckSts(self):
		del self._LckSts
		self._LckSts = base_types.UninitialisedField(self, 'LckSts', PartyLockStatus1, False)

	@property
	def OpngDt(self):
		return self._OpngDt

	@OpngDt.setter
	def OpngDt(self, value):
		self._OpngDt = value if value is not None else base_types.UninitialisedField(self, 'OpngDt', DatePeriodSearch1Choice, False)

	@OpngDt.deleter
	def OpngDt(self):
		del self._OpngDt
		self._OpngDt = base_types.UninitialisedField(self, 'OpngDt', DatePeriodSearch1Choice, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PartyIdentification136, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PartyIdentification136, False)

	@property
	def ResTp(self):
		return self._ResTp

	@ResTp.setter
	def ResTp(self, value):
		self._ResTp = value if value is not None else base_types.UninitialisedField(self, 'ResTp', ResidenceType1Code, False)

	@ResTp.deleter
	def ResTp(self):
		del self._ResTp
		self._ResTp = base_types.UninitialisedField(self, 'ResTp', ResidenceType1Code, False)

	@property
	def RspnsblPtyId(self):
		return self._RspnsblPtyId

	@RspnsblPtyId.setter
	def RspnsblPtyId(self, value):
		self._RspnsblPtyId = value if value is not None else base_types.UninitialisedField(self, 'RspnsblPtyId', PartyIdentification136, False)

	@RspnsblPtyId.deleter
	def RspnsblPtyId(self):
		del self._RspnsblPtyId
		self._RspnsblPtyId = base_types.UninitialisedField(self, 'RspnsblPtyId', PartyIdentification136, False)

	@property
	def RstrctnId(self):
		return self._RstrctnId

	@RstrctnId.setter
	def RstrctnId(self, value):
		self._RstrctnId = value if value is not None else base_types.UninitialisedField(self, 'RstrctnId', Max35Text, False)

	@RstrctnId.deleter
	def RstrctnId(self):
		del self._RstrctnId
		self._RstrctnId = base_types.UninitialisedField(self, 'RstrctnId', Max35Text, False)

	@property
	def RstrctnIsseDt(self):
		return self._RstrctnIsseDt

	@RstrctnIsseDt.setter
	def RstrctnIsseDt(self, value):
		self._RstrctnIsseDt = value if value is not None else base_types.UninitialisedField(self, 'RstrctnIsseDt', DateAndDateTimeSearch4Choice, False)

	@RstrctnIsseDt.deleter
	def RstrctnIsseDt(self):
		del self._RstrctnIsseDt
		self._RstrctnIsseDt = base_types.UninitialisedField(self, 'RstrctnIsseDt', DateAndDateTimeSearch4Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', SystemPartyType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', SystemPartyType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsgDt', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LckSts', type=PartyLockStatus1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngDt', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ResTp', type=ResidenceType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPtyId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnIsseDt', type=DateAndDateTimeSearch4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=SystemPartyType1Choice, min=0, max=1, mutex_group=None, array=False),
	))