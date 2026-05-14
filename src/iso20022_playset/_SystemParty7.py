# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Contact14 import Contact14
from ._ISODate import ISODate
from ._MarketSpecificAttribute1 import MarketSpecificAttribute1
from ._PartyLockStatus1 import PartyLockStatus1
from ._PartyName4 import PartyName4
from ._PostalAddress28 import PostalAddress28
from ._ResidenceType1Code import ResidenceType1Code
from ._SystemPartyIdentification9 import SystemPartyIdentification9
from ._SystemPartyType1Choice import SystemPartyType1Choice
from ._SystemRestriction1 import SystemRestriction1
from ._TechnicalIdentification2Choice import TechnicalIdentification2Choice

class SystemParty7(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_ClsgDt", "_CtctDtls", "_LckSts", "_MktSpcfcAttr", "_Nm", "_OpngDt", "_PtyId", "_ResTp", "_Rstrctn", "_TechAdr", "_Tp"]
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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

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