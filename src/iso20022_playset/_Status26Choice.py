# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IndividualOrderStatusAndReason8
from . import OrderStatusAndReason9

class Status26Choice(base_types._BaseFieldType):

	__slots__ = ["_CxlStsRpt", "_IndvCxlStsRpt"]
	@property
	def CxlStsRpt(self):
		return self._CxlStsRpt

	@CxlStsRpt.setter
	def CxlStsRpt(self, value):
		self._CxlStsRpt = value if value is not None else base_types.UninitialisedField(self, 'CxlStsRpt', OrderStatusAndReason9, False)

	@CxlStsRpt.deleter
	def CxlStsRpt(self):
		del self._CxlStsRpt
		self._CxlStsRpt = base_types.UninitialisedField(self, 'CxlStsRpt', OrderStatusAndReason9, False)

	@property
	def IndvCxlStsRpt(self):
		return self._IndvCxlStsRpt

	@IndvCxlStsRpt.setter
	def IndvCxlStsRpt(self, value):
		self._IndvCxlStsRpt = value if value is not None else base_types.UninitialisedField(self, 'IndvCxlStsRpt', IndividualOrderStatusAndReason8, True)

	@IndvCxlStsRpt.deleter
	def IndvCxlStsRpt(self):
		del self._IndvCxlStsRpt
		self._IndvCxlStsRpt = base_types.UninitialisedField(self, 'IndvCxlStsRpt', IndividualOrderStatusAndReason8, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlStsRpt', type=OrderStatusAndReason9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndvCxlStsRpt', type=IndividualOrderStatusAndReason8, min=1, max=None, mutex_group=1, array=True),
	))