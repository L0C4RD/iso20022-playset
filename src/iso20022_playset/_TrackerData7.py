# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import DateAndDateTime2Choice
from . import TrackerRecord5

class TrackerData7(base_types._BaseFieldType):

	__slots__ = ["_ConfdAmt", "_ConfdDt", "_TrckrRcrd"]
	@property
	def ConfdAmt(self):
		return self._ConfdAmt

	@ConfdAmt.setter
	def ConfdAmt(self, value):
		self._ConfdAmt = value if value is not None else base_types.UninitialisedField(self, 'ConfdAmt', ActiveCurrencyAndAmount, False)

	@ConfdAmt.deleter
	def ConfdAmt(self):
		del self._ConfdAmt
		self._ConfdAmt = base_types.UninitialisedField(self, 'ConfdAmt', ActiveCurrencyAndAmount, False)

	@property
	def ConfdDt(self):
		return self._ConfdDt

	@ConfdDt.setter
	def ConfdDt(self, value):
		self._ConfdDt = value if value is not None else base_types.UninitialisedField(self, 'ConfdDt', DateAndDateTime2Choice, False)

	@ConfdDt.deleter
	def ConfdDt(self):
		del self._ConfdDt
		self._ConfdDt = base_types.UninitialisedField(self, 'ConfdDt', DateAndDateTime2Choice, False)

	@property
	def TrckrRcrd(self):
		return self._TrckrRcrd

	@TrckrRcrd.setter
	def TrckrRcrd(self, value):
		self._TrckrRcrd = value if value is not None else base_types.UninitialisedField(self, 'TrckrRcrd', TrackerRecord5, True)

	@TrckrRcrd.deleter
	def TrckrRcrd(self):
		del self._TrckrRcrd
		self._TrckrRcrd = base_types.UninitialisedField(self, 'TrckrRcrd', TrackerRecord5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConfdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfdDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckrRcrd', type=TrackerRecord5, min=1, max=None, mutex_group=None, array=True),
	))