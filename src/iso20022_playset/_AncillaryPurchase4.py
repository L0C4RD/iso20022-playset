from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._CreditDebit3Code import CreditDebit3Code
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max15Text import Max15Text
from ._Max35Text import Max35Text
from ._Max4Text import Max4Text
from ._Tax44 import Tax44

class AncillaryPurchase4(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CdtDbt", "_CdtRsnCd", "_DocNb", "_Fee", "_NtlData", "_PrvtData", "_RltdDocNb", "_SummryCmmdtyId", "_SvcCtgyCd", "_SvcPrvdrSvcTp", "_SvcSubCtgyCd", "_Tax"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if type(value) != base_types.auto else self.make_default("CdtDbt")

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = None

	@property
	def CdtRsnCd(self):
		return self._CdtRsnCd

	@CdtRsnCd.setter
	def CdtRsnCd(self, value):
		self._CdtRsnCd = value if type(value) != base_types.auto else self.make_default("CdtRsnCd")

	@CdtRsnCd.deleter
	def CdtRsnCd(self):
		del self._CdtRsnCd
		self._CdtRsnCd = None

	@property
	def DocNb(self):
		return self._DocNb

	@DocNb.setter
	def DocNb(self, value):
		self._DocNb = value if type(value) != base_types.auto else self.make_default("DocNb")

	@DocNb.deleter
	def DocNb(self):
		del self._DocNb
		self._DocNb = None

	@property
	def Fee(self):
		return self._Fee

	@Fee.setter
	def Fee(self, value):
		self._Fee = value if type(value) != base_types.auto else self.make_default("Fee")

	@Fee.deleter
	def Fee(self):
		del self._Fee
		self._Fee = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def RltdDocNb(self):
		return self._RltdDocNb

	@RltdDocNb.setter
	def RltdDocNb(self, value):
		self._RltdDocNb = value if type(value) != base_types.auto else self.make_default("RltdDocNb")

	@RltdDocNb.deleter
	def RltdDocNb(self):
		del self._RltdDocNb
		self._RltdDocNb = None

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if type(value) != base_types.auto else self.make_default("SummryCmmdtyId")

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = None

	@property
	def SvcCtgyCd(self):
		return self._SvcCtgyCd

	@SvcCtgyCd.setter
	def SvcCtgyCd(self, value):
		self._SvcCtgyCd = value if type(value) != base_types.auto else self.make_default("SvcCtgyCd")

	@SvcCtgyCd.deleter
	def SvcCtgyCd(self):
		del self._SvcCtgyCd
		self._SvcCtgyCd = None

	@property
	def SvcPrvdrSvcTp(self):
		return self._SvcPrvdrSvcTp

	@SvcPrvdrSvcTp.setter
	def SvcPrvdrSvcTp(self, value):
		self._SvcPrvdrSvcTp = value if type(value) != base_types.auto else self.make_default("SvcPrvdrSvcTp")

	@SvcPrvdrSvcTp.deleter
	def SvcPrvdrSvcTp(self):
		del self._SvcPrvdrSvcTp
		self._SvcPrvdrSvcTp = None

	@property
	def SvcSubCtgyCd(self):
		return self._SvcSubCtgyCd

	@SvcSubCtgyCd.setter
	def SvcSubCtgyCd(self, value):
		self._SvcSubCtgyCd = value if type(value) != base_types.auto else self.make_default("SvcSubCtgyCd")

	@SvcSubCtgyCd.deleter
	def SvcSubCtgyCd(self):
		del self._SvcSubCtgyCd
		self._SvcSubCtgyCd = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != base_types.auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

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

