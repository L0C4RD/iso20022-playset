from . import base_types
from .KEKIdentifier4 import KEKIdentifier4
from .CryptographicKeyType4Code import CryptographicKeyType4Code
from .Max140Binary import Max140Binary
from .Max5000Binary import Max5000Binary

class ATMConfigurationParameter2(base_types._BaseFieldType):

	__slots__ = ["_HstChllng", "_Cert", "_KeyCtgy", "_KeyProps"]
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
	def KeyCtgy(self):
		return self._KeyCtgy

	@KeyCtgy.setter
	def KeyCtgy(self, value):
		self._KeyCtgy = value if type(value) != base_types.auto else self.make_default("KeyCtgy")

	@KeyCtgy.deleter
	def KeyCtgy(self):
		del self._KeyCtgy
		self._KeyCtgy = None

	@property
	def KeyProps(self):
		return self._KeyProps

	@KeyProps.setter
	def KeyProps(self, value):
		self._KeyProps = value if type(value) != base_types.auto else self.make_default("KeyProps")

	@KeyProps.deleter
	def KeyProps(self):
		del self._KeyProps
		self._KeyProps = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cert', type=Max5000Binary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='KeyCtgy', type=CryptographicKeyType4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyProps', type=KEKIdentifier4, min=0, max=None, mutex_group=None, array=True),
	))

