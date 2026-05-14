# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IndividualOrderStatusAndReason10 import IndividualOrderStatusAndReason10
from ._OrderStatusAndReason12 import OrderStatusAndReason12

class Status42Choice(base_types._BaseFieldType):

	__slots__ = ["_CxlStsRpt", "_IndvCxlStsRpt"]
	@property
	def CxlStsRpt(self):
		return self._CxlStsRpt

	@CxlStsRpt.setter
	def CxlStsRpt(self, value):
		self._CxlStsRpt = value if type(value) != base_types.auto else self.make_default("CxlStsRpt")

	@CxlStsRpt.deleter
	def CxlStsRpt(self):
		del self._CxlStsRpt
		self._CxlStsRpt = None

	@property
	def IndvCxlStsRpt(self):
		return self._IndvCxlStsRpt

	@IndvCxlStsRpt.setter
	def IndvCxlStsRpt(self, value):
		self._IndvCxlStsRpt = value if type(value) != base_types.auto else self.make_default("IndvCxlStsRpt")

	@IndvCxlStsRpt.deleter
	def IndvCxlStsRpt(self):
		del self._IndvCxlStsRpt
		self._IndvCxlStsRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlStsRpt', type=OrderStatusAndReason12, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndvCxlStsRpt', type=IndividualOrderStatusAndReason10, min=1, max=None, mutex_group=1, array=True),
	))