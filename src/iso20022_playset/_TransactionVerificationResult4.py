from . import base_types
from .Verification1Code import Verification1Code
from .Max500Text import Max500Text
from .AuthenticationMethod6Code import AuthenticationMethod6Code
from .AuthenticationEntity2Code import AuthenticationEntity2Code

class TransactionVerificationResult4(base_types._BaseFieldType):

	__slots__ = ["_Mtd", "_Rslt", "_VrfctnNtty", "_AddtlRslt"]
	@property
	def Mtd(self):
		return self._Mtd

	@Mtd.setter
	def Mtd(self, value):
		self._Mtd = value if type(value) != base_types.auto else self.make_default("Mtd")

	@Mtd.deleter
	def Mtd(self):
		del self._Mtd
		self._Mtd = None

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if type(value) != base_types.auto else self.make_default("Rslt")

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = None

	@property
	def VrfctnNtty(self):
		return self._VrfctnNtty

	@VrfctnNtty.setter
	def VrfctnNtty(self, value):
		self._VrfctnNtty = value if type(value) != base_types.auto else self.make_default("VrfctnNtty")

	@VrfctnNtty.deleter
	def VrfctnNtty(self):
		del self._VrfctnNtty
		self._VrfctnNtty = None

	@property
	def AddtlRslt(self):
		return self._AddtlRslt

	@AddtlRslt.setter
	def AddtlRslt(self, value):
		self._AddtlRslt = value if type(value) != base_types.auto else self.make_default("AddtlRslt")

	@AddtlRslt.deleter
	def AddtlRslt(self):
		del self._AddtlRslt
		self._AddtlRslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mtd', type=AuthenticationMethod6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=Verification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VrfctnNtty', type=AuthenticationEntity2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRslt', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
	))

