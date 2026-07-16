# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMSecurityDevice2
from . import ATMSecurityScheme3Code
from . import ATMSecurityScheme4Code
from . import CryptographicKey20
from . import Max140Binary

class ATMSecurityContext6(base_types._BaseFieldType):

	__slots__ = ["_CurSctySchme", "_HstChllng", "_Key", "_SctyDvc", "_SctySchmeCpblties"]
	@property
	def CurSctySchme(self):
		return self._CurSctySchme

	@CurSctySchme.setter
	def CurSctySchme(self, value):
		self._CurSctySchme = value if value is not None else base_types.UninitialisedField(self, 'CurSctySchme', ATMSecurityScheme3Code, False)

	@CurSctySchme.deleter
	def CurSctySchme(self):
		del self._CurSctySchme
		self._CurSctySchme = base_types.UninitialisedField(self, 'CurSctySchme', ATMSecurityScheme3Code, False)

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
		self._Key = value if value is not None else base_types.UninitialisedField(self, 'Key', CryptographicKey20, True)

	@Key.deleter
	def Key(self):
		del self._Key
		self._Key = base_types.UninitialisedField(self, 'Key', CryptographicKey20, True)

	@property
	def SctyDvc(self):
		return self._SctyDvc

	@SctyDvc.setter
	def SctyDvc(self, value):
		self._SctyDvc = value if value is not None else base_types.UninitialisedField(self, 'SctyDvc', ATMSecurityDevice2, False)

	@SctyDvc.deleter
	def SctyDvc(self):
		del self._SctyDvc
		self._SctyDvc = base_types.UninitialisedField(self, 'SctyDvc', ATMSecurityDevice2, False)

	@property
	def SctySchmeCpblties(self):
		return self._SctySchmeCpblties

	@SctySchmeCpblties.setter
	def SctySchmeCpblties(self, value):
		self._SctySchmeCpblties = value if value is not None else base_types.UninitialisedField(self, 'SctySchmeCpblties', ATMSecurityScheme4Code, True)

	@SctySchmeCpblties.deleter
	def SctySchmeCpblties(self):
		del self._SctySchmeCpblties
		self._SctySchmeCpblties = base_types.UninitialisedField(self, 'SctySchmeCpblties', ATMSecurityScheme4Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurSctySchme', type=ATMSecurityScheme3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Key', type=CryptographicKey20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyDvc', type=ATMSecurityDevice2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctySchmeCpblties', type=ATMSecurityScheme4Code, min=0, max=None, mutex_group=None, array=True),
	))