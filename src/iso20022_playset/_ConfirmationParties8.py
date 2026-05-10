from . import base_types
from ._ConfirmationPartyDetails12 import ConfirmationPartyDetails12
from ._ConfirmationPartyDetails14 import ConfirmationPartyDetails14
from ._ConfirmationPartyDetails15 import ConfirmationPartyDetails15

class ConfirmationParties8(base_types._BaseFieldType):

	__slots__ = ["_AffrmgPty", "_Brrwr", "_Buyr", "_Lndr", "_Sellr", "_TradBnfcryPty"]
	@property
	def AffrmgPty(self):
		return self._AffrmgPty

	@AffrmgPty.setter
	def AffrmgPty(self, value):
		self._AffrmgPty = value if type(value) != base_types.auto else self.make_default("AffrmgPty")

	@AffrmgPty.deleter
	def AffrmgPty(self):
		del self._AffrmgPty
		self._AffrmgPty = None

	@property
	def Brrwr(self):
		return self._Brrwr

	@Brrwr.setter
	def Brrwr(self, value):
		self._Brrwr = value if type(value) != base_types.auto else self.make_default("Brrwr")

	@Brrwr.deleter
	def Brrwr(self):
		del self._Brrwr
		self._Brrwr = None

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != base_types.auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	@property
	def Lndr(self):
		return self._Lndr

	@Lndr.setter
	def Lndr(self, value):
		self._Lndr = value if type(value) != base_types.auto else self.make_default("Lndr")

	@Lndr.deleter
	def Lndr(self):
		del self._Lndr
		self._Lndr = None

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if type(value) != base_types.auto else self.make_default("Sellr")

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = None

	@property
	def TradBnfcryPty(self):
		return self._TradBnfcryPty

	@TradBnfcryPty.setter
	def TradBnfcryPty(self, value):
		self._TradBnfcryPty = value if type(value) != base_types.auto else self.make_default("TradBnfcryPty")

	@TradBnfcryPty.deleter
	def TradBnfcryPty(self):
		del self._TradBnfcryPty
		self._TradBnfcryPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AffrmgPty', type=ConfirmationPartyDetails15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brrwr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lndr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradBnfcryPty', type=ConfirmationPartyDetails14, min=0, max=1, mutex_group=None, array=False),
	))

