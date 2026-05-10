from . import base_types
from .UpdateLogSystemPartyType1 import UpdateLogSystemPartyType1
from .UpdateLogPartyLockStatus1 import UpdateLogPartyLockStatus1
from .UpdateLogAddress2 import UpdateLogAddress2
from .UpdateLogPartyName1 import UpdateLogPartyName1
from .UpdateLogResidenceType1 import UpdateLogResidenceType1
from .UpdateLogDate1 import UpdateLogDate1
from .UpdateLogRestriction1 import UpdateLogRestriction1
from .UpdateLogTechnicalAddress1 import UpdateLogTechnicalAddress1
from .UpdateLogContact2 import UpdateLogContact2
from .UpdateLogProprietary1 import UpdateLogProprietary1
from .UpdateLogMarketSpecificAttribute1 import UpdateLogMarketSpecificAttribute1

class UpdateLogPartyRecord2Choice(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_TechAdr", "_Adr", "_OpngDt", "_LckSts", "_CtctDtls", "_Othr", "_ClsgDt", "_Nm", "_Rstrctn", "_MktSpcfcAttr", "_ResTp"]
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
	def TechAdr(self):
		return self._TechAdr

	@TechAdr.setter
	def TechAdr(self, value):
		self._TechAdr = value if type(value) != base_types.auto else self.make_default("TechAdr")

	@TechAdr.deleter
	def TechAdr(self):
		del self._TechAdr
		self._TechAdr = None

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != base_types.auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

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
	def CtctDtls(self):
		return self._CtctDtls

	@CtctDtls.setter
	def CtctDtls(self, value):
		self._CtctDtls = value if type(value) != base_types.auto else self.make_default("CtctDtls")

	@CtctDtls.deleter
	def CtctDtls(self):
		del self._CtctDtls
		self._CtctDtls = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

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
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def Rstrctn(self):
		return self._Rstrctn

	@Rstrctn.setter
	def Rstrctn(self, value):
		self._Rstrctn = value if type(value) != base_types.auto else self.make_default("Rstrctn")

	@Rstrctn.deleter
	def Rstrctn(self):
		del self._Rstrctn
		self._Rstrctn = None

	@property
	def MktSpcfcAttr(self):
		return self._MktSpcfcAttr

	@MktSpcfcAttr.setter
	def MktSpcfcAttr(self, value):
		self._MktSpcfcAttr = value if type(value) != base_types.auto else self.make_default("MktSpcfcAttr")

	@MktSpcfcAttr.deleter
	def MktSpcfcAttr(self):
		del self._MktSpcfcAttr
		self._MktSpcfcAttr = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=UpdateLogSystemPartyType1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TechAdr', type=UpdateLogTechnicalAddress1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Adr', type=UpdateLogAddress2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OpngDt', type=UpdateLogDate1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LckSts', type=UpdateLogPartyLockStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CtctDtls', type=UpdateLogContact2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=UpdateLogProprietary1, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='ClsgDt', type=UpdateLogDate1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nm', type=UpdateLogPartyName1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rstrctn', type=UpdateLogRestriction1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MktSpcfcAttr', type=UpdateLogMarketSpecificAttribute1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ResTp', type=UpdateLogResidenceType1, min=0, max=1, mutex_group=1, array=False),
	))

