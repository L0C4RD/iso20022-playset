from . import base_types
from .MICIdentifier import MICIdentifier
from .AnyMIC1Code import AnyMIC1Code

class SecuritiesTradeVenueCriteria1Choice(base_types._BaseFieldType):

	__slots__ = ["_AnyMIC", "_MIC"]
	@property
	def AnyMIC(self):
		return self._AnyMIC

	@AnyMIC.setter
	def AnyMIC(self, value):
		self._AnyMIC = value if type(value) != base_types.auto else self.make_default("AnyMIC")

	@AnyMIC.deleter
	def AnyMIC(self):
		del self._AnyMIC
		self._AnyMIC = None

	@property
	def MIC(self):
		return self._MIC

	@MIC.setter
	def MIC(self, value):
		self._MIC = value if type(value) != base_types.auto else self.make_default("MIC")

	@MIC.deleter
	def MIC(self):
		del self._MIC
		self._MIC = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnyMIC', type=AnyMIC1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MIC', type=MICIdentifier, min=1, max=None, mutex_group=1, array=True),
	))

