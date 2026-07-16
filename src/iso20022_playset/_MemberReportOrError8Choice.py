# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling3
from . import Member7

class MemberReportOrError8Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_Mmb"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if value is not None else base_types.UninitialisedField(self, 'BizErr', ErrorHandling3, False)

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = base_types.UninitialisedField(self, 'BizErr', ErrorHandling3, False)

	@property
	def Mmb(self):
		return self._Mmb

	@Mmb.setter
	def Mmb(self, value):
		self._Mmb = value if value is not None else base_types.UninitialisedField(self, 'Mmb', Member7, False)

	@Mmb.deleter
	def Mmb(self):
		del self._Mmb
		self._Mmb = base_types.UninitialisedField(self, 'Mmb', Member7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mmb', type=Member7, min=0, max=1, mutex_group=1, array=False),
	))