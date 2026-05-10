from . import base_types
from ._GenericIdentification5 import GenericIdentification5
from ._PriceSource import PriceSource
from ._MICIdentifier import MICIdentifier

class PriceSourceFormatChoice(base_types._BaseFieldType):

	__slots__ = ["_PlcAsDSS", "_NonLclMktPlc", "_LclMktPlc"]
	@property
	def PlcAsDSS(self):
		return self._PlcAsDSS

	@PlcAsDSS.setter
	def PlcAsDSS(self, value):
		self._PlcAsDSS = value if type(value) != base_types.auto else self.make_default("PlcAsDSS")

	@PlcAsDSS.deleter
	def PlcAsDSS(self):
		del self._PlcAsDSS
		self._PlcAsDSS = None

	@property
	def NonLclMktPlc(self):
		return self._NonLclMktPlc

	@NonLclMktPlc.setter
	def NonLclMktPlc(self, value):
		self._NonLclMktPlc = value if type(value) != base_types.auto else self.make_default("NonLclMktPlc")

	@NonLclMktPlc.deleter
	def NonLclMktPlc(self):
		del self._NonLclMktPlc
		self._NonLclMktPlc = None

	@property
	def LclMktPlc(self):
		return self._LclMktPlc

	@LclMktPlc.setter
	def LclMktPlc(self, value):
		self._LclMktPlc = value if type(value) != base_types.auto else self.make_default("LclMktPlc")

	@LclMktPlc.deleter
	def LclMktPlc(self):
		del self._LclMktPlc
		self._LclMktPlc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PlcAsDSS', type=GenericIdentification5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NonLclMktPlc', type=PriceSource, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LclMktPlc', type=MICIdentifier, min=0, max=1, mutex_group=1, array=False),
	))

