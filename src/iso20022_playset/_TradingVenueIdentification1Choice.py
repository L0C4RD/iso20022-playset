# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import MICIdentifier
from . import TradingVenueIdentification2

class TradingVenueIdentification1Choice(base_types._BaseFieldType):

	__slots__ = ["_MktIdCd", "_NtlCmptntAuthrty", "_Othr"]
	@property
	def MktIdCd(self):
		return self._MktIdCd

	@MktIdCd.setter
	def MktIdCd(self, value):
		self._MktIdCd = value if value is not None else base_types.UninitialisedField(self, 'MktIdCd', MICIdentifier, False)

	@MktIdCd.deleter
	def MktIdCd(self):
		del self._MktIdCd
		self._MktIdCd = base_types.UninitialisedField(self, 'MktIdCd', MICIdentifier, False)

	@property
	def NtlCmptntAuthrty(self):
		return self._NtlCmptntAuthrty

	@NtlCmptntAuthrty.setter
	def NtlCmptntAuthrty(self, value):
		self._NtlCmptntAuthrty = value if value is not None else base_types.UninitialisedField(self, 'NtlCmptntAuthrty', CountryCode, False)

	@NtlCmptntAuthrty.deleter
	def NtlCmptntAuthrty(self):
		del self._NtlCmptntAuthrty
		self._NtlCmptntAuthrty = base_types.UninitialisedField(self, 'NtlCmptntAuthrty', CountryCode, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', TradingVenueIdentification2, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', TradingVenueIdentification2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktIdCd', type=MICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtlCmptntAuthrty', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=TradingVenueIdentification2, min=0, max=1, mutex_group=1, array=False),
	))