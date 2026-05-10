import base_types
import Max140Binary
import CryptographicKey12
import ATMSignature2Choice

class SecurityParameters10(base_types._BaseFieldType):

	__slots__ = ["_HstChllng", "_SgntrChc", "_Key"]
	@property
	def HstChllng(self):
		return self._HstChllng

	@HstChllng.setter
	def HstChllng(self, value):
		self._HstChllng = value if type(value) != auto else self.make_default("HstChllng")

	@HstChllng.deleter
	def HstChllng(self):
		del self._HstChllng
		self._HstChllng = None

	@property
	def SgntrChc(self):
		return self._SgntrChc

	@SgntrChc.setter
	def SgntrChc(self, value):
		self._SgntrChc = value if type(value) != auto else self.make_default("SgntrChc")

	@SgntrChc.deleter
	def SgntrChc(self):
		del self._SgntrChc
		self._SgntrChc = None

	@property
	def Key(self):
		return self._Key

	@Key.setter
	def Key(self, value):
		self._Key = value if type(value) != auto else self.make_default("Key")

	@Key.deleter
	def Key(self):
		del self._Key
		self._Key = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrChc', type=ATMSignature2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Key', type=CryptographicKey12, min=0, max=None, mutex_group=None, array=True),
	))

