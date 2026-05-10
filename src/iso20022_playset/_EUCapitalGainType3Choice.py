from . import base_types
from ._GenericIdentification30 import GenericIdentification30
from ._EUCapitalGain2Code import EUCapitalGain2Code

class EUCapitalGainType3Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_EUCptlGn"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def EUCptlGn(self):
		return self._EUCptlGn

	@EUCptlGn.setter
	def EUCptlGn(self, value):
		self._EUCptlGn = value if type(value) != base_types.auto else self.make_default("EUCptlGn")

	@EUCptlGn.deleter
	def EUCptlGn(self):
		del self._EUCptlGn
		self._EUCptlGn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EUCptlGn', type=EUCapitalGain2Code, min=0, max=1, mutex_group=1, array=False),
	))

