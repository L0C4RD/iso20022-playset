# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Address2
from . import CardSecurityCapability1
from . import ISODate
from . import Max16Text
from . import Max256Text
from . import TrueFalseIndicator

class CardNotReceivedDetails3(base_types._BaseFieldType):

	__slots__ = ["_CardSctyCd", "_CardSctyCpblty", "_DtMld", "_MldFrPstlCd", "_MlngAdr", "_MlngAdrUstrd", "_VldFr"]
	@property
	def CardSctyCd(self):
		return self._CardSctyCd

	@CardSctyCd.setter
	def CardSctyCd(self, value):
		self._CardSctyCd = value if value is not None else base_types.UninitialisedField(self, 'CardSctyCd', TrueFalseIndicator, False)

	@CardSctyCd.deleter
	def CardSctyCd(self):
		del self._CardSctyCd
		self._CardSctyCd = base_types.UninitialisedField(self, 'CardSctyCd', TrueFalseIndicator, False)

	@property
	def CardSctyCpblty(self):
		return self._CardSctyCpblty

	@CardSctyCpblty.setter
	def CardSctyCpblty(self, value):
		self._CardSctyCpblty = value if value is not None else base_types.UninitialisedField(self, 'CardSctyCpblty', CardSecurityCapability1, True)

	@CardSctyCpblty.deleter
	def CardSctyCpblty(self):
		del self._CardSctyCpblty
		self._CardSctyCpblty = base_types.UninitialisedField(self, 'CardSctyCpblty', CardSecurityCapability1, True)

	@property
	def DtMld(self):
		return self._DtMld

	@DtMld.setter
	def DtMld(self, value):
		self._DtMld = value if value is not None else base_types.UninitialisedField(self, 'DtMld', ISODate, False)

	@DtMld.deleter
	def DtMld(self):
		del self._DtMld
		self._DtMld = base_types.UninitialisedField(self, 'DtMld', ISODate, False)

	@property
	def MldFrPstlCd(self):
		return self._MldFrPstlCd

	@MldFrPstlCd.setter
	def MldFrPstlCd(self, value):
		self._MldFrPstlCd = value if value is not None else base_types.UninitialisedField(self, 'MldFrPstlCd', Max16Text, False)

	@MldFrPstlCd.deleter
	def MldFrPstlCd(self):
		del self._MldFrPstlCd
		self._MldFrPstlCd = base_types.UninitialisedField(self, 'MldFrPstlCd', Max16Text, False)

	@property
	def MlngAdr(self):
		return self._MlngAdr

	@MlngAdr.setter
	def MlngAdr(self, value):
		self._MlngAdr = value if value is not None else base_types.UninitialisedField(self, 'MlngAdr', Address2, False)

	@MlngAdr.deleter
	def MlngAdr(self):
		del self._MlngAdr
		self._MlngAdr = base_types.UninitialisedField(self, 'MlngAdr', Address2, False)

	@property
	def MlngAdrUstrd(self):
		return self._MlngAdrUstrd

	@MlngAdrUstrd.setter
	def MlngAdrUstrd(self, value):
		self._MlngAdrUstrd = value if value is not None else base_types.UninitialisedField(self, 'MlngAdrUstrd', Max256Text, False)

	@MlngAdrUstrd.deleter
	def MlngAdrUstrd(self):
		del self._MlngAdrUstrd
		self._MlngAdrUstrd = base_types.UninitialisedField(self, 'MlngAdrUstrd', Max256Text, False)

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if value is not None else base_types.UninitialisedField(self, 'VldFr', ISODate, False)

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = base_types.UninitialisedField(self, 'VldFr', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardSctyCd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardSctyCpblty', type=CardSecurityCapability1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtMld', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MldFrPstlCd', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MlngAdr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MlngAdrUstrd', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))