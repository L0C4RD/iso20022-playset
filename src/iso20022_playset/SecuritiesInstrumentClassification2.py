import base_types
import Modification1Code
import Period4Choice
import CFIOct2015Identifier
import ISODate

class SecuritiesInstrumentClassification2(base_types._BaseFieldType):

	__slots__ = ["_VldtyPrd", "_LastUpdtd", "_Mod", "_Idr"]
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
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if type(value) != auto else self.make_default("Mod")

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = None

	@property
	def Idr(self):
		return self._Idr

	@Idr.setter
	def Idr(self, value):
		self._Idr = value if type(value) != auto else self.make_default("Idr")

	@Idr.deleter
	def Idr(self):
		del self._Idr
		self._Idr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VldtyPrd', type=Period4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastUpdtd', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mod', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Idr', type=CFIOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
	))

