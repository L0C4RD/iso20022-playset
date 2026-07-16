# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClosingDate4Choice
from . import CollateralAmount14

class DealTransactionDetails7(base_types._BaseFieldType):

	__slots__ = ["_ClsgDt", "_DealDtlsAmt"]
	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if value is not None else base_types.UninitialisedField(self, 'ClsgDt', ClosingDate4Choice, False)

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = base_types.UninitialisedField(self, 'ClsgDt', ClosingDate4Choice, False)

	@property
	def DealDtlsAmt(self):
		return self._DealDtlsAmt

	@DealDtlsAmt.setter
	def DealDtlsAmt(self, value):
		self._DealDtlsAmt = value if value is not None else base_types.UninitialisedField(self, 'DealDtlsAmt', CollateralAmount14, False)

	@DealDtlsAmt.deleter
	def DealDtlsAmt(self):
		del self._DealDtlsAmt
		self._DealDtlsAmt = base_types.UninitialisedField(self, 'DealDtlsAmt', CollateralAmount14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsgDt', type=ClosingDate4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealDtlsAmt', type=CollateralAmount14, min=0, max=1, mutex_group=None, array=False),
	))