# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LimitReport8 import LimitReport8

class Limits8(base_types._BaseFieldType):

	__slots__ = ["_CurLmt", "_DfltLmt"]
	@property
	def CurLmt(self):
		return self._CurLmt

	@CurLmt.setter
	def CurLmt(self, value):
		self._CurLmt = value if type(value) != base_types.auto else self.make_default("CurLmt")

	@CurLmt.deleter
	def CurLmt(self):
		del self._CurLmt
		self._CurLmt = None

	@property
	def DfltLmt(self):
		return self._DfltLmt

	@DfltLmt.setter
	def DfltLmt(self, value):
		self._DfltLmt = value if type(value) != base_types.auto else self.make_default("DfltLmt")

	@DfltLmt.deleter
	def DfltLmt(self):
		del self._DfltLmt
		self._DfltLmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurLmt', type=LimitReport8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DfltLmt', type=LimitReport8, min=0, max=None, mutex_group=None, array=True),
	))