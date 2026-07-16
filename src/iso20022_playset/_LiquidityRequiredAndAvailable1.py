# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LiquidResources1
from . import SettlementDate6Code
from . import StressLiquidResourceRequirement1

class LiquidityRequiredAndAvailable1(base_types._BaseFieldType):

	__slots__ = ["_LqdRsrcs", "_LqdtyHrzn", "_StrssLqdRsrcRqrmnt"]
	@property
	def LqdRsrcs(self):
		return self._LqdRsrcs

	@LqdRsrcs.setter
	def LqdRsrcs(self, value):
		self._LqdRsrcs = value if value is not None else base_types.UninitialisedField(self, 'LqdRsrcs', LiquidResources1, False)

	@LqdRsrcs.deleter
	def LqdRsrcs(self):
		del self._LqdRsrcs
		self._LqdRsrcs = base_types.UninitialisedField(self, 'LqdRsrcs', LiquidResources1, False)

	@property
	def LqdtyHrzn(self):
		return self._LqdtyHrzn

	@LqdtyHrzn.setter
	def LqdtyHrzn(self, value):
		self._LqdtyHrzn = value if value is not None else base_types.UninitialisedField(self, 'LqdtyHrzn', SettlementDate6Code, False)

	@LqdtyHrzn.deleter
	def LqdtyHrzn(self):
		del self._LqdtyHrzn
		self._LqdtyHrzn = base_types.UninitialisedField(self, 'LqdtyHrzn', SettlementDate6Code, False)

	@property
	def StrssLqdRsrcRqrmnt(self):
		return self._StrssLqdRsrcRqrmnt

	@StrssLqdRsrcRqrmnt.setter
	def StrssLqdRsrcRqrmnt(self, value):
		self._StrssLqdRsrcRqrmnt = value if value is not None else base_types.UninitialisedField(self, 'StrssLqdRsrcRqrmnt', StressLiquidResourceRequirement1, False)

	@StrssLqdRsrcRqrmnt.deleter
	def StrssLqdRsrcRqrmnt(self):
		del self._StrssLqdRsrcRqrmnt
		self._StrssLqdRsrcRqrmnt = base_types.UninitialisedField(self, 'StrssLqdRsrcRqrmnt', StressLiquidResourceRequirement1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LqdRsrcs', type=LiquidResources1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LqdtyHrzn', type=SettlementDate6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrssLqdRsrcRqrmnt', type=StressLiquidResourceRequirement1, min=1, max=1, mutex_group=None, array=False),
	))