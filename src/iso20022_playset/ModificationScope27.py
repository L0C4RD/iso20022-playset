from . import base_types
from .DataModification2Code import DataModification2Code
from .PartyProfileInformation5 import PartyProfileInformation5

class ModificationScope27(base_types._BaseFieldType):

	__slots__ = ["_InvstrPrflVldtn", "_ModScpIndctn"]
	@property
	def InvstrPrflVldtn(self):
		return self._InvstrPrflVldtn

	@InvstrPrflVldtn.setter
	def InvstrPrflVldtn(self, value):
		self._InvstrPrflVldtn = value if type(value) != base_types.auto else self.make_default("InvstrPrflVldtn")

	@InvstrPrflVldtn.deleter
	def InvstrPrflVldtn(self):
		del self._InvstrPrflVldtn
		self._InvstrPrflVldtn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstrPrflVldtn', type=PartyProfileInformation5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification2Code, min=1, max=1, mutex_group=None, array=False),
	))

