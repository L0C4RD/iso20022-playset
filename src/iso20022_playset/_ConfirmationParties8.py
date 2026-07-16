# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ConfirmationPartyDetails12
from . import ConfirmationPartyDetails14
from . import ConfirmationPartyDetails15

class ConfirmationParties8(base_types._BaseFieldType):

	__slots__ = ["_AffrmgPty", "_Brrwr", "_Buyr", "_Lndr", "_Sellr", "_TradBnfcryPty"]
	@property
	def AffrmgPty(self):
		return self._AffrmgPty

	@AffrmgPty.setter
	def AffrmgPty(self, value):
		self._AffrmgPty = value if value is not None else base_types.UninitialisedField(self, 'AffrmgPty', ConfirmationPartyDetails15, False)

	@AffrmgPty.deleter
	def AffrmgPty(self):
		del self._AffrmgPty
		self._AffrmgPty = base_types.UninitialisedField(self, 'AffrmgPty', ConfirmationPartyDetails15, False)

	@property
	def Brrwr(self):
		return self._Brrwr

	@Brrwr.setter
	def Brrwr(self, value):
		self._Brrwr = value if value is not None else base_types.UninitialisedField(self, 'Brrwr', ConfirmationPartyDetails12, False)

	@Brrwr.deleter
	def Brrwr(self):
		del self._Brrwr
		self._Brrwr = base_types.UninitialisedField(self, 'Brrwr', ConfirmationPartyDetails12, False)

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if value is not None else base_types.UninitialisedField(self, 'Buyr', ConfirmationPartyDetails12, False)

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = base_types.UninitialisedField(self, 'Buyr', ConfirmationPartyDetails12, False)

	@property
	def Lndr(self):
		return self._Lndr

	@Lndr.setter
	def Lndr(self, value):
		self._Lndr = value if value is not None else base_types.UninitialisedField(self, 'Lndr', ConfirmationPartyDetails12, False)

	@Lndr.deleter
	def Lndr(self):
		del self._Lndr
		self._Lndr = base_types.UninitialisedField(self, 'Lndr', ConfirmationPartyDetails12, False)

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if value is not None else base_types.UninitialisedField(self, 'Sellr', ConfirmationPartyDetails12, False)

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = base_types.UninitialisedField(self, 'Sellr', ConfirmationPartyDetails12, False)

	@property
	def TradBnfcryPty(self):
		return self._TradBnfcryPty

	@TradBnfcryPty.setter
	def TradBnfcryPty(self, value):
		self._TradBnfcryPty = value if value is not None else base_types.UninitialisedField(self, 'TradBnfcryPty', ConfirmationPartyDetails14, False)

	@TradBnfcryPty.deleter
	def TradBnfcryPty(self):
		del self._TradBnfcryPty
		self._TradBnfcryPty = base_types.UninitialisedField(self, 'TradBnfcryPty', ConfirmationPartyDetails14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AffrmgPty', type=ConfirmationPartyDetails15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brrwr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lndr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradBnfcryPty', type=ConfirmationPartyDetails14, min=0, max=1, mutex_group=None, array=False),
	))