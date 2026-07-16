# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Reason2
from . import RejectedElement1

class RejectionReason1Choice(base_types._BaseFieldType):

	__slots__ = ["_GblRjctnRsn", "_RjctdElmt"]
	@property
	def GblRjctnRsn(self):
		return self._GblRjctnRsn

	@GblRjctnRsn.setter
	def GblRjctnRsn(self, value):
		self._GblRjctnRsn = value if value is not None else base_types.UninitialisedField(self, 'GblRjctnRsn', Reason2, False)

	@GblRjctnRsn.deleter
	def GblRjctnRsn(self):
		del self._GblRjctnRsn
		self._GblRjctnRsn = base_types.UninitialisedField(self, 'GblRjctnRsn', Reason2, False)

	@property
	def RjctdElmt(self):
		return self._RjctdElmt

	@RjctdElmt.setter
	def RjctdElmt(self, value):
		self._RjctdElmt = value if value is not None else base_types.UninitialisedField(self, 'RjctdElmt', RejectedElement1, True)

	@RjctdElmt.deleter
	def RjctdElmt(self):
		del self._RjctdElmt
		self._RjctdElmt = base_types.UninitialisedField(self, 'RjctdElmt', RejectedElement1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GblRjctnRsn', type=Reason2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RjctdElmt', type=RejectedElement1, min=1, max=None, mutex_group=1, array=True),
	))