# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardProductType1Code
from . import ContentInformationType40
from . import Exact3AlphaNumericText
from . import Max100KBinary
from . import Max15NumericText
from . import Max30Text
from . import Max35Text
from . import Max3Text
from . import Max70Text
from . import PlainCardData22
from . import TrueFalseIndicator

class PaymentCard35(base_types._BaseFieldType):

	__slots__ = ["_AddtlCardData", "_AllwdPdct", "_CardBrnd", "_CardCcyCd", "_CardCtryCd", "_CardPdctPrfl", "_CardPdctSubTp", "_CardPdctTp", "_IntrnlCard", "_IssrBIN", "_MskdPAN", "_PlainCardData", "_PmtAcctRef", "_PrtctdCardData", "_PrvtCardData", "_SvcOptn"]
	@property
	def AddtlCardData(self):
		return self._AddtlCardData

	@AddtlCardData.setter
	def AddtlCardData(self, value):
		self._AddtlCardData = value if value is not None else base_types.UninitialisedField(self, 'AddtlCardData', Max70Text, False)

	@AddtlCardData.deleter
	def AddtlCardData(self):
		del self._AddtlCardData
		self._AddtlCardData = base_types.UninitialisedField(self, 'AddtlCardData', Max70Text, False)

	@property
	def AllwdPdct(self):
		return self._AllwdPdct

	@AllwdPdct.setter
	def AllwdPdct(self, value):
		self._AllwdPdct = value if value is not None else base_types.UninitialisedField(self, 'AllwdPdct', Max70Text, True)

	@AllwdPdct.deleter
	def AllwdPdct(self):
		del self._AllwdPdct
		self._AllwdPdct = base_types.UninitialisedField(self, 'AllwdPdct', Max70Text, True)

	@property
	def CardBrnd(self):
		return self._CardBrnd

	@CardBrnd.setter
	def CardBrnd(self, value):
		self._CardBrnd = value if value is not None else base_types.UninitialisedField(self, 'CardBrnd', Max35Text, False)

	@CardBrnd.deleter
	def CardBrnd(self):
		del self._CardBrnd
		self._CardBrnd = base_types.UninitialisedField(self, 'CardBrnd', Max35Text, False)

	@property
	def CardCcyCd(self):
		return self._CardCcyCd

	@CardCcyCd.setter
	def CardCcyCd(self, value):
		self._CardCcyCd = value if value is not None else base_types.UninitialisedField(self, 'CardCcyCd', Exact3AlphaNumericText, False)

	@CardCcyCd.deleter
	def CardCcyCd(self):
		del self._CardCcyCd
		self._CardCcyCd = base_types.UninitialisedField(self, 'CardCcyCd', Exact3AlphaNumericText, False)

	@property
	def CardCtryCd(self):
		return self._CardCtryCd

	@CardCtryCd.setter
	def CardCtryCd(self, value):
		self._CardCtryCd = value if value is not None else base_types.UninitialisedField(self, 'CardCtryCd', Max3Text, False)

	@CardCtryCd.deleter
	def CardCtryCd(self):
		del self._CardCtryCd
		self._CardCtryCd = base_types.UninitialisedField(self, 'CardCtryCd', Max3Text, False)

	@property
	def CardPdctPrfl(self):
		return self._CardPdctPrfl

	@CardPdctPrfl.setter
	def CardPdctPrfl(self, value):
		self._CardPdctPrfl = value if value is not None else base_types.UninitialisedField(self, 'CardPdctPrfl', Max35Text, False)

	@CardPdctPrfl.deleter
	def CardPdctPrfl(self):
		del self._CardPdctPrfl
		self._CardPdctPrfl = base_types.UninitialisedField(self, 'CardPdctPrfl', Max35Text, False)

	@property
	def CardPdctSubTp(self):
		return self._CardPdctSubTp

	@CardPdctSubTp.setter
	def CardPdctSubTp(self, value):
		self._CardPdctSubTp = value if value is not None else base_types.UninitialisedField(self, 'CardPdctSubTp', Max35Text, False)

	@CardPdctSubTp.deleter
	def CardPdctSubTp(self):
		del self._CardPdctSubTp
		self._CardPdctSubTp = base_types.UninitialisedField(self, 'CardPdctSubTp', Max35Text, False)

	@property
	def CardPdctTp(self):
		return self._CardPdctTp

	@CardPdctTp.setter
	def CardPdctTp(self, value):
		self._CardPdctTp = value if value is not None else base_types.UninitialisedField(self, 'CardPdctTp', CardProductType1Code, False)

	@CardPdctTp.deleter
	def CardPdctTp(self):
		del self._CardPdctTp
		self._CardPdctTp = base_types.UninitialisedField(self, 'CardPdctTp', CardProductType1Code, False)

	@property
	def IntrnlCard(self):
		return self._IntrnlCard

	@IntrnlCard.setter
	def IntrnlCard(self, value):
		self._IntrnlCard = value if value is not None else base_types.UninitialisedField(self, 'IntrnlCard', TrueFalseIndicator, False)

	@IntrnlCard.deleter
	def IntrnlCard(self):
		del self._IntrnlCard
		self._IntrnlCard = base_types.UninitialisedField(self, 'IntrnlCard', TrueFalseIndicator, False)

	@property
	def IssrBIN(self):
		return self._IssrBIN

	@IssrBIN.setter
	def IssrBIN(self, value):
		self._IssrBIN = value if value is not None else base_types.UninitialisedField(self, 'IssrBIN', Max15NumericText, False)

	@IssrBIN.deleter
	def IssrBIN(self):
		del self._IssrBIN
		self._IssrBIN = base_types.UninitialisedField(self, 'IssrBIN', Max15NumericText, False)

	@property
	def MskdPAN(self):
		return self._MskdPAN

	@MskdPAN.setter
	def MskdPAN(self, value):
		self._MskdPAN = value if value is not None else base_types.UninitialisedField(self, 'MskdPAN', Max30Text, False)

	@MskdPAN.deleter
	def MskdPAN(self):
		del self._MskdPAN
		self._MskdPAN = base_types.UninitialisedField(self, 'MskdPAN', Max30Text, False)

	@property
	def PlainCardData(self):
		return self._PlainCardData

	@PlainCardData.setter
	def PlainCardData(self, value):
		self._PlainCardData = value if value is not None else base_types.UninitialisedField(self, 'PlainCardData', PlainCardData22, False)

	@PlainCardData.deleter
	def PlainCardData(self):
		del self._PlainCardData
		self._PlainCardData = base_types.UninitialisedField(self, 'PlainCardData', PlainCardData22, False)

	@property
	def PmtAcctRef(self):
		return self._PmtAcctRef

	@PmtAcctRef.setter
	def PmtAcctRef(self, value):
		self._PmtAcctRef = value if value is not None else base_types.UninitialisedField(self, 'PmtAcctRef', Max70Text, False)

	@PmtAcctRef.deleter
	def PmtAcctRef(self):
		del self._PmtAcctRef
		self._PmtAcctRef = base_types.UninitialisedField(self, 'PmtAcctRef', Max70Text, False)

	@property
	def PrtctdCardData(self):
		return self._PrtctdCardData

	@PrtctdCardData.setter
	def PrtctdCardData(self, value):
		self._PrtctdCardData = value if value is not None else base_types.UninitialisedField(self, 'PrtctdCardData', ContentInformationType40, False)

	@PrtctdCardData.deleter
	def PrtctdCardData(self):
		del self._PrtctdCardData
		self._PrtctdCardData = base_types.UninitialisedField(self, 'PrtctdCardData', ContentInformationType40, False)

	@property
	def PrvtCardData(self):
		return self._PrvtCardData

	@PrvtCardData.setter
	def PrvtCardData(self, value):
		self._PrvtCardData = value if value is not None else base_types.UninitialisedField(self, 'PrvtCardData', Max100KBinary, False)

	@PrvtCardData.deleter
	def PrvtCardData(self):
		del self._PrvtCardData
		self._PrvtCardData = base_types.UninitialisedField(self, 'PrvtCardData', Max100KBinary, False)

	@property
	def SvcOptn(self):
		return self._SvcOptn

	@SvcOptn.setter
	def SvcOptn(self, value):
		self._SvcOptn = value if value is not None else base_types.UninitialisedField(self, 'SvcOptn', Max35Text, False)

	@SvcOptn.deleter
	def SvcOptn(self):
		del self._SvcOptn
		self._SvcOptn = base_types.UninitialisedField(self, 'SvcOptn', Max35Text, False)

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