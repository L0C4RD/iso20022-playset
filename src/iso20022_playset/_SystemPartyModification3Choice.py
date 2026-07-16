# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Contact14
from . import MarketSpecificAttribute1
from . import PartyLockStatus1
from . import PartyName3
from . import PostalAddress28
from . import ResidenceType1Code
from . import SystemParty2
from . import SystemPartyIdentification10
from . import SystemRestriction1
from . import TechnicalIdentification2Choice

class SystemPartyModification3Choice(base_types._BaseFieldType):

	__slots__ = ["_CtctDtls", "_LckSts", "_MktSpcfcAttr", "_PtyAdr", "_PtyId", "_PtyNm", "_ResTp", "_SysPtyDt", "_SysRstrctn", "_TechAdr"]
	@property
	def CtctDtls(self):
		return self._CtctDtls

	@CtctDtls.setter
	def CtctDtls(self, value):
		self._CtctDtls = value if value is not None else base_types.UninitialisedField(self, 'CtctDtls', Contact14, False)

	@CtctDtls.deleter
	def CtctDtls(self):
		del self._CtctDtls
		self._CtctDtls = base_types.UninitialisedField(self, 'CtctDtls', Contact14, False)

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
	def MktSpcfcAttr(self):
		return self._MktSpcfcAttr

	@MktSpcfcAttr.setter
	def MktSpcfcAttr(self, value):
		self._MktSpcfcAttr = value if value is not None else base_types.UninitialisedField(self, 'MktSpcfcAttr', MarketSpecificAttribute1, False)

	@MktSpcfcAttr.deleter
	def MktSpcfcAttr(self):
		del self._MktSpcfcAttr
		self._MktSpcfcAttr = base_types.UninitialisedField(self, 'MktSpcfcAttr', MarketSpecificAttribute1, False)

	@property
	def PtyAdr(self):
		return self._PtyAdr

	@PtyAdr.setter
	def PtyAdr(self, value):
		self._PtyAdr = value if value is not None else base_types.UninitialisedField(self, 'PtyAdr', PostalAddress28, False)

	@PtyAdr.deleter
	def PtyAdr(self):
		del self._PtyAdr
		self._PtyAdr = base_types.UninitialisedField(self, 'PtyAdr', PostalAddress28, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', SystemPartyIdentification10, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', SystemPartyIdentification10, False)

	@property
	def PtyNm(self):
		return self._PtyNm

	@PtyNm.setter
	def PtyNm(self, value):
		self._PtyNm = value if value is not None else base_types.UninitialisedField(self, 'PtyNm', PartyName3, False)

	@PtyNm.deleter
	def PtyNm(self):
		del self._PtyNm
		self._PtyNm = base_types.UninitialisedField(self, 'PtyNm', PartyName3, False)

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
	def SysPtyDt(self):
		return self._SysPtyDt

	@SysPtyDt.setter
	def SysPtyDt(self, value):
		self._SysPtyDt = value if value is not None else base_types.UninitialisedField(self, 'SysPtyDt', SystemParty2, False)

	@SysPtyDt.deleter
	def SysPtyDt(self):
		del self._SysPtyDt
		self._SysPtyDt = base_types.UninitialisedField(self, 'SysPtyDt', SystemParty2, False)

	@property
	def SysRstrctn(self):
		return self._SysRstrctn

	@SysRstrctn.setter
	def SysRstrctn(self, value):
		self._SysRstrctn = value if value is not None else base_types.UninitialisedField(self, 'SysRstrctn', SystemRestriction1, False)

	@SysRstrctn.deleter
	def SysRstrctn(self):
		del self._SysRstrctn
		self._SysRstrctn = base_types.UninitialisedField(self, 'SysRstrctn', SystemRestriction1, False)

	@property
	def TechAdr(self):
		return self._TechAdr

	@TechAdr.setter
	def TechAdr(self, value):
		self._TechAdr = value if value is not None else base_types.UninitialisedField(self, 'TechAdr', TechnicalIdentification2Choice, False)

	@TechAdr.deleter
	def TechAdr(self):
		del self._TechAdr
		self._TechAdr = base_types.UninitialisedField(self, 'TechAdr', TechnicalIdentification2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtctDtls', type=Contact14, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LckSts', type=PartyLockStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MktSpcfcAttr', type=MarketSpecificAttribute1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PtyAdr', type=PostalAddress28, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PtyNm', type=PartyName3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ResTp', type=ResidenceType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SysPtyDt', type=SystemParty2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SysRstrctn', type=SystemRestriction1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TechAdr', type=TechnicalIdentification2Choice, min=0, max=1, mutex_group=1, array=False),
	))