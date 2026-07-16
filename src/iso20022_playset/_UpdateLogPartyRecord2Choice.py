# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UpdateLogAddress2
from . import UpdateLogContact2
from . import UpdateLogDate1
from . import UpdateLogMarketSpecificAttribute1
from . import UpdateLogPartyLockStatus1
from . import UpdateLogPartyName1
from . import UpdateLogProprietary1
from . import UpdateLogResidenceType1
from . import UpdateLogRestriction1
from . import UpdateLogSystemPartyType1
from . import UpdateLogTechnicalAddress1

class UpdateLogPartyRecord2Choice(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_ClsgDt", "_CtctDtls", "_LckSts", "_MktSpcfcAttr", "_Nm", "_OpngDt", "_Othr", "_ResTp", "_Rstrctn", "_TechAdr", "_Tp"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', UpdateLogAddress2, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', UpdateLogAddress2, False)

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if value is not None else base_types.UninitialisedField(self, 'ClsgDt', UpdateLogDate1, False)

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = base_types.UninitialisedField(self, 'ClsgDt', UpdateLogDate1, False)

	@property
	def CtctDtls(self):
		return self._CtctDtls

	@CtctDtls.setter
	def CtctDtls(self, value):
		self._CtctDtls = value if value is not None else base_types.UninitialisedField(self, 'CtctDtls', UpdateLogContact2, False)

	@CtctDtls.deleter
	def CtctDtls(self):
		del self._CtctDtls
		self._CtctDtls = base_types.UninitialisedField(self, 'CtctDtls', UpdateLogContact2, False)

	@property
	def LckSts(self):
		return self._LckSts

	@LckSts.setter
	def LckSts(self, value):
		self._LckSts = value if value is not None else base_types.UninitialisedField(self, 'LckSts', UpdateLogPartyLockStatus1, False)

	@LckSts.deleter
	def LckSts(self):
		del self._LckSts
		self._LckSts = base_types.UninitialisedField(self, 'LckSts', UpdateLogPartyLockStatus1, False)

	@property
	def MktSpcfcAttr(self):
		return self._MktSpcfcAttr

	@MktSpcfcAttr.setter
	def MktSpcfcAttr(self, value):
		self._MktSpcfcAttr = value if value is not None else base_types.UninitialisedField(self, 'MktSpcfcAttr', UpdateLogMarketSpecificAttribute1, False)

	@MktSpcfcAttr.deleter
	def MktSpcfcAttr(self):
		del self._MktSpcfcAttr
		self._MktSpcfcAttr = base_types.UninitialisedField(self, 'MktSpcfcAttr', UpdateLogMarketSpecificAttribute1, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', UpdateLogPartyName1, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', UpdateLogPartyName1, False)

	@property
	def OpngDt(self):
		return self._OpngDt

	@OpngDt.setter
	def OpngDt(self, value):
		self._OpngDt = value if value is not None else base_types.UninitialisedField(self, 'OpngDt', UpdateLogDate1, False)

	@OpngDt.deleter
	def OpngDt(self):
		del self._OpngDt
		self._OpngDt = base_types.UninitialisedField(self, 'OpngDt', UpdateLogDate1, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', UpdateLogProprietary1, True)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', UpdateLogProprietary1, True)

	@property
	def ResTp(self):
		return self._ResTp

	@ResTp.setter
	def ResTp(self, value):
		self._ResTp = value if value is not None else base_types.UninitialisedField(self, 'ResTp', UpdateLogResidenceType1, False)

	@ResTp.deleter
	def ResTp(self):
		del self._ResTp
		self._ResTp = base_types.UninitialisedField(self, 'ResTp', UpdateLogResidenceType1, False)

	@property
	def Rstrctn(self):
		return self._Rstrctn

	@Rstrctn.setter
	def Rstrctn(self, value):
		self._Rstrctn = value if value is not None else base_types.UninitialisedField(self, 'Rstrctn', UpdateLogRestriction1, False)

	@Rstrctn.deleter
	def Rstrctn(self):
		del self._Rstrctn
		self._Rstrctn = base_types.UninitialisedField(self, 'Rstrctn', UpdateLogRestriction1, False)

	@property
	def TechAdr(self):
		return self._TechAdr

	@TechAdr.setter
	def TechAdr(self, value):
		self._TechAdr = value if value is not None else base_types.UninitialisedField(self, 'TechAdr', UpdateLogTechnicalAddress1, False)

	@TechAdr.deleter
	def TechAdr(self):
		del self._TechAdr
		self._TechAdr = base_types.UninitialisedField(self, 'TechAdr', UpdateLogTechnicalAddress1, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', UpdateLogSystemPartyType1, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', UpdateLogSystemPartyType1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=UpdateLogAddress2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ClsgDt', type=UpdateLogDate1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CtctDtls', type=UpdateLogContact2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LckSts', type=UpdateLogPartyLockStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MktSpcfcAttr', type=UpdateLogMarketSpecificAttribute1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nm', type=UpdateLogPartyName1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OpngDt', type=UpdateLogDate1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=UpdateLogProprietary1, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='ResTp', type=UpdateLogResidenceType1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rstrctn', type=UpdateLogRestriction1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TechAdr', type=UpdateLogTechnicalAddress1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tp', type=UpdateLogSystemPartyType1, min=0, max=1, mutex_group=1, array=False),
	))