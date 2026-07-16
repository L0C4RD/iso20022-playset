# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IndividualOrderStatusAndReason7
from . import OrderStatusAndReason10
from . import SwitchOrderStatusAndReason2

class Status24Choice(base_types._BaseFieldType):

	__slots__ = ["_IndvOrdrDtlsRpt", "_OrdrDtlsRpt", "_SwtchOrdrDtlsRpt"]
	@property
	def IndvOrdrDtlsRpt(self):
		return self._IndvOrdrDtlsRpt

	@IndvOrdrDtlsRpt.setter
	def IndvOrdrDtlsRpt(self, value):
		self._IndvOrdrDtlsRpt = value if value is not None else base_types.UninitialisedField(self, 'IndvOrdrDtlsRpt', IndividualOrderStatusAndReason7, True)

	@IndvOrdrDtlsRpt.deleter
	def IndvOrdrDtlsRpt(self):
		del self._IndvOrdrDtlsRpt
		self._IndvOrdrDtlsRpt = base_types.UninitialisedField(self, 'IndvOrdrDtlsRpt', IndividualOrderStatusAndReason7, True)

	@property
	def OrdrDtlsRpt(self):
		return self._OrdrDtlsRpt

	@OrdrDtlsRpt.setter
	def OrdrDtlsRpt(self, value):
		self._OrdrDtlsRpt = value if value is not None else base_types.UninitialisedField(self, 'OrdrDtlsRpt', OrderStatusAndReason10, False)

	@OrdrDtlsRpt.deleter
	def OrdrDtlsRpt(self):
		del self._OrdrDtlsRpt
		self._OrdrDtlsRpt = base_types.UninitialisedField(self, 'OrdrDtlsRpt', OrderStatusAndReason10, False)

	@property
	def SwtchOrdrDtlsRpt(self):
		return self._SwtchOrdrDtlsRpt

	@SwtchOrdrDtlsRpt.setter
	def SwtchOrdrDtlsRpt(self, value):
		self._SwtchOrdrDtlsRpt = value if value is not None else base_types.UninitialisedField(self, 'SwtchOrdrDtlsRpt', SwitchOrderStatusAndReason2, True)

	@SwtchOrdrDtlsRpt.deleter
	def SwtchOrdrDtlsRpt(self):
		del self._SwtchOrdrDtlsRpt
		self._SwtchOrdrDtlsRpt = base_types.UninitialisedField(self, 'SwtchOrdrDtlsRpt', SwitchOrderStatusAndReason2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndvOrdrDtlsRpt', type=IndividualOrderStatusAndReason7, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OrdrDtlsRpt', type=OrderStatusAndReason10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SwtchOrdrDtlsRpt', type=SwitchOrderStatusAndReason2, min=1, max=None, mutex_group=1, array=True),
	))