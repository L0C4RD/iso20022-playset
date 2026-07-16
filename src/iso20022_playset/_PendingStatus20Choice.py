# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NoSpecifiedReason1

class PendingStatus20Choice(base_types._BaseFieldType):

	__slots__ = ["_Fwdd", "_UdrInvstgtn"]
	@property
	def Fwdd(self):
		return self._Fwdd

	@Fwdd.setter
	def Fwdd(self, value):
		self._Fwdd = value if value is not None else base_types.UninitialisedField(self, 'Fwdd', NoSpecifiedReason1, False)

	@Fwdd.deleter
	def Fwdd(self):
		del self._Fwdd
		self._Fwdd = base_types.UninitialisedField(self, 'Fwdd', NoSpecifiedReason1, False)

	@property
	def UdrInvstgtn(self):
		return self._UdrInvstgtn

	@UdrInvstgtn.setter
	def UdrInvstgtn(self, value):
		self._UdrInvstgtn = value if value is not None else base_types.UninitialisedField(self, 'UdrInvstgtn', NoSpecifiedReason1, False)

	@UdrInvstgtn.deleter
	def UdrInvstgtn(self):
		del self._UdrInvstgtn
		self._UdrInvstgtn = base_types.UninitialisedField(self, 'UdrInvstgtn', NoSpecifiedReason1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Fwdd', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UdrInvstgtn', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
	))