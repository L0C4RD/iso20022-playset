from . import base_types
from .ResidenceType1Code import ResidenceType1Code
from .PartyName3 import PartyName3
from .MarketSpecificAttribute1 import MarketSpecificAttribute1
from .SystemRestriction1 import SystemRestriction1
from .PartyLockStatus1 import PartyLockStatus1
from .SystemPartyIdentification10 import SystemPartyIdentification10
from .PostalAddress28 import PostalAddress28
from .SystemParty2 import SystemParty2
from .TechnicalIdentification2Choice import TechnicalIdentification2Choice
from .Contact14 import Contact14

class SystemPartyModification3Choice(base_types._BaseFieldType):

	__slots__ = ["_PtyNm", "_TechAdr", "_PtyAdr", "_PtyId", "_ResTp", "_MktSpcfcAttr", "_SysPtyDt", "_LckSts", "_CtctDtls", "_SysRstrctn"]
	@property
	def PtyNm(self):
		return self._PtyNm

	@PtyNm.setter
	def PtyNm(self, value):
		self._PtyNm = value if type(value) != auto else self.make_default("PtyNm")

	@PtyNm.deleter
	def PtyNm(self):
		del self._PtyNm
		self._PtyNm = None

	@property
	def TechAdr(self):
		return self._TechAdr

	@TechAdr.setter
	def TechAdr(self, value):
		self._TechAdr = value if type(value) != auto else self.make_default("TechAdr")

	@TechAdr.deleter
	def TechAdr(self):
		del self._TechAdr
		self._TechAdr = None

	@property
	def PtyAdr(self):
		return self._PtyAdr

	@PtyAdr.setter
	def PtyAdr(self, value):
		self._PtyAdr = value if type(value) != auto else self.make_default("PtyAdr")

	@PtyAdr.deleter
	def PtyAdr(self):
		del self._PtyAdr
		self._PtyAdr = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	@property
	def ResTp(self):
		return self._ResTp

	@ResTp.setter
	def ResTp(self, value):
		self._ResTp = value if type(value) != auto else self.make_default("ResTp")

	@ResTp.deleter
	def ResTp(self):
		del self._ResTp
		self._ResTp = None

	@property
	def MktSpcfcAttr(self):
		return self._MktSpcfcAttr

	@MktSpcfcAttr.setter
	def MktSpcfcAttr(self, value):
		self._MktSpcfcAttr = value if type(value) != auto else self.make_default("MktSpcfcAttr")

	@MktSpcfcAttr.deleter
	def MktSpcfcAttr(self):
		del self._MktSpcfcAttr
		self._MktSpcfcAttr = None

	@property
	def SysPtyDt(self):
		return self._SysPtyDt

	@SysPtyDt.setter
	def SysPtyDt(self, value):
		self._SysPtyDt = value if type(value) != auto else self.make_default("SysPtyDt")

	@SysPtyDt.deleter
	def SysPtyDt(self):
		del self._SysPtyDt
		self._SysPtyDt = None

	@property
	def LckSts(self):
		return self._LckSts

	@LckSts.setter
	def LckSts(self, value):
		self._LckSts = value if type(value) != auto else self.make_default("LckSts")

	@LckSts.deleter
	def LckSts(self):
		del self._LckSts
		self._LckSts = None

	@property
	def CtctDtls(self):
		return self._CtctDtls

	@CtctDtls.setter
	def CtctDtls(self, value):
		self._CtctDtls = value if type(value) != auto else self.make_default("CtctDtls")

	@CtctDtls.deleter
	def CtctDtls(self):
		del self._CtctDtls
		self._CtctDtls = None

	@property
	def SysRstrctn(self):
		return self._SysRstrctn

	@SysRstrctn.setter
	def SysRstrctn(self, value):
		self._SysRstrctn = value if type(value) != auto else self.make_default("SysRstrctn")

	@SysRstrctn.deleter
	def SysRstrctn(self):
		del self._SysRstrctn
		self._SysRstrctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PtyNm', type=PartyName3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TechAdr', type=TechnicalIdentification2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PtyAdr', type=PostalAddress28, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ResTp', type=ResidenceType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MktSpcfcAttr', type=MarketSpecificAttribute1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SysPtyDt', type=SystemParty2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LckSts', type=PartyLockStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CtctDtls', type=Contact14, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SysRstrctn', type=SystemRestriction1, min=0, max=1, mutex_group=1, array=False),
	))

