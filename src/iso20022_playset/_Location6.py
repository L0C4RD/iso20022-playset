# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Address2
from . import ISO3NumericCurrencyCode
from . import Max256Text
from . import Max35Text
from . import Max70Text

class Location6(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_Cd", "_Desc", "_LclCcy", "_LclTmZone", "_Nm"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', Address2, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', Address2, False)

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', Max35Text, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', Max35Text, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max256Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max256Text, False)

	@property
	def LclCcy(self):
		return self._LclCcy

	@LclCcy.setter
	def LclCcy(self, value):
		self._LclCcy = value if value is not None else base_types.UninitialisedField(self, 'LclCcy', ISO3NumericCurrencyCode, False)

	@LclCcy.deleter
	def LclCcy(self):
		del self._LclCcy
		self._LclCcy = base_types.UninitialisedField(self, 'LclCcy', ISO3NumericCurrencyCode, False)

	@property
	def LclTmZone(self):
		return self._LclTmZone

	@LclTmZone.setter
	def LclTmZone(self, value):
		self._LclTmZone = value if value is not None else base_types.UninitialisedField(self, 'LclTmZone', Max70Text, False)

	@LclTmZone.deleter
	def LclTmZone(self):
		del self._LclTmZone
		self._LclTmZone = base_types.UninitialisedField(self, 'LclTmZone', Max70Text, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTmZone', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))