# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NonClearingReason2

class ClearingExceptionOrExemption2(base_types._BaseFieldType):

	__slots__ = ["_OthrCtrPty", "_RptgCtrPty"]
	@property
	def OthrCtrPty(self):
		return self._OthrCtrPty

	@OthrCtrPty.setter
	def OthrCtrPty(self, value):
		self._OthrCtrPty = value if value is not None else base_types.UninitialisedField(self, 'OthrCtrPty', NonClearingReason2, False)

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = base_types.UninitialisedField(self, 'OthrCtrPty', NonClearingReason2, False)

	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if value is not None else base_types.UninitialisedField(self, 'RptgCtrPty', NonClearingReason2, False)

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = base_types.UninitialisedField(self, 'RptgCtrPty', NonClearingReason2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrCtrPty', type=NonClearingReason2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=NonClearingReason2, min=1, max=1, mutex_group=None, array=False),
	))