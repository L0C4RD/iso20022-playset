# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountManagementStatus1Code
from . import RejectionReason31

class Status25Choice(base_types._BaseFieldType):

	__slots__ = ["_Rjctd", "_Sts"]
	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectionReason31, True)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectionReason31, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', AccountManagementStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', AccountManagementStatus1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rjctd', type=RejectionReason31, min=1, max=10, mutex_group=1, array=True),
		base_types.FieldEntry(name='Sts', type=AccountManagementStatus1Code, min=0, max=1, mutex_group=1, array=False),
	))