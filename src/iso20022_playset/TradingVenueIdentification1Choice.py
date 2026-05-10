from . import base_types
import MICIdentifier
import CountryCode
import TradingVenueIdentification2

class TradingVenueIdentification1Choice(base_types._BaseFieldType):

	__slots__ = ["_MktIdCd", "_NtlCmptntAuthrty", "_Othr"]
	@property
	def MktIdCd(self):
		return self._MktIdCd

	@MktIdCd.setter
	def MktIdCd(self, value):
		self._MktIdCd = value if type(value) != auto else self.make_default("MktIdCd")

	@MktIdCd.deleter
	def MktIdCd(self):
		del self._MktIdCd
		self._MktIdCd = None

	@property
	def NtlCmptntAuthrty(self):
		return self._NtlCmptntAuthrty

	@NtlCmptntAuthrty.setter
	def NtlCmptntAuthrty(self, value):
		self._NtlCmptntAuthrty = value if type(value) != auto else self.make_default("NtlCmptntAuthrty")

	@NtlCmptntAuthrty.deleter
	def NtlCmptntAuthrty(self):
		del self._NtlCmptntAuthrty
		self._NtlCmptntAuthrty = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktIdCd', type=MICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtlCmptntAuthrty', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=TradingVenueIdentification2, min=0, max=1, mutex_group=1, array=False),
	))

