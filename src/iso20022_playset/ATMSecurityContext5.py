import base_types
import ATMSecurityScheme4Code
import ATMSecurityScheme3Code
import ATMSecurityDevice2
import CryptographicKey11
import Max140Binary

class ATMSecurityContext5(base_types._BaseFieldType):

	__slots__ = ["_CurSctySchme", "_Key", "_SctyDvc", "_HstChllng", "_SctySchmeCpblties"]
	@property
	def CurSctySchme(self):
		return self._CurSctySchme

	@CurSctySchme.setter
	def CurSctySchme(self, value):
		self._CurSctySchme = value if type(value) != auto else self.make_default("CurSctySchme")

	@CurSctySchme.deleter
	def CurSctySchme(self):
		del self._CurSctySchme
		self._CurSctySchme = None

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

	@property
	def SctyDvc(self):
		return self._SctyDvc

	@SctyDvc.setter
	def SctyDvc(self, value):
		self._SctyDvc = value if type(value) != auto else self.make_default("SctyDvc")

	@SctyDvc.deleter
	def SctyDvc(self):
		del self._SctyDvc
		self._SctyDvc = None

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
	def SctySchmeCpblties(self):
		return self._SctySchmeCpblties

	@SctySchmeCpblties.setter
	def SctySchmeCpblties(self, value):
		self._SctySchmeCpblties = value if type(value) != auto else self.make_default("SctySchmeCpblties")

	@SctySchmeCpblties.deleter
	def SctySchmeCpblties(self):
		del self._SctySchmeCpblties
		self._SctySchmeCpblties = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurSctySchme', type=ATMSecurityScheme3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Key', type=CryptographicKey11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyDvc', type=ATMSecurityDevice2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctySchmeCpblties', type=ATMSecurityScheme4Code, min=0, max=None, mutex_group=None, array=True),
	))

