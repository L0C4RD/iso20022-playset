# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardProductType1Code import CardProductType1Code
from ._ContentInformationType40 import ContentInformationType40
from ._Exact3AlphaNumericText import Exact3AlphaNumericText
from ._Max100KBinary import Max100KBinary
from ._Max15NumericText import Max15NumericText
from ._Max30Text import Max30Text
from ._Max35Text import Max35Text
from ._Max3Text import Max3Text
from ._Max70Text import Max70Text
from ._PlainCardData22 import PlainCardData22
from ._TrueFalseIndicator import TrueFalseIndicator

class PaymentCard35(base_types._BaseFieldType):

	__slots__ = ["_AddtlCardData", "_AllwdPdct", "_CardBrnd", "_CardCcyCd", "_CardCtryCd", "_CardPdctPrfl", "_CardPdctSubTp", "_CardPdctTp", "_IntrnlCard", "_IssrBIN", "_MskdPAN", "_PlainCardData", "_PmtAcctRef", "_PrtctdCardData", "_PrvtCardData", "_SvcOptn"]
	@property
	def AddtlCardData(self):
		return self._AddtlCardData

	@AddtlCardData.setter
	def AddtlCardData(self, value):
		self._AddtlCardData = value if type(value) != base_types.auto else self.make_default("AddtlCardData")

	@AddtlCardData.deleter
	def AddtlCardData(self):
		del self._AddtlCardData
		self._AddtlCardData = None

	@property
	def AllwdPdct(self):
		return self._AllwdPdct

	@AllwdPdct.setter
	def AllwdPdct(self, value):
		self._AllwdPdct = value if type(value) != base_types.auto else self.make_default("AllwdPdct")

	@AllwdPdct.deleter
	def AllwdPdct(self):
		del self._AllwdPdct
		self._AllwdPdct = None

	@property
	def CardBrnd(self):
		return self._CardBrnd

	@CardBrnd.setter
	def CardBrnd(self, value):
		self._CardBrnd = value if type(value) != base_types.auto else self.make_default("CardBrnd")

	@CardBrnd.deleter
	def CardBrnd(self):
		del self._CardBrnd
		self._CardBrnd = None

	@property
	def CardCcyCd(self):
		return self._CardCcyCd

	@CardCcyCd.setter
	def CardCcyCd(self, value):
		self._CardCcyCd = value if type(value) != base_types.auto else self.make_default("CardCcyCd")

	@CardCcyCd.deleter
	def CardCcyCd(self):
		del self._CardCcyCd
		self._CardCcyCd = None

	@property
	def CardCtryCd(self):
		return self._CardCtryCd

	@CardCtryCd.setter
	def CardCtryCd(self, value):
		self._CardCtryCd = value if type(value) != base_types.auto else self.make_default("CardCtryCd")

	@CardCtryCd.deleter
	def CardCtryCd(self):
		del self._CardCtryCd
		self._CardCtryCd = None

	@property
	def CardPdctPrfl(self):
		return self._CardPdctPrfl

	@CardPdctPrfl.setter
	def CardPdctPrfl(self, value):
		self._CardPdctPrfl = value if type(value) != base_types.auto else self.make_default("CardPdctPrfl")

	@CardPdctPrfl.deleter
	def CardPdctPrfl(self):
		del self._CardPdctPrfl
		self._CardPdctPrfl = None

	@property
	def CardPdctSubTp(self):
		return self._CardPdctSubTp

	@CardPdctSubTp.setter
	def CardPdctSubTp(self, value):
		self._CardPdctSubTp = value if type(value) != base_types.auto else self.make_default("CardPdctSubTp")

	@CardPdctSubTp.deleter
	def CardPdctSubTp(self):
		del self._CardPdctSubTp
		self._CardPdctSubTp = None

	@property
	def CardPdctTp(self):
		return self._CardPdctTp

	@CardPdctTp.setter
	def CardPdctTp(self, value):
		self._CardPdctTp = value if type(value) != base_types.auto else self.make_default("CardPdctTp")

	@CardPdctTp.deleter
	def CardPdctTp(self):
		del self._CardPdctTp
		self._CardPdctTp = None

	@property
	def IntrnlCard(self):
		return self._IntrnlCard

	@IntrnlCard.setter
	def IntrnlCard(self, value):
		self._IntrnlCard = value if type(value) != base_types.auto else self.make_default("IntrnlCard")

	@IntrnlCard.deleter
	def IntrnlCard(self):
		del self._IntrnlCard
		self._IntrnlCard = None

	@property
	def IssrBIN(self):
		return self._IssrBIN

	@IssrBIN.setter
	def IssrBIN(self, value):
		self._IssrBIN = value if type(value) != base_types.auto else self.make_default("IssrBIN")

	@IssrBIN.deleter
	def IssrBIN(self):
		del self._IssrBIN
		self._IssrBIN = None

	@property
	def MskdPAN(self):
		return self._MskdPAN

	@MskdPAN.setter
	def MskdPAN(self, value):
		self._MskdPAN = value if type(value) != base_types.auto else self.make_default("MskdPAN")

	@MskdPAN.deleter
	def MskdPAN(self):
		del self._MskdPAN
		self._MskdPAN = None

	@property
	def PlainCardData(self):
		return self._PlainCardData

	@PlainCardData.setter
	def PlainCardData(self, value):
		self._PlainCardData = value if type(value) != base_types.auto else self.make_default("PlainCardData")

	@PlainCardData.deleter
	def PlainCardData(self):
		del self._PlainCardData
		self._PlainCardData = None

	@property
	def PmtAcctRef(self):
		return self._PmtAcctRef

	@PmtAcctRef.setter
	def PmtAcctRef(self, value):
		self._PmtAcctRef = value if type(value) != base_types.auto else self.make_default("PmtAcctRef")

	@PmtAcctRef.deleter
	def PmtAcctRef(self):
		del self._PmtAcctRef
		self._PmtAcctRef = None

	@property
	def PrtctdCardData(self):
		return self._PrtctdCardData

	@PrtctdCardData.setter
	def PrtctdCardData(self, value):
		self._PrtctdCardData = value if type(value) != base_types.auto else self.make_default("PrtctdCardData")

	@PrtctdCardData.deleter
	def PrtctdCardData(self):
		del self._PrtctdCardData
		self._PrtctdCardData = None

	@property
	def PrvtCardData(self):
		return self._PrvtCardData

	@PrvtCardData.setter
	def PrvtCardData(self, value):
		self._PrvtCardData = value if type(value) != base_types.auto else self.make_default("PrvtCardData")

	@PrvtCardData.deleter
	def PrvtCardData(self):
		del self._PrvtCardData
		self._PrvtCardData = None

	@property
	def SvcOptn(self):
		return self._SvcOptn

	@SvcOptn.setter
	def SvcOptn(self, value):
		self._SvcOptn = value if type(value) != base_types.auto else self.make_default("SvcOptn")

	@SvcOptn.deleter
	def SvcOptn(self):
		del self._SvcOptn
		self._SvcOptn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlCardData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllwdPdct', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardBrnd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardCcyCd', type=Exact3AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardCtryCd', type=Max3Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPdctPrfl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPdctSubTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPdctTp', type=CardProductType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrnlCard', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrBIN', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MskdPAN', type=Max30Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlainCardData', type=PlainCardData22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAcctRef', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdCardData', type=ContentInformationType40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtCardData', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcOptn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))