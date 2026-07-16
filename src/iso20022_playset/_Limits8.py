# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LimitReport8

class Limits8(base_types._BaseFieldType):

	__slots__ = ["_CurLmt", "_DfltLmt"]
	@property
	def CurLmt(self):
		return self._CurLmt

	@CurLmt.setter
	def CurLmt(self, value):
		self._CurLmt = value if value is not None else base_types.UninitialisedField(self, 'CurLmt', LimitReport8, True)

	@CurLmt.deleter
	def CurLmt(self):
		del self._CurLmt
		self._CurLmt = base_types.UninitialisedField(self, 'CurLmt', LimitReport8, True)

	@property
	def DfltLmt(self):
		return self._DfltLmt

	@DfltLmt.setter
	def DfltLmt(self, value):
		self._DfltLmt = value if value is not None else base_types.UninitialisedField(self, 'DfltLmt', LimitReport8, True)

	@DfltLmt.deleter
	def DfltLmt(self):
		del self._DfltLmt
		self._DfltLmt = base_types.UninitialisedField(self, 'DfltLmt', LimitReport8, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurLmt', type=LimitReport8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DfltLmt', type=LimitReport8, min=0, max=None, mutex_group=None, array=True),
	))