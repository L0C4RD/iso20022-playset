# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CoverTwoDefaulters1
from . import LiquidityRequiredAndAvailable1
from . import Max256Text

class LiquidityStressTestResult1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_LqdtyReqrdAndAvlbl", "_ScnroDfltrs"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max256Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max256Text, False)

	@property
	def LqdtyReqrdAndAvlbl(self):
		return self._LqdtyReqrdAndAvlbl

	@LqdtyReqrdAndAvlbl.setter
	def LqdtyReqrdAndAvlbl(self, value):
		self._LqdtyReqrdAndAvlbl = value if value is not None else base_types.UninitialisedField(self, 'LqdtyReqrdAndAvlbl', LiquidityRequiredAndAvailable1, False)

	@LqdtyReqrdAndAvlbl.deleter
	def LqdtyReqrdAndAvlbl(self):
		del self._LqdtyReqrdAndAvlbl
		self._LqdtyReqrdAndAvlbl = base_types.UninitialisedField(self, 'LqdtyReqrdAndAvlbl', LiquidityRequiredAndAvailable1, False)

	@property
	def ScnroDfltrs(self):
		return self._ScnroDfltrs

	@ScnroDfltrs.setter
	def ScnroDfltrs(self, value):
		self._ScnroDfltrs = value if value is not None else base_types.UninitialisedField(self, 'ScnroDfltrs', CoverTwoDefaulters1, False)

	@ScnroDfltrs.deleter
	def ScnroDfltrs(self):
		del self._ScnroDfltrs
		self._ScnroDfltrs = base_types.UninitialisedField(self, 'ScnroDfltrs', CoverTwoDefaulters1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LqdtyReqrdAndAvlbl', type=LiquidityRequiredAndAvailable1, min=6, max=6, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScnroDfltrs', type=CoverTwoDefaulters1, min=1, max=1, mutex_group=None, array=False),
	))