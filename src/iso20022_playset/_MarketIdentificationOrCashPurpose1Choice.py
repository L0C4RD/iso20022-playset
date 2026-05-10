from . import base_types
from ._ExternalMarketArea1Code import ExternalMarketArea1Code
from ._MarketIdentification87 import MarketIdentification87

class MarketIdentificationOrCashPurpose1Choice(base_types._BaseFieldType):

	__slots__ = ["_CshSSIPurp", "_SttlmInstrMktId"]
	@property
	def CshSSIPurp(self):
		return self._CshSSIPurp

	@CshSSIPurp.setter
	def CshSSIPurp(self, value):
		self._CshSSIPurp = value if type(value) != base_types.auto else self.make_default("CshSSIPurp")

	@CshSSIPurp.deleter
	def CshSSIPurp(self):
		del self._CshSSIPurp
		self._CshSSIPurp = None

	@property
	def SttlmInstrMktId(self):
		return self._SttlmInstrMktId

	@SttlmInstrMktId.setter
	def SttlmInstrMktId(self, value):
		self._SttlmInstrMktId = value if type(value) != base_types.auto else self.make_default("SttlmInstrMktId")

	@SttlmInstrMktId.deleter
	def SttlmInstrMktId(self):
		del self._SttlmInstrMktId
		self._SttlmInstrMktId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshSSIPurp', type=ExternalMarketArea1Code, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SttlmInstrMktId', type=MarketIdentification87, min=0, max=1, mutex_group=1, array=False),
	))

