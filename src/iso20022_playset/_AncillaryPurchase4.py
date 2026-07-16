# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import CreditDebit3Code
from . import ImpliedCurrencyAndAmount
from . import Max15Text
from . import Max35Text
from . import Max4Text
from . import Tax44

class AncillaryPurchase4(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CdtDbt", "_CdtRsnCd", "_DocNb", "_Fee", "_NtlData", "_PrvtData", "_RltdDocNb", "_SummryCmmdtyId", "_SvcCtgyCd", "_SvcPrvdrSvcTp", "_SvcSubCtgyCd", "_Tax"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if value is not None else base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@property
	def CdtRsnCd(self):
		return self._CdtRsnCd

	@CdtRsnCd.setter
	def CdtRsnCd(self, value):
		self._CdtRsnCd = value if value is not None else base_types.UninitialisedField(self, 'CdtRsnCd', Max35Text, False)

	@CdtRsnCd.deleter
	def CdtRsnCd(self):
		del self._CdtRsnCd
		self._CdtRsnCd = base_types.UninitialisedField(self, 'CdtRsnCd', Max35Text, False)

	@property
	def DocNb(self):
		return self._DocNb

	@DocNb.setter
	def DocNb(self, value):
		self._DocNb = value if value is not None else base_types.UninitialisedField(self, 'DocNb', Max15Text, False)

	@DocNb.deleter
	def DocNb(self):
		del self._DocNb
		self._DocNb = base_types.UninitialisedField(self, 'DocNb', Max15Text, False)

	@property
	def Fee(self):
		return self._Fee

	@Fee.setter
	def Fee(self, value):
		self._Fee = value if value is not None else base_types.UninitialisedField(self, 'Fee', ImpliedCurrencyAndAmount, False)

	@Fee.deleter
	def Fee(self):
		del self._Fee
		self._Fee = base_types.UninitialisedField(self, 'Fee', ImpliedCurrencyAndAmount, False)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def RltdDocNb(self):
		return self._RltdDocNb

	@RltdDocNb.setter
	def RltdDocNb(self, value):
		self._RltdDocNb = value if value is not None else base_types.UninitialisedField(self, 'RltdDocNb', Max15Text, False)

	@RltdDocNb.deleter
	def RltdDocNb(self):
		del self._RltdDocNb
		self._RltdDocNb = base_types.UninitialisedField(self, 'RltdDocNb', Max15Text, False)

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if value is not None else base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@property
	def SvcCtgyCd(self):
		return self._SvcCtgyCd

	@SvcCtgyCd.setter
	def SvcCtgyCd(self, value):
		self._SvcCtgyCd = value if value is not None else base_types.UninitialisedField(self, 'SvcCtgyCd', Max4Text, False)

	@SvcCtgyCd.deleter
	def SvcCtgyCd(self):
		del self._SvcCtgyCd
		self._SvcCtgyCd = base_types.UninitialisedField(self, 'SvcCtgyCd', Max4Text, False)

	@property
	def SvcPrvdrSvcTp(self):
		return self._SvcPrvdrSvcTp

	@SvcPrvdrSvcTp.setter
	def SvcPrvdrSvcTp(self, value):
		self._SvcPrvdrSvcTp = value if value is not None else base_types.UninitialisedField(self, 'SvcPrvdrSvcTp', Max35Text, False)

	@SvcPrvdrSvcTp.deleter
	def SvcPrvdrSvcTp(self):
		del self._SvcPrvdrSvcTp
		self._SvcPrvdrSvcTp = base_types.UninitialisedField(self, 'SvcPrvdrSvcTp', Max35Text, False)

	@property
	def SvcSubCtgyCd(self):
		return self._SvcSubCtgyCd

	@SvcSubCtgyCd.setter
	def SvcSubCtgyCd(self, value):
		self._SvcSubCtgyCd = value if value is not None else base_types.UninitialisedField(self, 'SvcSubCtgyCd', Max4Text, False)

	@SvcSubCtgyCd.deleter
	def SvcSubCtgyCd(self):
		del self._SvcSubCtgyCd
		self._SvcSubCtgyCd = base_types.UninitialisedField(self, 'SvcSubCtgyCd', Max4Text, False)

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', Tax44, True)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', Tax44, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtRsnCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocNb', type=Max15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fee', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdDocNb', type=Max15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCtgyCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcPrvdrSvcTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcSubCtgyCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax44, min=0, max=None, mutex_group=None, array=True),
	))