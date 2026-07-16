# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountParties12Choice
from . import ExtendedParty14
from . import InvestmentAccountOwnershipInformation16
from . import RegisteredShareholderName1Choice

class AccountParties17(base_types._BaseFieldType):

	__slots__ = ["_Admstr", "_Bnfcry", "_CtdnForMnr", "_Grntr", "_LglGuardn", "_OthrPty", "_PrncplAcctPty", "_Prtctr", "_PwrOfAttny", "_RegdShrhldrNm", "_ScndryOwnr", "_SnrMggOffcl", "_Sttlr", "_SucssrOnDth"]
	@property
	def Admstr(self):
		return self._Admstr

	@Admstr.setter
	def Admstr(self, value):
		self._Admstr = value if value is not None else base_types.UninitialisedField(self, 'Admstr', InvestmentAccountOwnershipInformation16, True)

	@Admstr.deleter
	def Admstr(self):
		del self._Admstr
		self._Admstr = base_types.UninitialisedField(self, 'Admstr', InvestmentAccountOwnershipInformation16, True)

	@property
	def Bnfcry(self):
		return self._Bnfcry

	@Bnfcry.setter
	def Bnfcry(self, value):
		self._Bnfcry = value if value is not None else base_types.UninitialisedField(self, 'Bnfcry', InvestmentAccountOwnershipInformation16, True)

	@Bnfcry.deleter
	def Bnfcry(self):
		del self._Bnfcry
		self._Bnfcry = base_types.UninitialisedField(self, 'Bnfcry', InvestmentAccountOwnershipInformation16, True)

	@property
	def CtdnForMnr(self):
		return self._CtdnForMnr

	@CtdnForMnr.setter
	def CtdnForMnr(self, value):
		self._CtdnForMnr = value if value is not None else base_types.UninitialisedField(self, 'CtdnForMnr', InvestmentAccountOwnershipInformation16, True)

	@CtdnForMnr.deleter
	def CtdnForMnr(self):
		del self._CtdnForMnr
		self._CtdnForMnr = base_types.UninitialisedField(self, 'CtdnForMnr', InvestmentAccountOwnershipInformation16, True)

	@property
	def Grntr(self):
		return self._Grntr

	@Grntr.setter
	def Grntr(self, value):
		self._Grntr = value if value is not None else base_types.UninitialisedField(self, 'Grntr', InvestmentAccountOwnershipInformation16, True)

	@Grntr.deleter
	def Grntr(self):
		del self._Grntr
		self._Grntr = base_types.UninitialisedField(self, 'Grntr', InvestmentAccountOwnershipInformation16, True)

	@property
	def LglGuardn(self):
		return self._LglGuardn

	@LglGuardn.setter
	def LglGuardn(self, value):
		self._LglGuardn = value if value is not None else base_types.UninitialisedField(self, 'LglGuardn', InvestmentAccountOwnershipInformation16, True)

	@LglGuardn.deleter
	def LglGuardn(self):
		del self._LglGuardn
		self._LglGuardn = base_types.UninitialisedField(self, 'LglGuardn', InvestmentAccountOwnershipInformation16, True)

	@property
	def OthrPty(self):
		return self._OthrPty

	@OthrPty.setter
	def OthrPty(self, value):
		self._OthrPty = value if value is not None else base_types.UninitialisedField(self, 'OthrPty', ExtendedParty14, True)

	@OthrPty.deleter
	def OthrPty(self):
		del self._OthrPty
		self._OthrPty = base_types.UninitialisedField(self, 'OthrPty', ExtendedParty14, True)

	@property
	def PrncplAcctPty(self):
		return self._PrncplAcctPty

	@PrncplAcctPty.setter
	def PrncplAcctPty(self, value):
		self._PrncplAcctPty = value if value is not None else base_types.UninitialisedField(self, 'PrncplAcctPty', AccountParties12Choice, False)

	@PrncplAcctPty.deleter
	def PrncplAcctPty(self):
		del self._PrncplAcctPty
		self._PrncplAcctPty = base_types.UninitialisedField(self, 'PrncplAcctPty', AccountParties12Choice, False)

	@property
	def Prtctr(self):
		return self._Prtctr

	@Prtctr.setter
	def Prtctr(self, value):
		self._Prtctr = value if value is not None else base_types.UninitialisedField(self, 'Prtctr', InvestmentAccountOwnershipInformation16, True)

	@Prtctr.deleter
	def Prtctr(self):
		del self._Prtctr
		self._Prtctr = base_types.UninitialisedField(self, 'Prtctr', InvestmentAccountOwnershipInformation16, True)

	@property
	def PwrOfAttny(self):
		return self._PwrOfAttny

	@PwrOfAttny.setter
	def PwrOfAttny(self, value):
		self._PwrOfAttny = value if value is not None else base_types.UninitialisedField(self, 'PwrOfAttny', InvestmentAccountOwnershipInformation16, True)

	@PwrOfAttny.deleter
	def PwrOfAttny(self):
		del self._PwrOfAttny
		self._PwrOfAttny = base_types.UninitialisedField(self, 'PwrOfAttny', InvestmentAccountOwnershipInformation16, True)

	@property
	def RegdShrhldrNm(self):
		return self._RegdShrhldrNm

	@RegdShrhldrNm.setter
	def RegdShrhldrNm(self, value):
		self._RegdShrhldrNm = value if value is not None else base_types.UninitialisedField(self, 'RegdShrhldrNm', RegisteredShareholderName1Choice, False)

	@RegdShrhldrNm.deleter
	def RegdShrhldrNm(self):
		del self._RegdShrhldrNm
		self._RegdShrhldrNm = base_types.UninitialisedField(self, 'RegdShrhldrNm', RegisteredShareholderName1Choice, False)

	@property
	def ScndryOwnr(self):
		return self._ScndryOwnr

	@ScndryOwnr.setter
	def ScndryOwnr(self, value):
		self._ScndryOwnr = value if value is not None else base_types.UninitialisedField(self, 'ScndryOwnr', InvestmentAccountOwnershipInformation16, True)

	@ScndryOwnr.deleter
	def ScndryOwnr(self):
		del self._ScndryOwnr
		self._ScndryOwnr = base_types.UninitialisedField(self, 'ScndryOwnr', InvestmentAccountOwnershipInformation16, True)

	@property
	def SnrMggOffcl(self):
		return self._SnrMggOffcl

	@SnrMggOffcl.setter
	def SnrMggOffcl(self, value):
		self._SnrMggOffcl = value if value is not None else base_types.UninitialisedField(self, 'SnrMggOffcl', InvestmentAccountOwnershipInformation16, True)

	@SnrMggOffcl.deleter
	def SnrMggOffcl(self):
		del self._SnrMggOffcl
		self._SnrMggOffcl = base_types.UninitialisedField(self, 'SnrMggOffcl', InvestmentAccountOwnershipInformation16, True)

	@property
	def Sttlr(self):
		return self._Sttlr

	@Sttlr.setter
	def Sttlr(self, value):
		self._Sttlr = value if value is not None else base_types.UninitialisedField(self, 'Sttlr', InvestmentAccountOwnershipInformation16, True)

	@Sttlr.deleter
	def Sttlr(self):
		del self._Sttlr
		self._Sttlr = base_types.UninitialisedField(self, 'Sttlr', InvestmentAccountOwnershipInformation16, True)

	@property
	def SucssrOnDth(self):
		return self._SucssrOnDth

	@SucssrOnDth.setter
	def SucssrOnDth(self, value):
		self._SucssrOnDth = value if value is not None else base_types.UninitialisedField(self, 'SucssrOnDth', InvestmentAccountOwnershipInformation16, True)

	@SucssrOnDth.deleter
	def SucssrOnDth(self):
		del self._SucssrOnDth
		self._SucssrOnDth = base_types.UninitialisedField(self, 'SucssrOnDth', InvestmentAccountOwnershipInformation16, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Admstr', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Bnfcry', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtdnForMnr', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Grntr', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LglGuardn', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrPty', type=ExtendedParty14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrncplAcctPty', type=AccountParties12Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtctr', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PwrOfAttny', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegdShrhldrNm', type=RegisteredShareholderName1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryOwnr', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SnrMggOffcl', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sttlr', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SucssrOnDth', type=InvestmentAccountOwnershipInformation16, min=0, max=None, mutex_group=None, array=True),
	))