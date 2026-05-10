from . import base_types
import Max10KBinary
import Max140Text
import MerchantCategoryCodeIdentifier
import CreditorServiceEnrolment1
import RTPPartyIdentification2

class CreditorEnrolment5(base_types._BaseFieldType):

	__slots__ = ["_Enrlmnt", "_MrchntCtgyCd", "_Cdtr", "_CdtrLogo", "_CdtrTradgNm", "_UltmtCdtr"]
	@property
	def Enrlmnt(self):
		return self._Enrlmnt

	@Enrlmnt.setter
	def Enrlmnt(self, value):
		self._Enrlmnt = value if type(value) != auto else self.make_default("Enrlmnt")

	@Enrlmnt.deleter
	def Enrlmnt(self):
		del self._Enrlmnt
		self._Enrlmnt = None

	@property
	def MrchntCtgyCd(self):
		return self._MrchntCtgyCd

	@MrchntCtgyCd.setter
	def MrchntCtgyCd(self, value):
		self._MrchntCtgyCd = value if type(value) != auto else self.make_default("MrchntCtgyCd")

	@MrchntCtgyCd.deleter
	def MrchntCtgyCd(self):
		del self._MrchntCtgyCd
		self._MrchntCtgyCd = None

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if type(value) != auto else self.make_default("Cdtr")

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = None

	@property
	def CdtrLogo(self):
		return self._CdtrLogo

	@CdtrLogo.setter
	def CdtrLogo(self, value):
		self._CdtrLogo = value if type(value) != auto else self.make_default("CdtrLogo")

	@CdtrLogo.deleter
	def CdtrLogo(self):
		del self._CdtrLogo
		self._CdtrLogo = None

	@property
	def CdtrTradgNm(self):
		return self._CdtrTradgNm

	@CdtrTradgNm.setter
	def CdtrTradgNm(self, value):
		self._CdtrTradgNm = value if type(value) != auto else self.make_default("CdtrTradgNm")

	@CdtrTradgNm.deleter
	def CdtrTradgNm(self):
		del self._CdtrTradgNm
		self._CdtrTradgNm = None

	@property
	def UltmtCdtr(self):
		return self._UltmtCdtr

	@UltmtCdtr.setter
	def UltmtCdtr(self, value):
		self._UltmtCdtr = value if type(value) != auto else self.make_default("UltmtCdtr")

	@UltmtCdtr.deleter
	def UltmtCdtr(self):
		del self._UltmtCdtr
		self._UltmtCdtr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Enrlmnt', type=CreditorServiceEnrolment1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgyCd', type=MerchantCategoryCodeIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=RTPPartyIdentification2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrLogo', type=Max10KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrTradgNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtCdtr', type=RTPPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
	))

