from . import base_types
from ._ATMSignature2Choice import ATMSignature2Choice
from ._CryptographicKey12 import CryptographicKey12
from ._Max140Binary import Max140Binary
from ._Max35Text import Max35Text
from ._Max5000Binary import Max5000Binary

class SecurityParameters9(base_types._BaseFieldType):

	__slots__ = ["_ATMChllng", "_Cert", "_Key", "_ReqdKey", "_SgntrChc"]
	@property
	def ATMChllng(self):
		return self._ATMChllng

	@ATMChllng.setter
	def ATMChllng(self, value):
		self._ATMChllng = value if type(value) != base_types.auto else self.make_default("ATMChllng")

	@ATMChllng.deleter
	def ATMChllng(self):
		del self._ATMChllng
		self._ATMChllng = None

	@property
	def Cert(self):
		return self._Cert

	@Cert.setter
	def Cert(self, value):
		self._Cert = value if type(value) != base_types.auto else self.make_default("Cert")

	@Cert.deleter
	def Cert(self):
		del self._Cert
		self._Cert = None

	@property
	def Key(self):
		return self._Key

	@Key.setter
	def Key(self, value):
		self._Key = value if type(value) != base_types.auto else self.make_default("Key")

	@Key.deleter
	def Key(self):
		del self._Key
		self._Key = None

	@property
	def ReqdKey(self):
		return self._ReqdKey

	@ReqdKey.setter
	def ReqdKey(self, value):
		self._ReqdKey = value if type(value) != base_types.auto else self.make_default("ReqdKey")

	@ReqdKey.deleter
	def ReqdKey(self):
		del self._ReqdKey
		self._ReqdKey = None

	@property
	def SgntrChc(self):
		return self._SgntrChc

	@SgntrChc.setter
	def SgntrChc(self, value):
		self._SgntrChc = value if type(value) != base_types.auto else self.make_default("SgntrChc")

	@SgntrChc.deleter
	def SgntrChc(self):
		del self._SgntrChc
		self._SgntrChc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cert', type=Max5000Binary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Key', type=CryptographicKey12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdKey', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrChc', type=ATMSignature2Choice, min=0, max=1, mutex_group=None, array=False),
	))

