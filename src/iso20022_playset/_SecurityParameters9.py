# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMSignature2Choice
from . import CryptographicKey12
from . import Max140Binary
from . import Max35Text
from . import Max5000Binary

class SecurityParameters9(base_types._BaseFieldType):

	__slots__ = ["_ATMChllng", "_Cert", "_Key", "_ReqdKey", "_SgntrChc"]
	@property
	def ATMChllng(self):
		return self._ATMChllng

	@ATMChllng.setter
	def ATMChllng(self, value):
		self._ATMChllng = value if value is not None else base_types.UninitialisedField(self, 'ATMChllng', Max140Binary, False)

	@ATMChllng.deleter
	def ATMChllng(self):
		del self._ATMChllng
		self._ATMChllng = base_types.UninitialisedField(self, 'ATMChllng', Max140Binary, False)

	@property
	def Cert(self):
		return self._Cert

	@Cert.setter
	def Cert(self, value):
		self._Cert = value if value is not None else base_types.UninitialisedField(self, 'Cert', Max5000Binary, True)

	@Cert.deleter
	def Cert(self):
		del self._Cert
		self._Cert = base_types.UninitialisedField(self, 'Cert', Max5000Binary, True)

	@property
	def Key(self):
		return self._Key

	@Key.setter
	def Key(self, value):
		self._Key = value if value is not None else base_types.UninitialisedField(self, 'Key', CryptographicKey12, False)

	@Key.deleter
	def Key(self):
		del self._Key
		self._Key = base_types.UninitialisedField(self, 'Key', CryptographicKey12, False)

	@property
	def ReqdKey(self):
		return self._ReqdKey

	@ReqdKey.setter
	def ReqdKey(self, value):
		self._ReqdKey = value if value is not None else base_types.UninitialisedField(self, 'ReqdKey', Max35Text, False)

	@ReqdKey.deleter
	def ReqdKey(self):
		del self._ReqdKey
		self._ReqdKey = base_types.UninitialisedField(self, 'ReqdKey', Max35Text, False)

	@property
	def SgntrChc(self):
		return self._SgntrChc

	@SgntrChc.setter
	def SgntrChc(self, value):
		self._SgntrChc = value if value is not None else base_types.UninitialisedField(self, 'SgntrChc', ATMSignature2Choice, False)

	@SgntrChc.deleter
	def SgntrChc(self):
		del self._SgntrChc
		self._SgntrChc = base_types.UninitialisedField(self, 'SgntrChc', ATMSignature2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cert', type=Max5000Binary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Key', type=CryptographicKey12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdKey', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrChc', type=ATMSignature2Choice, min=0, max=1, mutex_group=None, array=False),
	))