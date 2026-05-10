from . import base_types
from .InvestorProfile2 import InvestorProfile2
from .DataModification1Code import DataModification1Code

class ModificationScope46(base_types._BaseFieldType):

	__slots__ = ["_ModScpIndctn", "_InvstrPrfl"]
	@property
	def ModScpIndctn(self):
		return self._ModScpIndctn

	@ModScpIndctn.setter
	def ModScpIndctn(self, value):
		self._ModScpIndctn = value if type(value) != base_types.auto else self.make_default("ModScpIndctn")

	@ModScpIndctn.deleter
	def ModScpIndctn(self):
		del self._ModScpIndctn
		self._ModScpIndctn = None

	@property
	def InvstrPrfl(self):
		return self._InvstrPrfl

	@InvstrPrfl.setter
	def InvstrPrfl(self, value):
		self._InvstrPrfl = value if type(value) != base_types.auto else self.make_default("InvstrPrfl")

	@InvstrPrfl.deleter
	def InvstrPrfl(self):
		del self._InvstrPrfl
		self._InvstrPrfl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrPrfl', type=InvestorProfile2, min=1, max=1, mutex_group=None, array=False),
	))

