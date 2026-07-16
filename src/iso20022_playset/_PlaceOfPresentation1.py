# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import ExternalTypeOfParty1Code

class PlaceOfPresentation1(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_Plc"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@property
	def Plc(self):
		return self._Plc

	@Plc.setter
	def Plc(self, value):
		self._Plc = value if value is not None else base_types.UninitialisedField(self, 'Plc', ExternalTypeOfParty1Code, False)

	@Plc.deleter
	def Plc(self):
		del self._Plc
		self._Plc = base_types.UninitialisedField(self, 'Plc', ExternalTypeOfParty1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Plc', type=ExternalTypeOfParty1Code, min=1, max=1, mutex_group=None, array=False),
	))