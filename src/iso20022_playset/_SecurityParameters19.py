# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMSignature3Choice
from . import CryptographicKey21
from . import Max140Binary

class SecurityParameters19(base_types._BaseFieldType):

	__slots__ = ["_HstChllng", "_Key", "_SgntrChc"]
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
	def Key(self):
		return self._Key

	@Key.setter
	def Key(self, value):
		self._Key = value if value is not None else base_types.UninitialisedField(self, 'Key', CryptographicKey21, True)

	@Key.deleter
	def Key(self):
		del self._Key
		self._Key = base_types.UninitialisedField(self, 'Key', CryptographicKey21, True)

	@property
	def SgntrChc(self):
		return self._SgntrChc

	@SgntrChc.setter
	def SgntrChc(self, value):
		self._SgntrChc = value if value is not None else base_types.UninitialisedField(self, 'SgntrChc', ATMSignature3Choice, False)

	@SgntrChc.deleter
	def SgntrChc(self):
		del self._SgntrChc
		self._SgntrChc = base_types.UninitialisedField(self, 'SgntrChc', ATMSignature3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Key', type=CryptographicKey21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SgntrChc', type=ATMSignature3Choice, min=0, max=1, mutex_group=None, array=False),
	))