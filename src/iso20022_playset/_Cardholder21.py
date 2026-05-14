# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardholderAuthentication17 import CardholderAuthentication17
from ._LanguageCode import LanguageCode
from ._Max35Text import Max35Text
from ._Max45Text import Max45Text
from ._Max70Text import Max70Text
from ._MobileData6 import MobileData6
from ._PersonIdentification15 import PersonIdentification15
from ._PostalAddress22 import PostalAddress22
from ._TransactionVerificationResult4 import TransactionVerificationResult4
from ._Vehicle1 import Vehicle1

class Cardholder21(base_types._BaseFieldType):

	__slots__ = ["_Authntcn", "_BllgAdr", "_Id", "_Lang", "_MobData", "_Nm", "_PrsnlData", "_ShppgAdr", "_TripNb", "_TxVrfctnRslt", "_Vhcl"]
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
	def BllgAdr(self):
		return self._BllgAdr

	@BllgAdr.setter
	def BllgAdr(self, value):
		self._BllgAdr = value if type(value) != base_types.auto else self.make_default("BllgAdr")

	@BllgAdr.deleter
	def BllgAdr(self):
		del self._BllgAdr
		self._BllgAdr = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if type(value) != base_types.auto else self.make_default("Lang")

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = None

	@property
	def MobData(self):
		return self._MobData

	@MobData.setter
	def MobData(self, value):
		self._MobData = value if type(value) != base_types.auto else self.make_default("MobData")

	@MobData.deleter
	def MobData(self):
		del self._MobData
		self._MobData = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def PrsnlData(self):
		return self._PrsnlData

	@PrsnlData.setter
	def PrsnlData(self, value):
		self._PrsnlData = value if type(value) != base_types.auto else self.make_default("PrsnlData")

	@PrsnlData.deleter
	def PrsnlData(self):
		del self._PrsnlData
		self._PrsnlData = None

	@property
	def ShppgAdr(self):
		return self._ShppgAdr

	@ShppgAdr.setter
	def ShppgAdr(self, value):
		self._ShppgAdr = value if type(value) != base_types.auto else self.make_default("ShppgAdr")

	@ShppgAdr.deleter
	def ShppgAdr(self):
		del self._ShppgAdr
		self._ShppgAdr = None

	@property
	def TripNb(self):
		return self._TripNb

	@TripNb.setter
	def TripNb(self, value):
		self._TripNb = value if type(value) != base_types.auto else self.make_default("TripNb")

	@TripNb.deleter
	def TripNb(self):
		del self._TripNb
		self._TripNb = None

	@property
	def TxVrfctnRslt(self):
		return self._TxVrfctnRslt

	@TxVrfctnRslt.setter
	def TxVrfctnRslt(self, value):
		self._TxVrfctnRslt = value if type(value) != base_types.auto else self.make_default("TxVrfctnRslt")

	@TxVrfctnRslt.deleter
	def TxVrfctnRslt(self):
		del self._TxVrfctnRslt
		self._TxVrfctnRslt = None

	@property
	def Vhcl(self):
		return self._Vhcl

	@Vhcl.setter
	def Vhcl(self, value):
		self._Vhcl = value if type(value) != base_types.auto else self.make_default("Vhcl")

	@Vhcl.deleter
	def Vhcl(self):
		del self._Vhcl
		self._Vhcl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Authntcn', type=CardholderAuthentication17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BllgAdr', type=PostalAddress22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PersonIdentification15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MobData', type=MobileData6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max45Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrsnlData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgAdr', type=PostalAddress22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxVrfctnRslt', type=TransactionVerificationResult4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vhcl', type=Vehicle1, min=0, max=1, mutex_group=None, array=False),
	))