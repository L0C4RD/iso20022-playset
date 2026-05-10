from . import base_types
from ._TransactionVerificationResult5 import TransactionVerificationResult5
from ._LanguageCode import LanguageCode
from ._ATMCustomerProfile2 import ATMCustomerProfile2

class ATMCustomer9(base_types._BaseFieldType):

	__slots__ = ["_AuthntcnRslt", "_PrefrdLang", "_Prfl"]
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

	@property
	def PrefrdLang(self):
		return self._PrefrdLang

	@PrefrdLang.setter
	def PrefrdLang(self, value):
		self._PrefrdLang = value if type(value) != base_types.auto else self.make_default("PrefrdLang")

	@PrefrdLang.deleter
	def PrefrdLang(self):
		del self._PrefrdLang
		self._PrefrdLang = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthntcnRslt', type=TransactionVerificationResult5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrefrdLang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prfl', type=ATMCustomerProfile2, min=0, max=1, mutex_group=None, array=False),
	))

