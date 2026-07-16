# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import Limit7

class LimitOrError4Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_Lmt"]
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
	def Lmt(self):
		return self._Lmt

	@Lmt.setter
	def Lmt(self, value):
		self._Lmt = value if value is not None else base_types.UninitialisedField(self, 'Lmt', Limit7, False)

	@Lmt.deleter
	def Lmt(self):
		del self._Lmt
		self._Lmt = base_types.UninitialisedField(self, 'Lmt', Limit7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Lmt', type=Limit7, min=0, max=1, mutex_group=1, array=False),
	))