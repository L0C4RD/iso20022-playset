from . import base_types
from ._InvestmentAccountOwnershipInformation16 import InvestmentAccountOwnershipInformation16
from ._AccountParties12Choice import AccountParties12Choice
from ._ExtendedParty14 import ExtendedParty14
from ._RegisteredShareholderName1Choice import RegisteredShareholderName1Choice

class AccountParties17(base_types._BaseFieldType):

	__slots__ = ["_Admstr", "_Sttlr", "_ScndryOwnr", "_PrncplAcctPty", "_Grntr", "_RegdShrhldrNm", "_OthrPty", "_Prtctr", "_SucssrOnDth", "_Bnfcry", "_CtdnForMnr", "_LglGuardn", "_SnrMggOffcl", "_PwrOfAttny"]
	@property
	def Admstr(self):
		return self._Admstr

	@Admstr.setter
	def Admstr(self, value):
		self._Admstr = value if type(value) != base_types.auto else self.make_default("Admstr")

	@Admstr.deleter
	def Admstr(self):
		del self._Admstr
		self._Admstr = None

	@property
	def Sttlr(self):
		return self._Sttlr

	@Sttlr.setter
	def Sttlr(self, value):
		self._Sttlr = value if type(value) != base_types.auto else self.make_default("Sttlr")

	@Sttlr.deleter
	def Sttlr(self):
		del self._Sttlr
		self._Sttlr = None

	@property
	def ScndryOwnr(self):
		return self._ScndryOwnr

	@ScndryOwnr.setter
	def ScndryOwnr(self, value):
		self._ScndryOwnr = value if type(value) != base_types.auto else self.make_default("ScndryOwnr")

	@ScndryOwnr.deleter
	def ScndryOwnr(self):
		del self._ScndryOwnr
		self._ScndryOwnr = None

	@property
	def PrncplAcctPty(self):
		return self._PrncplAcctPty

	@PrncplAcctPty.setter
	def PrncplAcctPty(self, value):
		self._PrncplAcctPty = value if type(value) != base_types.auto else self.make_default("PrncplAcctPty")

	@PrncplAcctPty.deleter
	def PrncplAcctPty(self):
		del self._PrncplAcctPty
		self._PrncplAcctPty = None

	@property
	def Grntr(self):
		return self._Grntr

	@Grntr.setter
	def Grntr(self, value):
		self._Grntr = value if type(value) != base_types.auto else self.make_default("Grntr")

	@Grntr.deleter
	def Grntr(self):
		del self._Grntr
		self._Grntr = None

	@property
	def RegdShrhldrNm(self):
		return self._RegdShrhldrNm

	@RegdShrhldrNm.setter
	def RegdShrhldrNm(self, value):
		self._RegdShrhldrNm = value if type(value) != base_types.auto else self.make_default("RegdShrhldrNm")

	@RegdShrhldrNm.deleter
	def RegdShrhldrNm(self):
		del self._RegdShrhldrNm
		self._RegdShrhldrNm = None

	@property
	def OthrPty(self):
		return self._OthrPty

	@OthrPty.setter
	def OthrPty(self, value):
		self._OthrPty = value if type(value) != base_types.auto else self.make_default("OthrPty")

	@OthrPty.deleter
	def OthrPty(self):
		del self._OthrPty
		self._OthrPty = None

	@property
	def Prtctr(self):
		return self._Prtctr

	@Prtctr.setter
	def Prtctr(self, value):
		self._Prtctr = value if type(value) != base_types.auto else self.make_default("Prtctr")

	@Prtctr.deleter
	def Prtctr(self):
		del self._Prtctr
		self._Prtctr = None

	@property
	def SucssrOnDth(self):
		return self._SucssrOnDth

	@SucssrOnDth.setter
	def SucssrOnDth(self, value):
		self._SucssrOnDth = value if type(value) != base_types.auto else self.make_default("SucssrOnDth")

	@SucssrOnDth.deleter
	def SucssrOnDth(self):
		del self._SucssrOnDth
		self._SucssrOnDth = None

	@property
	def Bnfcry(self):
		return self._Bnfcry

	@Bnfcry.setter
	def Bnfcry(self, value):
		self._Bnfcry = value if type(value) != base_types.auto else self.make_default("Bnfcry")

	@Bnfcry.deleter
	def Bnfcry(self):
		del self._Bnfcry
		self._Bnfcry = None

	@property
	def CtdnForMnr(self):
		return self._CtdnForMnr

	@CtdnForMnr.setter
	def CtdnForMnr(self, value):
		self._CtdnForMnr = value if type(value) != base_types.auto else self.make_default("CtdnForMnr")

	@CtdnForMnr.deleter
	def CtdnForMnr(self):
		del self._CtdnForMnr
		self._CtdnForMnr = None

	@property
	def LglGuardn(self):
		return self._LglGuardn

	@LglGuardn.setter
	def LglGuardn(self, value):
		self._LglGuardn = value if type(value) != base_types.auto else self.make_default("LglGuardn")

	@LglGuardn.deleter
	def LglGuardn(self):
		del self._LglGuardn
		self._LglGuardn = None

	@property
	def SnrMggOffcl(self):
		return self._SnrMggOffcl

	@SnrMggOffcl.setter
	def SnrMggOffcl(self, value):
		self._SnrMggOffcl = value if type(value) != base_types.auto else self.make_default("SnrMggOffcl")

	@SnrMggOffcl.deleter
	def SnrMggOffcl(self):
		del self._SnrMggOffcl
		self._SnrMggOffcl = None

	@property
	def PwrOfAttny(self):
		return self._PwrOfAttny

	@PwrOfAttny.setter
	def PwrOfAttny(self, value):
		self._PwrOfAttny = value if type(value) != base_types.auto else self.make_default("PwrOfAttny")

	@PwrOfAttny.deleter
	def PwrOfAttny(self):
		del self._PwrOfAttny
		self._PwrOfAttny = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Admstr', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sttlr', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ScndryOwnr', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrncplAcctPty', type=AccountParties12Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Grntr', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegdShrhldrNm', type=RegisteredShareholderName1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPty', type=ExtendedParty14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prtctr', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SucssrOnDth', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Bnfcry', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtdnForMnr', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LglGuardn', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SnrMggOffcl', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PwrOfAttny', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
	))

