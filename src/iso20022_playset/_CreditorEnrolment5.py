# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditorServiceEnrolment1
from . import Max10KBinary
from . import Max140Text
from . import MerchantCategoryCodeIdentifier
from . import RTPPartyIdentification2

class CreditorEnrolment5(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_CdtrLogo", "_CdtrTradgNm", "_Enrlmnt", "_MrchntCtgyCd", "_UltmtCdtr"]
	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', RTPPartyIdentification2, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', RTPPartyIdentification2, False)

	@property
	def CdtrLogo(self):
		return self._CdtrLogo

	@CdtrLogo.setter
	def CdtrLogo(self, value):
		self._CdtrLogo = value if value is not None else base_types.UninitialisedField(self, 'CdtrLogo', Max10KBinary, False)

	@CdtrLogo.deleter
	def CdtrLogo(self):
		del self._CdtrLogo
		self._CdtrLogo = base_types.UninitialisedField(self, 'CdtrLogo', Max10KBinary, False)

	@property
	def CdtrTradgNm(self):
		return self._CdtrTradgNm

	@CdtrTradgNm.setter
	def CdtrTradgNm(self, value):
		self._CdtrTradgNm = value if value is not None else base_types.UninitialisedField(self, 'CdtrTradgNm', Max140Text, False)

	@CdtrTradgNm.deleter
	def CdtrTradgNm(self):
		del self._CdtrTradgNm
		self._CdtrTradgNm = base_types.UninitialisedField(self, 'CdtrTradgNm', Max140Text, False)

	@property
	def Enrlmnt(self):
		return self._Enrlmnt

	@Enrlmnt.setter
	def Enrlmnt(self, value):
		self._Enrlmnt = value if value is not None else base_types.UninitialisedField(self, 'Enrlmnt', CreditorServiceEnrolment1, False)

	@Enrlmnt.deleter
	def Enrlmnt(self):
		del self._Enrlmnt
		self._Enrlmnt = base_types.UninitialisedField(self, 'Enrlmnt', CreditorServiceEnrolment1, False)

	@property
	def MrchntCtgyCd(self):
		return self._MrchntCtgyCd

	@MrchntCtgyCd.setter
	def MrchntCtgyCd(self, value):
		self._MrchntCtgyCd = value if value is not None else base_types.UninitialisedField(self, 'MrchntCtgyCd', MerchantCategoryCodeIdentifier, False)

	@MrchntCtgyCd.deleter
	def MrchntCtgyCd(self):
		del self._MrchntCtgyCd
		self._MrchntCtgyCd = base_types.UninitialisedField(self, 'MrchntCtgyCd', MerchantCategoryCodeIdentifier, False)

	@property
	def UltmtCdtr(self):
		return self._UltmtCdtr

	@UltmtCdtr.setter
	def UltmtCdtr(self, value):
		self._UltmtCdtr = value if value is not None else base_types.UninitialisedField(self, 'UltmtCdtr', RTPPartyIdentification2, False)

	@UltmtCdtr.deleter
	def UltmtCdtr(self):
		del self._UltmtCdtr
		self._UltmtCdtr = base_types.UninitialisedField(self, 'UltmtCdtr', RTPPartyIdentification2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=RTPPartyIdentification2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrLogo', type=Max10KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrTradgNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Enrlmnt', type=CreditorServiceEnrolment1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgyCd', type=MerchantCategoryCodeIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtCdtr', type=RTPPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
	))