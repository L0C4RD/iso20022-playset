# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NumberOrPercentage2Choice
from . import ThresholdBasis1Choice

class VotingRightsThreshold2(base_types._BaseFieldType):

	__slots__ = ["_Thrshld", "_ThrshldBsis"]
	@property
	def Thrshld(self):
		return self._Thrshld

	@Thrshld.setter
	def Thrshld(self, value):
		self._Thrshld = value if value is not None else base_types.UninitialisedField(self, 'Thrshld', NumberOrPercentage2Choice, False)

	@Thrshld.deleter
	def Thrshld(self):
		del self._Thrshld
		self._Thrshld = base_types.UninitialisedField(self, 'Thrshld', NumberOrPercentage2Choice, False)

	@property
	def ThrshldBsis(self):
		return self._ThrshldBsis

	@ThrshldBsis.setter
	def ThrshldBsis(self, value):
		self._ThrshldBsis = value if value is not None else base_types.UninitialisedField(self, 'ThrshldBsis', ThresholdBasis1Choice, False)

	@ThrshldBsis.deleter
	def ThrshldBsis(self):
		del self._ThrshldBsis
		self._ThrshldBsis = base_types.UninitialisedField(self, 'ThrshldBsis', ThresholdBasis1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Thrshld', type=NumberOrPercentage2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrshldBsis', type=ThresholdBasis1Choice, min=0, max=1, mutex_group=None, array=False),
	))