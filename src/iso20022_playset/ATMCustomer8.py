from . import base_types
from .TransactionVerificationResult5 import TransactionVerificationResult5
from .CardholderAuthentication8 import CardholderAuthentication8
from .ATMCustomerProfile6 import ATMCustomerProfile6
from .LanguageCode import LanguageCode

class ATMCustomer8(base_types._BaseFieldType):

	__slots__ = ["_SelctdLang", "_Prfl", "_Authntcn", "_AuthntcnRslt"]
	@property
	def SelctdLang(self):
		return self._SelctdLang

	@SelctdLang.setter
	def SelctdLang(self, value):
		self._SelctdLang = value if type(value) != base_types.auto else self.make_default("SelctdLang")

	@SelctdLang.deleter
	def SelctdLang(self):
		del self._SelctdLang
		self._SelctdLang = None

	@property
	def Prfl(self):
		return self._Prfl

	@Prfl.setter
	def Prfl(self, value):
		self._Prfl = value if type(value) != base_types.auto else self.make_default("Prfl")

	@Prfl.deleter
	def Prfl(self):
		del self._Prfl
		self._Prfl = None

	@property
	def Authntcn(self):
		return self._Authntcn

	@Authntcn.setter
	def Authntcn(self, value):
		self._Authntcn = value if type(value) != base_types.auto else self.make_default("Authntcn")

	@Authntcn.deleter
	def Authntcn(self):
		del self._Authntcn
		self._Authntcn = None

	@property
	def AuthntcnRslt(self):
		return self._AuthntcnRslt

	@AuthntcnRslt.setter
	def AuthntcnRslt(self, value):
		self._AuthntcnRslt = value if type(value) != base_types.auto else self.make_default("AuthntcnRslt")

	@AuthntcnRslt.deleter
	def AuthntcnRslt(self):
		del self._AuthntcnRslt
		self._AuthntcnRslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SelctdLang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prfl', type=ATMCustomerProfile6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Authntcn', type=CardholderAuthentication8, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthntcnRslt', type=TransactionVerificationResult5, min=0, max=None, mutex_group=None, array=True),
	))

