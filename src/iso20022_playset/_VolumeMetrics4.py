# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import ReuseValue1Choice

class VolumeMetrics4(base_types._BaseFieldType):

	__slots__ = ["_ReuseVal", "_RinvstdCshAmt"]
	@property
	def ReuseVal(self):
		return self._ReuseVal

	@ReuseVal.setter
	def ReuseVal(self, value):
		self._ReuseVal = value if value is not None else base_types.UninitialisedField(self, 'ReuseVal', ReuseValue1Choice, False)

	@ReuseVal.deleter
	def ReuseVal(self):
		del self._ReuseVal
		self._ReuseVal = base_types.UninitialisedField(self, 'ReuseVal', ReuseValue1Choice, False)

	@property
	def RinvstdCshAmt(self):
		return self._RinvstdCshAmt

	@RinvstdCshAmt.setter
	def RinvstdCshAmt(self, value):
		self._RinvstdCshAmt = value if value is not None else base_types.UninitialisedField(self, 'RinvstdCshAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@RinvstdCshAmt.deleter
	def RinvstdCshAmt(self):
		del self._RinvstdCshAmt
		self._RinvstdCshAmt = base_types.UninitialisedField(self, 'RinvstdCshAmt', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReuseVal', type=ReuseValue1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstdCshAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))