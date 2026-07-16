# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import StandingOrder11

class StandingOrderOrError10Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_StgOrdr"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if value is not None else base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, True)

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, True)

	@property
	def StgOrdr(self):
		return self._StgOrdr

	@StgOrdr.setter
	def StgOrdr(self, value):
		self._StgOrdr = value if value is not None else base_types.UninitialisedField(self, 'StgOrdr', StandingOrder11, False)

	@StgOrdr.deleter
	def StgOrdr(self):
		del self._StgOrdr
		self._StgOrdr = base_types.UninitialisedField(self, 'StgOrdr', StandingOrder11, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='StgOrdr', type=StandingOrder11, min=0, max=1, mutex_group=1, array=False),
	))