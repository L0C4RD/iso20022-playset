# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NoSpecifiedReason1 import NoSpecifiedReason1
from ._Quantity51Choice import Quantity51Choice

class ReceivedByIssuerOrOfferorStatus1(base_types._BaseFieldType):

	__slots__ = ["_AccptdByIssrQty", "_RcvdByIssrOrOfferrRsn"]
	@property
	def AccptdByIssrQty(self):
		return self._AccptdByIssrQty

	@AccptdByIssrQty.setter
	def AccptdByIssrQty(self, value):
		self._AccptdByIssrQty = value if type(value) != base_types.auto else self.make_default("AccptdByIssrQty")

	@AccptdByIssrQty.deleter
	def AccptdByIssrQty(self):
		del self._AccptdByIssrQty
		self._AccptdByIssrQty = None

	@property
	def RcvdByIssrOrOfferrRsn(self):
		return self._RcvdByIssrOrOfferrRsn

	@RcvdByIssrOrOfferrRsn.setter
	def RcvdByIssrOrOfferrRsn(self, value):
		self._RcvdByIssrOrOfferrRsn = value if type(value) != base_types.auto else self.make_default("RcvdByIssrOrOfferrRsn")

	@RcvdByIssrOrOfferrRsn.deleter
	def RcvdByIssrOrOfferrRsn(self):
		del self._RcvdByIssrOrOfferrRsn
		self._RcvdByIssrOrOfferrRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdByIssrQty', type=Quantity51Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvdByIssrOrOfferrRsn', type=NoSpecifiedReason1, min=1, max=1, mutex_group=None, array=False),
	))