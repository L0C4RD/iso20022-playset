from . import base_types
from ._Max140Binary import Max140Binary
from ._ATMSignature2Choice import ATMSignature2Choice
from ._CryptographicKey12 import CryptographicKey12

class SecurityParameters10(base_types._BaseFieldType):

	__slots__ = ["_SgntrChc", "_Key", "_HstChllng"]
	@property
	def HstChllng(self):
		return self._HstChllng

	@HstChllng.setter
	def HstChllng(self, value):
		self._HstChllng = value if type(value) != base_types.auto else self.make_default("HstChllng")

	@HstChllng.deleter
	def HstChllng(self):
		del self._HstChllng
		self._HstChllng = None

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
		base_types.FieldEntry(name='HstChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Key', type=CryptographicKey12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SgntrChc', type=ATMSignature2Choice, min=0, max=1, mutex_group=None, array=False),
	))

