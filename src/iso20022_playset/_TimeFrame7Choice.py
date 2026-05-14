# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Number import Number
from ._YesNoIndicator import YesNoIndicator

class TimeFrame7Choice(base_types._BaseFieldType):

	__slots__ = ["_Prepmt", "_TPlus"]
	@property
	def Prepmt(self):
		return self._Prepmt

	@Prepmt.setter
	def Prepmt(self, value):
		self._Prepmt = value if type(value) != base_types.auto else self.make_default("Prepmt")

	@Prepmt.deleter
	def Prepmt(self):
		del self._Prepmt
		self._Prepmt = None

	@property
	def TPlus(self):
		return self._TPlus

	@TPlus.setter
	def TPlus(self, value):
		self._TPlus = value if type(value) != base_types.auto else self.make_default("TPlus")

	@TPlus.deleter
	def TPlus(self):
		del self._TPlus
		self._TPlus = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prepmt', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TPlus', type=Number, min=0, max=1, mutex_group=1, array=False),
	))