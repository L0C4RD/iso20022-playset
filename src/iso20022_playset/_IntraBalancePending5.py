# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraBalancePending6
from . import PendingStatusAndReason2

class IntraBalancePending5(base_types._BaseFieldType):

	__slots__ = ["_Mvmnt", "_StsAndRsn"]
	@property
	def Mvmnt(self):
		return self._Mvmnt

	@Mvmnt.setter
	def Mvmnt(self, value):
		self._Mvmnt = value if value is not None else base_types.UninitialisedField(self, 'Mvmnt', IntraBalancePending6, True)

	@Mvmnt.deleter
	def Mvmnt(self):
		del self._Mvmnt
		self._Mvmnt = base_types.UninitialisedField(self, 'Mvmnt', IntraBalancePending6, True)

	@property
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if value is not None else base_types.UninitialisedField(self, 'StsAndRsn', PendingStatusAndReason2, False)

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = base_types.UninitialisedField(self, 'StsAndRsn', PendingStatusAndReason2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mvmnt', type=IntraBalancePending6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsAndRsn', type=PendingStatusAndReason2, min=0, max=1, mutex_group=None, array=False),
	))