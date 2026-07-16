# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LimitIdentification8
from . import LimitIdentification9

class LimitStructure3Choice(base_types._BaseFieldType):

	__slots__ = ["_AllCurLmts", "_CurLmtId"]
	@property
	def AllCurLmts(self):
		return self._AllCurLmts

	@AllCurLmts.setter
	def AllCurLmts(self, value):
		self._AllCurLmts = value if value is not None else base_types.UninitialisedField(self, 'AllCurLmts', LimitIdentification9, False)

	@AllCurLmts.deleter
	def AllCurLmts(self):
		del self._AllCurLmts
		self._AllCurLmts = base_types.UninitialisedField(self, 'AllCurLmts', LimitIdentification9, False)

	@property
	def CurLmtId(self):
		return self._CurLmtId

	@CurLmtId.setter
	def CurLmtId(self, value):
		self._CurLmtId = value if value is not None else base_types.UninitialisedField(self, 'CurLmtId', LimitIdentification8, False)

	@CurLmtId.deleter
	def CurLmtId(self):
		del self._CurLmtId
		self._CurLmtId = base_types.UninitialisedField(self, 'CurLmtId', LimitIdentification8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AllCurLmts', type=LimitIdentification9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CurLmtId', type=LimitIdentification8, min=0, max=1, mutex_group=1, array=False),
	))