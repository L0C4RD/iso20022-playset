from . import base_types
from .MobileData6 import MobileData6
from .Max35Text import Max35Text
from .CardholderAuthentication17 import CardholderAuthentication17
from .TransactionVerificationResult4 import TransactionVerificationResult4
from .PersonIdentification15 import PersonIdentification15
from .Vehicle1 import Vehicle1
from .Max45Text import Max45Text
from .Max70Text import Max70Text
from .LanguageCode import LanguageCode
from .PostalAddress22 import PostalAddress22

class Cardholder21(base_types._BaseFieldType):

	__slots__ = ["_MobData", "_Id", "_BllgAdr", "_TripNb", "_Authntcn", "_Vhcl", "_ShppgAdr", "_Lang", "_Nm", "_PrsnlData", "_TxVrfctnRslt"]
	@property
	def MobData(self):
		return self._MobData

	@MobData.setter
	def MobData(self, value):
		self._MobData = value if type(value) != auto else self.make_default("MobData")

	@MobData.deleter
	def MobData(self):
		del self._MobData
		self._MobData = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def BllgAdr(self):
		return self._BllgAdr

	@BllgAdr.setter
	def BllgAdr(self, value):
		self._BllgAdr = value if type(value) != auto else self.make_default("BllgAdr")

	@BllgAdr.deleter
	def BllgAdr(self):
		del self._BllgAdr
		self._BllgAdr = None

	@property
	def TripNb(self):
		return self._TripNb

	@TripNb.setter
	def TripNb(self, value):
		self._TripNb = value if type(value) != auto else self.make_default("TripNb")

	@TripNb.deleter
	def TripNb(self):
		del self._TripNb
		self._TripNb = None

	@property
	def Authntcn(self):
		return self._Authntcn

	@Authntcn.setter
	def Authntcn(self, value):
		self._Authntcn = value if type(value) != auto else self.make_default("Authntcn")

	@Authntcn.deleter
	def Authntcn(self):
		del self._Authntcn
		self._Authntcn = None

	@property
	def Vhcl(self):
		return self._Vhcl

	@Vhcl.setter
	def Vhcl(self, value):
		self._Vhcl = value if type(value) != auto else self.make_default("Vhcl")

	@Vhcl.deleter
	def Vhcl(self):
		del self._Vhcl
		self._Vhcl = None

	@property
	def ShppgAdr(self):
		return self._ShppgAdr

	@ShppgAdr.setter
	def ShppgAdr(self, value):
		self._ShppgAdr = value if type(value) != auto else self.make_default("ShppgAdr")

	@ShppgAdr.deleter
	def ShppgAdr(self):
		del self._ShppgAdr
		self._ShppgAdr = None

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if type(value) != auto else self.make_default("Lang")

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def PrsnlData(self):
		return self._PrsnlData

	@PrsnlData.setter
	def PrsnlData(self, value):
		self._PrsnlData = value if type(value) != auto else self.make_default("PrsnlData")

	@PrsnlData.deleter
	def PrsnlData(self):
		del self._PrsnlData
		self._PrsnlData = None

	@property
	def TxVrfctnRslt(self):
		return self._TxVrfctnRslt

	@TxVrfctnRslt.setter
	def TxVrfctnRslt(self, value):
		self._TxVrfctnRslt = value if type(value) != auto else self.make_default("TxVrfctnRslt")

	@TxVrfctnRslt.deleter
	def TxVrfctnRslt(self):
		del self._TxVrfctnRslt
		self._TxVrfctnRslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MobData', type=MobileData6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=PersonIdentification15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgAdr', type=PostalAddress22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Authntcn', type=CardholderAuthentication17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vhcl', type=Vehicle1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgAdr', type=PostalAddress22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max45Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrsnlData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxVrfctnRslt', type=TransactionVerificationResult4, min=0, max=None, mutex_group=None, array=True),
	))

