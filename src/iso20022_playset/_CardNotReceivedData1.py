# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Address4 import Address4
from ._CardSecurityCapability2Code import CardSecurityCapability2Code
from ._ISODate import ISODate
from ._Max16Text import Max16Text
from ._Max256Text import Max256Text
from ._TrueFalseIndicator import TrueFalseIndicator

class CardNotReceivedData1(base_types._BaseFieldType):

	__slots__ = ["_CardSctyCd", "_CardSctyCpblty", "_DtMld", "_MldFrPstlCd", "_MlngAdr", "_MlngAdrUstrd", "_VldFr"]
	@property
	def CardSctyCd(self):
		return self._CardSctyCd

	@CardSctyCd.setter
	def CardSctyCd(self, value):
		self._CardSctyCd = value if type(value) != base_types.auto else self.make_default("CardSctyCd")

	@CardSctyCd.deleter
	def CardSctyCd(self):
		del self._CardSctyCd
		self._CardSctyCd = None

	@property
	def CardSctyCpblty(self):
		return self._CardSctyCpblty

	@CardSctyCpblty.setter
	def CardSctyCpblty(self, value):
		self._CardSctyCpblty = value if type(value) != base_types.auto else self.make_default("CardSctyCpblty")

	@CardSctyCpblty.deleter
	def CardSctyCpblty(self):
		del self._CardSctyCpblty
		self._CardSctyCpblty = None

	@property
	def DtMld(self):
		return self._DtMld

	@DtMld.setter
	def DtMld(self, value):
		self._DtMld = value if type(value) != base_types.auto else self.make_default("DtMld")

	@DtMld.deleter
	def DtMld(self):
		del self._DtMld
		self._DtMld = None

	@property
	def MldFrPstlCd(self):
		return self._MldFrPstlCd

	@MldFrPstlCd.setter
	def MldFrPstlCd(self, value):
		self._MldFrPstlCd = value if type(value) != base_types.auto else self.make_default("MldFrPstlCd")

	@MldFrPstlCd.deleter
	def MldFrPstlCd(self):
		del self._MldFrPstlCd
		self._MldFrPstlCd = None

	@property
	def MlngAdr(self):
		return self._MlngAdr

	@MlngAdr.setter
	def MlngAdr(self, value):
		self._MlngAdr = value if type(value) != base_types.auto else self.make_default("MlngAdr")

	@MlngAdr.deleter
	def MlngAdr(self):
		del self._MlngAdr
		self._MlngAdr = None

	@property
	def MlngAdrUstrd(self):
		return self._MlngAdrUstrd

	@MlngAdrUstrd.setter
	def MlngAdrUstrd(self, value):
		self._MlngAdrUstrd = value if type(value) != base_types.auto else self.make_default("MlngAdrUstrd")

	@MlngAdrUstrd.deleter
	def MlngAdrUstrd(self):
		del self._MlngAdrUstrd
		self._MlngAdrUstrd = None

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if type(value) != base_types.auto else self.make_default("VldFr")

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardSctyCd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardSctyCpblty', type=CardSecurityCapability2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtMld', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MldFrPstlCd', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MlngAdr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MlngAdrUstrd', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))