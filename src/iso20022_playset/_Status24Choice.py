from . import base_types
from ._SwitchOrderStatusAndReason2 import SwitchOrderStatusAndReason2
from ._IndividualOrderStatusAndReason7 import IndividualOrderStatusAndReason7
from ._OrderStatusAndReason10 import OrderStatusAndReason10

class Status24Choice(base_types._BaseFieldType):

	__slots__ = ["_OrdrDtlsRpt", "_SwtchOrdrDtlsRpt", "_IndvOrdrDtlsRpt"]
	@property
	def IndvOrdrDtlsRpt(self):
		return self._IndvOrdrDtlsRpt

	@IndvOrdrDtlsRpt.setter
	def IndvOrdrDtlsRpt(self, value):
		self._IndvOrdrDtlsRpt = value if type(value) != base_types.auto else self.make_default("IndvOrdrDtlsRpt")

	@IndvOrdrDtlsRpt.deleter
	def IndvOrdrDtlsRpt(self):
		del self._IndvOrdrDtlsRpt
		self._IndvOrdrDtlsRpt = None

	@property
	def OrdrDtlsRpt(self):
		return self._OrdrDtlsRpt

	@OrdrDtlsRpt.setter
	def OrdrDtlsRpt(self, value):
		self._OrdrDtlsRpt = value if type(value) != base_types.auto else self.make_default("OrdrDtlsRpt")

	@OrdrDtlsRpt.deleter
	def OrdrDtlsRpt(self):
		del self._OrdrDtlsRpt
		self._OrdrDtlsRpt = None

	@property
	def SwtchOrdrDtlsRpt(self):
		return self._SwtchOrdrDtlsRpt

	@SwtchOrdrDtlsRpt.setter
	def SwtchOrdrDtlsRpt(self, value):
		self._SwtchOrdrDtlsRpt = value if type(value) != base_types.auto else self.make_default("SwtchOrdrDtlsRpt")

	@SwtchOrdrDtlsRpt.deleter
	def SwtchOrdrDtlsRpt(self):
		del self._SwtchOrdrDtlsRpt
		self._SwtchOrdrDtlsRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndvOrdrDtlsRpt', type=IndividualOrderStatusAndReason7, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OrdrDtlsRpt', type=OrderStatusAndReason10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SwtchOrdrDtlsRpt', type=SwitchOrderStatusAndReason2, min=1, max=None, mutex_group=1, array=True),
	))

