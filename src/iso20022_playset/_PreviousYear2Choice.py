from . import base_types
from ._PreviousAll import PreviousAll
from ._ISOYear import ISOYear

class PreviousYear2Choice(base_types._BaseFieldType):

	__slots__ = ["_AllPrvsYrs", "_SpcfcPrvsYrs"]
	@property
	def AllPrvsYrs(self):
		return self._AllPrvsYrs

	@AllPrvsYrs.setter
	def AllPrvsYrs(self, value):
		self._AllPrvsYrs = value if type(value) != base_types.auto else self.make_default("AllPrvsYrs")

	@AllPrvsYrs.deleter
	def AllPrvsYrs(self):
		del self._AllPrvsYrs
		self._AllPrvsYrs = None

	@property
	def SpcfcPrvsYrs(self):
		return self._SpcfcPrvsYrs

	@SpcfcPrvsYrs.setter
	def SpcfcPrvsYrs(self, value):
		self._SpcfcPrvsYrs = value if type(value) != base_types.auto else self.make_default("SpcfcPrvsYrs")

	@SpcfcPrvsYrs.deleter
	def SpcfcPrvsYrs(self):
		del self._SpcfcPrvsYrs
		self._SpcfcPrvsYrs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AllPrvsYrs', type=PreviousAll, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SpcfcPrvsYrs', type=ISOYear, min=1, max=None, mutex_group=1, array=True),
	))

