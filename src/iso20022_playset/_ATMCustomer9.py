# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCustomerProfile2
from . import LanguageCode
from . import TransactionVerificationResult5

class ATMCustomer9(base_types._BaseFieldType):

	__slots__ = ["_AuthntcnRslt", "_PrefrdLang", "_Prfl"]
	@property
	def AuthntcnRslt(self):
		return self._AuthntcnRslt

	@AuthntcnRslt.setter
	def AuthntcnRslt(self, value):
		self._AuthntcnRslt = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnRslt', TransactionVerificationResult5, True)

	@AuthntcnRslt.deleter
	def AuthntcnRslt(self):
		del self._AuthntcnRslt
		self._AuthntcnRslt = base_types.UninitialisedField(self, 'AuthntcnRslt', TransactionVerificationResult5, True)

	@property
	def PrefrdLang(self):
		return self._PrefrdLang

	@PrefrdLang.setter
	def PrefrdLang(self, value):
		self._PrefrdLang = value if value is not None else base_types.UninitialisedField(self, 'PrefrdLang', LanguageCode, False)

	@PrefrdLang.deleter
	def PrefrdLang(self):
		del self._PrefrdLang
		self._PrefrdLang = base_types.UninitialisedField(self, 'PrefrdLang', LanguageCode, False)

	@property
	def Prfl(self):
		return self._Prfl

	@Prfl.setter
	def Prfl(self, value):
		self._Prfl = value if value is not None else base_types.UninitialisedField(self, 'Prfl', ATMCustomerProfile2, False)

	@Prfl.deleter
	def Prfl(self):
		del self._Prfl
		self._Prfl = base_types.UninitialisedField(self, 'Prfl', ATMCustomerProfile2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthntcnRslt', type=TransactionVerificationResult5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrefrdLang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prfl', type=ATMCustomerProfile2, min=0, max=1, mutex_group=None, array=False),
	))