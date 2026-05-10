from . import base_types
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .Max35Text import Max35Text
from .Max45Text import Max45Text
from .CardDataReading8Code import CardDataReading8Code
from .AmountUnit1Code import AmountUnit1Code
from .ActiveCurrencyCode import ActiveCurrencyCode
from .CardIdentificationType1Code import CardIdentificationType1Code

class LoyaltyAccount3(base_types._BaseFieldType):

	__slots__ = ["_IdTp", "_Ccy", "_NtryMd", "_Brnd", "_LltyId", "_Bal", "_Prvdr", "_OwnrNm", "_Unit"]
	@property
	def IdTp(self):
		return self._IdTp

	@IdTp.setter
	def IdTp(self, value):
		self._IdTp = value if type(value) != auto else self.make_default("IdTp")

	@IdTp.deleter
	def IdTp(self):
		del self._IdTp
		self._IdTp = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def NtryMd(self):
		return self._NtryMd

	@NtryMd.setter
	def NtryMd(self, value):
		self._NtryMd = value if type(value) != auto else self.make_default("NtryMd")

	@NtryMd.deleter
	def NtryMd(self):
		del self._NtryMd
		self._NtryMd = None

	@property
	def Brnd(self):
		return self._Brnd

	@Brnd.setter
	def Brnd(self, value):
		self._Brnd = value if type(value) != auto else self.make_default("Brnd")

	@Brnd.deleter
	def Brnd(self):
		del self._Brnd
		self._Brnd = None

	@property
	def LltyId(self):
		return self._LltyId

	@LltyId.setter
	def LltyId(self, value):
		self._LltyId = value if type(value) != auto else self.make_default("LltyId")

	@LltyId.deleter
	def LltyId(self):
		del self._LltyId
		self._LltyId = None

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	@property
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if type(value) != auto else self.make_default("Prvdr")

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = None

	@property
	def OwnrNm(self):
		return self._OwnrNm

	@OwnrNm.setter
	def OwnrNm(self, value):
		self._OwnrNm = value if type(value) != auto else self.make_default("OwnrNm")

	@OwnrNm.deleter
	def OwnrNm(self):
		del self._OwnrNm
		self._OwnrNm = None

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if type(value) != auto else self.make_default("Unit")

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IdTp', type=CardIdentificationType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryMd', type=CardDataReading8Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brnd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prvdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrNm', type=Max45Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Unit', type=AmountUnit1Code, min=0, max=1, mutex_group=None, array=False),
	))

