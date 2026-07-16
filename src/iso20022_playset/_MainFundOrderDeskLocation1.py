# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import UTCOffset1

class MainFundOrderDeskLocation1(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_TmZoneOffSet"]
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
	def TmZoneOffSet(self):
		return self._TmZoneOffSet

	@TmZoneOffSet.setter
	def TmZoneOffSet(self, value):
		self._TmZoneOffSet = value if value is not None else base_types.UninitialisedField(self, 'TmZoneOffSet', UTCOffset1, False)

	@TmZoneOffSet.deleter
	def TmZoneOffSet(self):
		del self._TmZoneOffSet
		self._TmZoneOffSet = base_types.UninitialisedField(self, 'TmZoneOffSet', UTCOffset1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmZoneOffSet', type=UTCOffset1, min=1, max=1, mutex_group=None, array=False),
	))