from . import base_types
import ISO3NumericCurrencyCode
import Address2
import Max256Text
import Max35Text
import Max70Text

class Location6(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_LclCcy", "_Nm", "_Adr", "_LclTmZone", "_Cd"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def LclCcy(self):
		return self._LclCcy

	@LclCcy.setter
	def LclCcy(self, value):
		self._LclCcy = value if type(value) != auto else self.make_default("LclCcy")

	@LclCcy.deleter
	def LclCcy(self):
		del self._LclCcy
		self._LclCcy = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def LclTmZone(self):
		return self._LclTmZone

	@LclTmZone.setter
	def LclTmZone(self, value):
		self._LclTmZone = value if type(value) != auto else self.make_default("LclTmZone")

	@LclTmZone.deleter
	def LclTmZone(self):
		del self._LclTmZone
		self._LclTmZone = None

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTmZone', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

