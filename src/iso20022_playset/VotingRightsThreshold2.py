from . import base_types
from .ThresholdBasis1Choice import ThresholdBasis1Choice
from .NumberOrPercentage2Choice import NumberOrPercentage2Choice

class VotingRightsThreshold2(base_types._BaseFieldType):

	__slots__ = ["_ThrshldBsis", "_Thrshld"]
	@property
	def ThrshldBsis(self):
		return self._ThrshldBsis

	@ThrshldBsis.setter
	def ThrshldBsis(self, value):
		self._ThrshldBsis = value if type(value) != auto else self.make_default("ThrshldBsis")

	@ThrshldBsis.deleter
	def ThrshldBsis(self):
		del self._ThrshldBsis
		self._ThrshldBsis = None

	@property
	def Thrshld(self):
		return self._Thrshld

	@Thrshld.setter
	def Thrshld(self, value):
		self._Thrshld = value if type(value) != auto else self.make_default("Thrshld")

	@Thrshld.deleter
	def Thrshld(self):
		del self._Thrshld
		self._Thrshld = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ThrshldBsis', type=ThresholdBasis1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Thrshld', type=NumberOrPercentage2Choice, min=1, max=1, mutex_group=None, array=False),
	))

