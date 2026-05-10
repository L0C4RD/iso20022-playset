import base_types
import Period4Choice
import ISODate
import TrueFalseIndicator
import Modification1Code
import CountryCodeAndName3

class SecuritiesCountryIdentification2(base_types._BaseFieldType):

	__slots__ = ["_LastUpdtd", "_Ctry", "_EEACtry", "_VldtyPrd", "_Mod"]
	@property
	def LastUpdtd(self):
		return self._LastUpdtd

	@LastUpdtd.setter
	def LastUpdtd(self, value):
		self._LastUpdtd = value if type(value) != auto else self.make_default("LastUpdtd")

	@LastUpdtd.deleter
	def LastUpdtd(self):
		del self._LastUpdtd
		self._LastUpdtd = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def EEACtry(self):
		return self._EEACtry

	@EEACtry.setter
	def EEACtry(self, value):
		self._EEACtry = value if type(value) != auto else self.make_default("EEACtry")

	@EEACtry.deleter
	def EEACtry(self):
		del self._EEACtry
		self._EEACtry = None

	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if type(value) != auto else self.make_default("VldtyPrd")

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = None

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if type(value) != auto else self.make_default("Mod")

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LastUpdtd', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCodeAndName3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EEACtry', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyPrd', type=Period4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mod', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
	))

