# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Contact14
from . import ISODate
from . import MarketSpecificAttribute1
from . import PartyLockStatus1
from . import PartyName4
from . import PostalAddress28
from . import ResidenceType1Code
from . import SystemPartyIdentification9
from . import SystemPartyType1Choice
from . import SystemRestriction1
from . import TechnicalIdentification2Choice

class SystemParty7(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_ClsgDt", "_CtctDtls", "_LckSts", "_MktSpcfcAttr", "_Nm", "_OpngDt", "_PtyId", "_ResTp", "_Rstrctn", "_TechAdr", "_Tp"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', PostalAddress28, True)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', PostalAddress28, True)

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if value is not None else base_types.UninitialisedField(self, 'ClsgDt', ISODate, False)

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = base_types.UninitialisedField(self, 'ClsgDt', ISODate, False)

	@property
	def CtctDtls(self):
		return self._CtctDtls

	@CtctDtls.setter
	def CtctDtls(self, value):
		self._CtctDtls = value if value is not None else base_types.UninitialisedField(self, 'CtctDtls', Contact14, True)

	@CtctDtls.deleter
	def CtctDtls(self):
		del self._CtctDtls
		self._CtctDtls = base_types.UninitialisedField(self, 'CtctDtls', Contact14, True)

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
		self._MktSpcfcAttr = value if value is not None else base_types.UninitialisedField(self, 'MktSpcfcAttr', MarketSpecificAttribute1, True)

	@MktSpcfcAttr.deleter
	def MktSpcfcAttr(self):
		del self._MktSpcfcAttr
		self._MktSpcfcAttr = base_types.UninitialisedField(self, 'MktSpcfcAttr', MarketSpecificAttribute1, True)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', PartyName4, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', PartyName4, False)

	@property
	def OpngDt(self):
		return self._OpngDt

	@OpngDt.setter
	def OpngDt(self, value):
		self._OpngDt = value if value is not None else base_types.UninitialisedField(self, 'OpngDt', ISODate, False)

	@OpngDt.deleter
	def OpngDt(self):
		del self._OpngDt
		self._OpngDt = base_types.UninitialisedField(self, 'OpngDt', ISODate, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', SystemPartyIdentification9, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', SystemPartyIdentification9, False)

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
	def Rstrctn(self):
		return self._Rstrctn

	@Rstrctn.setter
	def Rstrctn(self, value):
		self._Rstrctn = value if value is not None else base_types.UninitialisedField(self, 'Rstrctn', SystemRestriction1, True)

	@Rstrctn.deleter
	def Rstrctn(self):
		del self._Rstrctn
		self._Rstrctn = base_types.UninitialisedField(self, 'Rstrctn', SystemRestriction1, True)

	@property
	def TechAdr(self):
		return self._TechAdr

	@TechAdr.setter
	def TechAdr(self, value):
		self._TechAdr = value if value is not None else base_types.UninitialisedField(self, 'TechAdr', TechnicalIdentification2Choice, True)

	@TechAdr.deleter
	def TechAdr(self):
		del self._TechAdr
		self._TechAdr = base_types.UninitialisedField(self, 'TechAdr', TechnicalIdentification2Choice, True)

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
		base_types.FieldEntry(name='Adr', type=PostalAddress28, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctDtls', type=Contact14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LckSts', type=PartyLockStatus1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktSpcfcAttr', type=MarketSpecificAttribute1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=PartyName4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ResTp', type=ResidenceType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rstrctn', type=SystemRestriction1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TechAdr', type=TechnicalIdentification2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=SystemPartyType1Choice, min=1, max=1, mutex_group=None, array=False),
	))