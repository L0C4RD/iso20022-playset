from . import base_types
from .AdditionalInformation15 import AdditionalInformation15
from .Max350Text import Max350Text

class OtherTargetMarket1(base_types._BaseFieldType):

	__slots__ = ["_TrgtMktTp", "_AddtlInf"]
	@property
	def TrgtMktTp(self):
		return self._TrgtMktTp

	@TrgtMktTp.setter
	def TrgtMktTp(self, value):
		self._TrgtMktTp = value if type(value) != auto else self.make_default("TrgtMktTp")

	@TrgtMktTp.deleter
	def TrgtMktTp(self):
		del self._TrgtMktTp
		self._TrgtMktTp = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrgtMktTp', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
	))

