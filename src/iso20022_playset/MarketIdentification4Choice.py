from . import base_types
from .MICIdentifier import MICIdentifier
from .RestrictedFINXMax30Text import RestrictedFINXMax30Text

class MarketIdentification4Choice(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_MktIdrCd"]
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
	def MktIdrCd(self):
		return self._MktIdrCd

	@MktIdrCd.setter
	def MktIdrCd(self, value):
		self._MktIdrCd = value if type(value) != auto else self.make_default("MktIdrCd")

	@MktIdrCd.deleter
	def MktIdrCd(self):
		del self._MktIdrCd
		self._MktIdrCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=RestrictedFINXMax30Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MktIdrCd', type=MICIdentifier, min=0, max=1, mutex_group=1, array=False),
	))

