# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._TrackerRecord5 import TrackerRecord5

class TrackerData7(base_types._BaseFieldType):

	__slots__ = ["_ConfdAmt", "_ConfdDt", "_TrckrRcrd"]
	@property
	def ConfdAmt(self):
		return self._ConfdAmt

	@ConfdAmt.setter
	def ConfdAmt(self, value):
		self._ConfdAmt = value if type(value) != base_types.auto else self.make_default("ConfdAmt")

	@ConfdAmt.deleter
	def ConfdAmt(self):
		del self._ConfdAmt
		self._ConfdAmt = None

	@property
	def ConfdDt(self):
		return self._ConfdDt

	@ConfdDt.setter
	def ConfdDt(self, value):
		self._ConfdDt = value if type(value) != base_types.auto else self.make_default("ConfdDt")

	@ConfdDt.deleter
	def ConfdDt(self):
		del self._ConfdDt
		self._ConfdDt = None

	@property
	def TrckrRcrd(self):
		return self._TrckrRcrd

	@TrckrRcrd.setter
	def TrckrRcrd(self, value):
		self._TrckrRcrd = value if type(value) != base_types.auto else self.make_default("TrckrRcrd")

	@TrckrRcrd.deleter
	def TrckrRcrd(self):
		del self._TrckrRcrd
		self._TrckrRcrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConfdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfdDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckrRcrd', type=TrackerRecord5, min=1, max=None, mutex_group=None, array=True),
	))