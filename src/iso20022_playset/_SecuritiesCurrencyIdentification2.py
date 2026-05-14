# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CountryCodeAndName3 import CountryCodeAndName3
from ._CurrencyCodeAndName1 import CurrencyCodeAndName1
from ._ISODate import ISODate
from ._Max1Number import Max1Number
from ._Modification1Code import Modification1Code
from ._Period4Choice import Period4Choice
from ._TrueFalseIndicator import TrueFalseIndicator

class SecuritiesCurrencyIdentification2(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_CtryDtls", "_FrctnlDgt", "_LastUpdtd", "_Mod", "_PreEuro", "_VldtyPrd"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def CtryDtls(self):
		return self._CtryDtls

	@CtryDtls.setter
	def CtryDtls(self, value):
		self._CtryDtls = value if type(value) != base_types.auto else self.make_default("CtryDtls")

	@CtryDtls.deleter
	def CtryDtls(self):
		del self._CtryDtls
		self._CtryDtls = None

	@property
	def FrctnlDgt(self):
		return self._FrctnlDgt

	@FrctnlDgt.setter
	def FrctnlDgt(self, value):
		self._FrctnlDgt = value if type(value) != base_types.auto else self.make_default("FrctnlDgt")

	@FrctnlDgt.deleter
	def FrctnlDgt(self):
		del self._FrctnlDgt
		self._FrctnlDgt = None

	@property
	def LastUpdtd(self):
		return self._LastUpdtd

	@LastUpdtd.setter
	def LastUpdtd(self, value):
		self._LastUpdtd = value if type(value) != base_types.auto else self.make_default("LastUpdtd")

	@LastUpdtd.deleter
	def LastUpdtd(self):
		del self._LastUpdtd
		self._LastUpdtd = None

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if type(value) != base_types.auto else self.make_default("Mod")

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = None

	@property
	def PreEuro(self):
		return self._PreEuro

	@PreEuro.setter
	def PreEuro(self, value):
		self._PreEuro = value if type(value) != base_types.auto else self.make_default("PreEuro")

	@PreEuro.deleter
	def PreEuro(self):
		del self._PreEuro
		self._PreEuro = None

	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if type(value) != base_types.auto else self.make_default("VldtyPrd")

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=CurrencyCodeAndName1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryDtls', type=CountryCodeAndName3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrctnlDgt', type=Max1Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastUpdtd', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mod', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreEuro', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyPrd', type=Period4Choice, min=1, max=1, mutex_group=None, array=False),
	))