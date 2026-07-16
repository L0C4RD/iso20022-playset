# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCustomerProfile6
from . import CardholderAuthentication8
from . import LanguageCode
from . import TransactionVerificationResult5

class ATMCustomer8(base_types._BaseFieldType):

	__slots__ = ["_Authntcn", "_AuthntcnRslt", "_Prfl", "_SelctdLang"]
	@property
	def Authntcn(self):
		return self._Authntcn

	@Authntcn.setter
	def Authntcn(self, value):
		self._Authntcn = value if value is not None else base_types.UninitialisedField(self, 'Authntcn', CardholderAuthentication8, True)

	@Authntcn.deleter
	def Authntcn(self):
		del self._Authntcn
		self._Authntcn = base_types.UninitialisedField(self, 'Authntcn', CardholderAuthentication8, True)

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
	def Prfl(self):
		return self._Prfl

	@Prfl.setter
	def Prfl(self, value):
		self._Prfl = value if value is not None else base_types.UninitialisedField(self, 'Prfl', ATMCustomerProfile6, False)

	@Prfl.deleter
	def Prfl(self):
		del self._Prfl
		self._Prfl = base_types.UninitialisedField(self, 'Prfl', ATMCustomerProfile6, False)

	@property
	def SelctdLang(self):
		return self._SelctdLang

	@SelctdLang.setter
	def SelctdLang(self, value):
		self._SelctdLang = value if value is not None else base_types.UninitialisedField(self, 'SelctdLang', LanguageCode, False)

	@SelctdLang.deleter
	def SelctdLang(self):
		del self._SelctdLang
		self._SelctdLang = base_types.UninitialisedField(self, 'SelctdLang', LanguageCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Authntcn', type=CardholderAuthentication8, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthntcnRslt', type=TransactionVerificationResult5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prfl', type=ATMCustomerProfile6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SelctdLang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
	))