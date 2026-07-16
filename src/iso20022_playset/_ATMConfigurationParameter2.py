# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CryptographicKeyType4Code
from . import KEKIdentifier4
from . import Max140Binary
from . import Max5000Binary

class ATMConfigurationParameter2(base_types._BaseFieldType):

	__slots__ = ["_Cert", "_HstChllng", "_KeyCtgy", "_KeyProps"]
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
	def HstChllng(self):
		return self._HstChllng

	@HstChllng.setter
	def HstChllng(self, value):
		self._HstChllng = value if value is not None else base_types.UninitialisedField(self, 'HstChllng', Max140Binary, False)

	@HstChllng.deleter
	def HstChllng(self):
		del self._HstChllng
		self._HstChllng = base_types.UninitialisedField(self, 'HstChllng', Max140Binary, False)

	@property
	def KeyCtgy(self):
		return self._KeyCtgy

	@KeyCtgy.setter
	def KeyCtgy(self, value):
		self._KeyCtgy = value if value is not None else base_types.UninitialisedField(self, 'KeyCtgy', CryptographicKeyType4Code, False)

	@KeyCtgy.deleter
	def KeyCtgy(self):
		del self._KeyCtgy
		self._KeyCtgy = base_types.UninitialisedField(self, 'KeyCtgy', CryptographicKeyType4Code, False)

	@property
	def KeyProps(self):
		return self._KeyProps

	@KeyProps.setter
	def KeyProps(self, value):
		self._KeyProps = value if value is not None else base_types.UninitialisedField(self, 'KeyProps', KEKIdentifier4, True)

	@KeyProps.deleter
	def KeyProps(self):
		del self._KeyProps
		self._KeyProps = base_types.UninitialisedField(self, 'KeyProps', KEKIdentifier4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cert', type=Max5000Binary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HstChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyCtgy', type=CryptographicKeyType4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyProps', type=KEKIdentifier4, min=0, max=None, mutex_group=None, array=True),
	))