# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LimitIdentification8
from . import LimitOrError4Choice

class LimitReport8(base_types._BaseFieldType):

	__slots__ = ["_LmtId", "_LmtOrErr"]
	@property
	def LmtId(self):
		return self._LmtId

	@LmtId.setter
	def LmtId(self, value):
		self._LmtId = value if value is not None else base_types.UninitialisedField(self, 'LmtId', LimitIdentification8, False)

	@LmtId.deleter
	def LmtId(self):
		del self._LmtId
		self._LmtId = base_types.UninitialisedField(self, 'LmtId', LimitIdentification8, False)

	@property
	def LmtOrErr(self):
		return self._LmtOrErr

	@LmtOrErr.setter
	def LmtOrErr(self, value):
		self._LmtOrErr = value if value is not None else base_types.UninitialisedField(self, 'LmtOrErr', LimitOrError4Choice, False)

	@LmtOrErr.deleter
	def LmtOrErr(self):
		del self._LmtOrErr
		self._LmtOrErr = base_types.UninitialisedField(self, 'LmtOrErr', LimitOrError4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LmtId', type=LimitIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtOrErr', type=LimitOrError4Choice, min=1, max=1, mutex_group=None, array=False),
	))