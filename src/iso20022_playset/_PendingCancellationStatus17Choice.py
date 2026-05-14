# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NoReasonCode import NoReasonCode
from ._PendingCancellationStatusReason12 import PendingCancellationStatusReason12

class PendingCancellationStatus17Choice(base_types._BaseFieldType):

	__slots__ = ["_NotSpcfdRsn", "_Rsn"]
	@property
	def NotSpcfdRsn(self):
		return self._NotSpcfdRsn

	@NotSpcfdRsn.setter
	def NotSpcfdRsn(self, value):
		self._NotSpcfdRsn = value if type(value) != base_types.auto else self.make_default("NotSpcfdRsn")

	@NotSpcfdRsn.deleter
	def NotSpcfdRsn(self):
		del self._NotSpcfdRsn
		self._NotSpcfdRsn = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NotSpcfdRsn', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rsn', type=PendingCancellationStatusReason12, min=1, max=None, mutex_group=1, array=True),
	))