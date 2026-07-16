# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import AmountUnit1Code
from . import CardDataReading8Code
from . import CardIdentificationType1Code
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import Max45Text

class LoyaltyAccount3(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_Brnd", "_Ccy", "_IdTp", "_LltyId", "_NtryMd", "_OwnrNm", "_Prvdr", "_Unit"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', ImpliedCurrencyAndAmount, False)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', ImpliedCurrencyAndAmount, False)

	@property
	def Brnd(self):
		return self._Brnd

	@Brnd.setter
	def Brnd(self, value):
		self._Brnd = value if value is not None else base_types.UninitialisedField(self, 'Brnd', Max35Text, False)

	@Brnd.deleter
	def Brnd(self):
		del self._Brnd
		self._Brnd = base_types.UninitialisedField(self, 'Brnd', Max35Text, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def IdTp(self):
		return self._IdTp

	@IdTp.setter
	def IdTp(self, value):
		self._IdTp = value if value is not None else base_types.UninitialisedField(self, 'IdTp', CardIdentificationType1Code, False)

	@IdTp.deleter
	def IdTp(self):
		del self._IdTp
		self._IdTp = base_types.UninitialisedField(self, 'IdTp', CardIdentificationType1Code, False)

	@property
	def LltyId(self):
		return self._LltyId

	@LltyId.setter
	def LltyId(self, value):
		self._LltyId = value if value is not None else base_types.UninitialisedField(self, 'LltyId', Max35Text, False)

	@LltyId.deleter
	def LltyId(self):
		del self._LltyId
		self._LltyId = base_types.UninitialisedField(self, 'LltyId', Max35Text, False)

	@property
	def NtryMd(self):
		return self._NtryMd

	@NtryMd.setter
	def NtryMd(self, value):
		self._NtryMd = value if value is not None else base_types.UninitialisedField(self, 'NtryMd', CardDataReading8Code, False)

	@NtryMd.deleter
	def NtryMd(self):
		del self._NtryMd
		self._NtryMd = base_types.UninitialisedField(self, 'NtryMd', CardDataReading8Code, False)

	@property
	def OwnrNm(self):
		return self._OwnrNm

	@OwnrNm.setter
	def OwnrNm(self, value):
		self._OwnrNm = value if value is not None else base_types.UninitialisedField(self, 'OwnrNm', Max45Text, False)

	@OwnrNm.deleter
	def OwnrNm(self):
		del self._OwnrNm
		self._OwnrNm = base_types.UninitialisedField(self, 'OwnrNm', Max45Text, False)

	@property
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if value is not None else base_types.UninitialisedField(self, 'Prvdr', Max35Text, False)

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = base_types.UninitialisedField(self, 'Prvdr', Max35Text, False)

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if value is not None else base_types.UninitialisedField(self, 'Unit', AmountUnit1Code, False)

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = base_types.UninitialisedField(self, 'Unit', AmountUnit1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brnd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdTp', type=CardIdentificationType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryMd', type=CardDataReading8Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrNm', type=Max45Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prvdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Unit', type=AmountUnit1Code, min=0, max=1, mutex_group=None, array=False),
	))